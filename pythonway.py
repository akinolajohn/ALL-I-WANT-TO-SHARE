'''
print
print('jj')
x = 1
if x == 1: 
	print('your selected x is 1')
#------------------------------------------
# myfloat = 7.0
# myfloat = float(7)

# Lists--------------------------------------

mylist=['cu', 'bab', 'oau', 'illy', 'ui']

mylist.append(2)
print(mylist[0:4])
remainder = 110 % 3
print (remainder)
helloworld = "welcome TO" + " " + " JOHN'S world"
print (helloworld)

# ====String Formatting-=====---------------------------
name='John'
print('Hello,',name)
 # OR
name = "John"
print ("Hello, %s" %name)

age= 21
print('The CEO of QUINSA is %s, Akinola and He is %1.2f  Years Old'%(name, age))
# Basic String Operations-----------------------------
word= 'communicate'
print ( 'The  word being tested is %d characters long'   %len(word))
print ('The number of m\'s is '  , word.index('m'))
print (word.count(''))
print (' Printing the first four characters', word[0:5:1])
print ('Printing the value of word in caps' , word.upper())
print ( 'result when a condition to test if a value is in the variable: ', word.startswith('c'))
print ('How do I want to split: ' , word.split(" , "))
# ---------------------------------------------------------------
# import math
# print ('QUADRATIC EQUATION ')
# a = input('First Value :' )
# b = input('Second Value : ' )
# c = input('Third Value  : ' )
# d = (b**2) - (4*a*c)
# if d < 0:
# 	print("This equation has no real solution")
# elif d==0:
# 	d= (b**2) - (4*a*c)
# 	print("This equation has only one solution" )
# else:
# 	Quad1 = (-b -math.sqrt(d)) / (2*a)
# 	Quad2 = (+b -math.sqrt(d)) / (2*a)
# 	print(Quad1, Quad2)


# ----------------------------------------------------
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# # RECURSIVE--------------------------------------------------
# def factorial(n):
#     print("factorial has been called with n = " + str(n))
#     if n == 1:
#         return 1
#     else:
#         res = n * factorial(n-1)
#         print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
#         return res	

# print(factorial(5))
# print(' Instructor says print "Hello World\" ')

# import datetime
# now = datetime.datetime.now()
# print("Curent date and time: ")
# print(now.strftime(" %Y-%m-%d-%H:%M:%S"))

# import os, platform
# print("Operating system name: ")
# print('os.name')
# print('platform name:')
# print('platform system:')

#--------------------------25th MAY-------------------------


def  compare(a,b):
	if a is b:
		print('A is b')
	if a==b:
		print('The value of a and b are the same')

	if type(a) is type(b):
		print('Type A is the same as Type b')
compare(2,2)


isinstance(5,int)
print (list('Hello World'))
print (int(4/3))
'''
# ------------------------------------------
# a='All'
# b='work'
# c='and' 
# d='no'
# e='play'
# f='makes' 
# g='jack'
# h='a' 
# i='dull'
# j='boy'

# print(a,b,c,d,e,f,g,h,i, end="\n"+ j) 


# # # ----------------------------
# calc = 6*(1-2)

# print(calc)

# # -----OR------------------------

# calc = 6*1-2

# if calc==4:
	
# 	print((calc+2)*-1)
# # -----------------------------
# print(10*7+3/2)
# # With Bodmas-------------------
# print((10*7) + (3/2))
# # -------------------------------

# bruce=6
# print(bruce+4)

# # -------26TH ------------------------
# alpha = ['a','b','c','d' ]
# letter = alpha[2]
# print (letter)

# #=============------------------
# shape = "triangle"
# for char in shape:
# 	print(char)
# #============--------------------
# numbers = 1,2,3,4,5,6,7 
# for int in numbers:
#  	print(int)
#  # ======-------------------
# classs= ['js1', 'js2', 'js3']
# for str in classs:
# 	print(str)

# =======----------------------------
# text = 'banana'
# add_when = 0
# for letter in text:
# 	if letter =='a':
# 		# if a letter in the array is equal to a, then add 1 to the variable add_now
# 		add_when = add_when+1
# 		#  this keps adding 
# print('The number of times a  appears is %s times' %add_when)
# ==============--------------------
# Basic_Text = 'Hello World'
# New_BasicText = 'Y' + Basic_Text[1:] 
# # comment 
# New_BasicText = 'Y' + Basic_Text[:1]
# print(New_BasicText)
# print('The %s is my %s' %("Man", 'father'))

#=====EXERCISE 1===================================
# def is_even(n):
# 	if n%2 ==0:
# 		print('We have an even number')
# 	elif n%2!=0:
# 		print('We have an odd number')
# is_even(2)









#=============-- 30th May----------------------------------
# word1= 'alphabet'
# word2= 'christian'
# if len(word1) > len(word2):
# 	print(word1)
# else : print(word2)

# ------OR-----------------------
# def longestword(wordlist):
# 	longest = 0
# 	lword = ''
# 	for word in wordlist:
# 		if len(word) > longest:
# 			longest = len(word)
# 			lword = word

# return lword

# ============-- LISTS--------------------
# vocabulary = ['ameliorate', 'constitution', 'Mathematics']
# numbers = [17, 23]
# empty = []
# print(vocabulary, numbers, empty)

