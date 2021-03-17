numbers = []
import random

for i in range(int(input("Set a list length"))):
    numbers.append(i+1)

for z in range(len(numbers)):
  randintt = random.randint(0, len(numbers)-1)
  yemp = numbers[z]
  numbers[z] = numbers[randintt]
  numbers[randintt] = yemp

print(numbers) #The list of numbers

find_num = int(input("What number to find?"))

for x in range(len(numbers)):
    if (numbers[x] == find_num):
        print("Your number is in position {}.".format(x))