def Activity1():
    print("\n====================================================================\n")
    print("Activity 1\n")
    print("Hello World!")
    print("\n====================================================================\n")


def Activity2():
    print("\n====================================================================\n")
    print("Activity 2")
    num1 = eval(input("Enter a number: "))
    num2 = eval(input("Enter a number: "))
    answer = num1 + num2
    print(num1 , " plus " , num2 , " = " , answer)
    print("\n====================================================================\n")

def Activity3():
    print("\n====================================================================\n")
    print("Activity 3\n")
    Name = input("PLEASE INPUT YOUR NAME : ")               
    Nickname = input("PLEASE INPUT YOUR NICKNAME : ")
    Age = input("PLEASE INPUT YOUR AGE : ")
    Birthmonth = input("PLEASE INPUT YOUR BIRTHMONTH : ")
    Birthday = input("PLEASE INPUT YOUR BIRTHDAY : ")
    Birthyear = input("PLEASE INPUT YOUR BIRTHYEAR : ")
    Gender = input("PLEASE INPUT YOUR GENDER : ")
    Address = input("PLEASE INPUT YOUR ADDRESS : ")
    Nationality = input("PLEASE INPUT YOUR NATIONALITY : ")
    isMarried = False
    CivilStatus = input("PLEASE INPUT YOUR CIVILSTATUS : ")
    Religion = input("PLEASE INPUT YOUR RELIGION : ")
    Citizenship = input("PLEASE INPUT YOUR CITIZENSHIP : ")
    Height = input("PLEASE INPUT YOUR HEIGHT : ")
    Weight =  input("PLEASE INPUT YOUR WEIGHT : ")
    NameofFather = input("PLEASE INPUT YOUR NAMEOFFATHER : ")
    OccupationofFather = input("PLEASE INPUT YOUR OCCUPATIONOFFATHER : ")
    ContactNumberofFather = input("PLEASE INPUT YOUR CONTACTNUMBEROFFATHER : ")
    NameofMother = input("PLEASE INPUT YOUR NAMEOFMOTHER : ")
    OccupationofMother = input("PLEASE INPUT YOUR OCCUPATIONOFMOTHER : ")
    ContactNumberofMother = input("PLEASE INPUT YOUR CONTACTNUMBEROFMOTHER : ")
    Elementary = input("PLEASE INPUT YOUR ELEMENTARY : ")
    YearAttendedElementary = input("PLEASE INPUT YOUR YEARATTENDEDELEMENTARY : ")
    YearEndedElementary = input("PLEASE INPUT YOUR YEARENDEDELEMENTARY : ")
    HighSchool = input("PLEASE INPUT YOUR HIGHSCHOOL : ")
    YearAttendedHighSchool = input("PLEASE INPUT YOUR YEARATTENDEDHIGHSCHOOL : ")
    YearEndedHighSchool = input("PLEASE INPUT YOUR YEARENDEDHIGHSCHOOL : ")
    College = input("PLEASE INPUT YOUR COLLEGE : ")
    Course = input("PLEASE INPUT YOUR COURSE : ")
    Skills = input("PLEASE INPUT YOUR SKILLS : ")

    print("\n\nMy name is " + Name + ", I am often referred to as " + Nickname + ".\nI am " ,Age, " years old, born in " + Birthmonth + " on " + Birthday + ", " + Birthyear + ".\nI currently reside at " + Address + ".\nI am " + Gender + " by gender and my religion is " + Religion + "." + "\nMy nationality is " + Nationality + ", and I hold " + Citizenship + " citizenship" + ".\nIt is " ,isMarried, "that I am married and my civil status is " + CivilStatus + ".\nMy height is" ,Height, "in cm and I weigh" ,Weight,"in kg." + "\nMy father is " + NameofFather + ", works as a " + OccupationofFather + ".\nHe can be reached at " ,ContactNumberofFather,"\b.\nMy mother name is " + NameofMother + ", is employed as a " + OccupationofMother + "\b.\nShe can be reached at " ,ContactNumberofMother, "\nIn terms of my Educational Background,\nI completed my elementary education at " + Elementary + " from " ,YearAttendedElementary,"to",YearEndedElementary,"\b.\nI then attended High School in " + HighSchool + " from " ,YearAttendedHighSchool,"to",YearEndedHighSchool,"\b.\nI pursued higher education at " + College + ", where I studied " + Course + ".\nI have developed skills in " + Skills + ".\nDeveloping these skills will help me navigate complex situations, enhance my professional growth,\nand contribute more effectively goals.") 

    print("\n====================================================================\n")
    
