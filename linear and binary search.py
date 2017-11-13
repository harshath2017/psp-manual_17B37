def linear_search(myl, token):
    found = False
    for number in myl:
        if number == token:
            found = True
            break
    return found




def linear_search(mylist, token):
    return token in mylist





def binary_search(myl, token):
    found = False

    left  = 0
    right = len(myl)-1

    while left <= right and not found:
        mid = (right+left)//2
        if myl[mid] == token:
            found = True

        if myl[mid] > token:
            right = mid - 1
        else:
            left  = mid + 1       
    return found

def bsearch(mylist, token):
    if not mylist:
        return False
    mid = len(mylist)//2    
    if mylist[mid] is token:
        return True
    elif mylist[mid] > token:
        return bsearch(mylist[:mid], token)
    else:
        return bsearch(mylist[mid+1:], token)

L = [1,2,3,4]
print(binary_search(L,367))
