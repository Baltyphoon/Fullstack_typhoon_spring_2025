# garnaas 2 toon utga avna. Tus buriig huvisagchtai holbono.
# garnaas operation utga avna. =, -, *, / iim utguud avaad 
# tahain operationaas hamaaaran 2 toon utgiig urjuuleh nemeh hasah esvel huvaah uiluudiig hiigeed 
# hevlej haruuldag program bichne uu 


num1 = int(input('Give me first number: '))
print(f"{num1}")
num2 = int(input('Give me second number: '))
print(f"{num2}")
operator = input('Утга өгөх')

if operator == "+":
    addition =  int(num1) + int(num2)
    print(f"{num1} + {num2} = {addition}")

if operator ==  "-":
    subtraction = int(num1) - int(num2)
    print(f"{num1} - {num2} = {subtraction}")

if operator == "*":
    multiplication = int(num1) * int(num2)
    print(f"{num1} * {num2} = {multiplication}")

if operator == "/":
    division = int(num1) / int(num2)
    print(f"{num1} / {num2} = {division}")

if operator == "//":
    integer_division = int(num1) // (num2)
    print(f"{num1} // {num2} = {integer_division}")








