



def getEvenOdd(l):
     
    even = [ ele for ele in l if ele % 2 == 0]
    odd =  [ ele for ele in l if ele % 2 != 0 ]
    
    return even,odd

input = [1,2,3,4,5]
result = getEvenOdd(input)
print(result)