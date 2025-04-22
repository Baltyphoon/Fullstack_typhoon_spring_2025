#python loops

fruits = ["алим", "банана", "гүзээлзгэнэ"]

# Problem -- 100 shirheg jimsnii turultui list bval yah ve ?
print(fruits[0]) # алим
print(fruits[1]) # банана
print(fruits[2]) # гүзээлзгэнэ  

#Solution - Loop buyu davatalt 

# 1. FOR loop
for fruit in fruits:
    print(fruit)

# 0-ээс 4 хүртэл
for i in range(5): 
    print(i)

# 2s oos 8 hurtel
for i in range(2, 8):
    print(i)

# 1s 10 hurtel , 2 alhamaar
for i in range(1, 10, 2):
    print(i)

# string buyu text 
message = "python"

# Temdegt bureer davtalt 
for char in message:
    print(char)


# enumerate 
fruits_01 = ["алим", "банана", "гүзээлзгэнэ"] 
# index bolon elementiig avah 
for index, fruit in enumerate(fruits_01):
    print(f"index {index}: {fruit}")

#garalt
#index 0: alim
#index 1: banana
#index 2: guzeelzgene

# Todorhoi indexees ehleh 
for index, fruit in enumerate(fruits_01, start=1):
    print(f"index {index}: {fruit}")

#break 
for i in range(10):
    if i == 5:
        break # i нь 5 болсон үед давталтыг зогсоох
print(i)

# continue мэдэгдлийн жишээ
for i in range(10):
    if i % 2 == 0:
        continue # 
    print(i)

# else хэсэгтэй давталтын жишээ 
#break heregleegui ued lese heseg ajillana
for i in range(5):
    print(i)
else:
    print("Давталт дууслаа!")

#break hereglesen ued else heseg ajillahgui 
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("ene heseg ajillahgui")


# double loop 
# urjuuleh husnegt 
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("-----")


# engiin davtalt 
squares = []
for i in range (1,6):
    squares.append(i ** 2)
print(squares)  # [1, 4, 9, 16, 25]

#jagsaaltiuin oilgolt 
squares = [i ** 2 for i in range(1, 6 )]
print(squares) # [1, 4, 9, 16, 25]

#nuhtsultui jagsaaltiin oilgolt 
even_squared = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(even_squared) # [ 4, 16, 36, 64, 100, ]