def Activity4():
    print("\n====================================================================\n")
    print("Activity 4\n")
    Number1 = eval(input("Enter a number --->"))
    Number2 = eval(input("Enter a number --->"))
    answer = Number1 + Number2
    print("The sum of", Number1, "and", Number2, "is", answer)
    print("\n====================================================================\n")

def Activity5():
    print("\n====================================================================\n")
    print("Activity 5\n")
    print("Fahrenheit to Celcius")
    temp=eval(input('\nEnter Temperature in Fahrenheit: '))
    celsius=(temp - 32) * 5/9
    print(f'\n\nThe conversion of {temp} degrees Fahrenheit is {celsius} degrees Celsius\n\nor')
    print(f'\nThe conversion of {temp} degrees Fahrenheit is {round(celsius, 2)} degrees Celsius')
    print("\n====================================================================\n")

def Activity6():
    print("\n====================================================================\n")
    print("Activity 6\n")
    x=5
    print(x)
    x=x+10 
    print(x)
    x=x+15 
    print(x)
    x += 20 
    print(x)
    x=25 
    print(x)
    print("\n====================================================================\n")
    
def Activity7():
    print("\n====================================================================\n")
    print("Activity 7\n")
    gold = 0
    miner = input("What is your name: ")
    isGold = input("Did you mine gold today? ")
    if isGold.lower()=="yes":
        gold += 1
        print(f"Hi {miner}, Today you have a total of {gold} gold.")
    else: 
        print(f"Hi {miner}, Today you have a total of {gold} gold.")
    print("\n====================================================================\n")
    
def Activity8():
    print("\n====================================================================\n")
    print("Activity 8\n")
    password = input("Enter your password: ")
    if password.lower() == "secret": 
        print("Access Granted")
        print("Enjoy using the system")
    elif password.lower() == "1004":
        print("Welcome, Yoon Jeonghan")
        print("Access Granted")
    else:
        print("Incorrect password, Access Denied")

    print("Thank you!")
    print("\n====================================================================\n")
    

def Activity9():
    print("\n====================================================================\n")
    print("Activity 10\n")
    age = eval(input("Enter age: "))
    if age >=1 and age <=7:
        print(f"Toddler")
    elif age >=8 and age <= 13:
        print(f"Pre Teen")
    elif age >=14 and age <=18:
        print(f"Teenager")
    elif age >=19 and age <=31:
        print(f"Early Adulthood")
    elif age >=32 and age <=45:
        print(f"Mid Adulthood")
    elif age >=46 and age <=59:
        print(f"Post Adulthood")
    elif age >=60 and age <=150:
        print(f"Senior")
    print("\n====================================================================\n")
    
