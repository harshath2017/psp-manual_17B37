def selectsort(L): 
    for slot in range(len(L)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, slot + 1):
            if L[location] > L[positionOfMax]:
                positionOfMax = location

        temp             = L[slot]
        L[slot]          = L[positionOfMax]
        L[positionOfMax] = temp
    return L






def insertsort(L):

  for index in range(1, len(L)):
    key = L[index]
    j = index - 1

    while j >= 0 and (L[j] > key):
      L[j + 1] = L[j]
      j = j - 1
    L[j + 1] = key
  return L
L = [12,32,45,23,37,67]
print(selectsort(L))



