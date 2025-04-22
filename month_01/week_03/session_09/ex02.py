# 1.
def profile(name, age):
    print(f"{name} ni {age} nastai.")

# bairlalaar damjuulah
profile("bold", 25)

# nereer ni damjuulah
profile(age=25, name="bold")

#2.
def profile(name, age=30, city="ulaanbaatar"):
    print(f"{name} ni {age} nastai, {city}-d amidardag")
#Function-g duudah 
profile("bold") # anhnii utguudiig avna
profile("saraa", 25) # nas daragdaj buyu soligdono 
profile("bayr", city="darhan") # hotiin ner soligdono buyu daragdana

# many arguments 
def sum(*numbers):
    """Дурын тооны аргументуудын нийлбэрийг олох.
    Args:
        *numbers: Хувьсах тооны аргументууд
    Returns:
        int/float: Өгөгдсөн тоонуудын нийлбэр
    """
    total = 0
    for number in numbers:
        total += number
    return total
# Функцийг дуудах
print(sum(1, 2, 3)) # Гаралт: 6
print(sum(5, 10, 15, 20)) # Гаралт: 50
