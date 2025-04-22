# logical operators 

x = 5 
y = 10 

print(x > 0 and y > 0) # True 
print(x > 7 or y > 7) # True
print(not x > 7) # True 

# 
i_was_born_in_mongolia = True 
i_havee_mongolian_passport = True 
if i_was_born_in_mongolia and i_havee_mongolian_passport: 
    print("i'm mongolian")
else: 
    print("i'm not mongolian")

# 
score = int(input('Give me your grade: '))

if score >= 90: 
    print("А үнэлгээ")
elif score >= 80:
    print("B үнэлгээ")
elif score >= 70:
    print("C үнэлгээ")
elif score >= 60:
    print("D үнэлгээ")
else:
    print("F үнэлгээ") 

# 