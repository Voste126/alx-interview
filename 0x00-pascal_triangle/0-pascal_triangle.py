def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of n."""
    if n <= 0:
        return []  # Return an empty list if n is less than or equal to 0

    triangle = []  # Initialize the triangle as an empty list
    for i in range(n):
        row = [1] * (i + 1)  # Start with a row filled with 1s
        for j in range(1, i):  # Calculate the inner values of the row
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)  # Append the row to the triangle
    return triangle  # Return the completed triangle
