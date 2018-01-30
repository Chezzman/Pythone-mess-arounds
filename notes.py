
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~INTRODUCTION
camalCaseConvention = "camalCaseConvention"
underscore_convention = "underscore_convention"
#python prefers underscore_convention as the variables

string = "Hello world"
print(string)

integer = 123
print(integer)
#123
print(type(integer))
<class 'int'>

>>> real_num = 3.1415
>>> print(type(real_num))
#<class 'float'>
>>> print(real_num)
#3.1415

>>> a = 3.9
>>> b = 3.4
>>> print(int(b))
#3
>>> print(int(a))
#3
>>> print(float(a))
#3.9

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~PYMATH101
#!/usr/local/bin/python36
#need to find windows version of ^^
print(2+2)
print(3-5)
print(10 - -4)
print(3*9)
print(2**4)


print(7 / 3)
#2.33333333333
print(7 // 3)
#2

print ( 8 % 5 )
#3
#Because there is .3 left over from 8 / 5

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~SENTENCING
#!/usr/local/bin/python36

single_quite_str = 'single quotes'
double_quotes_str = "double quotes"

sentence1 = 'She said "go away," and it hurt'
sentence2 = "She said 'go away,' and it hurt"


sentence3 = 'She said \'go away,\' and it hurt'
sentence4 = "She said \"go away,\" and it hurt"

paragraph = '''This paragraph
has extended the lines
as triple single quotes
'''

print(sentence1)
print(sentence2)

print(sentence3)
print(sentence4)

print(paragraph)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~USING PYTHON API WITH STRING
#!/usr/local/bin/python36

science = "SCIENCE"
future = "future"

print(future)
future = future.upper()
print(future)

print(science.lower())
print(science.title())


science = "       science           "
science = science.strip().upper()
print(science)

#~@~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ STRING MANIPULATION

#!/usr/local/bin/python36



prefix = "python"
suffix = "_rules"

print(prefix + suffix)

astr = prefix + suffix
print(astr)

astr = astr.replace("_rules", "_kills")
astr = astr * 2
print(astr)
astr = astr.replace("_kills", "_rules" )
print(astr)

print(astr.count("_"))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Format
#!/usr/local/bin/python36

n = 11
f = 1.123456
s = "Computers"

print("I have 3 fingers {:d}".format(n))
print("I have 3 fingers {:b}".format(n))
#print it in binary

#There are many format types such as:
# e = exponents
# b- binary (base 2)
# o - octal (base 8)
# d - decimal (base 10)
# x - hexadecimal (base 16)
# f - floats (decimal numbers)
# s- string (default if none is specified)

print("{:f}".format(f))
#1.123456
print("{:.3f}".format(f))
#1.123
print("{:011.3f}".format(f))
#0000001.123

print("{0} {1} {2}".format(n, f, s))

print("{name} own(s) {amount} of {object}".format(
    name = "Charles",
    amount = 69,
    object = "Tequila shots"
))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ STRING MANIPULATION PLUS INPUT
#!/usr/local/bin/python36

# firstname, m. lastname

first_name = str(input("Please enter your first name: "))
middle_name = str(input("Please enter your middle name: "))
last_name = str(input("Please enter your last name: "))

first_name = first_name.capitalize()
middle_name = middle_name.capitalize()
last_name = last_name.capitalize()

name_format = "{first} {middle:.1s} {last}"
print(name_format.format(
    first=first_name,
    middle=middle_name,
    last=last_name
))

#Charle G van Oeffelen

#~~~~~~~~~~~~~~~~~~~~~~~~~~~lists~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

numbers = [5, -6, 2, 4, -5, 1]
names = ["Chaz", "Charles", "Sassy"]
print(names[0])
#Chaz
print(names[1])
#Charles
print(names[2])
#Sassy
print(names[3])
#Traceback (most recent call last):
# File "Printname.py", line 7, in <module>
#    print(names[3])
#IndexError: list index out of range

print(names)
#['Chaz', 'Charles', 'Sassy']
del names[1]
print(names)
#['Chaz', 'Sassy']

mystr = "Hello World"

print(mystr[0])
print(mystr[6])


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~LIST METHODS

alpha = ["a", "b", "c", "d"]
#['a', 'b', 'c', 'd']
alpha.append("e")
alpha = alpha + ["f", "g"]
print(alpha)
#['a', 'b', 'c', 'd', 'e', 'f', 'g']
d_index = alpha.index("d")
print("d_index: " + str(d_index))
#d_index: 3

del alpha[d_index]
print(alpha)
#['a', 'b', 'c', 'e', 'f']

alpha.remove("c")
print(alpha)
#['a', 'b',  'e', 'f']

alpha.insert(2, "c")
print(alpha)
#['a', 'b', 'c', 'e', 'f']

alpha.clear()
print(alpha)
#[]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ADVANCE LISTS(sorting and converting list to string)

alpha1 = ["a", "f", "b", "e", "d"]
alpha2 = ["g", "i", "h"]
alpha3 = "jklmnopqrstuvwxyz"

alpha1.sort()
alpha2.sort()
print(alpha1 + alpha2)
#['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i']
alpha1.insert(2, "c")
print(alpha1 + alpha2)
#['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']


alpha1 = ''.join(alpha1)
alpha2 = ''.join(alpha2)
print(alpha1 + alpha2)
#a b c d e fg h i

alphabet = alpha1 + alpha2 + alpha3
print(alphabet)
#abcdefghijklmnopqrstuvwxyz

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MATH LIST?
#min, max, sum, len
numbers = [3.14, -5, 10, 10**4, 17]
hello_world =  "HelloWorld"

print(min(numbers))
#-5
print(max(numbers))
#10000
print(sum(numbers))
#10025.14
print(len(numbers))
#5

print(min(hello_world))
#H
print(max(hello_world))
#r
print(len(hello_world))
#10


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2D ARRAYS AND ARRAY REFERENCES
#array as it has brackets
#2d arrays hold other arrays

#!usr/local/bin/python36

#import the pprint function from the pprint module as a function calle pretty_print
from pprint import pprint as pretty_print

#import the copy and deepcopy function from the copy module
from copy import copy, deepcopy
#copy for 1D lines
#deepcopy for compound object or 2d or higher
nums_2d = [
    [1,2,3,4,5,6,7],
    [8,9,10,11,12,13,14,15],
    [16,17,18,19,20,21,22]
]

#handling arrays
print(nums_2d[1][3])
#11
print(nums_2d)
#[[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22]]

pretty_print(nums_2d)
#[[1, 2, 3, 4, 5, 6, 7],
# [8, 9, 10, 11, 12, 13, 14, 15],
# [16, 17, 18, 19, 20, 21, 22]]

nums_2d[2][1] = -5
pretty_print(nums_2d)
#[[1, 2, 3, 4, 5, 6, 7],
# [8, 9, 10, 11, 12, 13, 14, 15],
# [16, -5, 18, 19, 20, 21, 22]]

letters = ["A", "B", "C", "D", "E"]
letters_2d = [letters, letters, letters]
pretty_print(letters_2d)
#[['A', 'B', 'C', 'D', 'E'],
# ['A', 'B', 'C', 'D', 'E'],
# ['A', 'B', 'C', 'D', 'E']]
letters_2d[0][0] = "F"
pretty_print(letters_2d)
#[['F', 'B', 'C', 'D', 'E'],
# ['F', 'B', 'C', 'D', 'E'],
# ['F', 'B', 'C', 'D', 'E']]

letters = ["A", "B", "C", "D", "E"]
letters_2d = [copy(letters), copy(letters), copy(letters)]
pretty_print(letters_2d)
letters_2d[0][0] = "F"
pretty_print(letters_2d)
#[['F', 'B', 'C', 'D', 'E'],
# ['A', 'B', 'C', 'D', 'E'],
# ['A', 'B', 'C', 'D', 'E']]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~SCLICING lists

#Use range to generate a list of numbers
a = list(range(0, 10))
print(a)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[0:5])
#[0, 1, 2, 3, 4]

