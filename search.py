# search.py.

# Updating parsing to handle potential missing or malformed request entries more gracefully

# Reinitialize counters and sets
unique_ips.clear()
status_200_count = 0
status_400_count = 0
doorbell_ip = None
googlebot_version = None
shellshock_ip = None
firefox_versions.clear()
http_methods.clear()
special_request_count = 0

# Parse each line in the log file with enhanced handling
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

        # Count HTTP methods (handle cases where request is empty or malformed)
        request_parts = request.split()
        if request_parts:
            method = request_parts[0]
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
# Result
{'Q1': 47,
 'Q2': 19,
 'Q3': 38,
 'Q4': 'No doorbell access detected',
 'Q5': '2.1',
 'Q6': 'No shellshock exploit attempt detected',
 'Q7': '31.0',
 'Q8': 'GET',
 'Q9': 'CONNECT',
 'Q10': 6}

# Here are the answers based on the analysis of the NGINX access log:

# Q1: 47 unique IP addresses reached the server.
# Q2: 19 requests yielded a 200 status.
# Q3: 38 requests yielded a 400 status.
# Q4: No doorbell access detected.
# Q5: The version of Googlebot that visited the website was 2.1.
# Q6: No shellshock exploit attempt was detected.
# Q7: The most popular version of Firefox used was 31.0.
# Q8: The most common HTTP method used was GET.
# Q9: The second most common HTTP method used was CONNECT.
# Q10: There were 6 requests for the special byte sequence \x04\x01\x00P\xC6\xCE\x0Eu0\x00. ​​

