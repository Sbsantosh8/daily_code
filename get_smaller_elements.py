
l = [8,100,20,40,3,7]
x=10
# op = [8,3,7]
smaller_elements = []


def get_smaller_elements(li,x):
    for e in li :
        if  e < x:
            smaller_elements.append(e)
    return smaller_elements


result = get_smaller_elements(l,x)
print(result)


