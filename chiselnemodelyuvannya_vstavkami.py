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
        
        print(f"{i}. j={i+1}; key=A[{i+1}]={key}; i={i+1}-1={j};", end=" ")
        
        # Пересуваємо елементи, більші за key, вправо
        moved = False
        while j >= 0:
            comparisons += 1
            print(f"i>0 (True) A[{j+1}]>key ({arr[j]}>{key}", end=" ")
            if arr[j] > key:
                print("- True) → ", end="")
                arr[j + 1] = arr[j]
                assignments += 1
                print(f"A[{j+2}]=A[{j+1}]={arr[j]};", end=" ")
                j -= 1
                assignments += 1
                moved = True
            else:
                print("- False)", end="")
                break
            if j >= 0:
                print()
                print(" " * (len(str(i)) + 2), end="")
        
        if not moved and j >= 0:
            print(f"i>0 (True) A[{j+1}]>key ({arr[j]}>{key} - False)")
        
        # Вставляємо key на правильну позицію
        arr[j + 1] = key
        assignments += 1
        print(f"A[{j+2}]=key={key}" if j >= 0 or moved else f"i>0 (False)\nA[{j+2}]=key={key}")
        print(f"А={arr}")
    
    print("(end for j)")
    print("Кінцевий результат:", arr)
    print(f"Загальна кількість порівнянь: {comparisons}")
    print(f"Загальна кількість присвоєнь: {assignments}")
    
    return arr, comparisons, assignments

arr = [80, 27, 37, 36, 91, 53, 86, 66, 98]
sorted_arr, comps, assigns = insertion_sort_with_counters(arr)
