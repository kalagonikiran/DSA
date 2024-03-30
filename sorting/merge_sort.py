def mergeSort(data):
    if len(data)>1:
        mid=len(data)//2
        right_list=data[mid:]
        left_list=data[:mid]
        mergeSort(left_list)
        '''divides the left_list of main list to right and left lists,
           when base case reaches mergeSort(left_list) pauses and moves to mergeSort(right_list)
        '''
        mergeSort(right_list)
        '''initially it divides the left_list of main list into sub right_lists ,
           after base case is reached  the merging part below gets executed and returns to mergeSort(left_list) and
           after complete execution of mergeSort(left_list) execution moves to mergeSort(right_list) to perform same tasks
           on right side of main list. 
        '''
        i=0
        j=0
        k=0
      
        while i<len(right_list) and j<len(left_list):
            if left_list[j]<right_list[i]:
                data[k]=left_list[j]
                j+=1
                k+=1
                '''right_list index does not move'''
            else:
                data[k]=right_list[i]
                i+=1
                k+=1
                '''Left_list index does not move'''
              

        while i<len(right_list):
            data[k]=right_list[i]
            i+=1
            k+=1
            '''left out values in right_list are added to main list'''
        while j<len(left_list):
            data[k]=left_list[j]
            j+=1
            k+=1
           '''left out values in left_list are added to main list'''

data=[5,4,3,2,1]
mergeSort(data)
print(data)
      
