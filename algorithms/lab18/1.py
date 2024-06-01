def first_fit_decreasing(item_sizes, bin_capacity):
    item_sizes.sort(reverse=True)
    print(item_sizes)
    boxes = []

    for item in item_sizes:
        for box in boxes:
            if sum(box) + item <= bin_capacity:
                box.append(item)
                break
        else:
            boxes.append([item])

    return boxes


if __name__ == '__main__':
    item_sizes = [20, 30, 40, 50, 7, 5, 5, 43]
    box_capacity = 50

    result = first_fit_decreasing(item_sizes, box_capacity)
    for i, box in enumerate(result, start=1):
        print(f"Ящик {i}: {box}")
