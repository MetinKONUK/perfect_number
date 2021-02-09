number = int(input("Enter: "))
count = 0
for i in range(1,number):
    if number % i == 0:
        count += i

if number == count:
    print("THIS IS A PERFECT NUMBER!")
else:
    print("THIS IS NOT!! A PERFECT NUMBER!")
