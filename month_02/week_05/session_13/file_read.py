# File REad

# Open File 
file = open('file_intro.md', 'r')
content = file.read()
print(content)
file.close()

# 'r' - Унших (анхны утга)
# 'w' - Бичих (шинэ файл үүсгэх эсвэл одоо байгаа файлыг хоослох)
# 'a' - Нэмэх (файлын төгсгөлд нэмнэ)
# 'x' - Exculusive Creation 
# 'b' - Хоёртын горим (бусад горимтой хамт хэрэглэнэ, ж.нь, 'rb')
# 't' - Текст горим (анхны утга)
# '+' - Update (read and write)

# file read line by line 
file = open('file_intro.md', 'r')
for i in range(8):
    content = file.readline()
    print(content)
file.close()

# file read and all lines
file = open('file_intro.md', 'r')
content = file.readlines()
print(content)
file.close()