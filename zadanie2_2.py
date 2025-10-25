def merge_sort_recursive_with_trace(arr, depth=0):
    indent = "  " * depth
    comparisons = 0
    assignments = 0
    recursive_calls = 1
    
    print(f"{indent}Виклик merge_sort_recursive({arr})")
    
    if len(arr) <= 1:
        print(f"{indent}Базовий випадок - масив відсортований")
        return arr, comparisons, assignments, recursive_calls
    
    mid = len(arr) // 2
    print(f"{indent}Розділяємо на: left = {arr[:mid]}, right = {arr[mid:]}")
    
    left_arr, c_left, a_left, r_left = merge_sort_recursive_with_trace(arr[:mid], depth + 1)
    right_arr, c_right, a_right, r_right = merge_sort_recursive_with_trace(arr[mid:], depth + 1)
    
    comparisons += c_left + c_right
    assignments += a_left + a_right
    recursive_calls += r_left + r_right
    
    print(f"{indent}Зливаємо: {left_arr} та {right_arr}")
    merged_arr, c_merge, a_merge = merge_recursive_with_trace(left_arr, right_arr, depth)
    comparisons += c_merge
    assignments += a_merge
    
    print(f"{indent}Результат злиття: {merged_arr}")
    return merged_arr, comparisons, assignments, recursive_calls

def merge_recursive_with_trace(left, right, depth=0):
    indent = "  " * depth
    merged = []
    comparisons = 0
    assignments = 0
    i = j = 0
    merge_step = 1
    
    print(f"{indent}Початок злиття:")
    
    while i < len(left) and j < len(right):
        comparisons += 1
        print(f"{indent}  Крок {merge_step}: порівнюємо left[{i}]={left[i]} та right[{j}]={right[j]}", end="")
        if left[i] <= right[j]:
            merged.append(left[i])
            assignments += 1
            print(f" -> додаємо {left[i]}")
            i += 1
        else:
            merged.append(right[j])
            assignments += 1
            print(f" -> додаємо {right[j]}")
            j += 1
        merge_step += 1
    
    while i < len(left):
        merged.append(left[i])
        assignments += 1
        print(f"{indent}  Додаємо залишок з left: {left[i]}")
        i += 1
    
    while j < len(right):
        merged.append(right[j])
        assignments += 1
        print(f"{indent}  Додаємо залишок з right: {right[j]}")
        j += 1
    
    return merged, comparisons, assignments

if __name__ == "__main__":
    my_array = [80, 27, 37, 36, 91, 53, 86, 66, 98]
    
    print("=" * 70)
    print("ТРАСУВАННЯ РЕКУРСИВНОГО СОРТУВАННЯ ЗЛИТТЯМ")
    print("Варіант 19 - послідовність:", my_array)
    print("=" * 70)
    
    sorted_rec, comp_rec, assign_rec, recur_calls = merge_sort_recursive_with_trace(my_array.copy())
    
    print("\n" + "РЕЗЮМЕ".center(70, "="))
    print(f"Оригінальний масив: {my_array}")
    print(f"Відсортований масив: {sorted_rec}")
    print(f"Кількість порівнянь: {comp_rec}")
    print(f"Кількість присвоювань: {assign_rec}")
    print(f"Рекурсивних викликів: {recur_calls}")
