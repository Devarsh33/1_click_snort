def binary_search(li, value):
    low, high = 0, len(li) - 1
    while low <= high:
        middle = (low + high) // 2
        if li[middle] < value:
            low = middle + 1
        elif value < li[middle]:
            high = middle - 1
        else:
            return middle
    return -1


input_list = [0, 1, 2, 3, 4, 5, 6]
user_input = 6
print(binary_search(input_list, user_input))