def Activity10():
    print("\n====================================================================\n")
    print("Activity 10\n")
    name = input("Enter Your Name: ")
    isStudent = input("Are you a student of DLL(Yes/No): ")
    if isStudent.lower()=="yes":
        print("Welcome to the DLL BSIT Scholarship form") 
        GG = input("Are you from Brgy. Gulang Gulang (yes/no):")
        if GG.lower()=="yes":
            print("Please fillup the second form")
            yearlevel = input("What year are you currently enrolled?\nF-Freshnen\nS-Sophomore\nJ-Junior\nR-Senior\nPlease input your answer here: ")

            if yearlevel.lower() == 'f':
                print(f"Hi {name}, Freshmen, Welcome to DLL")

            elif yearlevel.lower() == 's': 
                print(f"Hi {name}, Sophomore, Welcome to DLL")

            elif yearlevel.lower() == 'j': 
                print(f"Hi {name}, Junior, Welcome to DLL")

            elif yearlevel.lower() == 'r': 
                print(f"Hi {name}, Senior, Welcome to DLL")

            else:
                print("Invalid Option")
            IsNeeded = input("Would you like to apply for a scholarship? (yes/no): ")

            if IsNeeded.lower() == "yes":
                print("Scholarship approved")
            else:
                print("Unfortunately, this scholarship grant are only for residents of Gulang-Gulang")
            print("Your form has been successfully submitted")
    print("\n====================================================================\n")
    
def Activity11():
    print("\n====================================================================\n")
    print("Activity 11\n")
    for hannie in range(1,5):
        print("hanniehae")
        name = input("Hi! Please input your name: ")
        print(f"Hi {name}")
    print("\n====================================================================\n")
    
def Activity12():
    print("\n====================================================================\n")
    print("Activity 12\n")
    for k in range(1,10,3):
	    print(k)
    print("\n====================================================================\n")
    
def Activity13():
    print("\n====================================================================\n")
    print("Activity 13\n")
    print("Factorial\n")
    f = eval(input("Enter any number to factor: "))
    outcome = 1
    for x in range(f, 0, -1):
        outcome *= x
    print(f"The Factorial of {f} is {outcome} ")
    print("\n====================================================================\n")

def Activity14():
    print("\n====================================================================\n")
    print("Activity 14\n")
    for k in range (0,11):
        for y in range(0,11):
            print("*", end="")
        print()
    print("\n====================================================================\n")

def Activity15():
    print("\n====================================================================\n")
    print("Activity 15\n")
    for k in range (0,11):
        print(k, end="")
        for y in range(0,k):
            print("*", end="")
        print("")
    print("\n====================================================================\n")
    
def Activity16():
    print("\n====================================================================\n")
    print("Activity 16\n")
    for x in range(1,6):
        for y in range(1, x + 1):
            print(" ", end = " ")
        for z in range(6, x, -1):
            print("^",end=" ")
        for k in range(6, x, -1):
            print("*",end=" ")
        print()
    print("\n====================================================================\n")
    
def Activity17():
    print("\n====================================================================\n")
    print("Activity 17\n")
    col = eval(input("Enter number of columns: "))
    for x in range(1, 11):
        for y in range(1,col + 1):
            print(f"{x} x {y} = {x*y}",end = "\t")
        print()
    print("\n====================================================================\n")
    
def Activity18():
    print("\n====================================================================\n")
    print("Activity 18\n")
    no = eval(input("Enter number of triangles: "))
    for x in range(1, 5):
        for k in range(1,no + 1):
            for z in range(1,x + 1):
                print("*", end= " ")

            for e in range(5, x, -1):
                print(" ", end=" ")
        print()
    print("\n====================================================================\n")
    
def Activity19():
    print("\n====================================================================\n")
    print("Activity 19\n")
    tuloy = True
    while tuloy == True:
        name = input("Please enter a name: ")

        if name.lower() == "stop":
            print("Program Terminated")
            break
            tuloy = False
        else:
            continue
    print("\n====================================================================\n")
    
def Activity20():
    print("\n====================================================================\n")
    print("Activity 21\n")
    isContinue = True
    no = 0
    while isContinue == True:
        ask = input("Would you like to add another triangle (yes / no): ")

        if ask.lower() == "no":
            print("PROGRAM TERMINATED")
            break
            isContinue = False
        else:
            no += 1
            for x in range(1, 5):
                for r in range(1,no + 1):
                    for y in range(1,x + 1):
                        print("*", end= " ")

                    for z in range(5, x, -1):
                        print(" ", end=" ")
                print()
            continue
    print("\n====================================================================\n")
      
