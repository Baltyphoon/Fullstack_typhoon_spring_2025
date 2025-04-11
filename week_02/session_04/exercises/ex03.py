# dasgal 1
a = 15 
b = 7 
subtraction_result = a - b 
print(f"{a} - {b} = {subtraction_result}")
print(f"Үр дүнгийн төрөл: {type(subtraction_result)}")
multiplication_result = a * b 
print(f"{a} * {b} = {multiplication_result}")
print(f"Үр дүнгийн төрөл: {type(multiplication_result)}")
division_result = a / b 
print(f"{a} / {b} = {division_result}")
print(f"Үр дүнгийн төрөл: {type(division_result)}")
integer_division = a // b 
print(f"{a} // {b} = {integer_division}")
print(f"Үр дүнгийн төрөл: {type(integer_division)}")
remainder_result = a % b 
print(f"{a} % {b} = {remainder_result}")
print(f"Үр дүнгийн төрөл: {type(remainder_result)}")


#dasgal 2 
import math
# 25-ын квадрат язгуурыг тооцоолох
sqrt_result = math.sqrt(25)
print(f"25-ын квадрат язгуур = {sqrt_result}")

# -15-ын абсолют утгыг тооцоолох
number = -15
absolute_value = abs(number)
print(f"Absolute utga :" , {absolute_value})

# Тоог 2 орны нарийвчлалтай тоймлох
number = 22.323432423
toimlogdson_too = round(number, 2)
print(f"toimlogdson too :" , toimlogdson_too)

# 4.3-ын дээд хязгаарыг тооцоолох (4.3-аас их буюу тэнцүү хамгийн бага бүхэл тоо)
import math
number = 4.3 
print(f"deed hzygaar : {math.ceil(number)}")
number = 4.7 
print(f"dood hzygaar : {math.floor(number)}")

# 5 факториал (5!) тооцоолох
factorial_5 = math.factorial(5)
print(factorial_5)

# 48 ба 18-ын хамгийн их ерөнхий хуваагчийг (ХЕХХ) тооцоолох
a = 48
b = 18
hmm = math.gcd(a, b)
print(f"48 ba 18 iin XEXX ni : {hmm}")

# 90 градусын синусыг тооцоолох (эхлээд радианруу хөрвүүлэх)
degrees = 90
radians = math.radians(degrees)
sin_value = math.sin(radians)
print(f"{degrees} градусын синус = {sin_value}")

# 100-ын логарифм (суурь 10)-ыг тооцоолох
number = 100
log_value = math.log10(number)
print(f"log10.({number}) = {log_value}")


# DASGAL 3

decimal_num = 42
binary_num = bin(decimal_num)
print(f"{decimal_num} хоёртын системд: {binary_num}")

octal_num = oct(decimal_num)
print(f"{decimal_num} наймтын системд: {octal_num}")

hex_num = hex(decimal_num)
print(f"{decimal_num} арван зургаатын системд: {hex_num}")

binary_str = "101010"
decimal_from_bin = int(binary_str, 2)
print(f"{binary_str} (2-тын) = {decimal_from_bin} (10-т)")

octal_str = "52"
decimal_from_oct = int(octal_str, 8)
print(f"{octal_str} (8-тын) = {decimal_from_oct} (10-т)")

hex_str = "2A"
decimal_from_hex = int(hex_str, 16)
print(f"{hex_str} (16-тын) = {decimal_from_hex} (10-т)")








