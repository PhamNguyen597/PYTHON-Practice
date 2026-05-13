                        #CHAPTER 1
#1
# print("what is your name ?")
# name=input("my name is: ")
# print("How old are youngu?")
# age=int(input("i'm about: "))
# print("why do u study Python?")
# aim=input("well, because: ")

#2
# a=input("name= ")
# print("Hello, " + a)


#3
# a=input("age= ")
# print("you are "+ a +" years old")


#4
# a=int(input())
# b=int(input())
# print(a+b)


#5
# a=int(input())
# b=int(input())
# c=(a+b,a-b,a*b,a/b)
# for i in c:
#     if b==0:
#         print("error")
#     elif b!=0:
#         print(i)


#6
# a=int(input("Type a number: "))
# print(a**2)

#7
# length=int(input("Chieu dai la: "))
# width=int(input("Chieu rong la: "))
# print("Dien tich hinh chu nhat la S= ", length*width)


#8
# a=int(input("r= "))
# pi=3.14
# print("S hinh tron= ", pi*(a**2))


#9
# a=int(input())
# b=int(input())
# c=int(input())
# print("tong cua 3 so la:",a+b+c)


#10
# print("what is your name and what about your age?")
# a=input("name= ")
# b=input("age= ")
# print("My name is ",a," and i'm ",b," years old")


                                    #CHAPTER 2
#11
# a=int(input("Type a number: "))
# if a%2==0:
#     print("even")
# else :
#     print("odd")


#12
# a=int(input())
# if a>0:
#     print("positive")
# elif a<0:
#     print("negative")
# else:
#     print("zero")


#13
# a=int(input("age= "))
# if a>=18:
#     print("adult")
# else:
#     print("Minor")


#14
# a=float(input())
# if a>=8:
#     print("Grade: A")
# elif a<8 and a>=6.5:
#     print("Grade: B")
# elif a<6.5 and a>=5:
#     print("Grade: C")
# else:
#     print("Grade: F")


#15
# while True:
#     password=input("Password= ")
#     if password=="Python123":
#         print("Access granted")
#         break
#     else:
#         print("Access denied")


#16
# for i in range(1,21):
#     print(i)


#17
# for i in range (1,51):
#     if i%2==0:
#         print(i)
    

#18
# for i in range (1,51):
#     if i%2!=0:
#         print(i)


#19
# a=int(input("Type a number: "))
# total=0
# for i in range (1,a+1):
#     total+=i
# print(total)
    

#20
# a=int(input("Type a number: "))
# total=1
# for i in range(1,a+1):
#     total=total*i
# print(total)


#21
# n=int(input("Type a number: "))
# for i in range(1,11):
#     print(n,"x",i," =",n*i)


#22
# n=11
# while n!=1:
#     n=n-1
#     print(n)


#23
# n=int(input("Type a number: "))
# total=0
# i=1
# while i<=n:
#     total+=i
#     i+=1
# print(total)


#24
# total=0
# while True:
#     n=int(input("Type a number: "))
#     if n==0:
#         break
#     else:
#         total+=n
# print(total)


#25
# while True:
#     n=input("Type your name: ")
#     if n=="stop":
#         break
#     else:
#         print(n)


                                    #CHAPTER 3
#26
# def greet(name):
#     print("Hello, ",name)
# greet("nguyen")


#27
# def square(x):
#     print(x**2)
# square(2)


#28
# def cube(x):
#     print(x**3)
# cube(2)


#29
# def isodd(x):
#     if x%2!=0:
#         return True
#     else:
#         return False
# print(isodd(3))


#30
# def iseven(x):
#     if x%2==0:
#         return True
#     else: 
#         return False
# print(iseven(3))


#31
# def add(a,b):
#     print(a+b)
# add(1,2)


#32
# def subtract(a,b):
#     print(a-b)
# a=int(input())
# b=int(input())
# subtract(a,b)


#33
# def multiply(a,b):
#     print(a*b)
# a=int(input())
# b=int(input())
# multiply(a,b)


#34
# def devide(a,b):
#     print(a/b)
# a=int(input())
# b=int(input())
# devide(a,b)


#36
# def smallest(a,b,c):
#     if a<=b and a<=c :
#         return a
#     elif b<=a and b<=c :
#         return b
#     elif c<=a and c<=b:
#         return c
# a=int(input())
# b=int(input())
# c=int(input())
# print(smallest(a,b,c))


#35
# def biggest(a,b,c):
#     if a>=b and a>=c :
#          return a
#     elif b>=a and b>=c :
#         return b
#     elif c>=a and c>=b:
#         return c
# a=int(input())
# b=int(input())
# c=int(input())
# print(biggest(a,b,c))