# weekdays = ['Monday', 'Tuesday', 'Wednesday' ,'Thursday','Friday']
# for num in weekdays:
# 	print (num)
# 	weekdays[1]= 'Football'
# 	print (num)
# 	# print (len(num))

# primes = [2, 3, 5, 7]
# for prime in primes:
#     print (prime)
# for x in xrange(5): # or range(5)
#     print (x)
# ==========------------------------
# product= 4
# list = [1, 2, 3]
# for x in list:
#     product *= x

	
	
# def multiply(n):
#     total = [1,5,3,6,6]
#     for i in range(0, len(n)):
#         total *= n[i]
#     print (total)

# =========---------------------------

# chicken=[1,2,3,4,5,6,7,8,9,10,11,12]

# def multiply(n,k):
#      for i in range(0, len(n)):
#          print(n[i]*k)

# multiply(chicken,2)

# # ==============---------------------
# chicken=[1,2,3,4,5,6,7,8,9,10,11,12]
	
# for everyc in range(0, len(chicken)):
#     print(chicken[everyc]*3)
# ===========----------------------
# weekdays = ['Monday', 'Tuesday', 'Wednesday' ,'Thursday','Friday']
# for abd in weekdays:
# 	print(abd[1:4] ,[])

# mylist=[1,2,3,4,5,6,7,8,9,10,11,12]
# def domuliplication(numbers):
# 	for eachnumber in numbers:
# 		print ( eachnumber*2)
# domuliplication(mylist)
	

# =======LIST CLONING====-----------

# # EXERCISES
# # 1.
# myarr = [1,2,3,4,5]
# a= [0]
# b= [1]
# for number in myarr
# 2.
# 3.
# 4.
# 5.
# 
# =====31st MAY===-



# 
# word = 'magnify'
# word[0] = 's',
# word[8] = 'Y',
# print(word)


# z = "MAGNIFY"
# # y = z[-1]+z[1:len(z)-1 ]+z[0]
# y = z[0] + z[1:-1] + z[-1]

# print(y)

# def cat_n_times(s,n):
# 	for number in range (1,n+1):
# 		print(s)
# cat_n_times('Spam ',7)
# # end='' means continue on the same line
	
# def jj(say,do):
# 	for word in range(0, do):
# 		print(say)
# jj('Hello sir Emeka',1)


# def seun(come, go):
# 	for action in range(1, go):
# 		print(come, end='')
# 	seun('its ok', 4)


# EX : test an integer's divisibility by 3
# def is_divisible_by_3(num):
# 	if num%3==0:
# 		print('Number is divisible by 3')
# 	else :
# 		print('Number is not divisible by 3')
# print(is_divisible_by_3(3))

# didn't work

# this should always be at the end



# ============EXERCISE 2=====--------------------------
# numbers = [1,-2,3,4,5,6,7,8]
# newnumbers=[]
# smallest = numbers[0]
# biggest=numbers[0]
# for digit in numbers:
# 	if digit < smallest:
# 			smallest = digit
# 	if digit>biggest:
# 		biggest=digit
# print(smallest, biggest)
# # ========================================
# for digit in numbers:
# 		if digit !=smallest:
# 			newnumbers.append(digit)
# print(newnumbers)

# nsmallest=newnumbers[0]

# for digit in newnumbers:
# 	if digit<nsmallest:
# 		nsmallest=digit

# print(nsmallest)


# USING SORT
# li = [1,2,23,4,5,6,6]
# li.sort()
# print(li)





# int(input('press key'))
# def is_even(n):
# 	if n%2 ==0:
# 		print('We have an even number')
# 	elif n%2!=0:
# 		print('We have an odd number')
# print(is_even(2))



# ====EXAMPLE OF POP===========--------------------------
# testlist = [2,34,45,4,56,56,76,6]
# testlist.pop(2)
# testlist.pop(4)
# testlist.pop(5)
# print(testlist)

# li = range(1,1000)
# print(li)

# ====1 st JUNE 2017======= COURSE SELECTION PROBLEM ===================================================================================================

# math = {'m','e','p','c'}
# eng = {'m','e','g','b'}
# phy = {'m','e','p','b'}
# chem = {'m','e','p','c'}
# getinput=input('Enter four courses between m, e, p, b, c, g, a')
# userinput=set(getinput)
# if userinput ==math:
# 	print('Your Approved course is maths')
# if userinput ==eng:
# 	print('Your Approved course is english')
# if userinput ==phy:
# 	print('Your Approved course is physics')
# if userinput ==chem:
# 	print('Your Approved course is chemistry')
# else: print('kindly enter a subject')




# # =====works=-------------------------
# math = {'a','b','c','d'}
# eng = {'b','c','e','d'}
# phy = {'c','b','e','d'}
# chem = {'d','e','b','c'}

# alist =[]
# for userinput in range(5):
# 	userinput = input("Enter a subject: ")
# 	alist.append(userinput)

# Nuserlist = set(alist)
# if Nuserlist.intersection(math)==math:
# 	print ('YOu are ADMITTED to Study MAths')
# break
# if Nuserlist.intersection(eng)==eng:
# 	print ('YOu are ADMITTED to Study English')
# if Nuserlist.intersection(phy)==phy:
# 	print ('YOu are ADMITTED to Study Physics')
# if Nuserlist.intersection(chem)==chem:
# 	print ('YOu are ADMITTED to Study Chemistry')	
# else: print("Enter a nuber between a,b,")

