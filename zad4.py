# В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из 
# которых 9 белых. Из каждого ящика вытаскивают случайным образом по два мяча. Какова вероятность
# того, что все мячи белые? Какова вероятность того, что ровно два мяча белые? Какова вероятность
# того, что хотя бы один мяч белый?

from math import factorial

def combination(n,k):
    return(factorial(n)/(factorial(k)*(factorial(n-k))))

def bernuli(n,k,p):
    return(combination(n,k)*p**k*(1-p)**(n-k))

n1=10
m1=7

n2=11
m2=9

k=2

p1B=combination(m1,k)/combination(n1,k)
p2B=combination(m2,k)/combination(n2,k)
pB=p1B*p2B*100
print(f'Вероятность того, что все мячи белые = {pB :.2f}%')

p1TolkoBel=combination(m1,k)/combination(n1,k)
p2TolkoChern=combination(n2-m2,k)/combination(n2,k)

pA1=p1TolkoBel*p2TolkoChern

p1TolkoChern=combination(n1-m1,k)/combination(n1,k)
p2TolkoBel=combination(m2,k)/combination(n2,k)

pA2=p1TolkoChern*p2TolkoBel

p1OdinBel=(combination(m1,k-1)*combination(n1-m1,k-1))/combination(n1,k)
p2OdinBel=(combination(m2,k-1)*combination(n2-m2,k-1))/combination(n2,k)

pA3=p1OdinBel*p2OdinBel

pRovno2Bel=(pA1+pA2+pA3)*100

print(f'Вероятность того, что ровно два мяча белые = {pRovno2Bel :.2f}%')

pOdinBel=(1-p1TolkoChern*p2TolkoChern)*100

print(f'Вероятность того, что хотя бы один мяч белый = {pOdinBel :.2f}%')