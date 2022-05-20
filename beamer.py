import math
n=int(input())
m=int(input())
print(m,n)
#If we accept as outcomes all possible ways of placing n particles in m boxes distinguishing the identity of each particle the prob is s_1
#If we assume that the particles are not distinguishable, that is, if alltheir permutations count as one then prob is s_2
#If we do not distinguish between the particles and also we assumethat in each box we are allowed to place at most one particle the prob is s_3
s_1=(math.factorial(n))/math.pow(m,n)
s_2=(math.factorial(m-1)*math.factorial(n))/math.factorial(n+m-1)
s_3=(math.factorial(n)*math.factorial(m-n))/math.factorial(m)
print(s_1,s_2,s_3)
