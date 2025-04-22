# for loop ashiglaad 10n udaa Hello World gej hevlene uu 
for i in range(10):
    print("Hello World")
    print("###########")

for i in range(10):
    print("Hello World")     # davtahiig build in function 
    print("###########")

# bid nar uursduu yamar negen zuil hiideg function todorhoiliyo.
# function decleration - punkts todorhoiloh
# ()- parametriin haalt
def greeting(name):
    for i in range(2):
         print("Hello {name}")

# function call - punktsiig duudah
greeting("KHangai")
greeting("tamir")
greeting("buyanaa")
greeting("oyunbold")
greeting("balt")


# olon parametrtei punkts

def add(a, b):
    """hoyr toog nemeh.
    Args:
        a (int/float): Ehnii too
        b (int/float): hoyr dahi too
    
    Returns:
        int/float: hoyr toonii niilber
    """
    return a + b 

# punktsiig duudah 
result = add(5, 3)
print(result) # garalt: 8

# 3 parametr avaad tuunii niilberiig ni butsaadag addThree gdeg punktsiig todorhoiloh
# addthree gedeg punkts todorhoiloh
# 3 argument uguud tuniigee shalgah 
def addThree(a, b, c):
    return a+b+c
result1 = addThree(4, 5, 6) 
print(result1) # garalt 15
# 2 parametr avaad tuunii urjveriig bustaadag
# multiply gedeg punkts todorhoiloh
# 2 argumentdaa utguud ugvh function test
def multiply(a, b):
    return a*b
result2 = multiply(4, 5)
print("Hariu ni:" + str(result2)) # garalt 20




