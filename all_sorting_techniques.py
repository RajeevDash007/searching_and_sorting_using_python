def bubble_sort(sort_list):
    changes=0
    for j in range(len(sort_list)):
        for k in range(len(sort_list) - 1):
            if sort_list[k] > sort_list[k + 1]:
                sort_list[k], sort_list[k + 1] = sort_list[k + 1], sort_list[k]
                changes += 1
    print(f"bubble sort = {sort_list}")


def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])
    print(f"Selection Sort = {array}")

def mergeSort(nlist):
    
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    
    print(f"Merge Sort = {nlist}")


def partition(array,low,high):    
        pivot = array[high]
        i = low - 1
        
        for j in range(low,high):
            if array[j] <= pivot:
                i = i + 1
                
                (array[i],array[j]) = (array[j],array[i])
                
        
        (array[i+1],array[high]) = (array[high],array[i+1])
        
        return i + 1
        


def quick_sort(array,low,high):
    if low < high:
        pii = partition(array,low,high)
        
        quick_sort(array,low,pii-1)
        quick_sort(array,pii+1,high)
    


def insertionSort(array,size):
 
    # Traverse through 1 to len(arr)
    for i in range(1,size):
 
        key = array[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
        array[j + 1] = key

    print(f"insertion sort =  {array}")
    

def counting_sort(data):
    # Creates 2D list of size max number in the array
    counts = [0 for i in range(max(data)+1)]
    
 
    # Finds the "counts" for each individual number
    for value in data:
        counts[value] += 1
        
 
    # Finds the cumulative sum counts
    for index in range(1, len(counts)):
        counts[index] = counts[index-1] + counts[index]
    
 
    # Sorting Phase
    arr = [0 for loop in range(len(data))]
    for value in data:
        index = counts[value] - 1
        arr[index] = value
        counts[value] -= 1
 
    print(f"counting sort = {arr}")
    
    
#shellSort
def shellSort(arr, n):
  
    gap=n//2
     
     
    while gap>0:
        j=gap
        # Check the array in from left to right
        # Till the last possible index of j
        while j<n:
            i=j-gap # This will keep help in maintain gap value
             
            while i>=0:
                # If value on right side is already greater than left side value
                # We don't do swap else we swap
                if arr[i+gap]>arr[i]:
 
                    break
                else:
                    arr[i+gap],arr[i]=arr[i],arr[i+gap]
 
                i=i-gap # To check left side also
                            # If the element present is greater than current element
            j+=1
        gap=gap//2
    print(f"shell sort = {arr}")


#gnome sort
def gnomeSort( arr, n):
    index = 0
    while index < n:
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index - 1]:
            index = index + 1
        else:
            arr[index], arr[index-1] = arr[index-1], arr[index]
            index = index - 1
  
    print(f"Gnome Sort = {arr}")

print("*** Welcome To the World of Sorting ***")
print("*** Good afternoon Folks ***")
lst = []
size = int(input("Enter size of the list: "))
 
for i in range(size):
    elements = int(input(f"Enter {i+1} element: "))
    lst.append(elements)
 
gnomeSort(lst,size)
shellSort(lst, size)
counting_sort(lst)
insertionSort(lst, size)
quick_sort(lst, 0, size-1)
print(f"quick sort = {lst}")
mergeSort(lst)
selectionSort(lst, size)
bubble_sort(lst)


