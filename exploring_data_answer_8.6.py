num_list = list()

while True:
    num = input("Enter a number: ")
    # num = float(num)
    if num.isdecimal():
        num = float(num)
        num_list.append(num)
    if num == "done":
        break
print("Maximum: " + str(max(num_list)))
print("Minimum: " + str(min(num_list)))
