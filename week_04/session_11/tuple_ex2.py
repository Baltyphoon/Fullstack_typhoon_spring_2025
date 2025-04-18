"""
Дасгал 2: Кортежийн үйлдлүүд.

Кортеж болон түүний өөрчлөгдөхгүй шинж чанартай ажиллах дадлага.
"""
# DSAGAL 2.1 

def create_tuple():
    """
    Эхний 5 эерэг бүхэл тоог агуулсан кортеж үүсгэж буцаа.

    Буцаах утга:
        tuple: 1-ээс 5 хүртэлх тоонуудыг агуулсан кортеж
    """
    # Таны код энд
    return (1, 2, 3, 4, 5)
print(create_tuple()) # garalt (1, 2, 3, 4, 5)
# DASGAL 2.2
def tuple_to_list_and_back(my_tuple):
    """
    Кортежийг жагсаалт болгож, өөрчилж, дахин кортеж болго.

    Аргументууд:
        my_tuple (tuple): Элементүүдийн кортеж

    Буцаах утга:
        tuple: Эхний болон сүүлийн элементүүд нь солигдсон шинэ кортеж
    """
    # Таны код энд
    jagsaalt = list(my_tuple)
    if len(jagsaalt) >= 2:
        jagsaalt[0], jagsaalt[-1] = jagsaalt[-1], jagsaalt[0]
    kortej = tuple(jagsaalt)
    return kortej
print(tuple_to_list_and_back((1, 2, 3, 4))) #garalt (4, 2, 3, 1)

# DASGAL 2.3 
def tuple_unpacking(person_info):
    """
    Кортежийг задалж, форматласан тэмдэгт мөр буцаа.

    Аргументууд:
        person_info (tuple): (нэр, нас, хот) агуулсан кортеж

    Буцаах утга:
        str: "Нэр нь Нас настай бөгөөд Хот-д амьдардаг" гэх мэт форматласан тэмдэгт мөр
    """
    # Таны код энд
    ner, nas, hot = person_info
    # return f"{ner} ni {nas} nastai buguud {hot}-d amidardag"
    return(ner + " ni " + str(nas) + " nastai buguud " + hot + " -d amidarag")
print(tuple_unpacking(("temuujin", 25, "Ulaanbaatar"))) # garalt temuujin ni 25 nastai buguud Ulaanbaatar -d amidarag

# DASGAL 2.4
def nested_tuple_access(nested_tuple):
    """
    Давхар кортеж бүтцээс элементүүдэд хандах.

    Аргументууд:
        nested_tuple (tuple): Давхар кортеж бүтэц

    Буцаах утга:
        list: Давхар кортежоос тодорхой элементүүдийг агуулсан жагсаалт
    """
    # Таны код энд
    # Эхний дотоод кортежийн эхний элемент,
    # сүүлийн дотоод кортежийн сүүлийн элемент,
    # дундах дотоод кортежийн дундах элементийг агуулсан жагсаалт буцаа
    nested_tuple = ((1, 2, 3,), (4, 5, 6), (7, 8, 9))
    ehniih = nested_tuple[0] [0]
    dundah_kortej = nested_tuple[len(nested_tuple) // 2]
    dundah_element = dundah_kortej[len(dundah_kortej) // 2]
    suuliih = nested_tuple[-1] [-1]
    return [ehniih, dundah_element, suuliih]
print(nested_tuple_access(((1, 2, 3), (4, 5, 6), (7, 8, 9))))


# DASGAL 2.5
# Тест тохиолдлууд
if __name__ == "__main__":
    # create_tuple функцийг шалгах
    my_tuple = create_tuple()
    print(f"Үүсгэсэн кортеж: {my_tuple}")  # Хэвлэх: Үүсгэсэн кортеж: (1, 2, 3, 4, 5)

    # tuple_to_list_and_back функцийг шалгах
    modified_tuple = tuple_to_list_and_back((1, 2, 3, 4, 5))
    print(
        f"Өөрчилсөн кортеж: {modified_tuple}"
    )  # Хэвлэх: Өөрчилсөн кортеж: (5, 2, 3, 4, 1)

    # tuple_unpacking функцийг шалгах
    info = ("Болд", 30, "Улаанбаатар")
    formatted = tuple_unpacking(info)
    print(formatted)  # Хэвлэх: Болд нь 30 настай бөгөөд Улаанбаатар-д амьдардаг

    # nested_tuple_access функцийг шалгах
    nested = ((1, 2), (3, 4, 5), (6, 7))
    elements = nested_tuple_access(nested)
    print(f"Давхар элементүүд: {elements}")  # Хэвлэх: Давхар элементүүд: [1, 4, 7]