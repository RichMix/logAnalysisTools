# squid.sh

# Look for any Epoch timestamps in the log entries, typically in the first field. Convert one of these to a human-readable date using Epoch Converter.
# Q2 & Q3: Fastest and Longest Request Times:
cat squid_access.log | awk '{print $2}' | sort -n
# The first value is the fastest request time, and the last value is the longest.


# Q4: Unique IP Addresses:
# To count unique client IP addresses (typically the third field), you can use:
cat squid_access.log | awk '{print $3}' | sort | uniq | wc -l


# Q5 & Q6: GET and POST Requests:
# Extract the HTTP request method (often the 6th field), and count occurrences:
cat squid_access.log | awk '{print $6}' | sort | uniq -c


# Q7: Antivirus Company for Host 192.168.0.224:
# Search for any lines with 192.168.0.224 and check the URLs in these requests for mentions of antivirus companies.
cat squid_access.log | grep "192.168.0.224"


# Q8: Antivirus Update URL:
# Look for URLs that contain terms like "virus" or "definitions" to find the specific antivirus update URL:
cat squid_access.log | grep "192.168.0.224" | grep -i "virus" | grep -i "definitions"


# What URL is used to download an antivirus update?
# Use the command from the question above and then find the URL that includes “virus” and “definitions”

# The Squid log typically includes an Epoch timestamp in the first column. You can convert any of these timestamps to a human-readable format using an online Epoch converter like Epoch Converter.
head -n 1 squid_access.log | awk '{print $1}' | xargs -I {} date -d @{}
# This command extracts the first timestamp and converts it to a human-readable date.

#How many milliseconds did the fastest request take?
#To find the fastest request time, which is usually in the second field, use the following command to sort these times and get the minimum:
cat squid_access.log | awk '{print $2}' | sort -n | head -n 1
# How many milliseconds did the longest request take?

# Use the same method as above but get the maximum instead:
cat squid_access.log | awk '{print $2}' | sort -n | tail -n 1

#How many different IP addresses did the proxy service in this log?
# This counts unique client IP addresses, generally in the third field:
cat squid_access.log | awk '{print $3}' | sort | uniq | wc -l

# How many GET requests were made?
# The HTTP request type is typically the 6th field. Count occurrences of GET requests:
cat squid_access.log | awk '{print $6}' | grep "GET" | wc -l

# How many POST requests were made?
# Use the same method as above but search for POST requests:
cat squid_access.log | awk '{print $6}' | grep "POST" | wc -l

# What company created the antivirus used on the host at 192.168.0.224?
# Search for any entries from this IP and look within the URLs for recognizable antivirus names:
cat squid_access.log | grep "192.168.0.224"

# What URL is used to download an antivirus update?
# Look for any URLs containing terms like "virus" or "definitions" associated with 192.168.0.224:
cat squid_access.log | grep "192.168.0.224" | grep -i "virus" | grep -i "definitions"

# These commands should help you analyze the file and answer each question. Let me know if there’s anything further I can assist with in this analysis! ​​


