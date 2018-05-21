fhand = open("test.txt")
for line in fhand:
    if "A" in line:
        fout = open("add.txt","a")
        print(line)
        fout.write(line)
fout.close()
fout = open("add.txt")        
for line in fout:
    print(line)
