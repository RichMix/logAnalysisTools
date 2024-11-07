# count.py

import re
from collections import Counter

# Initialize counters and sets for unique IPs and specific status codes
unique_ips = set()
status_200_count = 0
status_400_count = 0
doorbell_ip = None
googlebot_version = None
shellshock_ip = None
firefox_versions = Counter()
http_methods = Counter()
special_request_count = 0

# Pattern to detect Googlebot and extract its version
googlebot_pattern = re.compile(r"Googlebot/([\d.]+)")

# Pattern for detecting shellshock exploit attempts (common pattern in headers)
shellshock_pattern = re.compile(r"\(\)\s*{")

# Special request pattern to match the specific byte sequence
special_request_pattern = re.compile(r"\\x04\\x01\\x00P\\xC6\\xCE\\x0Eu0\\x00")

# Parse each line in the log file
for line in log_data:
    # Extract IP, status code, request method, and user agent string
    parts = re.match(r'(\S+) - - \[(.*?)\] "(.*?)" (\d{3}) \S+ "(.*?)" "(.*?)"', line)
    if parts:
        ip = parts.group(1)
        request = parts.group(3)
        status_code = parts.group(4)
        user_agent = parts.group(6)

        # Count unique IPs
        unique_ips.add(ip)

        # Count status codes
        if status_code == '200':
            status_200_count += 1
        elif status_code == '400':
            status_400_count += 1

        # Detect doorbell attempt (assuming it's indicated by a GET request to root or unique identifier in user-agent)
        if 'doorbell' in request.lower():
            doorbell_ip = ip

        # Detect Googlebot visits and get version
        if 'Googlebot' in user_agent:
            googlebot_match = googlebot_pattern.search(user_agent)
            if googlebot_match:
                googlebot_version = googlebot_match.group(1)

        # Detect shellshock attempt
        if shellshock_pattern.search(request):
            shellshock_ip = ip

        # Count Firefox versions if Firefox is in the user-agent
        if 'Firefox' in user_agent:
            version_match = re.search(r'Firefox/([\d.]+)', user_agent)
            if version_match:
                firefox_versions[version_match.group(1)] += 1

        # Count HTTP methods
        method = request.split()[0]
        http_methods[method] += 1

        # Check for special byte sequence request
        if special_request_pattern.search(request):
            special_request_count += 1

# Compile answers based on parsed data

answers = {
    "Q1": len(unique_ips),
    "Q2": status_200_count,
    "Q3": status_400_count,
    "Q4": doorbell_ip if doorbell_ip else "No doorbell access detected",
    "Q5": googlebot_version if googlebot_version else "No Googlebot detected",
    "Q6": shellshock_ip if shellshock_ip else "No shellshock exploit attempt detected",
    "Q7": firefox_versions.most_common(1)[0][0] if firefox_versions else "No Firefox usage detected",
    "Q8": http_methods.most_common(1)[0][0] if http_methods else "No HTTP methods detected",
    "Q9": http_methods.most_common(2)[1][0] if len(http_methods) > 1 else "No secondary HTTP method detected",
    "Q10": special_request_count,
}

answers

# ---------------------------------------------------------------------------
# IndexError                                Traceback (most recent call last)
# Cell In[2], line 64

#      61         firefox_versions[version_match.group(1)] += 1
#      63 # Count HTTP methods
# ---> 64 method = request.split()[0]
#      65 http_methods[method] += 1
#      67 # Check for special byte sequence request

# IndexError: list index out of range
