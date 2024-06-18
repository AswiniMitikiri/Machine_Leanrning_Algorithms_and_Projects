#!/usr/bin/env python
# coding: utf-8

# # Heading

# ## Heading

# ### Heading

# #### Choose markdown in above option and then type "# and text" and click shift and enter. enter #'s to reduce font size

# ##### 5 times # to convert to italic

# In[1]:


print('Hello World')


# In[2]:


print("Aswini Mitikiri")


# In[4]:


#string formating
name='Aswini' 
age=21
print("Name:{}, Age:{}".format(name,age))


# In[6]:


print('India','America','Russia','Srilanka',sep=',')


# In[7]:


print('India','America','Russia','Srilanka',sep='#')


# In[8]:


print('India','America','Russia','Srilanka',sep='/')


# In[9]:


print('India','America','Russia','Srilanka',sep='+')


# In[10]:


print('India','America','Russia','Srilanka',sep='=')


# In[11]:


print("Hello")
print("Raj")


# In[12]:


# to print in same line, we use end=" " as seperater(useful for dealing with different kind of statements and loops
print("Hello",end=" ")
print("Raj") )


# In[13]:


x=50
print(x)


# In[14]:


# adding a value to a variable and print
y=10
y=y+10
print(y)


# In[15]:


# subtarct with variable
y=y-5
print(y)


# In[16]:


# multiplication
x=10
x=x*10
print(x)


# In[17]:


# Multiple variables
a=100
b=50
print(a+b)


# In[18]:


a-b


# In[19]:


a*b


# In[20]:


a,b,c=10,20,30
print(a)
print(b)
print(c)


# In[21]:


#Datatypes
#int
#float
#boolean
a=100
print(a)
print(type(a))


# In[22]:


b=10.0
print(b)
print(type(b))


# In[23]:


17/2%2*2**2


# # Operators

# In[24]:


# Arithmetic Operators
a=10
b=2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)


# In[25]:


a=25
print(a**0.5)


# In[26]:


print(17/2%2*3**3)


# In[28]:


# Relational Operator
a=100
b=50
print(a<b)
print(a>b)
print(a>=b)
print(a<=b)


# In[30]:


# Membership Operator
s='Python'
print('y' in s) 
print('h' in s) 
print('z' in s) 


# In[31]:


print('lo' in 'Hello world')


# # List

# In[35]:


# List can store mumber of elements and
# are determined within square brackets
list=['Mohan',25,6.5,'Delhi']
print(list)


# In[36]:


# Length of list
print(len(list))


# In[37]:


list[0]


# In[38]:


list[1]


# In[39]:


list[2]


# In[40]:


list[3]


# In[41]:


list[-1]


# In[42]:


list[-2]


# In[43]:


list[0]=100
print(list)


# In[44]:


# Slicing- access the range of values from the list 
# list[start:end]
list[1:3]


# In[46]:


list[0:2]


# In[47]:


list[2:4]


# In[55]:


list[2:]


# In[56]:


#reversing a list
print(list[::-1])


# In[57]:


list.append(4)


# In[58]:


print(list)


# In[59]:


list.extend([5,6,7])


# In[60]:


print(list)


# In[ ]:


list.clear()


# In[62]:


print(list)


# # Tuples

# In[1]:


# Tuples are immutable, can not be changes and 
#denoted by parenthesis

tup=('street','sagar',254)
print(tup)


# In[2]:


type(tup)


# In[3]:


print(tup[0])


# In[4]:


print(tup[1])


# In[5]:


#slicing with tuple
print(tup[1:])


# In[6]:


#deleting tuple
del(tup)


# In[7]:


#error as we delected the tuple
print(tup)


# In[8]:


x=(3,1,2,4,5)
print(max(x)) #min, sum,len


# In[15]:


print(x)
y=sorted(x)
print(y) #sorting converts tuple into a list

# in tuple sort() does not work. so it will br sorted()


# In[19]:


tup=tuple(y)
# y=tuple(sorted(x)) this will also work
print(tup)

# concatination
tup=(1,2,3)
tup2=(4,5,6)
result=tup+tup2
print(result)


# # Sets

# In[22]:


# Sets are collection of Unique values and uses surly braces
# no index is attached to the elements

a={1,2,3,4,5}
print(a)
type(a)


# In[23]:


a.add(6)
print(a)


# In[24]:


a.remove(5)
print(a)


# In[25]:


set1={1,2,3}
set2={2,3,4}
set1-set2


# In[26]:


print(set1)


# In[28]:


set1.clear()
# to clear a set 


# In[29]:


