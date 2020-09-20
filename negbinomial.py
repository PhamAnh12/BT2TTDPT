import math

def factorial(n):
    Factorial = 1;
    for i in range(2, n+1):
        Factorial *= i;
    return Factorial;
    
def nCk (n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))
    
def prob(n, p, r):
    return nCk(n-1, r-1) * pow(p, r) * pow(1 - p, n - r)

def infoMeasure(n, p, r):
    return (-math.log(prob(n, p, r), 2))

def sumProb(N, p, r):
    sum = 0.0
    for i in range(r, N):
        sum += prob(i, p, r)
    return sum
    """ Kết quả của hàm sumProb(150, 0.15, 3) là: 0.999999988717619 ~ 1
    Kết quả của hàm sumProb(300, 0.3, 3) là: 0.9999999999999991 ~ 1
    Vậy hàm sumProb có thể sử dụng để kiểm chứng tổng xác suất của phân bố negative nebinomial bằng 1 """

def approxEntropy(N, p, r):
    entropy = 0.0
    for i in range(r, N):
        entropy += prob(i, p, r) * infoMeasure(i, p, r)
    return entropy
""" Kết quả của hàm approxEntropy(150, 0.5, 3) là: 3.1156477963110514
    Kết quả của hàm approxEntropy(500, 0.5, 5) là:  3.5831050320041116"""