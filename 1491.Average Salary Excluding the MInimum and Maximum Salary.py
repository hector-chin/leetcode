def average(salary):
    """
    :type salary: List[int]
    :rtype: float
    """
    minimum = salary[0]
    maximum = 0
    total_salary = 0
    staff_nums = 0
    for i in range(0, len(salary)):
        total_salary += salary[i]
        staff_nums += 1
        if salary[i] < minimum:
            minimum = salary[i]
        elif salary[i] > maximum:
            maximum = salary[i]
    average_without_max_min = (total_salary - minimum - maximum)/(staff_nums - 2)
    print(f"minimum is {minimum}")
    print(f"maximum is {maximum}")
    print(f"target_average is {average_without_max_min}")




salary = [48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]
test = average(salary)
