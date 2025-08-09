
def quick_sort(items):
    if len(items) <= 1:
        return items
    key = items[0]
    left = [x for x in items[1:] if x < key]
    right = [x for x in items[1:] if x >= key]
    return quick_sort(left) + [key] + quick_sort(right)

a = [3, 2, 3, 5, 7, 9, 20, 9, 7, 31]
print(quick_sort(a))