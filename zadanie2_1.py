def merge_sort_iterative_with_trace(arr):
    n = len(arr)
    a = arr.copy()
    comparisons = 0
    assignments = 0
    
    print("ПОЧАТОК ІТЕРАТИВНОГО СОРТУВАННЯ ЗЛИТТЯМ")
    print(f"Початковий масив: {a}")
    print("-" * 50)
    
    size = 1
    step = 1
    while size < n:
        print(f"\nКРОК {step}: size = {size}")
        left = 0
        while left < n:
            mid = min(left + size, n)
            right = min(left + 2 * size, n)
            
            if mid < right:
                print(f"  Злиття: a[{left}:{mid}] = {a[left:mid]} та a[{mid}:{right}] = {a[mid:right]}")
                c, a_count = merge_iterative_with_trace(a, left, mid, right)
                comparisons += c
                assignments += a_count
                print(f"  Після злиття: {a}")
            
            left += 2 * size
        size *= 2
        step += 1
    
    print("\n" + "=" * 50)
    print("ЗАВЕРШЕННЯ СОРТУВАННЯ")
    print(f"Фінальний масив: {a}")
    print(f"Загальна кількість порівнянь: {comparisons}")
    print(f"Загальна кількість присвоювань: {assignments}")
    return a, comparisons, assignments

def merge_iterative_with_trace(a, left, mid, right):
    comparisons = 0
    assignments = 0
    
    left_arr = a[left:mid]
    right_arr = a[mid:right]
    assignments += (mid - left) + (right - mid)
    
    print(f"    Створено тимчасові масиви:")
    print(f"      left_arr = {left_arr}")
    print(f"      right_arr = {right_arr}")
    
    i = j = 0
    k = left
    merge_step = 1
    
    print("    Процес злиття:")
    while i < len(left_arr) and j < len(right_arr):
        comparisons += 1
        print(f"      Крок {merge_step}: порівнюємо {left_arr[i]} та {right_arr[j]}", end="")
        if left_arr[i] <= right_arr[j]:
            a[k] = left_arr[i]
            assignments += 1
            print(f" -> додаємо {left_arr[i]} з лівого масиву")
            i += 1
        else:
            a[k] = right_arr[j]
            assignments += 1
            print(f" -> додаємо {right_arr[j]} з правого масиву")
            j += 1
        k += 1
        merge_step += 1
    
    while i < len(left_arr):
        a[k] = left_arr[i]
        assignments += 1
        print(f"      Додаємо залишок з лівого: {left_arr[i]}")
        i += 1
        k += 1
    
    while j < len(right_arr):
        a[k] = right_arr[j]
        assignments += 1
        print(f"      Додаємо залишок з правого: {right_arr[j]}")
        j += 1
        k += 1
    
    return comparisons, assignments

if __name__ == "__main__":
    my_array = [80, 27, 37, 36, 91, 53, 86, 66, 98]
    
    print("=" * 70)
    print("ТРАСУВАННЯ ІТЕРАТИВНОГО СОРТУВАННЯ ЗЛИТТЯМ")
    print("Варіант 19 - послідовність:", my_array)
    print("=" * 70)
    
    sorted_iter, comp_iter, assign_iter = merge_sort_iterative_with_trace(my_array.copy())
    
    print("\n" + "РЕЗЮМЕ".center(70, "="))
    print(f"Оригінальний масив: {my_array}")
    print(f"Відсортований масив: {sorted_iter}")
    print(f"Кількість порівнянь: {comp_iter}")
    print(f"Кількість присвоювань: {assign_iter}")
