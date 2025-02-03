
arr1 = [1, 2, 3, 5, 8]
arr2 = [1, 5, 7, 3, 5]
arr3 = []


def compare_array(arr1, arr2):
   for i in range (len(arr1)):
        for j in range (len(arr2)):
            if arr1[i] == arr2[j]:
              arr3.append(arr1[i])
        


compare_array(arr1, arr2)
print(arr3)


