a=10
b=12
c=a+b
print(c)
d=12
e=6
f=d-e
print(f)
g=12
h=23
i=g*h
print(i)
j=2
k=3
l=j/k
print(l)


#reverse a number 
a=10
b=20
(a,b)=(b,a)
print(a,b)



#factorial of a number
num=5
fact = 1

for i in range(1, num + 1):
    fact *= i

print(fact)i

#celius to fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(fahrenheit)

 
#banking system
pin = 1234
attempts = 0

while attempts < 3:
    a = int(input("Enter the PIN: "))

    if pin == a:
        print("Valid")
        break
    else:
        print("Invalid")
        attempts += 1

if attempts == 3:
    print("Try later after 24 hours")


# hotel reception
confirm=input("do u want to eat (yes or no):")
if confirm == "yes":
    print("dosa or idli:")
else:
    drink = input("Do you want coffee or tea? (yes or no): ").lower()

    if drink == "yes":
        print("Coffee or Tea?")
    else:
        water = input("Do you want a water bottle? (yes or no): ").lower()

        if water == "yes":
            print("Here is your water bottle.")
        else:
            print("Okay, go out!")

#Simple Calculator 

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

match op:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"

print("Result:", result)

#sum of cubes
total_cube_sum = 0
for num in range(1, 11):
    if num % 2 != 0:
        cube = num ** 3
        print(f"Cube of {num} is {cube}")
        total_cube_sum += cube
print(f"Total sum of cubes: {total_cube_sum}")

#Odd and Even numbers less than 100
num = 1

print("Even Numbers:")
while num <= 100:
    if num % 2 == 0:
        print(num, end=" ")
    num += 1

# Reset num for odd numbers
num = 1
print("\nOdd Numbers:")
while num <= 100:
    if num % 2 != 0:
        print(num, end=" ")
    num += 1

#sum of 'n' Natural numbers


n = int(input("Enter a natural number: "))
sum_n = n * (n + 1) // 2
print(sum_n)

#finding larger number among 3 numbers

a = float(input("Enter the nmber 1:"))
b= float(input("Enter the nmber 2:"))
c= float(input("Enter the nmber 3:"))
larger = max(a,b,c)
print(larger)

#simple interest
p=int(input("enter the princile:"))
t=int(input("enter the time:"))
r=int(input("enter the rate of interest:"))
print("simple interest is:",((p*t*r)/100))

# calculating sem fee and mess fee 
sem = int(input("Enter 1 for one semester, 2 for both semesters: "))
mess = int(input("Enter 0 for no mess, 1 for one sem mess, 2 for both sem mess: "))

hostel_fee = 50000 if sem == 1 else 80000
mess_fee = 15000 if mess == 1 else 30000 if mess == 2 else 0
total_fee = hostel_fee + mess_fee

print(f"Total fee to be paid: ₹{total_fee}")


# few operations on list
l1=[2.57,3,78,10,5,786,76.09,8]
l1.sort()
#l1.reverse()
#print(l1)
#l1.pop(0)
#print(l1.pop(0))
print(l1)

