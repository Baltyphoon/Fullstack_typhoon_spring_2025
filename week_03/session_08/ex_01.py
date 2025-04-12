# Python - For loop

# Recapture 

colors = ["red", "yellow", "blue", "green", "purple"] # list
print(colors)

#print out "blue"

print(colors[2]) #blue
print(colors[0])
print(colors[1])
print(colors[3])
print(colors[4])
# print(color[5])

# Solution - Loop
# For - Loop
for a in colors:
    print(a)

# For range
for i in range(9):
    print(i)

for i in range(1, 10):
    print(i)

for i in range(3, 10, 3):
    print(i)


# WHILE - Loop
w = 1 
while w < 9:
    print(w) # infinite loop control C
    w = w + 1 # w += 1 


# exercise 

# WHILe loop ashiglan 10 -aas 100 hurtelx toonuudiig hevle

i = 10 
while i <= 100:
    print(i)
    i = i +1 

# 20s 60 hurtelh tonuudiig zuvhun tegsh 

i = 20 
while i <= 60:
    print(i)
    i = i + 2

i = 20 
while i <= 60:
    if i % 2 == 0:
        print(i)
    i = i + 1

