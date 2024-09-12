t = int(input())
nums = list(map(int, input().split()))
res = sorted(nums)
print(res[0], res[-1])