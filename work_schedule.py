import random
from collections import deque

def work_schedule():
    weekday_employee_list = ["근로자1", "근로자2", "근로자3", "근로자4", "근로자5"]
    weekend_employee_list = ["근로자1", "근로자2", "근로자3", "근로자4", "근로자5", "근로자6"]
    weekday_list = ["월", "화", "수", "목", "금"]
    weekend_list = ["토", "일"]

    table = []
    random.shuffle(weekday_employee_list)
    random.shuffle(weekend_employee_list)
    for i in range(0,4):
        table.append(str(i+1) + "주차")
        week = []
        for e, j in enumerate(weekday_list, start=0):
            week.append(j)
            week.append(weekday_employee_list[e])
        weekday_employee_deque = deque(weekday_employee_list)
        weekday_employee_deque.rotate(-1)
        weekday_employee_list = list(weekday_employee_deque)
        for e, k in enumerate(weekend_list, start=0):
            week.append(k)
            week.append(weekend_employee_list[e])
        weekend_employee_deque = deque(weekend_employee_list)
        weekend_employee_deque.rotate(-1)
        weekend_employee_list = list(weekend_employee_deque)
        if week[9] == week[11]:
            week[11], week[13] = week[13], week[11]
        elif week[1] == week[13]:
            week[1], week[3] = week[3], week[1]
        else:
            week
        table.append(week)
    return print(table)

work_schedule()