# DICTIONARY
# letter_count ={}
# for letter in 'mississsipi':
# 	letter_count[letter] = letter_count.get(letter,0) +1
# print(letter_count)
# 
# =====================================================
# p = str(input("Hello!, what is your name?\n"))
# print("Hello", p," time to input your 5 'o' level courses \n" )
# q = []
# count = 1
# for i in range(5):
#     s = input("Enter course number %d:" % count)
#     q.append(s)
#     count += 1
# r = set(q)
# u = set([])
# possible_courses = []
# Mech = set(['M','E','P','C','T'])
# Comp = set(['M','E','P','C','B'])
# MIS = set(['M','E','P','C','B'])
# phy = set(['M','E','P','F','C'])
# Math = set(['M','E','F','P','C'])
# if r.difference(Mech) == u:
#         possible_courses.append("Mech")
# if r.difference(Comp) == u:
#     possible_courses.append("Computer Engineering")
# if r.difference(MIS) == u:
#     possible_courses.append("MIS")
# if r.difference(phy) == u:
#     possible_courses.append("Physics")
# if r.difference(Math) == u:
#     possible_courses.append("Mathematics")
# print(p,"the possible courses for you are:",possible_courses)

# ===============================================
# fill=[]
# for item in range(5):
# 	Tuser=input('Enter the word red,green, purple and black ')
# 	fill.append(Tuser)
# 	# Nfill = fill.split(' , ')
# 	print(sorted(fill))
# 
# =========================================================
# a={'a': 1, 'b':2, 'c':3}
# b={'d':4, 'e':5} 
# b.update(a)
# print(sorted(b))
# ============================================
# x= {}
# for i in range(1,16):
# 	x[i] = i**2
# print(x)

# ======2nd JUNE =============================
# The code below prints sets count to a function by passing it as an arguement. The value of count changes, but only as long as it's in the function
# count = 2000
# def addcount(count):
# 	count *=1
# 	print(count)
# addcount(2333)
# print(count)
# =====GLOBAL VARIABLES======================
# count = 2000
# def addcount():
# 	global count
# 	count +=1
# 	print(count
# )


# ======MODULES=======================


# =====5th  JUNE===---------------------
# CONTROL STATEMENTS
# variable = 0
# if variable:
# 	print('True expression ')
# 	print(variable)
# else:
# 	print('False expression')
# 	print(variable)

# print('See you later')

# credits = 5
# userinput = int(input('How many credits do you have ? \n'))
# if credits==userinput :
# 	print('You are eligible for graduation')
# elif userinput>credits:
# 	print('You are eligible for graduation')	
# else:
# 	print('Sorry you are not eligible for graduation')
# ==========---1st way to use FOR-----------------------------
# fruits = ['banannna', 'apple','lime', 'orange']
# for each in fruits:
# 	print('the fruits are: ', each)

# ====----2nd WAY TO USE FOR--in case of many------------------
# fruits = ['banannna', 'apple','lime', 'orange']
# for each in range(len(fruits)):
# 	print(fruits[each])
 	# for (i=0, i<100, i++)

# ====----3ed WAY TO USE FOR--------------------
# for num in 


# ====----TABLES-------------------
# for x in range(13):
# 	print(x, 2**x)
# You use a FOR loop when you have a VALUE to loop through. But if I don't know the number of times to loop, then I use the WHILE to test for a condition. 

# MY CALCULATOR
# def calculate():
# 	print ('===================WELCOME TO THE ULTIMATE PYTHON CALCULATOR=======================')
	
# 	print('1 is for add operation')
# 	print('2 is for subtract operation')
# 	print('3 is for divide operation')
# 	print('4 is for multiply operation')
# 	print ('======================================================================================')

# 	userinput = int(input('\n What calculation Operation Do you want to Do? \n '))
# 	if userinput == 1:
# 		print('=============You have chosen the addition operation=============')
# 		number1 = int(input('Enter First Number'))
# 		number2 = int(input('Enter second Number'))
# 		add(number1, number2)

# 	elif userinput == 2:
# 		print('=============You have chosen the subtraction operation=======')
# 		number1 = int(input('Enter First Number: '))
# 		number2 = int(input('Enter second Number: '))
# 		subt(number1, number2)

# 	elif userinput == 3:
# 		print('=============You have chosen the Division operation=============')
# 		number1 = int(input('Enter First Number: '))
# 		number2 = int(input('Enter second Number: '))
# 		division(number1, number2)

# 	elif userinput == 4:
# 		print('=============You have chosen the Multiplication operation=============')


# 		number1 = int(input('Enter First Number: '))
# 		number2 = int(input('Enter second Number: '))
# 		multiplication(number1, number2)

# 	else :
# 		print('Kindly Select a number between 1 and 4 for operations')



# def add(number1, number2):
# 	addition = number1 + number2
# 	print (' The sum of ', number1,  ' and ', number1 ,' is: ' , addition)

# def subt(number1, number2):
# 	if number1 > number2:
# 		subtraction1 = number1 - number2 
# 		print (' The subtraction of ', number2,  ' from ', number1 ,' is: ' , subtraction1)

# 	elif number2 > number1:
# 		subtraction2 = number2 - number1
# 		print (' The  subtraction of ', number1,  ' from ', number2 ,' is: ' , subtraction2)

# 	else : print('You did not enter correct values')

# def division(number1, number2):
# 	division =float(number1/number2)
# 	print (' The division of ', number1,  ' by ', number2 ,' is: ' , division)

