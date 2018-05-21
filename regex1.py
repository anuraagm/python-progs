import re
fhand = open("mboxt.txt")
for line in fhand:
    if(re.search("^X\S*:[0-9]+"),line):
        print(line)