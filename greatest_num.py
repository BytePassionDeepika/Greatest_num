number_input=input("enter the numbers by space:")
number_split=number_input.split()
greatest=int(number_split[0])
for num in number_split[1:]:
    if int(num)>=greatest:
        greatest=int(num)
print("the greatest number is:",greatest)