def Activity21():
    print("\n====================================================================\n")
    print("Activity 21\n")
    def pang_hello():
        print("Hello Kyzel")

    def pang_hello_v2(name):
        print(f"Hello {name}")

    def activity2():
        num1 = eval(input("Enter a number: "))
        num2 = eval(input("Enter a number: "))
        answer = num1 + num2
        print(num1 , " plus " , num2 , " = " , answer)

    tuloy = True
    while tuloy == True:
        ask = input("Please provide a name: ")

        if ask.lower() != "stop":
            pang_hello_v2(ask)
            if ask.lower() == "2":
                activity2()
            continue
        
        else:
            break
    print("\n====================================================================\n")
    
def Activity22():
    print("\n====================================================================\n")
    print("Activity 22\n")
    #Name listing and then count names

    loop = True
    names = []
    while loop == True:
        Name = input("What name would you like to add? ")
        if Name.lower() == "stop":
            print(names)
            print(f"You have entered {len(names)} names! ")
            break
        else:
            names.append(Name)
    print("\n====================================================================\n")
    
def Activity23():
    print("\n====================================================================\n")
    print("Activity 23\n")
    def factorial(number):
        fact = 1
        for k in range(number, 0, -1):
            fact *= 1
        return fact
    print("\n====================================================================\n")
    
def Activity24():
    print("\n====================================================================\n")
    print("Activity 24\n")
    from Activity23 import factorial
    print(f"The Factorial of 4 is {factorial(4)}")
    print("\n====================================================================\n")
    
def Activity25():
    print("\n====================================================================\n")
    print("Activity 25\n")
    # Python list
    fruits = ["apples", "banana", "oranges", "star apple", "grapes"]
    print(fruits)

    #Indexing / Index - address / location of an item inside a list 
    #           0       1           2           3           4
    #fruits = ["apples", "banana", "oranges", "star apple", "grapes"]
    print(f"My favorite childhood fruit is {fruits[3]}")

    print(f"The last item on the list is {fruits[-1]}")

    #adding another item on the list
    fruits.append("longgan")
    print(fruits)
    fruits.append("strawberry")
    print(fruits)
    #inserting item on a specific index
    fruits.insert(3, "strawberry")
    print(fruits)
    fruits.remove("longgan")
    print(fruits)

    while True:
        fruits = input("Do you wish to add more fruits: ")

        if fruits.lower() == "no":
            print(fruits)
            break
        else:
            fruits.append(fruits)
            print("Fruit added to list ")
            continue
    print("\n====================================================================\n")

def code_challenge1():
    print("\n====================================================================\n")
    print("Code Challenge 1\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t*\n\t\t\t\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t\t\t\t\t\t*\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n====================================================================\n")

def code_challenge2():
    print("\n====================================================================\n")
    print("Code Challenge 2\n")
    name = input("Please enter a name -----> ")
    print("Hi", name)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t*\n\t\t\t\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t\t*\t\t    ","Hi", name,"\t\t\t*\t\n\t\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t\t\t\t\t\t*\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n====================================================================\n")

