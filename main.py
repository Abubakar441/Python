print("my frist output")
print("""for
show
in next line""")
print("for next line \n like this")
print('it\'s will wrok')
"""it is also used for quatations """
#for input from user: 
name= input("enyer your name:")
print (name)
age=int(input("enter you age:"))
print(age)
#for simple plus minus and others (eval)
add=eval(input("enter your equation:"))
print(add)
# for know your datatype
name="ali"
age=12
print((type(name)) ,(type (age)))
#for type casting
a=11
b="23.5"
print (type(a))
print (type(b))
b = float(b)
c=a+b
print(c)
print(type(c))
#for swap:
x=12
y=20
#for swap
z=x
x=y
y=z
print(y)
print(x)
#method 2
a=15
b=17
a,b=b,a
print(a)
print(b)
#experiment for print both at same time but in different line
name = input("enter your name:")
name_2=input("enetr adain:")
print(name+ "\n" + name_2)
print ("""name
name_2""")
#this means 2 ki power 2
print (2**5)
#% modulus
print (8%3)#ans 2
#floor division
print(8//3) # means without decimals ans = 2 
#comparsion operators
print(3<6)
print(3!=4) #not equal to
#logical operators
and (if both true or false)or(if one is true) not(if both not then true and both have false opposite to and)
#assignment operators
x = 2
y += 1 
z -=1
a *=2
x=5#like that 
x +=1 # here 1 means add jo ap add krna caha it will 2 and ans bs 7
print(x) # 6 
#identity operators
There are 2 identity operators:
is
x=2
y=2
print (x is y) # true
is not
x=4
y=5
print(x is not y) # true (it tells that id is stored in same memory or not)
#bitwise operator
#for binary numbers nikilna k lia
print (bin(101)) #here bin is function to ans binary
# and operator
print(10&8) # & means and (ans=8) (both same then 1 )
# or operator
print (10|8) #| is means or (ans = 10) (jis ma 1 ho eo ans 1 )
#xor operator (if similar then 0 then 1)
x=8
y=10
print(x^y) # ans = 2
#Left shift (<<) me last wala bit khatam nahi hota.
#Balke right side pe zeros add hote hain.
#🔹 Right Shift (>>)
#Right wala bit remove ho jata hai
#Left side pe 0 add hota hai (positive numbers me)
print (10<<2)
print(10>>2)
#membership operator
in not in
x="hello"
print("ll" not in x) #false because ll have in x


                                                  
                                                  

 


