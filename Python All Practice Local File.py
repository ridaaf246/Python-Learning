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