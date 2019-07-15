arr = []

size = int(input("Enter size of the list: \t"))

print("Enter the elements: \t")

for i in range(size):

    elements = int(input())
    arr.append(elements)


for j in range(len(arr)):
    while j>0:
        if arr[j-1] > arr[j]:
            arr[j-1],arr[j] = arr[j],arr[j-1]
        else:
            break
        j = j-1
print (arr)