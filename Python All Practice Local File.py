print("hello world",78,"hi")
print(5)                    
print("i am a good girl \nbut i can't help you this time")
# i AM PRACTICING OF PYTHON

print("hello world",78,"hi") #JUST REPEATING
#JUSTDSFW
#FDEWFFWE

'''
i 
am
doing 
bs
Artificial Intelligence
'''

""""
i 
am 
practicing
my 
python
 """
#methods to put comments


print("hey i am a good boy\nare you? \"good boy\" i hope you will be ")
print("are you a \"good girl\" ?")
#if we want to put double quotes in our print statement we use (\"______\")


print( "hey", 7, 8, "bye", 0, sep="*")
print("egg")
#sep= "__" use to separate all our statements by using special data we put in double quotes

print( "hey", 7, 8, "bye", 0, end="11 ")
print("egg")
#end="__" use to put any statement we write in double quotes after ending the current line and print the next line on the same line



a = 1
print(a)

b = "rida"
print(b)
print("the data type of" , type(a))

c = complex(6,9)
print(c)
print("the data type of c is " , type(c))

print(35+3)
print(3435-544)
print(34*3544)
print(35/34)
print(5%34)
print(345**2)



a = 10
b = 33

print(a+b)
print(a-b)
print(a*b)
print(a/b)


a = "rida"
b = "fatima"
print (a + b)
# a+b is possible cause we have both strings our output will be rida fatima

a = "1"
b = "2"
print ("a"+ "b")

a = 1
b = 1
print (a+b)

a = "1"
b = "2"
print (int (a)+ int(b))



a = "1"
b = "2" 
print(a+b)


c = 1.4
d = 3
print (c+d)

print(type(a))
#print data type of a varibale

a = 10
b = "5" 
print (a + int(b))
#convert data type of varibale b form string to int

string = "15"
number = 7
string_number = int(string)
sum = number + string_number
print ("the sum of both numbers is:" ,sum)
#code where we convert our data type of string variable to int using another variable



a = input()
print (a)
#invisible input ;)


print ("Enter your name")
a = input()
print ("your name is" , a )

a = input ("Enter your age")
print( a )

a = input("Enter first number")
b = input("Enter second number")
print ( "a" + "b")
#our output will be ab no matter what we give input cause both a and b are typed as string in print command

a = input("Enter first number")
b = input("Enter second number")
print(a+b)
#get both words whatever you write in output terminal cause input is taken as string in pyhton

a = input("Enter first number")
b = input("Enter second number")
print(int(a)+int(b))
#here convert data type of both inputs to int then we will get our output


a = input("Enter first number")
b = input("Enter second number")
print(float(a) + float(b))
#here convert data type of both inputs to float then we will get our output

print("final, end")

name = "rida"
classs = "bs AI"
grades = "not bad but not good"
msg = "hey, keep learning, " \
"you will get the result" \
"inshallah" \
"yeah i am focousing on my skills"
# for multiple string we can simple press enter as well, it is done by the vs code to make it a multiple string with no error
print(name + classs + grades + msg)

apple = 'he siad, "he like apples"'
print(apple)

ball = '''he said,
"he really want to play with ball".
i think we should go and play what he want
oky
we can play with ball first'''
#multiple line string can be written in single quotes
print (ball)




ball = """he said,
"he really want to play with ball".
i think we should go and play what he want
oky
we can play with ball first"""

print (ball)
#multiple line string can be written in single quotes





print(name [2])
#print specific string character, here array is used

for character in msg:
 print(character)
 #loop use to print all the characters of a string, syntax( for _______ in ____ )
 #1st blank contain loop variable name, 2nd blank contain our varibale name whose characters we want to print



names = "Rida Fatima"

#syntax
#variable name[start:end]
#starting chaarcter prints : ending character does not print(the character before to it prints)

print(names [0:5])

length = len(names)
print(length)


print("my name is", length, "letter long")


fruit = "watermelon"
print(fruit[0:3])
#print from 1st character to 3rd characrer


length_of_fruit = len(fruit)
print(length_of_fruit)

print(fruit [:])
#work only for STRINGS, we can't use here varibale length_of_fruit, python automatically consider zero on left side and the number of last character in the variable on right side of the  of colon and print characters from start to end

print(fruit [:5])
##work only for STRINGS, we can't use here varibale length_of_fruit, python automatically consider zero on left side of the  of colon and print characters from start to array 5


print(fruit[-1 : -3])
#Minus means count from the end of the string
#prints the chatracters to oppostie side
#need to keep in mind interger scale

print(fruit[-6 : -3])

print(fruit[-8:-2])

nm = "harry"
print(nm[-4:-2])
#output is ar




a = "Rida Fatima"

print(a)
print(a.upper())
print(a.lower())
#convert string to upper and lower case


b = "Rida Fatimaaaaaaaaaaaaaaaaaaaaaa"
print(b.rstrip("a"))
#remove the character from the right side only if the given character in on the last, not in middle or start


c = "!!!!!!!!rida!!!!"
print(c.rstrip("!"))


b = "Rida Fatima"
print(b.rstrip("a"))


b = "Rida Fatima"
print(b.rstrip("i"))