def code_challenge3():
    print("\n====================================================================\n")
    print("Code Challenge 3\n")
    Name = input("PLEASE INPUT YOUR NAME : ")               
    Nickname = input("PLEASE INPUT YOUR NICKNAME : ")
    Age = input("PLEASE INPUT YOUR AGE : ")
    Birthmonth = input("PLEASE INPUT YOUR BIRTHMONTH : ")
    Birthday = input("PLEASE INPUT YOUR BIRTHDAY : ")
    Birthyear = input("PLEASE INPUT YOUR BIRTHYEAR : ")
    Gender = input("PLEASE INPUT YOUR GENDER : ")
    Address = input("PLEASE INPUT YOUR ADDRESS : ")
    Nationality = input("PLEASE INPUT YOUR NATIONALITY : ")
    isMarried = False
    CivilStatus = input("PLEASE INPUT YOUR CIVILSTATUS : ")
    Religion = input("PLEASE INPUT YOUR RELIGION : ")
    Citizenship = input("PLEASE INPUT YOUR CITIZENSHIP : ")
    Height = input("PLEASE INPUT YOUR HEIGHT : ")
    Weight =  input("PLEASE INPUT YOUR WEIGHT : ")
    NameofFather = input("PLEASE INPUT YOUR NAMEOFFATHER : ")
    OccupationofFather = input("PLEASE INPUT YOUR OCCUPATIONOFFATHER : ")
    ContactNumberofFather = input("PLEASE INPUT YOUR CONTACTNUMBEROFFATHER : ")
    NameofMother = input("PLEASE INPUT YOUR NAMEOFMOTHER : ")
    OccupationofMother = input("PLEASE INPUT YOUR OCCUPATIONOFMOTHER : ")
    ContactNumberofMother = input("PLEASE INPUT YOUR CONTACTNUMBEROFMOTHER : ")
    Elementary = input("PLEASE INPUT YOUR ELEMENTARY : ")
    YearAttendedElementary = input("PLEASE INPUT YOUR YEARATTENDEDELEMENTARY : ")
    YearEndedElementary = input("PLEASE INPUT YOUR YEARENDEDELEMENTARY : ")
    HighSchool = input("PLEASE INPUT YOUR HIGHSCHOOL : ")
    YearAttendedHighSchool = input("PLEASE INPUT YOUR YEARATTENDEDHIGHSCHOOL : ")
    YearEndedHighSchool = input("PLEASE INPUT YOUR YEARENDEDHIGHSCHOOL : ")
    College = input("PLEASE INPUT YOUR COLLEGE : ")
    Course = input("PLEASE INPUT YOUR COURSE : ")
    Skills = input("PLEASE INPUT YOUR SKILLS : ")

    print("\n\nMy name is " + Name + ", I am often referred to as " + Nickname + ".\nI am " ,Age, " years old, born in " + Birthmonth + " on " + Birthday + ", " + Birthyear + ".\nI currently reside at " + Address + ".\nI am " + Gender + " by gender and my religion is " + Religion + "." + "\nMy nationality is " + Nationality + ", and I hold " + Citizenship + " citizenship" + ".\nIt is " ,isMarried, "that I am married and my civil status is " + CivilStatus + ".\nMy height is" ,Height, "in cm and I weigh" ,Weight,"in kg." + "\nMy father is " + NameofFather + ", works as a " + OccupationofFather + ".\nHe can be reached at " ,ContactNumberofFather,"\b.\nMy mother name is " + NameofMother + ", is employed as a " + OccupationofMother + "\b.\nShe can be reached at " ,ContactNumberofMother, "\nIn terms of my Educational Background,\nI completed my elementary education at " + Elementary + " from " ,YearAttendedElementary,"to",YearEndedElementary,"\b.\nI then attended High School in " + HighSchool + " from " ,YearAttendedHighSchool,"to",YearEndedHighSchool,"\b.\nI pursued higher education at " + College + ", where I studied " + Course + ".\nI have developed skills in " + Skills + ".\nDeveloping these skills will help me navigate complex situations, enhance my professional growth,\nand contribute more effectively goals.") 

    print("\n====================================================================\n")

def code_challenge4():
    print("\n====================================================================\n")
    print("Code Challenge 4\n")
    number1 = eval(input("Enter a number --> "))
    number2 = eval(input("Enter a number --> "))
    answer1 = number1 + number2
    answer2 = number1 - number2
    answer3 = number1 * number2
    answer4 = number1/number2
    answer5 = number1 ** number2
    answer6 = number1 % number2
    answer7 = number1 // number2
    print("The sum of", number1, "and", number2, "is", answer1)
    print("The difference of", number1, "and", number2, "is", answer2)
    print("The product of", number1, "and", number2, "is", answer3)
    print("The quotient of", number1, "and", number2, "is", answer4) 
    print("The exponent by", number1, "and", number2, "is", answer5)
    print("The remainder of", number1, "and", number2, "is", answer6)
    print("The floor division of", number1,"and", number2, "is", answer7)
    print("\n====================================================================\n")

