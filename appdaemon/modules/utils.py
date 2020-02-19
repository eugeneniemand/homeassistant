def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
    
def intersect(a, b):
    return list(set(a) & set(b))