'''
a=int(input())
b=int(input())
if a>b:
    print (b)
if b>a:
    print (a) #наименьшее из двух чисел
    
Решение Наташи:
a=int(input())
b=int(input())
if a>b:
    print(b)
else:
    print(a)


a=int(input())
if 0<a<10:
    print ("Однозначное")
if 10<=a<100:
    print ("Двузначное") #однозначное или двузначное число

Решение Наташи:
a=int(input())
if (a>9 or a<-9):
    print("two-digit number")
else:
    print("one-digit number")


a=int(input())
b=int(input())
if abs(a)>abs(b):
    print (a)
if abs(b)>abs(a):
    print (b) #наибольшее из двух чисел по модулю

Решение Наташи:
a=int(input())
b=int(input())
if abs(a)>abs(b):
    print(a)
else:
    print(b)


a=int(input())
b=int(input())
if a==b:
    print(True)
else:
    print (False) #равны ли числа

Решение Наташи:
a=int(input())
b=int(input())
print(a==b)


a=input()
print (len(a)) #длина строки


a=input()
if len(a)>10:
    print("More")
else:
    print("Less") #длиннее ли строка 10 символов

#Решение Наташи:
a=input()
if len(a)>10:
    print("MORE")
else:
    print("LESS")


a=input()
if "X" in a:
    print("Yes")
else:
    print("No") #длиннее ли буква Х в строке


a=input()
b=input()
if a in b:
    print("Yes")       
else:
    print("No") #содержится ли одна строка в другой


a=int(input())
b=int(input())
c=int(input())
if a>b>c or b>a>c:
    print(c)
elif a>c>b or c>a>b:
    print(b)
elif c>b>a or b>c>a:
    print(a) #наименьшее из трёх чисел

#Решение Наташи:
a=int(input())
b=int(input())
c=int(input())
if a<b and a<c:
    print(a)
elif b<a and b<c:
    print(b)
else:
    print(c)


a1=int(input())
b1=int(input())
c1=int(input())
a=abs(a1)
b=abs(b1)
c=abs(c1)
if a>b>c or b>a>c:
    print(c)
elif a>c>b or c>a>b:
    print(b)
else:
    print(a) #наименьшее из трёх чисел по модулю
    
#Решение Наташи:
a=int(input())
b=int(input())
c=int(input())
if abs(a)>abs(b) and abs(a)>abs(c):
    print(a)
elif abs(b)>abs(a) and abs(b)>abs(c):
    print(b)
else:
    print(c)


a=int(input())
b=int(input())
c=int(input())
if a==b==c:
    print(3)
elif a==b or b==c or c==a:
    print(2)
elif a!=b or b!=c or c!=a:
    print(0) #сколько совпадающих чисел

#Решение Наташи:
a=int(input())
b=int(input())
c=int(input())
if a==b==c:
    print(3)
elif a==b or b==c or a==c:
    print(2)
else:
    print(0)


a=int(input())
if a>0:
    print(1)
elif a==0:
    print (0)
else:
    print(-1) #положительное или отрицательное число
            
#Решение Наташи:    
a=int(input())
if a>0:
    print(1)
elif a<0:
    print(-1)
else:
    print(0)


a=int(input())
if a%4==0 and a%100!=0 or a%400==0:
    print("Високосный, 366 дней")
else:
    print("Не високосный, 365 дней") #сколько дней в году

#Решение Наташи: 
a=int(input())
if (a%4==0 and a%100!=0) or a%400==0:
    print(366)
else:
    print(365)


X=int(input())
Y=int(input())
if X>0 and Y>0:
    print("I")
if X<0 and Y>0:
    print("II")    
if X<0 and Y<0:
    print("III")
if X>0 and Y<0:
    print("IV") #координатная четверть

#Решение Наташи:
x=int(input())
y=int(input())
if x>0:
    if y>0:
        print("I")
    else:
        print("IV")
else:
    if y>0:
        print("II")
    else:
        print("III")    


a=int(input())
b=int(input())
c=int(input())
if a+b>=c and b+c>=a and a+c>=b:
    print("Yes")
else:
    print("No")

#Решение Наташи:
a=int(input())
b=int(input())
c=int(input())
if (a+b)>=c and (b+c)>=a and (a+c)>=b:
    print("YES")
else:
    print("NO")


a=int(input())
if a%15==0 and a%5==0 and a%3==0:
    print ("15, 5, 3")
if a%15==0:
    print ("15")
if a%5==0:
    print ("5")
if a%3==0:
    print ("3")
else:
    print()

#Решение Наташи:
a=int(input())
if a%15==0:
    print('Divisible by 15')
elif a%5==0:
    print('Divisible by 5')
elif a%3==0:
    print('Divisible by 3')
else:
    print("-")
'''
    
