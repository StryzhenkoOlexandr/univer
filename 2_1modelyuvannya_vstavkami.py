def insertion_sort_numerical_modeling(arr):
    arr = arr.copy()
    n = len(arr)
    comparisons = 0
    assignments = 0
    
    print(f"Вихідні дані: А = {arr} A.length = {n}")
    print("(for j)")
    print()
    
    for j in range(1, n):
        key = arr[j]
        assignments += 1
        i = j - 1
        assignments += 1
        
        print(f"{j}. j={j+1}; key=A[{j+1}]={key}; i={j+1}-1={i};", end=" ")
        
        # Пересуваємо елементи, більші за key, вправо
        moved = False
        while i >= 0:
            comparisons += 1
            print(f"i>0 (True) A[{i+1}]>key ({arr[i]}>{key}", end=" ")
            if arr[i] > key:
                print("- True) → ", end="")
                arr[i + 1] = arr[i]
                assignments += 1
                print(f"A[{i+2}]=A[{i+1}]={arr[i]};", end=" ")
                i -= 1
                assignments += 1
                moved = True
            else:
                print("- False)", end="")
                break
        
        # Вставляємо key на правильну позицію
        arr[i + 1] = key
        assignments += 1
        
        if moved:
            print(f"A[{i+2}]=key={key}")
        else:
            if i >= 0:
                print(f"A[{i+2}]=key={key}")
            else:
                print(f"i>0 (False)")
                print(f"A[{i+2}]=key={key}")
        
        print(f"А={arr}")
        print()
    
    print("(end for j)")
    print(f"Кінцевий результат: {arr}")
    print(f"Загальна кількість порівнянь: {comparisons}")
    print(f"Загальна кількість присвоєнь: {assignments}")
    
    return arr, comparisons, assignments

arr = [80, 27, 37, 36, 91, 53, 86, 66, 98]
sorted_arr, comps, assigns = insertion_sort_numerical_modeling(arr)