def code_challenge5():
    print("\n====================================================================\n")
    print("Code Challenge 5\n")
    name = input("Please enter your name: ")
    deposit = eval(input("Please enter amount to deposit: "))
    one_th = deposit // 1000
    one_th1 = deposit % 1000
    five_h = one_th1 // 500
    five_h1  = one_th1 % 500
    two_h = five_h1 // 200
    two_h1 = five_h1 % 200
    one_h = two_h1 // 100
    one_h1 = two_h1 % 100
    fifty = one_h1 // 50
    fifty1 = one_h1 % 50
    twenty =  fifty1 // 20
    twenty1 = fifty1 % 20
    ten = twenty1 // 10
    ten1 = twenty1 % 10
    five = ten1 // 5
    five1 = ten1 % 5
    one = five1 // 1
    print("Hi,", name,  "the breakdown of your deposit is: ")
    print(one_th, "-1000")
    print(five_h, "-500")
    print(two_h, "-200")
    print(one_h, "-100")
    print(fifty, "-50")
    print(twenty, "-20")
    print(ten, "-10")
    print(five, "-5")
    print(one, "-1")
    print("\n====================================================================\n")

def code_challenge6():
    print("\n====================================================================\n")
    print("Code Challenge 6\n")
    Prelim = eval(input("Enter Prelim grade --> "))
    Midterm = eval(input("Enter Midterm grade --> "))
    Semifinal = eval(input("Enter Semifinal grade --> "))
    Final = eval(input("Enter Final grade --> "))
    Quiz = eval(input("Enter Quiz grade --> "))
    Project = eval(input("Enter Project grade --> "))

    if(Prelim >=65 and Prelim <=100) and (Midterm >=65 and Midterm <=100) and (Semifinal >=65 and Semifinal <=100) and (Final >=65 and Final <=100) and (Quiz >=65 and Quiz <=100) and (Project >=65 and Project <=100):
        FinalGrade = (Prelim * 0.15) + (Midterm * 0.15) + (Semifinal * 0.15) + (Final * 0.15) + (Quiz * 0.25) + (Project * 0.15)
    print(f"Your grade is : {round(FinalGrade, 2)}")
    if FinalGrade > 100 :
        print("Invalid Grade, Perhaps a mistake?")
    elif FinalGrade >= 75 : 
        print("Congratulations! You've passed the course")
    else:
        print("Unfortunately, You failed")
    print("\n====================================================================\n")

def code_challenge7():
    print("\n====================================================================\n")
    print("Code Challenge 7\n")
    name = input("Enter your name :")
    purchased_or_not = input("Did you purchase a grocery today? (Yes or No) :")
    if purchased_or_not.lower() == "yes": 
        purchased = input("What did you purchase :")
    else:
        print(exit("You didn't purchase a grocery today"))
    
    orig_price = eval(input("Item Price :"))
    age = int(input("Age :"))

    #if purchased a grocery, product price would be taxed 12.3% added to the orig_price
    #if the purchase is not more than four thousand
    taxed_price = (orig_price * 0.123) + orig_price

    #if purchase is more than four thousand, there will be a discount of 3.8%
    discount = orig_price - (orig_price * 0.038) 
    discount_taxed_price = orig_price - (discount * 0.123)

    #if you are a senior not exceeding the age of 150, there will be a discount of 12.3%
    discount_senior = orig_price - (taxed_price * 0.123)

    #if senior and purchase is more than four thousand
    two_discount = orig_price - (taxed_price * 0.161)

    if age >= 60 and age <= 150 and orig_price >= 4000 :
    print(f'Total : {round(two_discount,2)}')
    payment = eval(input("Payment :"))
    print(f'Change : {round(payment - two_discount,2)}')
        
    elif orig_price >= 4000 :
    print(f'Total : {round(discount_taxed_price, 2)} ')
    payment = eval(input("Payment :"))
    print(f'Change : {round(payment - discount_taxed_price, 2)} ')

    elif age >= 60 and age <= 150 :
    print(f'Total : {round(discount_senior,2)} ')
    payment = eval(input("Payment :"))
    print(f'Change : {round(payment - discount_senior,2)} ')
        
    else : 
        print(f'Total : {round(taxed_price,2)} ')
        payment = eval(input("Payment :"))
        print(f'Change : {round(payment - taxed_price,2)} ')
    print("\n====================================================================\n")