# def multiplication(number1, number2):
# 	multiplication = number1 * number2
# 	print (' The multiplication of ', number1,  ' and ', number1 ,' is: ' , multiplication)

# calculate()

# practicing functions
# def f(x):
# 	print( 3*x**2-2*x+5)
# f(4)

#==========---------------------- 
# first_list=[2,4,5,16,24,5,145]
# list2 = [8,2,3,2,7]
# userinput = input('Enter Number 1')
# def sum_nub(list2):
# 	calc = 0
# 	for item in list2:
# 		calc+=item
# 	print(calc)
# sum_nub(list2)
#  If I didn't set calc to 0 I would have the answer, but anything I change in the list will not change the answer.
# # ==================---------------------------------------
# def changeme(mylist):
# 	mylist =[1,2,3,4]
# 	print('The values are:', mylist)
# 	return
# changeme(mylist)
# ==================---------------------------------------
# alist = 'green-red-yellow-black-white'
# alistN = alist.split(" ")
# alistN.sort()
# print(alistN)

#FUNCTION ARGUEMENTS *arguement takes one value, **arguement takes a dictionary 
# BUILT-IN FUNCTIONS
# largest = max(4,6,7)
# print(largest)

# MORE ON FUNCTIONS
# examle 1
# def sample(a, s_list=[]):
# 	s_list.append(a)
# 	return s_list
# 	# this return is very important here
# print (sample(2))

# ======INTRO INTO OOP==============================================================================S3AQ
# ==============Method 1=============================
# class bottle: 
# 	type = ''
# 	volume = 0
# 	content = ''
# 	# set variable to class
# fanta = bottle()
# fanta.type = 'Pet Bottle'
# fanta.volume = 35
# fanta.content = 'Cola, sugar, water'
# print (fanta.volume)

# ============================================================

# class bottle: 
# 	type = ''
# 	volume = 0
# 	content = ''
# 	def __init__(self, type, volume, content):
# 		self.type = type
# 		self.volume = volume
# 		self.content = content

# fanta = bottle('pet', 50, 'Cokacola')
# print(fanta.content)

# # myexam# ===============example 2================================
# # at the end, a variable prints the atributes of its class.
# class suits:
# 	type = ''
# 	size = ''
# 	number = 0
# 	def __init__(self, ty, sz, num):
# 		self.type = ty
# 		self.size = sz
# 		self.number = num
# variable = suits('Two piece', 'big' , '12')
# print (variable.type)

# ===============example 3===============================
# class body:
# 	hands = ''
# 	legs = ''
# 	head = ''
# 	def __init__(self, hn, lg,hd):
# 		self.hands = hn
# 		self.legs = lg
# 		self.head = hd
# pob = body('two hands', 'two legs', 'one head')
# print(pob.legs)

# ===============example 4================================
# class education:
# 	sclass=''
# 	pos=''
# 	year=''
# 	def __init__(self, sclass, pos, year):
# 		self.sclass = sclass
# 		self.pos = pos
# 		self.year = year
# std1 = education('jss1', '1st', '2017')
# print(std1.sclass)

# =========================================
# class school:
# 	name = ''
# 	age = ''
# 	sex = ''
# 	choiceCourse = ''
# student = school()
# student.name = 'Akinola John'
# student.age = '21'
# student.sex = 'male'
# student.choiceCourse = "Computer Science"

# print (student.name)

# ===============Method 2================================
# Same way I can create a class like a function
# class fruits(type, size, amount):
# 	type = ''
# 	size = ''
# 	amount = ''
# apple = fruits('apple', 24, '120')




# =========BOTTLE EXAMPLE==========================================================================

# class Bottle:
#     type=""
#     volume=0
#     content=""
# def __init__(self,t,v,c):
#    self.volume = v
#    self.content = c
# coke = Bottle("pet", 50, "cocacola")
# print(coke.volume,coke.type,coke.content)
# print(coke)

# class Employee:
#     empCount = 0

#     def __init__(self,name,salary):
#        self.salary = salary
#        Employee.empCount += 1

#     def displayCount(self):
#        print("Total Employee %d"%Employee.empCount)

#     def displayEmployee(self):
#        print("Name:",self.name,"salary:",self.salary, "Age", self.age)

# empname= Employee("employee1",160000)
# empname.age=7
# empname.displayCount()
# empname.displayEmployee()

# empname= Employee("employee2",230000)
# empname.age=8
# empname.displayCount()
# empname.displayEmployee()

# empname= Employee("employee3",560000)
# empname.age=66
# empname.displayCount()
# empname.displayEmployee()

# if hasattr(empname,'age'):
#    print("oh yes")
# else:
#    print("ERROR HV4537BEVG7")

# class Person:
#     taste=""
#     volumecon = 0
#     def __init__(self, name, status):
#         self.name= name
#         self.status= status

#     def drink(a):
#         return a
#         volumecon += a



# class Bottle:
#     status = 0
#     content = ""
#     volume = 0
#     volcontent = 0

#     def __init__(self,content,volume):
#         self.content = content
#         self.volume = volume
#         self.volcontent = volume

#     def isempty(self):
#         if self.volcontent == 0:
#             print("This bottle is empty")
#         else:
#             print("This bottle has content")

#     def isclosed(self):
#         if self.status == 0:
#             print("This bottle is closed")
#         else:
#             print("The bottle is open")

