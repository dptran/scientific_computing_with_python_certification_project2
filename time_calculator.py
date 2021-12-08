def add_time(start, duration, *day):
    start_array = start.split(" ")
    time_array = start_array[0].split(":")
    duration_array = duration.split(":")
    start_hour = int(time_array[0])
    start_min = int(time_array[1])
    duration_hour = int(duration_array[0])
    minutes_passed = int(duration_array[1])
    days_passed = round(duration_hour / 24)
    hours_passed = duration_hour % 24
    day_of_week = {
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
        "Sunday": 7
    }
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    m_o_a = 0
    # count of how many times the day switches from am to pm to am etc. odd numbers mean that it will be different from what it started with while for even, it will remain the same.
    
    new_time = ""
    new_hour = 0
    new_min = 0
    am_or_pm = start_array[1]
    # if am_or_pm == "PM":
    #     new_hour += 12
    # else:
    #     pass
    
    if (start_min + minutes_passed) >= 60:
        m_o_a += 1
        
    print(m_o_a)
    
    if (start_min + minutes_passed) >= 60:
        new_hour += 1
        new_min += ((start_min + minutes_passed) % 60)
    else:
        new_min += (start_min + minutes_passed)
        
    if (start_hour + hours_passed) % 12 == 0:
        new_hour += 12
    else:
        new_hour += ((start_hour + hours_passed) % 12)
    
    if am_or_pm == "PM" and 24 > (start_hour + duration_hour) >= 12:
        am_or_pm = "AM"
    
    m_o_a += round(duration_hour / 12)
    print(start_hour)
    print(new_hour)
    if m_o_a % 2 != 0:
        if am_or_pm == "AM":
            am_or_pm = "PM"
        elif am_or_pm == "PM":
            am_or_pm = "AM"
    else:
        pass
    
    print(m_o_a)
    days_passed = round((duration_hour + new_hour) / 24)
    hours_passed = (duration_hour + new_hour) % 24

    
    if new_hour % 12 == 0:
        new_hour = 12
    else:
        new_hour = new_hour % 12

    
    
    if len(str(new_min)) == 1:
        new_time += str(new_hour) + ":" + "0" + str(new_min) + " " + am_or_pm
    else:
        new_time += str(new_hour) + ":" + str(new_min) + " " + am_or_pm
    
    if len(day) == 0:
        pass
    elif (days_passed % 7 == 0):
        new_time += ", " + day[0].title()
    else:
        x = (day_of_week[day[0].title()] + days_passed) % 7
        new_day = week[x - 1]
        new_time += ", " + new_day
    
    if (start_array[1] == "PM" and am_or_pm == "AM" and days_passed == 0) or days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"
    
    return new_time