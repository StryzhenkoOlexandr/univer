def selection_sort_trace(arr):
    arr = arr.copy()
    n = len(arr)
    comparisons = 0
    assignments = 0
    
    print("Початковий масив:", arr)
    print("------------------------------")
    
    for i in range(n - 1):
        min_index = i
        assignments += 1
        
        print(f"Ітерація {i}:")
        print(f"Поточний елемент (для обміну): arr[{i}] = {arr[i]}")
        print(f"Шукаємо мінімальний елемент у частині: {arr[i:]}")
        
        # Пошук мінімального елемента
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
                assignments += 1
                print(f"Знайдено новий мінімум: arr[{j}] = {arr[j]}")
        
        # Виконуємо обмін
        comparisons += 1
        if min_index != i:
            print(f"Обмін arr[{i}] ({arr[i]}) і arr[{min_index}] ({arr[min_index]})")
            arr[i], arr[min_index] = arr[min_index], arr[i]
            assignments += 3
        else:
            print(f"Мінімальний елемент вже на своєму місці")
            print("Обміну не потрібно")
        
        print(f"Масив після ітерації {i}: {arr}")
        print("------------------------------")
    
    print("Сортування завершено.")
    print(f"Фінальний відсортований масив: {arr}")
    print(f"Загальна кількість порівнянь: {comparisons}")
    print(f"Загальна кількість присвоєнь: {assignments}")
    
    return arr, comparisons, assignments

# Використання для варіанту 19
arr = [80, 27, 37, 36, 91, 53, 86, 66, 98]
sorted_arr, comps, assigns = selection_sort_trace(arr)
