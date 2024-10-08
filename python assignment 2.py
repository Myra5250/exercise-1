#1 The volume of a sphere with radius r is (4/3)* pie * r**2.
#What is the volume of the sphere with radius 5.
#Make sure the program enters the radius from the keyboard and provide the answer in 2 decimal places.

r = float(input("Enter the radius of the sphere"))
pie = 22/7
volume = (4/3) * pie * r **2
print(f"The volume of the sphere: {volume:.2f}")

#2 Create a program to calculate the area of a triangle (1/2 * base * height).
#Base and height should be entered using the keyboard

base = float(input("Enter the base of the triangle"))
height = float(input("Enter the height of the triangle"))
area_of_the_triangle = (1/2 * base * height)
print(f"The area of the triangle")

#3 WITI has tasked you to automate a simple grading system.
#As a python student, write a program using to display the grades that
#the students will be receiving based on the mark scored in a subject.
#The grades are:
#90% - 100% Grade is A
#80% - 89% Grade is B
#70% - 79% Grade is C 
#60% - 69% Grade is D
#50% - 59% Grade is E
#< 50% Fail

score = float(input("Enter the students score: "))
if 90<= score <= 100:
    print("A")
elif 80<= score <= 89:
    print("B")
elif 70<= score <= 79:
    print("C")
elif 60<= score <= 69:
    print("D")
elif 50<= score <= 59:
    print("E")
else:
    print("Fail")

#4 WITI Academy is proposimg a sacco to help students save their money.
#Design a platform that will do the following.
#Welcome to, WITI Academy Sacco.
#1. Deposit Money
#2. Withdraw Money
#3. Check Balance 
#Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000.
#If the student selects 2, money should be withdrawn amd a minimum withdraw is 500.
#If the student selects 3, the account balance should be displayed.

initial_balance = 0
print("Welcome to WITI Academy sacco")
print("1. Deposit Money")
print("2. Withdraw Money")
print("3. Check Balance")
choice = input("Select option 1,2,3")
if choice == "1":
    amount = float(input("Enter the amount to deposit"))
    if amount >= 1000:
        initial_balance += amount
        print(f"Successfully withdrew {amount}. New balance is {initial_balance}")
    else:
        print("Minimum deposit is 1000")
elif choice == "2":
    amount = int(input("Enter amount to withdraw: "))
    if amount >=500:
        if initial_balance >= amount:
            initial_balance -= amount
            print(f"Successfully withdrawn {amount}. New balance is {initial_balance} ")
        else:
            print("Insufficient balance")
    else:
        print("Minimum withdraw")
elif choice == 3:
    print(f"Current balance is {initial_balance}.")
else:
    print("Invalid request")