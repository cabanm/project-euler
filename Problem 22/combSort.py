#does not work for alphabetical sorting

def combsort(array):
    gap = len(array) #initialize gap size
    swaps = 1
    while ((gap != 1) and (swaps != 0)):
        #update the gap value for a next comb. Below is an example
        gap = int(gap // 1.247330950103979)
        if gap < 1:
          #minimum gap is 1
          gap = 1
        i = 0
        swaps = 0 #see bubblesort for an explanation
        
        #a single "comb" over the input list
        while (i + gap < len(array)): #see shellsort for similar idea
            if array[i] > array[i+gap]:
                array[i], array[i+gap] = array[i+gap], array[i]
                swaps = 1 # Flag a swap has occurred, so the
                          # list is not guaranteed sorted
            i = i + 1
    return array
