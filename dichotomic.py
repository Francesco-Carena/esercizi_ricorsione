def dichotomic(arr, val):
    if len(arr)==1:
        if arr[0]==val:
            return True
        else:
            return False
    else:
        mid=len(arr)//2
        return (dichotomic(arr[:mid],val)
            or dichotomic(arr[mid:],val))



if __name__ == '__main__':
    arr=[1,2,3,4,5,6]
    obiettivo=5
    print(dichotomic(arr,obiettivo))
    print(dichotomic(arr,11))