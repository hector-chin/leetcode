def floodFill(image, sr, sc, color):
    if image[sr][sc] == color:
        return image

    pixel, og_color = [(sr, sc)], image[sr][sc]
    m, n = len(image), len(image[0])

    while pixel:
        row, col = pixel.pop()
        if row in range(m) and col in range(n) and image[row][col] == og_color:
            image[row][col] = color
            pixel.append((row + 1, col))
            pixel.append((row - 1, col))
            pixel.append((row, col + 1))
            pixel.append((row, col - 1))
    return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
a = floodFill(image, 1, 1, 2)
print(a)
