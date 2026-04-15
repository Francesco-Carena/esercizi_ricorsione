import random

def quicksort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr[0]
        """arr_smaller=[]
        arr_pivot=[]
        arr_larger=[]
        for i in arr:
            if i>pivot:
                arr_larger.append(i)
            elif i<pivot:
                arr_smaller.append(i)
            else:
                arr_pivot.append(i)
        return quicksort(arr_smaller) + arr_pivot + quicksort(arr_larger)"""

        arr_smaller=[n for n in arr if n<pivot]
        arr_pivot=[n for n in arr if n==pivot]
        arr_larger=[n for n in arr if n>pivot]
        return quicksort(arr_smaller) + arr_pivot + quicksort(arr_larger)


if __name__=='__main__':
    arr = [1,2,3,4,5,6,7,8,9,10]
    random.shuffle(arr)
    print(f"prima: {arr}")
    print(f"dropo: {quicksort(arr)}")
