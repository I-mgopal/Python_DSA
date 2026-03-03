#1. Store frequency in pyhton
# Method - 1 (Uisng dictionary)
input = [1,2,3,4,5,5,2,3,6,7]
Hash = {}/dict()

for i in input:
    if i in Hash:
        Hash[i]+=1
    else:
        Hash[i] = 1

print(Hash)
T.C - O(n)
S.C - O(n)

#Method - 2 
for i in input:
    Hash[i] = Hash.get(i,0)+1
T.C - O(n)
S.C - O(n)
print(Hash)

#2 check how many occerence of the second arrays element in the first array
m = [5,3,2,2,1,5,5,7,5,10]
n = [10,11,1,9,5,6,7,2]
freq = dict()
list1 = []

for i in m:
    freq[i] = freq.get(i,0)+1

for i in n:
    if i in freq:
        list1.append(freq[i])
    else:
        list1.append(0)

print(list1)
T.C - O(n)
S.C - O(n)






