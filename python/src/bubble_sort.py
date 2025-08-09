def bubble_sort(items):
    items_new = items.copy()
    for i in range(len(items_new)):
        swapped = False
        for j in range(len(items_new) - i - 1):
            if items_new[j] > items_new[j+1]:
                items_new[j], items_new[j+1] = items_new[j+1], items_new[j]
                swapped = True

        if not swapped:
            break
    return items_new




a = [3, 2, 3, 5, 7, 9, 20, 9, 7, 31]
print(bubble_sort(a))