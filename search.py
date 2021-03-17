numbers = []

for i in range(int(input("Set a list length"))):
    numbers.append(i+1)
print(numbers) #The list of numbers

find_num = int(input("What number to find?"))

for x in range(len(numbers)):
    if (numbers[x] == find_num):
        print("Your number is in position {}.".format(x))