#dasgal 1 

number = int(input("Number: "))
if number < 0 :
    print("Number is negative.")
elif number == 0:
    print("Tegtei tentsuuyum bnaa")
else: 
    print("Number is Positive")

#dasgal 2

year = int(input("Number of year ?"))
if (year % 4 == 0 and year % 400 == 0):
    print(str(year) + "ni undur jil ")

