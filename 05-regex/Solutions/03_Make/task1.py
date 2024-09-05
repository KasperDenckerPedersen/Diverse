import re

# Read the data
ipAddresses = []
fileHandler = open('05-regex/03_Make/ipAddresses.txt', 'r')
for ip in fileHandler:
    ipAddresses.append(ip)
fileHandler.close()

regv4 = re.compile(
    "^((25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$"
)

regv6 = re.compile("^([0-9a-f]{4}:){7}([0-9a-f]{4}){1}$")

ipv4 = []
ipv6 = []
invalid = []

for ip in ipAddresses:
    mv4 = regv4.match(ip)
    mv6 = regv6.match(ip)
    if mv4 != None:
        ipv4.append(mv4.group(0))
        #print(f'{mv4.group(0)} is a valid IPv4 address')
    elif mv6 != None:
        ipv6.append(mv6.group(0))
        #print(f'{mv6.group(0)} is a valid IPv6 address')
    else:
        invalid.append(ip)
        #print(f'{ip} is not a valid IP address')

print(f'IPv4: {len(ipv4)}')
print(f'IPv6: {len(ipv6)}')
print(f'Invalid: {len(invalid)}')
print(invalid)