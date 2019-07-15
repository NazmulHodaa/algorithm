def selectionSort(alist):
    for i in range(len(alist)):

        minPosition = i

        for j in range(i + 1, len(alist)):
            if alist[minPosition] > alist[j]:
                minPosition = j

        alist[i],alist[minPosition] = alist[minPosition],alist[i]

    print(alist)


arr = []

size = int(input("Enter size of the list: \t"))

print("Enter the elements: \t")

for i in range(size):

    elements = int(input())
    arr.append(elements)

selectionSort(arr)