print(a[2:len(a)])
#[2, 3, 4, 5, 6, 7, 8, 9]
#go from two too the length of the list

print(a[:])
#prints entire array

#STEP
print(a[::2])
#[0, 2, 4, 6, 8]

#from 0 to 6 print every other...
print(a[0:6:2])
print(a[0:6:3])
#[0, 2, 4]
#[0, 3]

#goes from top of list backwards
print(a[-1])
print(a[-2])
#9
#8

#goese from 2 to the second from back which is 8(8 not inculed)
print(a[2:-2])
#[2, 3, 4, 5, 6, 7]

#Commical way to put a list backwards
print(a[::-1])
#[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(a[::-2])
#[9, 7, 5, 3, 1]
#every other on reverse

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CONDITIONALS

#control flow is the ability to make a decision, this is done by the if statement block

#!usr/local/bin/python36
name = "Charlie"
life = "HELL"
if life == "HELL":
    print("Yes we are in HEll")
    if name == "Charlie":
        print("Charlie is here for the ride")
# if the statements were not == then you will not get a response

#~~~~~~~~~~~~~~~~~~OPERATORS

#Equal to ==
#Not equal to !=
#greater than >
#lessthan <
#less than or equal to <=
#greater than or equal to >=

temp = """
 (-100 , -30] REALLY COLD!
 (-30, 0)     COLD
 0            zero
 (0, 20)      perfect
 [20, 40)     hot
 [40, 100]    REALLY HOT! """

