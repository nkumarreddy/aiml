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
