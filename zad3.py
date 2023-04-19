# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

from math import factorial

def combination(n,k):
    return(factorial(n)/(factorial(k)*(factorial(n-k))))

n=144
k=70
p=0.5

def bernuli(n,k,p):
    return(combination(n,k)*p**k*(1-p)**(n-k))

pm=bernuli(n,k,p)*100

print(f'Вероятность того, что орел выпадет ровно 70 раз = {pm :.2f}%')