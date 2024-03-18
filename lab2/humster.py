def calculate_max_hamsters(first, last, counted_hamsters, s, hamsters):
    midl = (first + last) // 2
    hamsters_count = midl + 1

    add_list = sorted([hamster[0] + hamster[1] * midl for hamster in hamsters])
    food_needs = sum(add_list[:midl + 1])
    counted_hamsters[midl] = food_needs
    if food_needs == s:
        return hamsters_count
    elif food_needs > s:
        last = midl - 1
        return calculate_max_hamsters(first, last, counted_hamsters, s, hamsters)
    else:
        next_ = midl + 1
        if counted_hamsters[next_] > s:
            return hamsters_count
        first = midl + 1
        return calculate_max_hamsters(first, last, counted_hamsters, s, hamsters)


def find_max_hamsters(s, hamsters):
    first = 0
    last = len(hamsters) - 1
    counted_hamsters = [0] * (len(hamsters) + 1)

    max_hamsters = calculate_max_hamsters(first, last, counted_hamsters, s, hamsters)

    return max_hamsters


array = [[1, 3], [4, 0], [2, 2]]

print(find_max_hamsters(10, array))
