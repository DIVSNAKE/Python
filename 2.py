'''
n=int(input())
h=n//60%12
m=n%60
print(str(h)+":"+str(m)) #часы


apples=10
print(apples==10)
print(apples<int(input()))
print(apples<=10)
print(apples>10)
print(apples>=10)
print(apples!=10)


apples=10
print(apples<20 and apples>5)
print(apples<10 and apples>int(input()))
print(apples<=10 and apples>5)
print(apples<3 or apples>7)
print(apples<3 or apples>15)
print(apples<3 or apples>10)


apples=10
print(not(apples<3))
print(not apples<3)
print(not(apples<20 or apples>5))
print(not apples<20 or apples>5)


apples=10
print(not apples<3 or apples<15 and apples>5)
print(not (apples<3 or apples<15) and apples>5)


day=int(input())
month=int(input())
#print(not(day==28 and month==7))
#print(day!=28 or month!=7)


a=int(input())
if a>0:
    print ("Положительное")
    print ("qwerty")
else:
    print ("Отрицательное")
    x=15
    print(x**a)
print (123)


a=int(input())
if a>0:
    print ("Положительное")
elif a<0:
    print ("Отрицательное")
else:
    print ("Ноль")


a=int(input())
if a>0:
    if a%2==0:
        print ("Положительное чётное")
    else:
        print ("Положительное нечётное")
elif a<0:
    if a%2==0:
        print ("Отрицательное чётное")
    else:
        print ("Отрицательное нечётное")
else:
    print ("Равно 0")


a=int(input())
if a%15==0:
    print ("Делится на 15")
if a%5==0:
    print ("Делится на 5")
if a%3==0:
    print ("Делится на 3")
else:
    print ("")
'''


    


