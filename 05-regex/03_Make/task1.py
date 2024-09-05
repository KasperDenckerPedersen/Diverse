import re

# Read the data
ipAddresses = []
fileHandler = open('05-regex/03_Make/ipAddresses.txt', 'r')
for ip in fileHandler:
    ipAddresses.append(ip)
fileHandler.close()

# Your code starts here
countV4 = 0
countV6 = 0
countTotalIP = 0

regV4 = re.compile("((\d{0,255})\.){3}(\d{0,255})")
regV6 = re.compile("([0-9a-f]{4}\:){7}[0-9a-f]{4}")

for ip in ipAddresses:
    m = regV4.match(ip)
    n = regV6.match(ip)
    if m:
        countV4 += 1
        countTotalIP += 1
    else:
        countTotalIP += 1
        if n:
            countV6 += 1
        else:
            print(f"Ip: {ip} Not Valid\n")

NotValidIP = countTotalIP - countV4 - countV6
print(f"There is a total of {countTotalIP} IP adresses.")
print(f"There is: {countV4} valid V4 IP adresses\nThere is: {countV6} valid V6 IP adresses")
print(f"There is a total of {NotValidIP} not valid IP V6 or V4 adresses.")