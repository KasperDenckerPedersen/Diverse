import re

#reg = re.compile("(http(s|)://)?www\.(wiwi\.)?(google|youtube|uni-wuerzburg)\.(de|com)(/wiba/startseite/)?")

reg = re.compile("(https?://)?www\.[a-z\-\.]+\.(de|com|dk|uk)([a-z\-\./])*")

m = reg.match("www.google.com")
print(m)

m = reg.match("https://www.youtube.com")
print(m)

m = reg.match("http://www.uni-wuerzburg.de")
print(m)

m = reg.match("www.wiwi.uni-wuerzburg.de/wiba/startseite/")
print(m)

m = reg.match("www.international.au.dk")
print(m)