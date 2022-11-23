#Class calculator

#options to calculate
def select_option():
    print("CALCULATOR")
    print ("1.Add")
    print ("2.Subtract")
    print ("3.Divide")
    print ("4.Multiply")
    print ("5.Exit")

select_option()

#statement ask to display one of the options above if one of the numbers is inserted
while True:
    try:
        choice = int(input ("Choose one of the options above? 1/ 2/ 3 /4 /5: "))
        break
    except ValueError:
        print("Please input one of the numbers/choices above!")

def Add(x, y):
    return x + y
    
def Subtract(x, y):
    return x - y
    
def Divide(x, y):
    return x / y
    
def Multiply(x , y):
    return x * y



if choice == 1:
    num1 = int (input("Input your first number:"))
    num2 = int (input("Input your second number:"))
    print (num1, "+", num2, "=", Add(num1, num2))
    f = open("Calc.txt", 'a')
    f.write(str(num1))
    f.write("+")
    f.write(str(num2))
    f.write('=')
    f.write(str(Add(num1, num2)))
    f.close()
    

elif choice == 2:
    num1 = int (input("Input your first number:"))
    num2 = int (input("Input your second number:"))
    print (num1,"-", num2, "=", Subtract(num1, num2))
    f = open("Calc.txt", "a")
    f.write("\n")
    f.write (str(num1))
    f.write("-")
    f.write(str(num2))
    f.write("=")
    f.write(str(Subtract(num1, num2)))
    f.close()

elif choice == 3:
    num1 = int (input("Input your first number:"))
    num2 = int (input("Input your second number:"))
    print (num1, "/", num2, "=", Divide(num1, num2))
    f = open("Calc.txt", "a")
    f.write("\n ")
    f.write(str(num1))
    f.write("/")
    f.write(str(num2))
    f.write('=')
    f.write(str(Divide(num1, num2)))
    f.close()

elif choice == 4:
    num1 = int (input("Input your first number:"))
    num2 = int (input("Input your second number:"))
    print (num1, "*", num2, "=", Multiply(num1, num2))
    f = open ("Calc.txt", 'a')
    f.write("\n")
    f.write (str(num1))
    f.write("*")
    f.write(str(num2))
    f.write("=")
    f.write(str(Multiply(num1, num2)))
    f.close

# elif choice == 4:
#     print("Choice from the list above")
    

elif choice == 5:
   exit()

else:
    print("Invalid input")
    

#Currency converter
#options for user which currency to convert from
def Select_Currency():
    while True:
        try:
         print("Which currency would you like to convert from?")
         print("1.ZAR")
         print("2.EUR")
         print("3.USD")
         print("4.Exit")
         x = input("Select yout first option:")
         ans1 = int(x)

#options for user which currency to convert to
         print("Which currency would you like to covert to?")
         print("1.ZAR")
         print("2.EUR")
         print("3.USD")
         print("4.Exit")
         y = input("Select your second option:")
         ans2 = int (y)

#this if-statements displays error messages if you try to convert two of the same currencies
         if ans1 == 1 and ans2 == 1:
            print ("Please choose two different currencies!")
            Select_Currency()

         if ans1 == 2 and ans2 == 2:
            print("Please choose two different currencies!")
            Select_Currency()

         if ans1 == 3 and ans2 == 3:
            print("Please choose two different currencies!")
            Select_Currency()


         elif ans1 == 1 and ans2 == 2:
            ZAR_to_EUR()
            Select_Currency()

         elif ans1 == 1 and ans2 == 3:
            ZAR_to_USD()
            Select_Currency()

         elif ans1 == 1 and ans2 == 4:
            exit()

        ###############################################################

         elif ans1 == 2 and ans2 == 1:
            EUR_to_ZAR()
            Select_Currency()

         elif ans1 == 2 and ans2 == 3:
            EUR_to_USD()
            Select_Currency()

         elif ans1 == 4 and ans2== 4:
            exit()


        ##########################################################

         elif ans1 == 3 and ans2 == 1:
            USD_to_ZAR()
            Select_Currency()

         elif ans1 == 3 and ans2 ==2:
            USD_to_EUR()
            Select_Currency()

         elif ans1 == 3 and ans2 == 3:
            print("error")
            Select_Currency()

         elif ans1 == 3 and ans2 == 4:
            exit()

        ##########################################################

         else:
            exit()
         break
        except ValueError:
            print("error")

#convert ZAR to EUR
def ZAR_to_EUR():
    while True:
        try:
         x = input("How much would you like to convert to EUR? ")
         answer = int(x) * float(0.06)
         print(answer)
         break
        except ValueError:
            print("error")

#convert ZAR to USD
def ZAR_to_USD():
    while True:
        try:
         x = input("How much would you like to convert to USD? ")
         answer = int(x) * float(0.0666)
         print(answer)
         break
        except ValueError:
            print("error")

#covert EUR to ZAR
def EUR_to_ZAR():
    while True:
        try:
         x = input("How much would you like to convert to ZAR?")
         answer = int(x) * float(16,46)
         print(answer)
         break
        except ValueError:
            print("error")

#convert EUR to USD
def EUR_to_USD():
    while True:
        try:
         x = input("How much would you like to convert to USD?")
         answer = int(x) * float(1.10)
         print(answer)
         break
        except ValueError:
            print("error")

#convert USD to ZAR
def USD_to_ZAR():
    while True:
        try:
         x = input("How much would you like to convert to ZAR? ")
         answer = int(x) * float(14.99)
         print(answer)
         break
        except ValueError:
            print("error")

#convert USD to EUR
def USD_to_EUR():
    while True:
        try:
         x = input("How much would like to convert to EUR? ")
         answer = int(x) * float(0.91)
         print(answer)
         break
        except ValueError:
            print("error")
            
Select_Currency()
    








