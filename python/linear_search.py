# array_to_search_through = []
# for number in range(1, 1001):
#     array_to_search_through.append(number)

def linear_search(value_to_find, array_to_search_through):
    x = value_to_find
    y = array_to_search_through
    z = []

    for i in range(0, len(y)):
        if(x == y[i]):
            z.append(i)

    if(len(z) == 0):
        return None
    elif(len(z) == 1):
        return z[0]
    else:
        return z