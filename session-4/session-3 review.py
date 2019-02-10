a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

def findElemGreaterThan5():
    for elem in a:
        if elem <= 5:
            b.append(elem)
    print(b) 

findElemGreaterThan5() 