#37
# def grade(x):
#     if x>=8:
#         print("Grade: A")
#     elif x<8 and x>=6.5:
#         print("Grade: B")
#     elif x<6.5 and x>=5:
#         print("Grade: C")
#     else:
#         print("Grade: F")
# while True:
#     x=int(input())
#     if x>10 or x<0:
#         print("try again")
#     else:
#         grade(x)
#         break


#38
# def age(x):
#     if x>=18:
#         print("Adult")
#     else:
#         print("Minor")
# a=int(input())
# age(a)


#39
# def number(x):
#     if x>0:
#         return True
#     else:
#         return False
# a=int(input())
# print(number(a))


#40
# def length(a):
#     print(len(a))
# x=input()
# length(x)


                                #CHAPTER 4
#41
# fruit=["apple","banana","orange"]
# for i in fruit:
#     print(i)


#42
# fruit=["apple","banana","orange"]
# print(fruit[0])
# print(fruit[-1])


#43
# fruit=["apple","banana","orange"]
# print(len(fruit))


#44
# empty=[]
# empty.append("nguyen")
# print(empty)


#45
# fruit=["apple","banana","orange"]
# fruit.insert(1,"nguyen")
# print(fruit)


#46
# fruit=["apple","banana","orange"]
# fruit.remove('apple')
# print(fruit)


#47
# numb=[5,4,67,37,2,5,7]
# numb.sort()
# print(numb)


#48
# numb=[5,4,67,37,2,5,7]
# numb.sort(reverse=True)
# print(numb)


#49
# numb=[5,4,67,37,2,5,7]
# a=0
# for k,v in enumerate(numb):
#     if v==5:
#         a+=1
#     else:
#         a+=0
# print("number of 5: ", a) #dung numb.count(5) cung duoc


#50
# numb=[5,4,67,37,2,5,7]
# total=0
# for i in numb:
#     total+=i
# print(total)  #sum(numb) cho ngan


#51
# numb=[5,4,67,37,2,5,7]
# numb.sort()
# print("the biggest number here is: ", numb[-1])  #max(numb) cung duoc nhe


#52
# numb=[5,4,67,37,2,5,7]
# numb.sort()
# print("the smallest number here is: ", numb[0]) #tuon tu tren min


#53
# numb=[5,4,67,37,2,5,7]
# newnumb=[]
# for i in numb:
#     if i%2==0:
#         newnumb.append(i)
#     else:
#         continue
# print(newnumb)


#54
# numb=[5,4,67,37,2,5,7]
# newnumb=[]
# for i in numb:
#     if i%2!=0:
#         newnumb.append(i)
#     else:
#         continue
# print(newnumb)


#55
# numb=[4,7,3,78,3]
# newnumb=[]
# for i in range(len(numb)-1,-1,-1):
#     newnumb.append(numb[i])
# print(newnumb)


                                #CHAPTER 5
#56
# student = {
#     "name": "Nguyen",
#     "age": 18,
#     "city": "Bac Giang"}
# for key in student.keys():
#     print(key)
# for value in student.values():
#     print(value)
# for key, value in student.items():
#     print(key, value)

# student = {
#     "name": "Nguyen",
#     "age": 18,
#     "city": "Bac Giang"}
# print(student.keys())
# print(student.values())
# print(student.items())



#57
# student = {"name": "Nguyen", "age": 18, "class": "02"}
# print(list(student.keys()))
# print(list(student.values()))
# print(list(student.items()))


#58
# student = {"name": "Nguyen", "age": 18, "class": "02"}
# def check(a):
#     if "name" in a :
#         return True
#     else: 
#         return False
# print(check(student))


#59
# student = {"name": "Nguyen", "age": 18, "class": "02"}
# def check(a):
#     if "school" in a:
#         print(a.get("school"))
#     else:
#         print("not found")
# check(student)

#60
# message = "hello world"
# numb={}
# for i in message:
#     if i not in numb:
#         numb[i]=0
#     numb[i]+=1
# print(numb)
    

#61
# names = ['Lan', 'Nam', 'Lan', 'An', 'Nam', 'Lan']
# numb={}
# for i in names:
#     if i not in numb:
#         numb[i]=0
#     numb[i]+=1
# print(numb)


#62
# inventory = {'rope': 1, 'torch': 6, 'gold coin': 42}
# total=0
# for i in inventory:
#     total+=inventory[i]
# print(total," items")


#63
# stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# def displayinventory(inv):
#     print("Inventory: ")
#     total=0
#     for k,v in inv.items():
#         print("  ",k, ": ", v)
#         total+=v
#     print("Total of items: ", total)
# displayinventory(stuff)


#64
# def addtoinventory(inventory, addeditems):
#     for i in addeditems:
#         if i not in inventory:
#             inventory[i]=0
#         inventory[i]+=1
#     return inventory
# inv= {'gold coin': 42, 'rope': 1}
# add= ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# print(addtoinventory(inv,add))


