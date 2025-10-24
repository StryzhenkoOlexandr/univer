def selection_sort_numerical_modeling(arr):
    arr = arr.copy()
    n = len(arr)
    comparisons = 0
    assignments = 0
    
    print(f"Вихідні дані: А = {arr} n = {n}")
    print("(for i)")
    print()
    
    for i in range(n - 1):
        min_index = i
        assignments += 1
        
        print(f"{i+1}. i={i}; min={min_index}; j={i}+1={i+1}; A[{i+1}]<A[{min_index}] ({arr[i+1]}<{arr[min_index]})", end=" ")
        
        if arr[i+1] < arr[min_index]:
            min_index = i+1
            assignments += 1
            print(f"min={min_index}")
        else:
            print(f"min={min_index}")
        
        for j in range(i + 2, n):
            comparisons += 1
            print(f"j={j} A[{j}]<A[{min_index}] ({arr[j]}<{arr[min_index]})", end=" ")
            if arr[j] < arr[min_index]:
                min_index = j
                assignments += 1
                print(f"min={min_index}")
            else:
                print(f"min={min_index}")
        
        print("(end for j)")
        
        comparisons += 1
        if min_index != i:
            print(f"b=A[{i}] A[{i}]=A[{min_index}] A[{min_index}]=b A[{i}]={arr[min_index]} A[{min_index}]={arr[i]}")
            arr[i], arr[min_index] = arr[min_index], arr[i]
            assignments += 3
        else:
            print(f"min=i, обміну немає")
        
        print(f"А={arr}")
        print()
    
    print("(end for i)")
    print(f"Кінцевий результат: {arr}")
    print(f"Загальна кількість порівнянь: {comparisons}")
    print(f"Загальна кількість присвоєнь: {assignments}")
    
    return arr, comparisons, assignments

# Використання для варіанту 19
arr = [80, 27, 37, 36, 91, 53, 86, 66, 98]
sorted_arr, comps, assigns = selection_sort_numerical_modeling(arr)
