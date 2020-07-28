if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    arr=list(set(arr))
    arr.sort(reverse=True)
    print(arr[1])