#65
# users = {'alice': 2, 'bob': 5, 'charlie': 1, 'admin': 7}
# for i in users:
#     if users[i]>3:
#         print("User who have failed login > 3: ",i)


#66
# allguests = {
#     'Alice': {'apples': 5, 'pretzels': 12},
#     'Bob': {'ham sandwiches': 3, 'apples': 2},
#     'Carol': {'cups': 3, 'apple pies': 1}
# }
# def totalBrought(guests, item):
#     itemss={}
#     for k,v in guests.items():
#         for i in v:
#             if i not in itemss:
#                 itemss[i]=0
#             itemss[i]+=v[i]
#     if item in itemss:
#         return(itemss.get(item,0))
# print(totalBrought(allguests,"pretzels"))


#68
# scores = {'Lan': 8, 'Nam': 6, 'An': 9}
# for i in scores:
#     if max(scores.values())==scores[i]:
#         print(i,": ", max(scores.values()))


#67
# sentence = "python is good and python is fun"
# count={}
# word=sentence.split()   #split tach cau thanh tu
# for i in word:
#     if i not in count:
#         count[i]=0
#     count[i]+=1
# print(count)


#69
# scores = {'Lan': 8, 'Nam': 6, 'An': 9}
# for i in scores:
#     if min(scores.values())==scores[i]:
#         print(i,": ", min(scores.values()))


#70
# board1 = {
#     '1a': 'bking',
#     '6c': 'wqueen',
#     '2g': 'bbishop',
#     '5h': 'bqueen',
#     '3e': 'wking'}
# def isvalidchessbroad(board):
#     chess=["king","queen","knight","bishop","rook","pawn"]
#     wking=0
#     bking=0
#     wpawn=0
#     bpawn=0
#     wpiece=0
#     bpiece=0
#     for k,v in board.items():
#         if len(k)!=2:
#             return False
#         if k[0] not in "12345678":
#             return False
#         if k[1] not in "abcdefgh":
#             return False
#         if v[0] not in "wb":
#             return False
#         if v[1:] not in chess:
#             return False
#         if v[0]=="w":
#             wpiece+=1
#             if v[1:]=="king":
#                 wking+=1
#             if v[1:]=="pawn":
#                 wpawn+=1
#         elif v[0]=="b":
#             bpiece+=1
#             if v[1:]=="king":
#                 bking+=1
#             if v[1:]=="pawn":
#                 bpawn+=1
#         if wking!=1 or bking!=1:
#             return False
#         if wpawn>8 or bpawn>8:
#             return False
#         if wpiece>16 or bpiece>16:
#             return False
#     return True
# print(isvalidchessbroad(board1))
        

                                        #PROJECT
#1
# student = {"name": "Nguyen","age": 18,"city": "Bac Giang"}
# print(student.items())
# a=int(input("Your new age: "))
# student["age"]=a
# print(student.items())
# if "name" in student:
#     print(True)
        

#2
# numbers = [12, 5, 8, 21, 4, 9, 10, 3]
# total=0
# even=0
# odd=0
# for i in numbers:
#     total+=i
#     if i%2==0:
#         odd+=1
#     elif i%2!=0:
#         even+=1
# print("Total of all numbers: ", total)
# print("so chan",odd)
# print("so le",even)
# print("biggest ",max(numbers))
# print("smallest ",min(numbers))


#3
# a=input()
# a=a.split()
# b={}
# for i in a:
#     if i not in b:
#         b[i]=0
#     b[i]+=1
# print(b)


#4
# inventory = {'rope': 1, 'torch': 6, 'gold coin': 42}
# print(inventory)
# print("The new changes in which items ?")
# a=str(input())
# print("the new figures?")
# b=int(input())
# inventory[a]=b
# print(inventory)
# total=0
# for i in inventory:
#     total+=inventory[i]
# print("Total number of all items: ",total)
# c=str(input())
# if c in inventory:
#     print(True)
# else:
#     print(False)
    
    
#5
# import random
# users = {'alice': 2, 'bob': 5, 'charlie': 1}
# print(users)
# users["alice"]+=1
# print(users)
# for i in users:
#     if users[i]>3 :
#         print("account locked")
    

#7
# scores = {'Lan': 8, 'Nam': 6, 'An': 9}
# total=0
# for k,v in scores.items():
#     print(k,": ", v)
#     total+=v
#     if v>=8:
#         print("A")
#     elif v>=6.5 and v<8:
#         print("B")
#     elif v>=5 and v<6.5:
#         print("C")
#     else:
#         print("F")
# print("Average point of class: ",total/len(scores))
# print("the highest point in class:",max(scores, key=scores.get),": ",max(scores.values()))










