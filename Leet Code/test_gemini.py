def generate_pascals_triangle(num_rows):
    """
    Generates Pascal's triangle up to a specified number of rows.

    Args:
        num_rows: The number of rows to generate.

    Returns:
        A list of lists, where each inner list represents a row
        in Pascal's triangle. Returns an empty list if num_rows is non-positive.
    """
    if num_rows <= 0:
        return []

    # The first row is always [1]
    triangle = [[1]]

    # Generate subsequent rows
    for i in range(1, num_rows):
        prev_row = triangle[-1]
        new_row = [1]  # Start each new row with 1

        # Calculate the numbers between the 1s
        for j in range(len(prev_row) - 1):
            # Each new number is the sum of the two numbers above it
            new_row.append(prev_row[j] + prev_row[j + 1])

        new_row.append(1)  # End each new row with 1
        triangle.append(new_row)

    return triangle

def print_pascals_triangle(triangle):
    """
    Prints a generated Pascal's triangle with proper spacing to make it look like a pyramid.

    Args:
        triangle: A list of lists representing Pascal's triangle.
    """
    if not triangle:
        print("The triangle is empty.")
        return

    # Calculate the width needed for the last, longest row
    # This helps in centering the other rows
    width = len(" ".join(map(str, triangle[-1])))

    for row in triangle:
        row_str = " ".join(map(str, row))
        print(row_str.center(width))

# --- Main Execution ---
if __name__ == "__main__":
    try:
        rows = int(input("Enter the number of rows for Pascal's triangle: "))
        if rows < 0:
            print("Please enter a non-negative number.")
        else:
            pascals_triangle = generate_pascals_triangle(rows)
            print("\nPascal's Triangle:")
            print_pascals_triangle(pascals_triangle)
    except ValueError:
        print("Invalid input. Please enter an integer.")

