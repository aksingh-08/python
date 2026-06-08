def analyze_numbers(numbers):
    if not numbers:
        return "Empty list"

    # even_count = sum(1 for n in numbers if n % 2 == 0)
    # odd_count = sum(1 for n in numbers if n % 2 != 0)
    # smallest = min(numbers)
    # largest = max(numbers)

    # is_increasing = all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))
    # is_decresing = all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))

    return {
        "even" : even_count, 
        "odd": odd_count,
        "min": smallest,
        "max":largest,
        "increasing": is_increasing,
        "decreasing": is_decresing
    }