#     def open(self):
#         self.status = 1
#     def close(self):
#         self.status = 0

#     def pour(self,a):
#         if self.status == 0:
#             print("Pease open the bottle first")
#         elif self.volcontent >= a:
#             self.volcontent -= a
#         else:
#             print("the volume of content is insufficient")
#     def viewstatus(self):
#         if self.status == 0:
#             a = "closed"
#         else:
#             a = "opened"
#         print("Content",self.content,"volume",self.volume,"open/closed",a,"volcontent",self.volcontent)

#     def spill(self,a):
#         if self.status == 1:
#             if self.volcontent<a:
#                 self.volcontent=0
#             else:
#                 self.volcontent -= a

# bottle1 = Bottle("cocacola",50)
# bottle1.open()
# bottle1.pour(30)
# bottle1.viewstatus()
# bottle1.close()
# bottle1.viewstatus()
# bottle1.open()
# bottle1.pour(30)
# bottle1.viewstatus()
# bottle1.open()
# bottle1.spill(30)



# ===================SOLVING THE MARRIAGE PROBLEM JUNE 8TH===========================================================================================================

# class person:
# 	fname = ''
# 	lname = ''
# 	sex = 'M'
# 	age = 0
# 	bloodgp = 'aa'
# 	jobstatus = ''
# 	spouse = ''

# 	def __init__(self,fn,ln,ag,sx,bg,js):
# 		self.fname = fn
# 		self.age = ag
# 		self.lname = ln
# 		self.sex = sx
# 		self.bloodgp = bg
# 		self.jobstatus = js
	
	

# # the functions here work in place of the variable being set to the class attributes.
# # the real issue here is getting the logic
# 	def get_fname(self):
# 		return self.fname


# 	def inc_age(self,a):
# 		self.age += a

	
# 	def get_lname(self):
# 		return self.name

# 	def set_lname(self, b):
# 		if self.sex != "M":
# 			self.lname = b
# 		else:
# 			print("You are a man! Name cannot be changed")
# 	def status(self):
# 		c = fname+ " "+lname
# 		if self.spouse == '':
# 			b = ''
# 		else:
# 			b= self.spouse


# 	def get_spouse(self):
# 	 	self.spouse = spouse
		
# 	def get_sex(self):
# 		return self.sex

# 	def set_BG(self, bloodgp):
# 		self.bloodgp = bloodgp

# 	def set_jobstatus(self):
# 		return self.jobstatus
# 	def set_jobstatus(self):
# 		return self.jobstatus

# 	def t_spouse(self):
# 		self.t_spouse	

# 	def marriage_status(self):

# 		if self.spouse != "":
# 			print("Married")
# 		else:
# 			print("Not Married")

# # The  ultimate function that makes others work


# 	def marry(a , b):
# 		if a.inc_age() < 18 or b.inc_age ()< 18:
# 			print('You are too young to get married')

# 		elif a.get_sex() ==b.get_sex():
# 			print('You cannot get marries because you are both male')

# 		elif a.set_jobstatus() =='unemployed' and b.get_jobstatus() =='unemployed':
# 			print('You cannot get married because you are both unemployed')
# 		elif a.set_BG()=='as' and b.set_BG() == 'as':
# 			print('sorry you cannot get married')
# 		elif a.self.spouse() == '' and b.self.spouse() == '' :
# 			a.spouse() = a.get_fname()
# 			a.spouse() = a.get_lname()
# 			b.spouse() = b.get_fname()
# 			b.spouse() = a.get_lname()
# 			print('Hurray You Are Married !!!!!!!!')
# 		else: 
# 			print('Sorry you were not able to fufil the obligations for marriage')


# b = person('Seun','Igalo',32,'F','as','employed')
# a = person('John','Doe',20, 'M','aa','employed')
# print(b.spouse)












# 	def marry(a, b):
# 		A=['AS','SS']
# 		if a.get_Age < 18 or b.get_Age < 18:
# 			print("Age condition not met")
# 		elif a.get_status == '':
# 			print("status is void")
# 		elif a.get_sex =='M' and b.get_sex == 'M':
# 			print("SEx condition not yet")
# 		elif a.get_jobstatus() == 'Employed':
# 			print("You are suitable for the marriage")
# 		elif get_bloodgp == 'AS' and b.get_bloodgp == 'AS':
# 			print("Ofcourse not, You cannot marry anybody")
# do_marriage = marriage( )


# ===================INHERITANCE JUNE 9TH===========================================================================================================


# class parent:
# 	parentAttr=100
# 	def __init__(self):
# 		print('calling parent constructor')	
# 	def parentMethod(self):
# 		print('calling parent method')
# 	def setAttr(self,attr):
# 		parent.parentAttr=attr
# 	def getAttr(self):
# 			print('parent attribute:',parent.parentAttr)


# class child(parent):
# 	def __init__(self):
# 		print('calling child constructor')
# 	def childMethod(self):
# 		print('Calling child method')
# 	c=child()
# 	c.childMethod()
# 	c.parentMethod()
# 	c.setAttr(200)
# 	c.getAttr()
# ==================================================================
# class primaryColor:
# 	red = ''
# 	green = ''
# 	blue = ''

# 	def __init__(self, rd, gr, bl):
# 		self.red = rd
# 		self.green = gr
# 		self.blue = bl
# 	def get_red(self):
# 		return self.red
# 		print('you have called red')
# 	def get_green(self):
# 		return self.blue
# 		print('you have called blue')

