def mergeSort(array):
    
    if len(array)>1:
        mid = len(array)//2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        index_new_array=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                array[index_new_array]=lefthalf[i]
                i=i+1
            else:
                array[index_new_array]=righthalf[j]
                j=j+1
            index_new_array=index_new_array+1

        while i<len(lefthalf):
            array[index_new_array]=lefthalf[i]
            i=i+1
            index_new_array=index_new_array+1

        while j<len(righthalf):
            array[index_new_array]=righthalf[j]
            j=j+1
            index_new_array=index_new_array+1
    
    return array
     
