# mbox-short.txt

fname = input("Enter name of file to search: ")

fhand = open(fname)

lines = [line.strip() for line in fhand if line.startswith("From ")]

day_dict = {}

for words in lines:
    words = words.split()
    day_dict[words[2]] = day_dict.get(words[2], 0) + 1

print(day_dict)