# 	def get_blue(self):
# 		return self.green
# 		print('you have called green')

# pcolor = primaryColor('red', 'green', 'blue')
# # print(pcolor.blue)

# class secColor:
# 	def __init__(self):
# c = secColor()
# c.get_blue()
# ==============================================================
# class Parent: # define parent class
#  parentAttr = 100
#  def __init__(self):
#  	print ("Calling parent constructor")
#  def parentMethod(self):
#  	print ('Calling parent method')
#  def setAttr(self, attr):
#  	Parent.parentAttr = attr
#  def getAttr(self):
#  	print ("Parent attribute :", Parent.parentAttr)


# class Child(Parent): # define child class
#  def __init__(self):
#  	print ("Calling child constructor")
#  def childMethod(self):
#  	print ('Calling child method')
# c = Child() # instance of child
# c.childMethod() # child calls its method
# c.parentMethod() # calls parent's method
# c.setAttr(200) # again call parent's method
# c.getAttr() # again call parent's method
# # 	def __init__(self):	

# ===OVERLOADING OPERATORS========================
# class vector:
# 	def __init__(self, a,b):
# 		self.a = a
# 		self.b = b
# 	def __str__(self):
# 		return 'vector(%d,%d)' %(self.a, self.b)
# 	def __add__(self, other):
# 		return vector (self.a+other.a, self.b+other.b)

# v1 = vector(2,10)
# v2  =vector(5,-2)
# print(v1+v2)
# # =============DATA HIDING======================================
# class justCounter:
# 	_secretCoun = 0
# 	def count(self):
# 		self._secretCoun+=1
# 		print(self._secretCoun)
# counter = justCounter()
# counter.count()
# counter.count()
# print(counter._secretCoun)
# # ======SINGLE AND SUPER INHERITORS==============================
# class mammal(object):
# 	def __init__(self, mammalName):
# 		print(mammalName, 'Is a waarm blooded animal')
# class Dog(mammal):
# 	def __init__(self):
# 		print('Dog has four legs')
# 		super().__init__('Dog')
# d1 = Dog()

# #SUPER WITH MULTIPLE IINHERITANCE
# class animal:	
# 	def __init__(self, animalName):
# 		print(animalName, 'is an animal')
# class Mammal(animal):
# 	def ___init__(self, mammalName):
# 		print(mammalName, 'is a warm-blooded animal')
# 	super().__init__(mammalName)
# class NonWingedMammal(Mammal):
# 	def __init__(self, NonWingedMammal):
# 		print(NonWingedMammal,'cannot fly') 
# 	super().__init__(NonWingedMammal)

# MULTIPLE INHERITANCE
# class NonMarineMammal(Mammal):
# 	def __init__(self, NonMarineMammalName):
# 		print(NonMarineMammalName, 'cannot swim')
# 		super().__init__(NonMarineMammalName)
# class Dog(NonMarineMammal, NonWingedMammal):
# 	def __init__(self):
# 		print('Dog has four legs')
# 		super().__init__('Dog')

# d = Dog()
# print('')
# bat  = NonMarineMammal('Bat')

# =================================================
# class rectangle():
# 	length = 12
# 	width = 23
# area = rectangle()

# print ('The area of the rectangle =',area.length*area.width)


# class rectangle2:
# 	def __init__(self,width,length):
# 		self.length = length 
# 		self.width = width
# 	def calculate(self):
# 		return self.length * self.width

# c = rectangle2(30,45)
# print(c.calculate())

# class rectangle3:
# 	def __init__(self, length, width):
# 		self.length = length
# 		self.width = width
# 	def area(self):
# 		if self.width > self.length:
# 			return self.width /self.length
# 		else :
# 			print ('Error please input a bigger figure for width ')
# calc = rectangle3(83, 78)
# print(calc.area())



# # =============================================================
# import random
# class person():
# 	pin = ''
# 	acc_no = ''

# 	def __init__(self, name):
# 		self.name = name
# 	def get_pin(self):
# 		return self.pin
# 	def set_pin(self,pn):
# 		self.pin = pn
# 	def set_Acc(self, acc):
# 		self.acc_no = acc
# 	def insert_card(self):
# 		list = [self.pin ,self.acc_no]
# 		return list2

# class account():
# 	accName = ''
# 	accBal = ''
# 	pin = ''
# 	accType = ''
# 	def __init__(person, amount, pin, Type ):
# 		self.accName = person
# 		self.accBal = amount
# 		self.pin = pin
# 		self.accType = Type
#=====JUNE 12TH========================================================
# WORKINNG WITH TIME
# import time;
# ticks = time.time()
# print(ticks)
# localtime =time.asctime( time.localtime(ticks))
# print(localtime)

# import time;
# year = time.strftime(' %Y' , time.localtime(time.localtime()))
# print('The Full Date :')
# localtime = time.strftime('%a %b %Y %H:%M: %S' , time.localtime(time.time()))
# print(localtime, '\n')

# print('the  year only')
# localtime2 = time.strftime('%Y ' , time.localtime(time.time()))
# print(localtime2, '\n')

# print('the  Month only')
# localtime3 = time.strftime('%m', time.localtime(time.time()) )
# print(localtime3,'\n')

# print('The week number only')
# localtime4 = time.strftime('%W' , time.localtime(time.time()))
# print(localtime4, '\n')

