def bubble_sort(sort_list):

    for j in range(len(sort_list)):

        for k in range(len(sort_list) - 1):

            if sort_list[k] > sort_list[k + 1]:
                sort_list[k], sort_list[k + 1] = sort_list[k + 1], sort_list[k]

    print(sort_list)


arr = []

size = int(input("Enter size of the list: \t"))

print("Enter the elements: \t")

for i in range(size):

    elements = int(input())
    arr.append(elements)

bubble_sort(arr)