b = "Rida Fatimaaaaaaaaaaaaiiiiii"
print(b.rstrip("a"))


b = "Rida Fatimaaaaaaaa"
print(b.rstrip("t"))


c = "!!!!!!!!rida!!!!rida"
print(c.replace("rida" , "eman"))
#repalce the string wiwth other string)


d = "rida fatima is a girl"
print(d.split(" "))
#make a list of string after every character you choose

d = "rida fatima is a girl"
print(d.split("a"))

d = "rida fatima is a girl"
print(d.split("m"))


f = "learning python to have a skill"
print(f.capitalize())
#capitalize the first character of a string

f = """learning python to have a skill.
i hope, i will have advantage of it in future.
my skill and ai togetehr will be amazing"""
print(f.capitalize())


f = """Learning pYthon to have a skill.
i hope, i Will Have advantage of it In future.
My skill and ai togetehr will be AMAZing"""
print(f.capitalize())


str1 = "welcome to learning python"
print(str1.center(80))
#add empty spaces to your string

d = "everything is amazing"
print(d.count("a"))
#tells how many time a character or word is present in a string

d = "everything is amazing" \
"everything is amazing" \
"everything is amazing" \
"everything is amazing" \
"everything is amazing"
print(d.count("is"))

g = "everything is amazing" \
"everything is amazing" \
"everything is amazing" \
"everything is amazing" \
"everything is amazing!!!!" \
"there was all great things," \
"we enjoy a lot"
print(g.endswith("!"))
#tells that our string wether ends with that character specific character

g = "there was all great things," \
"we enjoy a lot"
print(g.endswith("t"))
#if it is ending, we will see true in our output, if it's not we will see false in our output


g = "everything is amazing" \
"everything is amazing" \
"everything is amazing" \
"everything is amazing" \
"everything is amazing!!!!" \
"there was all great things," \
"we enjoy a lot"
print(g.find("is"))
#tells at which index your character is present, just for first one index not others

g = "everything is amazing" \
"everything is amazing" \
"everything is amazing" \
"everything is amazing" \
"everything is amazing!!!!" \
"there was all great things," \
"we enjoy a lot"
print(g.find("b"))
#tells that how many times a character or word is present in string, gives -1 if we on't have that character or word in our string


g = "everything is amazing" \
"everything is amazing" \
"everything is amazing" \
"everything is amazing" \
"everything is amazing!!!!" \
"there was all great things," \
"we enjoy a lot"
print(g.find("i"))
#similar to find

g = "everything is amazing" \
"everything is amazing" \
"everything is amazing" \
"everything is amazing" \
"everything is amazing!!!!" \
"there was all great things," \
"we enjoy a lot"
#print(g.index("b"))
#but shows error if that charcter or word is not found instead of -1


s = "welcome to this world"
print(s.isalnum())
# used to check whether a string contains only letters and numbers
# True - if the string has only A–Z, a–z, or 0–9
# False - if it contains spaces, symbols, or punctuation

# f = "232424"
# print(f.isalnum())
#isalnum works only on strings, it shows error

f = "232424"
print(f.isalnum())


f = "abcdef"
print(f.isalnum())


f = "abc5372"
print(f.isalnum())

f = "adcn!d434"
print(f.isalnum())

f = "abc 435 number %"
print(f.isalnum())


s = "welcometothisworld"
print(s.isalpha())
#check whether a string contains only letters
#True only if the string has only A–Z, a–z
#False,if it contains numbers, spaces, symbols, or punctuation

s = "welcome to this world"
print(s.isalpha())

s = "welcometothisworld00"
print(s.isalpha())

s = "welcome_to_this_world"
print(s.isalpha())


s = "welcome to this world"
print(s.islower())
#use to check wether chracters in the string are in lower case, does not bother the number, space, symbol or puntuations
#gives true if all are lower case, every single caharters needs to be lower case to be true
#gives false if upper case is found

s = "Welcome To This World"
print(s.islower())

s = "welcome to this world00"
print(s.islower())

s = "welcome to this @ world00"
print(s.islower())


s = "Welcome To This World"
print(s.isprintable())
#shows true if all the chracters of the strings are printable
#shows false if any character of the string is not printable

s = "Welcome To This World\n"
d = "you will enjoy this palce"
print(s.isprintable())
# \n is not printable, output will be flase

s = "           "
print(s.isspace())
#gives true only if we have only space in our string

s = "     sd      "
print(s.isspace())
#it will gives false


s = "Welcome To This World"
print(s.istitle())
#gives true onyl if all first characters of all words in a string are capital

s = "Welcome to this world"
print(s.istitle())
#otherwise returns false


s = "Welcome to this world"
print(s.isupper())
#use to check wether chracters in the string are in uppercase, does not bother the number, space, symbol or puntuations
#gives true if all are upper case, every single caharters needs to be upper case to be true
#gives false if lower case is found


s = "Welcome to this world"
print(s.startswith("Welcome"))
#gives true if string is starting with your given string

s = "Welcome to this world"
print(s.startswith("welcome"))
#otherwise gives false

s = "welcome to THIS WORLD"
print(s.swapcase())
#converts lower case to upper, upper case to lower


s = "Welcome to this world"
print(s.title())
#convert string into title case, capitalize first characters of every word