# print('The week day')
# localtime5 = time.strftime('%a' , time.localtime(time.time()))
# print(localtime5, '\n')

# print('The day of the year')
# localtime6 = time.strftime('%j', time.localtime(time.time()))
# print(localtime6,'\n')

# print('The day of the Month')
# localtime7 = time.strftime('%d', time.localtime(time.time()))
# print(localtime7,'\n')

# print('The day of the week')
# localtime8 = time.strftime('%u', time.localtime(time.time()))
# print(localtime8)

# year = time.strftime(' %Y' , time.localtime(time.localtime()))
# print(year)
# ========DELAYING TIME =====================================
# import time
# def proceedure():
# 	time.sleep(2.5)
# t0 = time.clock()
# proceedure()
# print(time.clock(),-t0,'Seconds process time')

#===== WORKING WITH CALENDERS ==================================
# import calendar
# calen = calendar.month(1996, 6)
# print(calen)
#===== WORKING WITH TRY ==========w or r========================
# try:
# 	fh = open("testfile", "w")
# 	fh.write('This is a file I am creating \n' )
# 	fh.write('I want to use it to practice')

# except IOError:
# 	print('We cannot Find the file')
# else: 
# 	('Print your content was written susccessfully')
# 	print(fh.write)
# finally: 
# 	print('We are done with the operation')
# 	fh.close()
# # Example 1==============
# try:
# 	get_input = int(input('Enter a number to find inverse \n'))
# 	inverse = 1/get_input
# 	print('The inverse of %d is ' %get_input, inverse)

# except ArithmeticError:
# 		print('Arithmetic Error')
# except ValueError:
# 		print('What you entered is not a number ')
# except ZeroDivisionError:
# 		print('Zero Errror')

#===== WORKING WITH ASSSERTION ERRORS ==================================


#===== WORKING WITH RANDOM ==================================
# import random
# numbers = [1,2,3,4,5,5,7,8,9,9,0,100]
# random.shuffle(numbers)
# print(numbers)
# # random

# Open a file .name, .closed .mode
# fo = open("textfile.txt", 'w') 
# print ("Name of the file: ", fo.name)
# print ("Closed or not : ", fo.closed)
# print ("Opening mode : ", fo.mode)
# fo.close()

# The code below dosen't work because I used .txt
# see = open('testfile.txt', "w")
# see.write('Akinola mJohn')
# see.write('Computer Science')
# see.write('200 jjjjlevel')

# The code here checks the number of a's 

# fh = open("testfile", "w")
# fh.write(' Akinola John \n' )
# fh.write('I want to use it to practice\n')

# fh = open("testfile", "r")
# counter = 0

# for myline in fh:
# 	count = 0
# 	for letter in myline:
# 		if letter == 'a':
# 			count+=1
# 	print("The number of a's in %s is %d" %(myline, count))
# 	counter += count
# print("The total number of a's in", fh.name, "is %d" %(counter))
# fh.close() 
# #  fh.seek, .read, .read

# STARTING OUT WITH TKINTER
# ======first example--------------
# import tkinter
# window = tkinter.Tk()
# window.mainloop()
# =======second example-------------
# from tkinter import messagebox
# import tkinter
# window = tkinter.Tk()
# def callme():
# 	messagebox.showinfo('This Is my first GUI experience.')
# B =tkinter.Button(window, text = ' Welcome to My Program', command = callme)
# B.pack()
# B.place(bordermode = tkinter.OUTSIDE, height = 500 , width = 500)
# window.mainloop()
# =======third example======-----------------
# import tkinter
# root = tkinter.Tk()
# for each in range(5):
# 	for val in range(5):
# 		tkinter.Label(root, text='R%s/C%s'%(each,val), borderwidth = 1).grid(row=each,column=val)
# root.mainloop()
# =======fourth example==========------------------
# import tkinter
# window = tkinter.Tk()
# abc = tkinter.Label(window, text='Kindly tell us your name: ')
# abc.pack({'side':'top'})
# entName = tkinter.Entry(window)
# entName.pack({'side':'top'})
# # entName( bordermode = tkinter.OUTSIDE, height= 200 , width= 300 ) Entry is not callabe
# window.mainloop()

# mybutton = tkinter.Button(window, text ='Submit', command='submitForm')
# mybutton.pack({'side':'top','pady':20})
# window.mainloop()
# 
# Converting a file to list
# read = open('testfile', 'r')
# val = ''
# lst = []
# for each in read:
# 	print(each)
# 	val+=each
	
# 	lst.append(each)
# print(lst)

# Converting a list to file
# file = open('testfile','w')
# a = ['shoe','bag','ornament','ring']
# for item in a:
# 	file.write(item+'\n')

# Output from file with average 
# ===============wahala of the day================
# newf = open('outputfile.txt','r')
# newfs =  open('inputfile.txt','w')
# newl = []
# for line in newf:
# 	tlist = line.split(' ')
# 	print(tlist)
# 	a = (int(tlist[2])+int(tlist[3])+int(tlist[4]))/3
# 	newfs.write(line+str(a)+'\n')
# 	# print(newfs.read)


# ==========Personal Practice=================
# import tkinter
# window = tkinter.Tk()
# abc = tkinter.Label(window, text='Enter your name')
# abc.pack({'side':'top'})

# entName = tkinter.Entry(window)
# entName.pack({'side':'top'})

# mybtn = tkinter.Button(window, text = 'Submit', command='submitForm')
# mybtn.pack({'side':'top','pady':30})