def code_chalenge8():
    print("\n====================================================================\n")
    print("Code Challenge 8\n")
    print("Summation of 10 random numbers\n")
    x = 0
    even = 0
    odd = 0 
    for k in range (1,11):
        add = eval(input(f"Input (k) = "))
        x += add
        if add % 2 == 0:
            even += add
        else:
            odd += add

    print(f"The Summation of the number is: {x} ")
    print(f"The Summation of the number is: {even} ")
    print(f"The Summation of the number is: {odd} ")
    print("\n====================================================================\n")

def code_challenge9():
    print("\n====================================================================\n")
    print("Code Challenge 9\n")
    z = eval(input("Enter a number: "))
    for x in range(z, 0,-1):
        for y in range(z,x,-1):
            print(" ", end=" ")
        print("* " * x)
    print("\n====================================================================\n")

def code_challenge10():
    print("\n====================================================================\n")
    print("Code Challenge 10\n")
    for k in range(1,6):
        for y in range(6, k, -1):
            print(" ", end = " ")
        for z in range(1, k+1):
            print("*", end=" ")
        for e in range(1, k+1):
            print("*", end =" ")
        print()

    for k in range(1,6):
        for y in range(1, k + 1):
            print(" ", end = " ")
        for z in range(6, k ,-1):
            print("*", end=" ")
        for e in range(6, k, -1):
            print("*", end =" ")
        print()
    print("\n====================================================================\n")

def code_challenge11():
    print("\n====================================================================\n")
    print("Code Challenge 11\n")
    for k in range(1,5):
        for y in range(5, k, -1):
            print(" ", end = " ")
        for z in range(0, k+0):
            print("*", end=" ")
        for e in range(1, k+0):
            print("*", end =" ")
        print()

    for k in range(1,4):
        for y in range(1, k + 2):
            print(" ", end = " ")
        for z in range(4, k ,-1):
            print("*", end=" ")
        for e in range(3, k, -1):
            print("*", end =" ")
        print()
    print("\n====================================================================\n")

def code_challenge12():
    print("\n====================================================================\n")
    print("Code Challenge 12\n")
    for k in range(1,5):
        for y in range(5, k, -1):
            print(" ", end = " ")
        for z in range(1, k+1):
            print("*", end=" ")
        for e in range(1, k+1):
            print("*", end =" ")
        print()

    for k in range(0,4):
        for y in range(4, 0, -1):
            print(" ", end = " ")
        for z in range(2,4):
            print("*", end=" ")
        for e in range(4, 0, -1):
            print(" ", end =" ")
        print()
    print("\n====================================================================\n")

def code_challenge13():
    print("\n====================================================================\n")
    print("Code Challenge 13\n")
    for k in range(1,7):
        for y in range(6, k, -1):
            print(" ", end = " ")
        for y in range(k, 1, -1):
            print(y, end=" ")
        for z in range(1, k+1):
            print(z, end =" ")
        print()

    for k in range(5,0,-1):
        for y in range(6, k, -1):
            print(" ", end = " ")
        for y in range(k,1,-1):
            print(y, end=" ")
        for z in range(1,k+1):
            print(z, end =" ")
        print()
    print("\n====================================================================\n")
   
