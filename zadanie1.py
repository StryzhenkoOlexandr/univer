def merge_sort_iterative(arr):
    n = len(arr)
    a = arr.copy()
    comparisons = 0
    assignments = 0
    
    size = 1
    while size < n:
        left = 0
        while left < n:
            mid = min(left + size, n)
            right = min(left + 2 * size, n)
            
            if mid < right:
                c, a_count = merge_iterative(a, left, mid, right)
                comparisons += c
                assignments += a_count
            
            left += 2 * size
        size *= 2
    
    return a, comparisons, assignments

def merge_iterative(a, left, mid, right):
    comparisons = 0
    assignments = 0
    
    left_arr = a[left:mid]
    right_arr = a[mid:right]
    assignments += (mid - left) + (right - mid)
    
    i = j = 0
    k = left
    
    while i < len(left_arr) and j < len(right_arr):
        comparisons += 1
        if left_arr[i] <= right_arr[j]:
            a[k] = left_arr[i]
            assignments += 1
            i += 1
        else:
            a[k] = right_arr[j]
            assignments += 1
            j += 1
        k += 1
    
    while i < len(left_arr):
        a[k] = left_arr[i]
        assignments += 1
        i += 1
        k += 1
    
    while j < len(right_arr):
        a[k] = right_arr[j]
        assignments += 1
        j += 1
        k += 1
    
    return comparisons, assignments

if __name__ == "__main__":
    my_array = [80, 27, 37, 36, 91, 53, 86, 66, 98]
    print("ІТЕРАТИВНЕ СОРТУВАННЯ ЗЛИТТЯМ")
    print("Послідовність:", my_array)
    sorted_iter, comp_iter, assign_iter = merge_sort_iterative(my_array)
    print("Відсортований масив:", sorted_iter)
    print("Порівнянь:", comp_iter)
    print("Присвоювань:", assign_iter)
