import math

def factorial(n):
    Factorial = 1;
    for i in range(2, n+1):
        Factorial *= i;
    return Factorial;
    
def nCk (n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))
    
def prob(n, p, N):
    return nCk(N, n) * pow(p, n) * pow(1 - p, N - n)

def infoMeasure(n, p, N):
    return (-math.log(prob(n, p, N), 2))

def sumProb(N, p):
    sum = 0.0
    for i in range(1, N):
        sum += prob(i, p, N)
    return sum

    """ Kết quả của hàm sumProb(15, 0.15) là: 0.9999999999741233 ~ 1
        Kết quả của hàm sumProb(300, 0.3) là:  0.9999999999999832 ≈ 1
        => Hàm sumProb có thể sử dụng để kiểm chứng tổng xác suất của phân bố binamial = 1 """

def approxEntropy(N, p):
    entropy = 0.0
    for i in range(1, N):
        entropy += prob(i, p, N) * infoMeasure(i, p, N)
    return entropy

    """ Kết quả của hàm approxEntropy(15, 0.5) là: 2.9989956395253916
        Kết quả của hàm approxEntropy(500, 0.5) là: 5.529987244677518 """
