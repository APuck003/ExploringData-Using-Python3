# romeo.txt

file_name = input("Enter the name of txt file to search: ")

try:
    file_handle = open(file_name)
except:
    print("Sorry, could not find:", file_name)
    exit()

word_list = []

for lines in file_handle:
    lines = lines.strip().split()
    for word in lines:
        if word not in word_list:
            word_list.append(word)
            word_list = sorted(word_list)
print(word_list)
