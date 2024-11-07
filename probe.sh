# To find shellshock attempts
grep -E '\(\) { :; };' access.log

# To find probing requests (doorbell attempts)
grep -E '/(admin|config|login|test|xmlrpc\.php)' access.log
grep -E 'User-Agent:.*(curl|wget|scanner|nmap)' access.log