
# utga butsaah 
def square(x):
    """Тооны квадратыг олох.
    Args:
        x (int/float): Квадратыг олох тоо
    Returns:
        int/float: Тооны квадрат
    """
    return x ** 2
# Функцийг дуудах
result = square(4)
print(result) # Гаралт: 16


# Олон утга буцаах (Returning multiple values)
def numbers_stats(numbers):
    """Тооны жагсаалтын статистик үзүүлэлтүүдийг тооцоолох.
    Args:
        numbers (list): Тооны жагсаалт
    Returns:
        tuple: (нийлбэр, дундаж, хамгийн_их, хамгийн_бага)
    """
    total = sum(numbers)
    average = total / len(numbers)
    max_num = max(numbers)
    min_num = min(numbers)
    
    return total, average, max_num, min_num
# Функцийг дуудах
numbers = [5, 10, 15, 20, 25]
total, average, max_num, min_num = numbers_stats(numbers)

print(f"Нийлбэр: {total}")
print(f"Дундаж: {average}")
print(f"Хамгийн их: {max_num}")
print(f"Хамгийн бага: {min_num}")