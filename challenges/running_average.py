def running_average():
    running_average.total = 0
    running_average.cnt = 0

    def inner(number):
        while True:
            running_average.total += number
            running_average.cnt += 1
            return running_average.total / running_average.cnt

    return inner


rAvg = running_average()
rAvg(10) # 10.0
rAvg(11) # 10.5
rAvg(12) # 11

rAvg2 = running_average()
rAvg2(1) # 1
rAvg2(3) # 2
