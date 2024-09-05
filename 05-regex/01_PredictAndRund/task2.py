import re

text = "This book on tennis cost $3.99 at Walmart."

reg2 = re.compile("$This") #Will always give an error, typing something after $ dosn't make sence since there is never anything after the end of the line.
match = reg2.search(text)
print(match)

reg2 = re.compile("^This")
match = reg2.search(text)
print(match)

reg2 = re.compile("This^") #Same as after $, dosn't make sence to search before the line even starts. 
match = reg2.search(text)
print(match)

reg2 = re.compile("This$")
match = reg2.search(text)
print(match)

reg2 = re.compile("Walmart\.$") #\. means we are searching for a literal . without \ it would just be a place holder and anything could take its place.
match = reg2.search(text)
print(match)

#Word boundary \bsomething\b, here we search for something.