print(temp)

t = int(input())

if (t <= -30):
    print("REALLY COLD!")
if (t < 0):
    if (t > -30):
        print("cold")
if (t == 0):
    print("Zero")
if (t > 0):
    if(t < 20):
        print("perfect")
if(t >= 20):
    if(t < 40):
        print("hot")
if(t >= 40):
    print("damn thats hot")


#~~~~~~~~~~~~~~~~~~~ ELSE ELIF

#else and ELIF

#!usr/local/bin/python36

name = "Beelzubus"

if name  == "J Dawgh":
    print("Big J mein")
else:
    print("rock this world")

if name == "Sue":
    print("OH Sue")
elif name == "Mike":
    print("Mikeal Mathers")
elif name == "J Dawgh":
    print("J DAWG")
elif name == "Joe":
    print("NAaa not Joe")
else:
    print("It was none of the names specified")

n = 70
if n < 20:
    print("n < 20")
elif n < 60:
    print("n < 60")
else:
    print("It was greater than 60")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#!/usr/local/bin/python36

# or, and, Not

T = True
F = False

statment1 = 3 > 4 #Flase
statment2 = 10 % 5 == 0 #True
statment3 = "A".lower() == "a" #True

#or
if F or F:print("F or F")
if F or T:print("F or T")
if T or F:print("T or F")
if T or T:print("T or T")
#F or T
#T or F
#T or T

#and
if F and F:print("F or F")
if F and T:print("F or T")
if T and F:print("T or F")
if T and T:print("T or T")
#T or T

#Not
# not(3 == 6)
print(not(3 == 6)) #True
print( 3 != 6 ) #True
if not F: print("Not F")
if not T: print("Not T")
#Not F

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#write a program that given two numbers a, b print "divisible"
#if one of the two numbers divides the other
#my go.....
a = 6
b = 3
if a/b:
    print("they can divide")
else:
    print("they do not divide")
#Required input
a,b =int(input("a = ")), int(input("b = "))
if a % b == 0 or b % a == 0:
    print("divisible")

#given input a, b print a/b if b is not equal to Zero
#my input
a = int(input())
b = int(input())
if b != 0:
    print(a/b)
else:
    print("Did you put a zero in there")
#Now learnt
a, b = int(input("a = ")), int(input("b = "))
if b != 0: print(a/b)
if b is not 0: print(a/b)
if not(b == 0): print(a/b)

#write a program that given three names prints "equal"
#if all three names are equal to each opther when lowercase

name1 = input("name 1: ")
name2 = input("name 2: ")
name3 = input("name 3: ")

if name1.lower() == name2.lower() == name3.lower():
    print("equal")

#~~~~~~~~~~~~~~~~~~MINI PROGRAM  4.6

#!/usr/local/bin/python36

import sys # sys.exit() quites the PROGRAM

line = input()
split = line.split()

if len(split) !=3:
    print("Wrong format")
    sys.exit()

left = int(split[0])
op = split[1]
right = int(split[2])

val = 0

if op == '+':
    val = left + right
elif op == '-':
    val = left - right
elif op == '*':
    val = left * right
elif op == '/':
    if right == 0:
        print("Division by zero. Halting")
        sys.exit()
    val = left / right
else:
    print("Sorry I did not reconize that operator: {operator}".format(operator=op))
    sys.exit()
print("{line_expr} = {value:.2f}".format(line_expr=line, value=val))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~WHILE AND FOR LOOP 5.1

s = "hello world"
a = [3, 6, 9]

print( 5 in a )
print( 4 in a )
print( "ello" in s )


for even_number in [2, 4, 6, 8, 10]:
    print(even_number)
    # add more code here..

odds = [1,3,5,7,9,11]

for odd_number in odds:
    print(odd_number)

print(range(len(odds)))
for index in range(len(odds)):
    print("index: {:d}, odd number: {:d}".format(index, odds[index]))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

index = 0
names= ["Josh", "Harry", "Leah", "Micah" ]

while index < len(names):
    name =names[index]
    print(name)
    index = index + 1

total = 0
v = 1

while v <= 10:
    total = total + v
    v = v + 1
    print(total)

    #never ending while loop untill the condition have been METHODSprint("Make the sum of a + b equal 20")
while True:

    a, b = int(input("a: ")), int(input("b: "))
    if a + b == 20:
        print("Stopping loop")
        break
    else:
         print("thats not 20")
