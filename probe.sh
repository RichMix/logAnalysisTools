# To find shellshock attempts
grep -E '\(\) { :; };' access.log

# To find probing requests (doorbell attempts)
grep -E '/(admin|config|login|test|xmlrpc\.php)' access.log
grep -E 'User-Agent:.*(curl|wget|scanner|nmap)' access.log

# Scan for IOT devices
nmap -n -Pn -sSU -pT:[0-65535,U:0‐65535 -v -A (192.168.00.0/24)]

# [] = need to be tailored to each system
# nnmap commands:
# -n skip DNS resolution 
# -Pn treats all hosts as if they are online
# -sSU do both TCP,SYN, & UDP scans
# -pT: range of ports to scan
# -U: range of ports
# -v Verbosity level
# -A detect the OS, version followed by IP mask