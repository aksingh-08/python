numbers = int(input("Enter: "))
def analyze_numbers(numbers):
    if not numbers:
        return "Empty list"

    # even_count = sum(1 for n in numbers if n % 2 == 0)
    # odd_count = sum(1 for n in numbers if n % 2 != 0)
    # smallest = min(numbers)
    # largest = max(numbers)

    # is_increasing = all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))
    # is_decresing = all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))

    even_count = 0
    odd_count = 0
    smallest = numbers[0]
    largest = numbers[0]
    is_increasing = True
    is_decreasing = True
    seen = set()
    first_duplicate = None
    previous = numbers[0]

    for i, n in enumerate(numbers):
        if n % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        if n < smallest:
            smallest = n
        if n > largest:
            largest = n

        if n in seen and first_duplicate is None:
            first_duplicate = n
        seen.add(n)

        if i > 0:
            if n <= previous:
                is_increasing = False
            if n >= previous:
                is_decreasing = False
        previous = n
    
    return {
        "even" : even_count, 
        "odd": odd_count,
        "min": smallest,
        "max":largest,
        "increasing": is_increasing,
        "decreasing": is_decresing,
        "first_duplicate": first_duplicate
    }
