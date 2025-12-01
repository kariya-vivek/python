def linear_search(values, search_for):
    search_at = 0
    search_res = False
    while search_at < len(values) and not search_res:
        if values[search_at] == search_for:
            search_res = True
        else:
            search_at += 1
    return search_res

list1 = [64, 34, 25, 12, 22, 11, 90]
print(linear_search(list1, 12))
