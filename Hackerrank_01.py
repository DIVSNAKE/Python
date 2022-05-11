'''
a=int(input())
b=int(input())
c=int(input())
print(a+b+c) #сумма трёх чисел


a=int(input())
print(a**2) #квадрат числа


a=int(input())
print(a**3) #число в кубе (у Наташи: print(a*a*a))


a=int(input())
print(a**100) #число в 100 степени


a=int(input())
b=int(input())
print(a*b) #площадь прямоугольника


a=int(input())
b=int(input())
print(1/2*a*b) #площадь прямоугольного треугольника

#решение Наташи:
print((a*b)/2))


a=int(input())
print(a%10) #последняя цифра числа


n=int(input())
k=int(input())
print(k//n)
print(k%n) #делёж печенек с остатком


a=int(input())
b=int(input())
c=int(input())
print(a//2+a%2+b//2+b%2+c//2+c%2) #парты 1, деление с остатком

#решение Наташи:
a=int(input())
b=int(input())
c=int(input())
import math
a1=math.ceil(a/2)
b1=math.ceil(b/2)
c1=math.ceil(c/2)
print(a1+b1+c1)


a=float(input())
print(round(a,2)) #округление в большую сторону до двух знаков


a=int(input())
b=int(input())
import math
c=round(math.sqrt(a**2+b**2),11 
print(c) #гипотенуза прямоугольного треугольника
#решение Наташи:
a=int(input())
b=int(input())
import math
c=round(math.sqrt(a*a+b*b),11)
print(c)


name=input()
print("How are you doing, "+name+"?") #ввод имени


a=int(input())
print("The next number of the number "+str(a)+ " is "+str(a+1)+".")
print("The previous number of the number "+str(a)+ " is "+str(a-1)+".")
#следующее и предыдущее число


a=int(input())
a1=a//100
a2=a//10%10
a3=a%10
print("The first digit of the number "+str(a)+ " is equal to "+str(a1)+".")
print("The second digit of the number "+str(a)+ " is equal to "+str(a2)+".")
print("The third digit of the number "+str(a)+ " is equal to "+str(a3)+".")
#все цифры трёхзначного числа подряд
#решение Наташи:
a=int(input())
b=a//100
c=(a//10)%10
d=a%10
print('The first digit of the number '+str(a)+' is equal to '+str(b)+'.')
print('The second digit of the number '+str(a)+' is equal to '+str(c)+'.')
print('The third digit of the number '+str(a)+' is equal to '+str(d)+'.')


n=int(input())
h=n//60%12
m=n%60
print(str(h)+":"+str(m)) #часы
'''
