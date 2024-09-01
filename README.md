OVERVIEW:

This program reads one flow log data and one string table which can be used to map the flow log entry to specific tags using the destination port and protocol. It then creates a report that identifies the frequency of each tag along with the possibles port / protocols in the flow logs. I appreciate the chance given to me to take the assessment. All the assessment have been done in Python 3. 11. 0. The following libraries have been employed:

.csv

HOW TO RUN THE PROGRAM:
Prerequisites:

Ensure Python 3 is installed on your system.
The input files (flow_logs.txt and lookup_table.csv) should be in the same directory as the script.
Input Files:

lookup_table.csv: A CSV file containing the mapping of dstport, protocol, and tag.
flow_logs.txt: A text file containing the flow logs in the default format (version 2).
Running the Program:

Open a terminal and navigate to the directory containing Network_traffic_analyzer.py.
Run the script using the following command:

python Network_traffic_analyzer.py
The program will generate an output file named output_report.txt in the same directory.

The Tests folder has 3 different tests:
Generated outputs with different set of Flowlogs and Lookup tables:
1. output-Test1.Basic.txt
2. output-Test2-NoMatches.txt
3. output-Test3.CaseInsensitivity.txt

ASSUMPTIONS:

The program assumes that the flow log file is in the default format, version 2, as specified in the AWS documentation.
The program is case-insensitive, treating tcp and TCP the same.
If a protocol other than TCP, UDP, or ICMP is found, the program will skip that entry.
Flow logs that do not match any entry in the lookup table will be labeled as "Untagged."
The flow log file can be up to 10 MB, and the lookup table can contain up to 10,000 mappings.

TESTS:

The program has been tested with sample flow log entries and lookup tables to ensure correct mapping and tagging.
Tests have been performed for basic matching, no matches, and case insensitivity scenarios.

INSIGHTS:

The program also reads and processes the flow log files line by line allowing for the processing of files of about 10 MB.
Explicit dictionaries for lookup is effectively employed in order to enable fast and efficient matching of tags.
In the development of the program, measures have been taken in order to ensure that the program is easy to extend should there be a need to introduce more protocols or any custom processing in the future.

FILES INCLUDED:

Network_traffic_analyzer.py: The main Python script.
flow_logs.txt: A sample flow log file.
lookup_table.csv: A sample lookup table.
output_report.txt: The generated output report (after running the script).