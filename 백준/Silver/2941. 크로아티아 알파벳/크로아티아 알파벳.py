n = input()
cr = ["c=", "c-", "dz=","d-","lj","nj","s=","z="]

for i in cr:
    n = n.replace(i, "a")

print(len(n))