## Objective
Build a problem solution that uses APIs with logs at different stages. These logs should be stored in some log files such as `log1.log`, `log2.log`, etc. You need to build a Query Interface that traverses through these log files and fetches logs based on timestamp, log string, source of the log, etc.

--Log Ingestor
--The log ingestor calls to various APIs and logs messages in JSON format to different log files. Each log entry includes:
----level: Log level (info, error, success)
----log_string: The log message
----timestamp: The timestamp of the log entry
----metadata: Additional metadata including the source log file name

--Query Interface
--The query interface allows users to search through log files based on various filters:
----start_timestamp: Start date and time for filtering logs
----end_timestamp: End date and time for filtering logs
----log_string: Substring to search within log messages
----source: Source log file name
----log_file_name: Specific log file to search in

--Features Implemented
--Log ingestion from API calls
--Log storage in JSON format in separate log files
---CLI for searching logs based on:
------Start and end timestamp
------Log file name
------Log message substring
------Source log file

--Identified Issues
----Currently, logs are ingested only from hardcoded API endpoints. In a production system, the API URLs should be dynamically configurable.
----No log rotation or archiving mechanism is implemented. For a production system, it's crucial to manage log file sizes and archival.
----The current implementation reads log files sequentially, which might be a bottleneck for very large log files.
----Limited error handling and reporting in the query interface script.
----Taking much time to fetch api's

# How to run the program

## Prerequisites

-- Ensure you have Python installed.

---1. Install Required Package:
-----Install the `requests` package which is needed to call the APIs.
-----pip install requests

# First run the log_ingestor.py file
# then run the query_interface.py file

# in last of query_interface file 
-- there are different filter funtion 
--so comment out the unwanted and passed the required argument to the funtion to filter

# In hope you would find this impressive
