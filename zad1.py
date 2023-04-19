# Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8. Стрелок 
# выстрелил 100 раз. Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.

from math import factorial

def combination(n,k):
    return(factorial(n)/(factorial(k)*(factorial(n-k))))

n=100
k=85
p=0.8

def bernuli(n,k,p):
    return(combination(n,k)*p**k*(1-p)**(n-k))

pn=bernuli(n,k,p)*100

print(f'Вероятность того, что стрелок попадет в цель ровно 85 раз = {pn :.2f}%')