# window.mainloop()

# ========JUNE 14TH=================
# from tkinter import *
# import tkinter
# window = tkinter.Tk()
# # username and password here
# name = tkinter.Label(window, text= 'Username',font= 'Arial 12 bold')
# name.pack()

# uinput = tkinter.Entry(window)
# uinput.pack()

# password = tkinter.Label(window, text= 'Password',font= 'Arial 12 bold')
# password.pack()
# passd = tkinter.Entry(window)
# passd.pack()

# login = tkinter.Button(window, text='Login', command = 'submitForm',font= 'Arial 12 bold')
# login.pack()
# # invalid syntax error when I didn't use ' , '

# # check boxes here
# check1 = tkinter.IntVar()
# check2 = tkinter.IntVar()

# a = tkinter.Checkbutton(window, text ='Covenant', variable = check1, onvalue= 1, offvalue= 0, width= 20)
# a.pack()
# b = tkinter.Checkbutton(window, text = 'Babcock', variable = check2, onvalue= 1, offvalue= 0, width= 20 )
# b.pack()

# # radiobutton
# # define a function
# def myfun():
# 	usrSelect = 'You selected the option' + str(myvar.get())
# 	label.config(text = usrSelect)

# #--text--variable--value--command
# # command takes function name
# # variable takes variable name
# # what is anchor = E
# myvar = IntVar()
# opt1 = Radiobutton(window, text='Male',variable= myvar,value= 1,command= myfun)
# opt1.pack()
# opt2 = Radiobutton(window, text='Female',variable= myvar,value= 2,command= myfun)
# opt2.pack()
# opt3 = Radiobutton(window, text='Other',variable= myvar,value= 3,command= myfun)
# opt3.pack()

# # define label
# label =tkinter.Label(window)
# label.pack()




# # frame here
# frame = Frame(window)
# frame.pack()

# bframe = Frame(window)
# bframe.pack(side = BOTTOM)

# rdbtn = Button(frame, text ='red',fg='red')
# rdbtn.pack(side = LEFT)

# grnbtn = Button(frame, text ='green',fg='green')
# grnbtn.pack(side=LEFT)

# bluebtn = Button(frame, text ='blue',fg='blue')
# bluebtn.pack(side=LEFT)

# blackbtn = Button(frame, text ='black',fg='black')
# blackbtn.pack(side=BOTTOM)

# # =====How TO Use SPINBOX========================
# sb = tkinter.Spinbox(window, from_=0 ,to = 15 )
# sb.pack()
# # ===============================================
# # =====MESSAGEBOX==============
# from tkinter import messagebox
# def show():
# 	messagebox.showinfo('Welldone!',' Congratulations')
# mybtn2 = tkinter.Button(window, text= 'Submit Form', command=show)
# mybtn2.pack({'side':'top','pady':20})
# =====LIST BOXES============
# lstbx = Listbox(window, width = 20, font= 'Arial 12 bold')
# countries = ['Nigeria', 'Botswana','Congo', 'China', 'Algeria']
# lstbx.pack()
# for i in countries:
# 	lstbx.insert(lstbx.size(),i)
# .size is very important
# ======Scale=================
# tryto = Scale(window, from_ = 0, to = 20, orient= 'horizontal', length= 20)
# tryto.pack()
# # =========COMBO BOX===================
from tkinter import ttk
window = Tk()
week = ['monday','Tuesday','Wednesday','Thursday','Friday']
showeek = ttk.Combobox(window, values = week)
showeek.grid()

window.mainloop()


#==========MENUS=============
# from tkinter import Tk, Frame,Menu





#==========MVC'S=============
# import tkinter
# # import controller 
# # create a function as controller
# def click():
# 	# set a counter
# 	counter.set(counter.get()+1)
# 	if __name__ == '__main__':
# window.tkinter.Tk()
# # Model
# counter= tkinter.IntVar()
# counter.set(0)
# # Views 
# frame = tkinter.Frame(window)
# frame.pack()

# Button = tkinter.Button(frame, text ='Click', command= click)
# label = tkinter.Button(frame, textvariable='counter')
# label.pack()
# window.mainloop()

from tkinter import Tk, Frame, Menu
class Example(Frame):
	def __init__(self,frame):
		Frame.__init__(self,frame)

		self.frame=frame
		self.initUI()
	def initUI(self):
		self.frame.title('simple menu')

		menubar = Menu(self.frame)
		self.frame.config(menu=menubar)
		fileMenu = Menu(menubar)
		mrmenu = Menu()
		submenu = Menu(mrmenu)
		# submenu is added under mrmenu
		# cascade submenu under mrmenu and mrmenu under menu
		submenu.add_command(label='News')
		submenu.add_command(label='Gist')
		submenu.add_command(label='Advice')
		mrmenu.add_cascade(label='Import',menu=mrmenu)

		fileMenu.add_command(label="Exit", command=self.onExit)
		menubar.add_cascade(label="File", menu=fileMenu)
		menubar.add_cascade(label="Sales", menu=mrmenu)
		menubar.add_cascade(label="Purchases", menu=mrmenu)
		menubar.add_cascade(label="Help", menu=mrmenu)

	def onExit(self):
		self.quit()
	def main():
		root = Tk()
		root.geometry('250x150+300+300')
		# use x not *
		app = Example(root)
		root.mainloop()
if __name__ =='__main__':
	Example.main()






 