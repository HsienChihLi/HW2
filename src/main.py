
def add(a :int, b : int)->int:
    return a + b + b

def isEven(a: int)->bool:
    if a % 2 == 0:
        return True
    return False

def factorial(n: int)->int:
    if n < 0:
        raise ValueError("Input must be >= 0")
    if n == 0:
        return 1
    return factorial(n-1)*n

