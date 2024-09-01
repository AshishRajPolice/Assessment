import csv
from collections import defaultdict

def load_lookup_table(lookup_file):
    lookup_dict = {}
    
    try:
        with open(lookup_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    key = (int(row['dstport']), row['protocol'].lower())
                    lookup_dict[key] = row['tag']
                except (KeyError, ValueError) as e:
                    print(f"Error processing row in lookup table: {row}. Error: {e}")
    except FileNotFoundError:
        print(f"Error: Lookup file '{lookup_file}' not found.")
    except IOError as e:
        print(f"Error reading lookup file '{lookup_file}': {e}")
    
    return lookup_dict

def process_flow_logs(flow_log_file, lookup_dict):
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)
    untagged_count = 0
    
    try:
        with open(flow_log_file, mode='r') as file:
            for line in file:
                try:
                    parts = line.strip().split()
                    if len(parts) < 14 or parts[0] != '2':
                        continue

                    dstport = int(parts[6])
                    protocol_number = parts[7]

                    if protocol_number == '6':
                        protocol = 'tcp'
                    elif protocol_number == '17':
                        protocol = 'udp'
                    elif protocol_number == '1':
                        protocol = 'icmp'
                    else:
                        protocol = 'unknown'

                    key = (dstport, protocol)

                    if key in lookup_dict:
                        tag = lookup_dict[key]
                        tag_counts[tag] += 1
                    else:
                        untagged_count += 1

                    port_protocol_counts[key] += 1
                except (IndexError, ValueError) as e:
                    print(f"Error processing line: {line}. Error: {e}")
    except FileNotFoundError:
        print(f"Error: Flow log file '{flow_log_file}' not found.")
    except IOError as e:
        print(f"Error reading flow log file '{flow_log_file}': {e}")
    
    return tag_counts, port_protocol_counts, untagged_count

def save_report(tag_counts, port_protocol_counts, untagged_count, output_file):
    try:
        with open(output_file, mode='w') as file:
            file.write("Tag Counts:\n")
            file.write("Tag,Count\n")
            for tag, count in tag_counts.items():
                file.write(f"{tag},{count}\n")
            file.write(f"Untagged,{untagged_count}\n\n")

            file.write("Port/Protocol Combination Counts:\n")
            file.write("Port,Protocol,Count\n")
            for (port, protocol), count in port_protocol_counts.items():
                file.write(f"{port},{protocol},{count}\n")
    except IOError as e:
        print(f"Error writing to output file '{output_file}': {e}")

def main():
    lookup_file = 'lookup_table.csv'
    flow_log_file = 'flow_logs.txt'
    output_file = 'output_report.txt'

    lookup_dict = load_lookup_table(lookup_file)
    if not lookup_dict:
        print("Lookup table is empty or failed to load. Exiting.")
        return

    tag_counts, port_protocol_counts, untagged_count = process_flow_logs(flow_log_file, lookup_dict)
    save_report(tag_counts, port_protocol_counts, untagged_count, output_file)
    print(f"Report generated and saved to {output_file}")

if __name__ == '__main__':
    main()
