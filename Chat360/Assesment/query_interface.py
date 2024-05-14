import os
import json
from datetime import datetime, timezone

def search_logs(log_dir, start_timestamp=None, end_timestamp=None, log_string=None, source=None, log_file_name=None):
    log_files = [f for f in os.listdir(log_dir) if os.path.isfile(os.path.join(log_dir, f))]
    results = []

    for log_file in log_files:
        # filter by the file name if given
        if log_file_name and log_file != log_file_name:
            continue

        with open(os.path.join(log_dir, log_file), 'r') as file:
            for line in file:
                log_entry = json.loads(line.strip())
                log_time = datetime.fromisoformat(log_entry['timestamp'].replace('Z', '+00:00'))

                if start_timestamp:
                    start_timestamp = start_timestamp.replace(tzinfo=timezone.utc)
                if end_timestamp:
                    end_timestamp = end_timestamp.replace(tzinfo=timezone.utc)

                # filters
                if start_timestamp and log_time < start_timestamp:
                    continue
                if end_timestamp and log_time > end_timestamp:
                    continue
                if log_string and log_string.lower() not in log_entry['log_string'].lower():
                    continue
                if source and log_entry['metadata']['source'] != source:
                    continue

                results.append(log_entry)

    return results

# Sample queries

# Filter by start and end date
def filter_datetime(start_time,end_time):

    start_time = datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%SZ')
    end_time = datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%SZ')
    results_by_date = search_logs('logs', start_timestamp=start_time, end_timestamp=end_time)
    print("Results in the range of date and time:")
    for result in results_by_date:
        print(json.dumps(result, indent=4))

# filtering by the log file names like api1.log or api4.log
def filter_filename(name):

    results_by_file = search_logs('logs', log_file_name=name)
    print("Results by log file name:")
    for result in results_by_file:
        print(json.dumps(result, indent=4))

# Filter or search by the string present in the log file
def filter_string(string):

    results_by_log_string = search_logs('logs', log_string=string)
    print("Results by log string:")
    for result in results_by_log_string:
        print(json.dumps(result, indent=4))

# Filter by source which was logged into the meta data
def filter_source(source):

    results_by_source = search_logs('logs', source=source)
    print("Results by source:")
    for result in results_by_source:
        print(json.dumps(result, indent=4))

# Filter base the levels(error, info,...)
def filter_level(level):

    results_by_log_string = search_logs('logs', log_string=level)
    print(f"Results by levels:")
    for result in results_by_log_string:
        print(json.dumps(result, indent=4))

# Combining all the filters
def filter_combined(start_time,end_time,string,source):
    
    start_time = datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%SZ')
    end_time = datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%SZ')
    combined_results = search_logs('logs', start_timestamp=start_time, end_timestamp=end_time, log_string=string, source=source)
    print("Results by combined filters:")
    for result in combined_results:
        print(json.dumps(result, indent=4))


# Filter by start and end date
# filter_datetime('2024-05-12T00:00:00Z','2024-05-31T23:59:59Z')

# filtering by the log file names like api1.log or api4.log
# filter_filename('api1.log')

# Filter or search by the string present in the log file
filter_string('the goddess Bast, who had a woman')

# Filter by source which was logged into the meta data
# filter_source('api3.log')


# Filter base the levels(error, info,...)
# filter_level('info')

# filter by combining all the filters
# filter_combined('2024-05-12T00:00:00Z','2024-05-31T23:59:59Z','error','api5.log')

