def PalinArray(arr ,n):
    count=0
    for i in range(n):
        string=str(arr[i])
        reverse=string[::-1]
        if arr[i] == int(reverse):
            count=count+1
            if count == n:
                return 1
        else:
            return 0
