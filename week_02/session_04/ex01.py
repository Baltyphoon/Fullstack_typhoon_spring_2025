# python variables 
name = "john"
age = 25
height = 1.75
is_studennt = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_studennt))

x  = y = z = 0
print(x, y, z)
a, b, c = 1, 2, 3
print(a, b, c) 

coordinates = (3, 4)
x, y = coordinates
print(x, y) 

a, b = 5, 10 
a, b = b, a #Python ii toon utgiig soloh arga
print(a, b) #10 5 


x - 10 
print(type(x)) # <class 'str'>

# turul huvruuleh 
float_number = float(10)
integer = int(3.14)
string_number = str(42)

print(type(float_number))
print(type(integer))
print(type(string_number))

is_active = True
is_xomleted = False

#and logic - 2 utga 2-uulaa unen ued unen baidag
print(False and False) #false
print(False and True) #false
print(True and False) #false
print(True and True) #true 

# Or logic - ali neg utga ni unen baival unen boldog tohioldol 
print(False or False) #False
print(False or  True) #True
print(True or  False) #True
print(True or True) #True

# Not logic - tuhain boolean utgiin esreg 
print(not False) #True
print(not True) #False

#logic uildluud 
print(True and False) #False
print(True)

#jagsaalt uusgeh
fruits = ["алим", "банана", "интоор"]
mixed_list = [1, "sain baina", 3.14, True]
 
#Elementuud ruu handah 
first_fruit = fruits[0] #"alim"
last_fruit = fruits[-1] #"intoor"

#jagsaaltiig uurchluh 
fruits.append("ulaan looli") #tugsguld nemeh
fruits.insert(1, "mango") #Todorhoi bairlald oruulah 
fruits.remove("банана") #Utgaar ni hasah 
popped_fruits = fruits.pop() #Suuliin elementiig hasaj butsaah 

# jagsaaltiig hesegchlel 
numbers = [0, 1, 2, 3, 4, 5]
subset = numbers[1:4] # [1, 2, 3]


#hyzgaar uusgeh 
numbers = range(5) # 0, 1, 2, 3, 4, 5 
print(numbers)
# range (ehlel, tugsgul)
numbers = range(2, 7) # 2, 3, 4, 5, 6, 
print = numbers
#range(ehlel, tugsgul, alham)
even_numbers = range(0, 10, 2) # 0, 2, 4, 6, 8 
#hyzgaariig jagsaalt bolgoh 
numbers_list = lsit(range(5)) #[0, 1, 2, 3, 4]
print(numbers_list)

x = 10 #undsen onoolt
# niilmel onoolt
x += 5 # x = x + 5 (15)
x -= 3 # x = x - 3 (12)
x *= 2 # x = x * 2 (24)
x /= 4 # x = x / 4 (6)
x //= 2 # x = x // 2 (3.0)
x %= 2 # x = x % 2 (1.0)
x **= 3 # x = x ** 3 (1.0)

a = 10 
b = 5 
equal = a == b #false
not_equal = a != b #true
greater_than = a > b #true
less_than = a < b #false
greater_equal = a >= b #true
less_equal = a <= b #false

# ginjin haritsuulalt
result = 1 < 3 < 5 #true (1 < 3  and 3 < 5 gesentei adil )
result = 5 > 3 < 1 # false (5 > 3 and 3 < 1 gesentei adil )
