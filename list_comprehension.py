

l = [9,15,12,3,7,11]
x = 10

def get_smaller_list_comprehension(li,x):

    return [ele for ele in li if ele<x]


result = get_smaller_list_comprehension(l,x)
print(result)