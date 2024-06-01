def find_subset_sum(numbers, target_sum):
    numbers.sort(reverse=True)
    result = []
    subset = []
    index = 0
    current_sum = 0

    def backtrack(current_sum, index):
        if current_sum == target_sum:
            result.append(subset[:])
        if current_sum >= target_sum:
            return

        for i in range(index, len(numbers)):
            if current_sum + numbers[i] <= target_sum:
                subset.append(numbers[i])
                backtrack(current_sum + numbers[i], i + 1)
                subset.pop()

    backtrack(current_sum, index)
    return result


if __name__ == '__main__':
    numbers = [3, 34, 5, 12, 3, 2, 2]
    target_sum = 9

    result = find_subset_sum(numbers, target_sum)

    if result:
        print(f"Возможные комбинации элементов множества {numbers}, дающие сумму {target_sum}:")
        for subset in result:
            print(subset)
    else:
        print(f"Нет возможных комбинаций элементов множества {numbers}, дающих сумму {target_sum}")