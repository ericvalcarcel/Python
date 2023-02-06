Gryffindor = 0 
Ravenclaw  = 0
Hufflepuff = 0
Slytherin  = 0

answer = int(input('Q1) What do you prefer?\n    1)Donald Duck \n    2)Donald Trump\n'))
if answer == 1:
   Gryffindor += 1
   Ravenclaw += 1
elif answer == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print ('Wrong Input')

answer2 = int(input('Q2) When im dead, i want people to remember me as: \n    1)The wise \n    2)The good \n    3)The bold \n    4)The great\n'))
if answer2 == 1:
    Gryffindor += 1
elif answer2 == 2:
    Ravenclaw += 1
elif answer2 == 3:
    Hufflepuff += 1
elif answer2 == 4:
    Slytherin += 1
else:
    print('Wrong Input!')

answer3 = int(input('Q3) Which kind of instrument most pleases your ear? \n    1)The violin \n    2)The trumpet \n    3)The piano \n    4)The drum\n'))
if answer3 == 1:
    Gryffindor += 1
elif answer3 == 2:
    Ravenclaw += 1
elif answer3 == 3:
    Hufflepuff += 1
elif answer3 == 4:
    Slytherin += 1
else:
    print('Wrong Input!')
print('----Results-----')
print('---Gryffindor---')
print (Gryffindor)
print('---Ravenclaw----')
print(Ravenclaw)
print('---Hufflepuff---')
print(Hufflepuff)
print('---Slytherin----')
print(Slytherin)

if Gryffindor >=  Ravenclaw and Gryffindor >= Hufflepuff and Gryffindor >= Slytherin:
    print ('Gryffindor won!')
elif Ravenclaw >= Hufflepuff and Ravenclaw >= Slytherin:
    print('Ravenclaw!')
elif Hufflepuff >= Slytherin:
    print('Hufflepuff!')
else:
    print('Slytherin!')