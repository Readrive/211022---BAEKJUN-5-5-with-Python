N = int(input("수를 입력하세요"))

arr = list(map(int, input().split()))

arrMax = max(arr)

for i in range(N):
    arr[i] = arr[i] / arrMax * 100
    avg = sum(arr) / N

print("%.2f" %avg)