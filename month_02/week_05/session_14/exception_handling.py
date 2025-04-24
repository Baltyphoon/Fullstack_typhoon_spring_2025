# exception 

# problem 

print('THis line will print')
x = 10
y = 0 

if x == 5: 
    print('Hello')
          
print('Next line')

# Division by Zero 
# print(x / y)

print('Third line')

# Undsen butets - Exception handler 
try: 
    # Aldaa garj bolzohsgui 
    result = 10 / 0
except ZeroDivisionError:
    # Aldaa garval hiih uildel
    print("Tegeer huvaah bolomjgui")

print('Fourth line')

# Olon turliin aldaag barih 
try:
    number = int(input("too oruulna uu : "))
    result = 10 / number
    print(result)
except ValueError:
    print("Zuv too oruulna uu!")
except ZeroDivisionError:
    print("Tegeer huvaah bolomjgui")

print('Fifth line')

# Hed heden aldaag neg door barih
try:
    number = int(input("too oruulna uu : "))
    result = 10/ number
    print(result)
except (ValueError, ZeroDivisionError):
    print("Buruu orolt esvel tegeer huvaah oroldlogo!")

# Hervee yamar neg aldaag busdaas ylgaj chadahgui bol
# buh aldaag barih (bolgoomjtoi heregleh)

 # file = open("noneexistent.txt", "r")

try:
    # ersdeltei code
    file = open("noneexistent.txt", "r")
except Exception as e:
    print(f"aldaa garlaa: {e}")

print("Sixth line")

# aldaanii medeelel avah:
try: 
    x = 10 / 0 
except Exception as e:
    print(f"Aldaanii turul: {type(e).__name__}")
    print(f"Aldaanii message: {str(e)}")

# else block - aldaa garaagui ued ajillana:
try:
    number = int(input("Too oruulna uu :"))
    result = 10 / number
except ValueError:
    print("Zuv too oruulna uu!")
except ZeroDivisionError:
    print("Tegeer huvaah bolomjgui")
else:
    # Aldaa garaagui bol ajillana
    print(f"ur dun : {result}")

# Finally block - aldaa garsan esehees ul hamaaran ajillana:
try:
    # ersdeltei code 
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File oldoogui!")
else:
    print(f"File ner: {file.name}")
    print(f"file undes: {file.undest}")
finally:
    # ul hamaaran ajillana
    if 'file' in locals() and not file.closed:
        file.close()

# Aldaa damjuulah (re-raising):
try: 
    x = int("too bish")
except ValueError:
    print("ValueError bolovsruulj baina...")
    # Aldaag damjuulah
    # raise

# Uur aldaa uusgeh :
try: 
    age = int(input("Nasaa oruulna uu: "))
    if age < 0:
        raise ValueError("Nas surug too baij bolohgui")
except ValueError as e:
    if "invalid literal" in str(e):
        print("Zuv too oruulna uu")
    else:
        print(e)

# Exception chaining: (Aldaa holboh):
try:
    # Anhnii aldaa
    x = int("too bish ")
except ValueError as e:
    # shine aldaa uusgej, anhnii aldaatai holboh
    # raise RuntimeError("Bolovsruulalt amjiltgui bolson") from e 
    print(e)

# traceback module ashiglah: 
import traceback

try: 
    # aldaa garch bolzoshgui code
    1 / 0 
except Exception:
    # Delgerengui traceback medeelel hevleh 
    traceback.print_exc()


# Exercise divide gedeg function bicheed a, b gedeg parametr avdag bolgono u
# enehuu function ni tuhain parametruudiig too esehiig shalgaad too bish bol
# ValueError aldaa ugdug harin 0d huvaalal zeroValueError ugdug bailgaarai 

def divide(a,b):
    try:
        int(a)
        int(b)
        result = a / b 
    except ValueError:
        print("Give me correct number")
    except ValueError:
        print("Give me correct number")
    except ZeroDivisionError:
        print("Do not divide number by zero")
    except Exception:
        print('Error occurated')
    else:
        print(result)

divide(4, 0) # Do not divide number by zero"
divide('4', 5) # Do not divide number by zero"
divide("hi", "hi") #  Give me correct number 