def code_challenge14():
    print("\n====================================================================\n")
    print("Code Challenge 14\n")
    for k in range(1,7):
    tuloy = True
    a = 0
    while tuloy == True:
        number = eval(input("Enter a number: "))
        if number == 0:
            print("Program Terminated")
            print(f"The total of the number you enter is {a}")
            break
        else:
            a += number
            continue
    print("\n====================================================================\n")
    
def code_challenge15():
    print("\n====================================================================\n")
    print("Code Challenge 15\n")
    import os

    isContinue = True
    no = 0
    while isContinue == True:
        ask = input("Would you like to add another triangle (yes / no )--> ")

        if ask.lower() == "no":
            print("PROGRAM TERMINATED")
            break
            isContinue = False
        elif ask.lower() == "yes":
            os.system('cls')
            no += 1
            for x in range (1, 6):
                for r in range (1 , no + 1):
                    for y in range (1 , x + 1):
                        print("*", end=" ")
                    for z in range (6, x, -1):
                        print(" ",end=" ")
                print()
        else:
            print("INVALID ANSWER it's only (yes/no)")
            continue
    print("\n====================================================================\n")
    
def code_challenge16():
    print("\n====================================================================\n")
    print("Code Challenge 16\n")
    def denomination(amount):
        print("\nDenomination Breakdown:")
        a = amount // 1000
        amount %= 1000

        b = amount // 500
        amount %= 500

        c = amount // 200
        amount %= 200

        d = amount // 100
        amount %= 100

        e = amount // 50
        amount %= 50

        f = amount // 20
        amount %= 20

        g = amount // 10
        amount %= 10

        h = amount // 5
        amount %= 5

        i = amount // 1

        print(f"1000--- {a}")
        print(f"500---- {b}")
        print(f"200---- {c}")
        print(f"100---- {d}")
        print(f"50----- {e}")
        print(f"20----- {f}")
        print(f"10----- {g}")
        print(f"5------ {h}")
        print(f"1------ {i}")


    accounts = {}

    def create_account():
        username = input("Enter a username: ")
        if username in accounts:
            print("Account already exists!")
        else:
            accounts[username] = 0
            print(f"Account created successfully for {username}.")


    def deposit():
        username = input("Enter your username: ")
        if username in accounts:
            try:
                amount = int(input("Enter amount to deposit: "))
                if amount > 0:
                    accounts[username] += amount
                    print(f"Deposited {amount} successfully. New balance: {accounts[username]}")
                    denomination(amount)
                else:
                    print("Amount must be positive!")
            except ValueError:
                print("Invalid input! Please enter a whole number.")
        else:
            print("Account not found!")


    def withdrawal():
        username = input("Enter your username: ")
        if username in accounts:
            try:
                amount = int(input("Enter amount to withdraw (whole numbers only): "))
                if 0 < amount <= accounts[username]:
                    accounts[username] -= amount
                    print(f"Withdrawn {amount} successfully. Remaining balance: {accounts[username]}")
                    denomination(amount)
                else:
                    print("Insufficient funds or invalid amount!")
            except ValueError:
                print("Invalid input! Please enter a whole number.")
        else:
            print("Account not found!")


    def check_balance():
        username = input("Enter your username: ")
        if username in accounts:
            print(f"Your balance: {accounts[username]}")
        else:
            print("Account not found!")


    def options():
        while True:
            print("\nBanking System")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Exit")
            choice = input("Choose an option (1-5): ")

            if choice == '1':
                create_account()
            elif choice == '2':
                deposit()
            elif choice == '3':
                withdrawal()
            elif choice == '4':
                check_balance()
            elif choice == '5':
                print("Thank you for using the Banking System!")
                break
            else:
                print("Invalid option. Please try again.")

    options()
    print("\n====================================================================\n")
   


   
def main():
    while True:
        x = input("enter a command: ")
        if x == "exit":
            print("programm executed")
            break
        else:
            if x == "sample":
                sample()
            elif x == "Act1":
                Activity1()
            elif x == "Act2": 
                Activity2()
            elif x == "Act3":
                Activity3()
main()


   