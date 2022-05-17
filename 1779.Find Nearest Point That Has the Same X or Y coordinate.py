def nearestValidPoint(x, y, points) -> int:
    dict_of_distance = {}
    list_of_distance = []
    a = 0
    for i in range(0, len(points)):
        distance = 0
        if points[i][0] == x:
            distance += abs(points[i][1] - y)
            dict_of_distance[i] = distance
            list_of_distance.append([i, distance])
            a += 1
        elif points[i][1] == y:
            distance += abs(points[i][0] - x)
            dict_of_distance[i] = distance
            list_of_distance.append([i, distance])
            a += 1
        else:
            pass

    try:
        key_list = list(dict_of_distance.keys())
        value_list = list(dict_of_distance.values())
        position = value_list.index(min(dict_of_distance.values()))
        return key_list[position]
    except:
        return -1






x = 3
y = 4
points = [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]

# x = 3
# y = 4
# points = [[3, 4]]

# x = 3
# y = 4
# points = [[2, 3]]

test = nearestValidPoint(x, y, points)
