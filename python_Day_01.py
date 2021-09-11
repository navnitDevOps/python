#TASK 01


test = 'this is day1 of python'
print(len(test))  
print(test.upper())

number = 2
print(number)
print(type(number))


#Task 02
list = [1,2,3,4,5,6,7,8,9]
for i in list: # its a simple iteration over a loop
    print(i)


j = 0
for j in range(1,len(list),2): # here we can have start stop and step as well in range
    print(list[j])


#TASK 03
##################USING FOR LOOP ####################
start = int(input("Enter the start range: "))
end = int(input("enter the end range: "))
print("the even numbers are ")
for num in range(start, end+1):
    if num %2 ==0:
        print(num)
print("the odd numbers are ")
for odd in range(start, end+1):
    if odd%2!=0:
        print(odd)

#################USING WHILE LOOP ####################
num = int(input(" Please Enter the Maximum Value : "))
 
number = 1
print("the odd numbers are below")
while number <= num:
    if(number % 2 != 0):
        print(number)
    number = number + 1
print("the even numbers are below")
even=1
while even <= num:
    if(even%2==0):
        print(even)
    even = even+1
    
######FIZZBUZZ PROBLEM #######
start = int(input(" Please Enter the start Value : "))
end = int(input("Please Enter the end Value :"))

for number in range(start, end +1):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
        continue
    elif number % 3 == 0:
        print("fizz")
        continue
    elif number % 5 == 0:
        print("buzz")
        continue
    print(number)

