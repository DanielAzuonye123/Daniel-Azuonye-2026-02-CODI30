print("Python Learning Folder Ready!")

name = "Daniel"
age = 16

print("Name:", name)
print("Age:", age)

user = input("Type your name: ")
print("Hello", user)

print("\n=== Day 2 ===")

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# number comparison
num = int(input("Enter a number: "))

if num > 10:
    print("Greater than 10")
elif num == 10:
    print("Exactly 10")
else:
    print("Less than 10")

favorite = int(input("What is your favorite number? "))

if favorite == 7:
    print("lucky")
else:
    print("not lucky")
