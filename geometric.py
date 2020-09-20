import math

def prob(n, p):
    return p * pow((1 - p), n - 1)

def infoMeasure(n, p):
    return (- math.log(prob(n, p), 2))
    
def sumProb(N, p):
    sum = 0
    for i in range(1, N):
        sum += prob(i, p)
    return sum
    """ Kết quả của hàm sumProb(150, 0.15) là: 0.999999999969561 ≈ 1
        Kết quả của hàm sumProb(1500, 0.15) là: 0.9999999999999999 ≈ 1
        => Hàm sumProb có thể sử dụng để kiểm chứng tổng xác suất của phân bố geometric = 1 """

def approxEntropy(N, p):
    
    entropy = 0
    for i in range(1, N):
        entropy += prob(i, p) * infoMeasure(i, p)
    return entropy
    """ Kết quả của hàm approxEntropy(30, 0.5) là: 1.9999999422580004 ≈ 2
        Kết quả của hàm approxEntropy(500, 0.5) là: 1.9999999999999998 ≈
        => Hàm approxEntropy tính xấp xỉ entropy của nguồn tin geometric & 
        entropy của nguồn geometric có giá trị = 2 """