# mbox-short.txt

try:
    fhand = open('mbox-short.txt')
except:
    print("Sorry, could not find file.")
    exit()

count = 0
for lines in fhand:
    if lines.startswith("From "):
        lines = lines.rstrip().split()
        print(lines[1])
        count += 1
print("There were {} lines in the file with From as the first word.".format(count))
