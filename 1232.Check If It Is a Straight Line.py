def checkStraightLine(coordinates) -> bool:
    if len(coordinates) <= 2:
        print('True')
        return True
    else:
        for i in range(0, len(coordinates)):
            if i < len(coordinates) - 2:

                delta_x_1 = coordinates[i+1][0] - coordinates[i][0]
                delta_y_1 = coordinates[i+1][1] - coordinates[i][1]

                delta_x_2 = coordinates[i+2][0] - coordinates[i+1][0]
                delta_y_2 = coordinates[i+2][1] - coordinates[i+1][1]
                if (delta_x_2 == delta_x_1) & (delta_x_2 == 0):
                    pass
                elif (delta_x_1 != 0) & (delta_x_2 != 0):
                    slope_1 = delta_y_1 / delta_x_1
                    slope_2 = delta_y_2 / delta_x_2
                    if slope_1 == slope_2:
                        pass
                    else:
                        print('False')
                        return False
                else:
                    print('False')
                    return False
            else:
                print('True')
                return True


# coordinates_test = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
# coordinates_test = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# coordinates_test = [[0,0],[0,1],[0,-1]]
coordinates_test = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]

test = checkStraightLine(coordinates_test)