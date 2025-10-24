def insertion_sort_with_counters(arr):
    arr = arr.copy()
    n = len(arr)
    comparisons = 0
    assignments = 0
    
    print("Трасування сортування вставками:")
    print("Початковий масив:", arr)
    print("------------------------------")
    
    for i in range(1, n):
        key = arr[i]
        assignments += 1
        j = i - 1
        assignments += 1
        
        print(f"Ітерація {i}:")
        print(f"Елемент для вставки (key): {key}")
        print(f"Відсортована частина: {arr[:i]}")
        
        # Пересуваємо елементи, більші за key, вправо
        moved_elements = []
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                assignments += 1
                moved_elements.append(arr[j])
                j -= 1
                assignments += 1
            else:
                break
        
        # Вставляємо key на правильну позицію
        arr[j + 1] = key
        assignments += 1
        
        if moved_elements:
            print(f"Зсунуто елементи: {moved_elements}")
        print(f"Вставка {key} на позицію {j + 1}")
        print(f"Масив після ітерації {i}: {arr}")
        print("------------------------------")
    
    print("Сортування завершено.")
    print(f"Фінальний відсортований масив: {arr}")
    print(f"Загальна кількість порівнянь: {comparisons}")
    print(f"Загальна кількість присвоєнь: {assignments}")
    
    return arr, comparisons, assignments

arr = [80, 27, 37, 36, 91, 53, 86, 66, 98]
sorted_arr, comps, assigns = insertion_sort_with_counters(arr)
