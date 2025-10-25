def merge_sort_recursive(arr):
    comparisons = 0
    assignments = 0
    recursive_calls = 1
    
    if len(arr) <= 1:
        return arr, comparisons, assignments, recursive_calls
    
    mid = len(arr) // 2
    
    left_arr, c_left, a_left, r_left = merge_sort_recursive(arr[:mid])
    right_arr, c_right, a_right, r_right = merge_sort_recursive(arr[mid:])
    
    comparisons += c_left + c_right
    assignments += a_left + a_right
    recursive_calls += r_left + r_right
    
    merged_arr, c_merge, a_merge = merge_recursive(left_arr, right_arr)
    comparisons += c_merge
    assignments += a_merge
    
    return merged_arr, comparisons, assignments, recursive_calls

def merge_recursive(left, right):
    merged = []
    comparisons = 0
    assignments = 0
    i = j = 0
    
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            merged.append(left[i])
            assignments += 1
            i += 1
        else:
            merged.append(right[j])
            assignments += 1
            j += 1
    
    while i < len(left):
        merged.append(left[i])
        assignments += 1
        i += 1
    
    while j < len(right):
        merged.append(right[j])
        assignments += 1
        j += 1
    
    return merged, comparisons, assignments

if __name__ == "__main__":
    my_array = [80, 27, 37, 36, 91, 53, 86, 66, 98]
    print("РЕКУРСИВНЕ СОРТУВАННЯ ЗЛИТТЯМ")
    print("Послідовність:", my_array)
    sorted_rec, comp_rec, assign_rec, recur_calls = merge_sort_recursive(my_array)
    print("Відсортований масив:", sorted_rec)
    print("Порівнянь:", comp_rec)
    print("Присвоювань:", assign_rec)
    print("Рекурсивних викликів:", recur_calls)
