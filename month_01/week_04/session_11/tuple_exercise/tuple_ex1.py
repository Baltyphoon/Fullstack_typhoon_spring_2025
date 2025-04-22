"""
Дасгал 1: Кортежийн үндэс.

Python дахь кортеж үүсгэх, хандах, ажиллах дадлага.
"""

# DASGAL 1.1
def create_tuple():
    """
    Эхний 5 эерэг бүхэл тоог агуулсан кортеж үүсгэж буцаа.

    Буцаах утга:
        tuple: 1-ээс 5 хүртэлх тоонуудыг агуулсан кортеж
    """
    # Таны код энд 
    return (1, 2, 3, 4, 5)
    # create_tuple = (1, 2, 3, 4, 5)
    # return create_tuple
print(create_tuple()) # garalt (1, 2, 3, 4, 5)

# DASGAL 1.2
def access_elements(my_tuple):
    """
    Өгөгдсөн кортежоос тодорхой элементүүдийг авч буцаа.

    Аргументууд:
        my_tuple (tuple): Элементүүдийн кортеж

    Буцаах утга:
        tuple: Дараах элементүүдийг агуулсан кортеж:
            - Эхний элемент
            - Сүүлийн элемент
            - Дундах элемент (кортежийн урт сондгой бол)
    """
    # Таны код энд
    ehniih = my_tuple[0]
    goliih = my_tuple[len(my_tuple) // 2] if len(my_tuple) % 2 == 1 else None
    suuliih = my_tuple[-1]
    return (ehniih, suuliih, goliih)
print(access_elements((1, 2, 3, 4, 5))) # garalt (1, 5, 3) first, *middle, last

# DASGAL 1.3 
def tuple_operations():
    """
    Кортежтэй янз бүрийн үйлдлүүдийг гүйцэтгэ.

    Буцаах утга:
        tuple: Дараах утгуудыг агуулсан кортеж:
            - (1, 2, 3) ба (4, 5, 6) кортежуудыг нэгтгэсэн кортеж
            - 5 тоог 3 удаа давтсан кортеж
            - (1, 2, 3, 4, 5) кортежийн урт
    """
    # Таны код энд
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    netgeed = tuple1 + tuple2
    davtalt = (5,) * 3 
    urt = len((1, 2, 3, 4, 5))
    return (netgeed, davtalt, urt)
print(tuple_operations()) # garalt ((1, 2, 3, 4, 5, 6), (5, 5, 5), 5)

# DASGAL 1.4 
def count_elements(my_tuple, element):
    """
    Кортеж дахь элементийн тоог тоол.

    Аргументууд:
        my_tuple (tuple): Элементүүдийн кортеж
        element: Тоолох элемент

    Буцаах утга:
        int: Элемент хэдэн удаа давтагдсан
    """
    # Таны код энд
    return my_tuple.count(element)
example = (1, 2, 1, 1, 2, 1, 2, 3, 4, 5)
print(count_elements(example, 1)) # garalt 4 


# DASGAL 1.5
def tuple_to_other_types(my_tuple):
    """
    Кортежийг бусад өгөгдлийн төрөл рүү хөрвүүлж буцаа.

    Аргументууд:
        my_tuple (tuple): Элементүүдийн кортеж

    Буцаах утга:
        tuple: Дараах утгуудыг агуулсан кортеж:
            - Кортежоос үүсгэсэн жагсаалт
            - Жагсаалтаас үүсгэсэн кортеж
    """
    # Таны код энд
    jagsaalt = list(my_tuple)
    kortej = tuple(jagsaalt)
    return(jagsaalt, kortej)
print(tuple_to_other_types((1, 2, 3)))