print(set1)
# we get an empty set


# # Dictionary

# In[30]:


# data type that stores data in key value pair & uses culry braces
d={'name':'Raju', 'age':21}
d


# In[31]:


type(d)


# In[32]:


d['name']


# In[33]:


d['age']


# In[34]:


#we can use print function as well
print(d['age'])


# In[35]:


# update dictionary
d['age']=40
print(d)


# In[37]:


# we can not update only key but 
# we can change either only value or both key and value
d['Exp']=d.pop('age')
print(d)


# In[39]:


d.items()


# In[40]:


d.keys()


# In[41]:


d.values()


# In[43]:


# To remove a key value pair using pop function
dict={'a':1,'b':2,'c':3}
dict.pop('a')
print(dict)


# In[44]:


len(dict)


# In[46]:


# Adding new key value pair in Dictionary

dict['d']=4
dict['e']=5
print(dict)


# In[47]:


# To fetch a value from the user, we use input funtion & data type will be string
# we use int funtion to convert the input into int datatype from default string datatype

x=int(input('Enter a number'))

print(x)
type(x)


# # Statements

# In[ ]:


# if
# if else
# elif


# In[49]:


# if
x=int(input('Enter a number '))
if x==100:         # we use : in if statement for indentation in nextline
    print('you Entered my favourite number')
    
    # Indentation is 1 tab space


# In[50]:


# ifelse

x=int(input('Enter a number '))
if x==100:         
    print('you Entered my favourite number')
else:
    print('This is not my favourite number')


# In[52]:


# elif

a=int(input('Enter the value of a '))
b=int(input('Enter the value of b '))
if a < b:         
    print('b is greater')
elif a==b:
    print('a is equal to be')
else:
    print('a is greater')
    


# In[55]:


# nestes if else
x=int(input('Enter the value of x: '))
if x>5:
    print("x is greater than 5")
    if x % 2 == 0:
        print("x is even")
    else:
        print("x is odd")
else:
    print("x is less than or equal to 5")


# # Loops

# In[ ]:


# loops are used to repeat curtain block of code unless some condition is met


# In[57]:


# for loop and while loop

# syntax: for x in sentence ( goes through each element in sentence variable and print it)

'''  for x in sentence:   # x is a variable and "sentence" is a declared variable
         print(x)   # sentence variable has to be declared here'''
    
# range(start,end,gap(#optional))

for i in range(5):
    print(i)


# In[58]:


for i in range(5):
    print(i, end=" ")


# In[59]:


cars=['BMW','Audi','Mercedes','Volkswagen','Skoda']
for i in cars:
    print(i)


# In[60]:


for i in range(10,25):
    print(i)


# In[ ]:


#while loop reapetedly executes untill a certain condition is true

'''while condition:
       (code) '''


# In[61]:


i = 0

while i<=5:
    print(i)
    i=i+1


# In[62]:


# while loop with "continue" statement
# print all values and skips a value that meets the condition

i=0

while i<=7:
    i+=1
    if i==6:
        continue
    print(i)


# In[63]:


# while loop with "break" statement
# will not execute(comes out of the loop) after the condition is met

i=0

while i<6:
    print(i)
    if i==3:
        break
    i+=1  # i=i+1


# In[64]:


for i in range(10):
    if i % 2 == 0:
        pass  # Placeholder for future code to handle even numbers
    else:
        print(i)


# # Fuunctions

# In[66]:


# a block of code that can be either predefined and declared that can be called to perform a specific task 
# Syntax: def function_name(parameter1, parameter2....):
#         function code


# decalring a fucntion

def func1():
    print("Hello I am a function")
    print("I am Ready")


# In[67]:


# Calling a function

func1()


# In[71]:


def func2(fname):
    print('Good Evening. I welcome to the session ' +fname)


# In[72]:


func2("Aswini")


# In[73]:


def f3(a,b):
    c=a+b
    print(c)


# In[74]:


f3(100,35)


# In[75]:


# area of a circle
def area(r):
    a=3.14*r**2
    print(a)


# In[77]:


area(5)


# In[ ]:


# Lamba Expressions
# anonymous functions to declare in a line, when we nedd them short period of time

lambda arguments: expression


# In[78]:


# add 10 to an argument a
x=lambda a: a+10
print(x(20))


# In[79]:


x= lambda a,b: a+b
print(x(50,20))


# In[80]:


x= lambda a,b,c: a+b+c
print(x(50,20,30))


# In[81]:


x=lambda a,b: a-b
print(x(30,10))


# In[82]:


x=lambda a,b: a*b
print(x(30,10))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




