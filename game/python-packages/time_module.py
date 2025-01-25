import datetime

def time_shift(time_dict, shift):
    if "year" in shift.keys():
        print("Sensing Year Shift. Adjusting...")
        if not "day" in shift.keys():
            shift["day"] = 0
        shift['day'] = shift['day'] + shift['year'] * 365
    print("Performing time shift")
    if shift == None:
        print("Specify shift")
        return
    time_dict_temp = {}
    shift_string = "datetime.timedelta("
    shift_delta = {}

    for time_piece in ["year", "month", "day", "hour", "minute"]:
        if not(time_piece in time_dict):
            time_dict_temp[time_piece] = int(eval("datetime.datetime.now()." + time_piece))
        else:
            time_dict_temp[time_piece] = int(time_dict[time_piece])
    print(time_dict)
    print(time_dict_temp)

    time_datetime = datetime.datetime(year=time_dict_temp["year"],
        month=time_dict_temp["month"],
        day=time_dict_temp["day"],
        hour=time_dict_temp["hour"],
        minute=time_dict_temp["minute"])
    print("time_datetime: ")
    print(time_datetime)
    for time_piece in ["week", "day", "hour", "minute"]:
        if time_piece in shift:
            shift_string = shift_string + time_piece + "s=" + str(shift[time_piece]) + ","
    print(shift_string)
    exec("shift_delta =" + shift_string[:-1] + ')')
    print(shift_delta)
    new_time = time_datetime + shift_delta
    print("new_time: ")
    print(new_time)

    new_time_dict = {}
    for time_piece in ["year", "month", "day", "hour", "minute"]:
        if eval("new_time." + time_piece + " != time_datetime." + time_piece) or time_piece in time_dict:
            new_time_dict[time_piece] = eval("new_time." + time_piece)
    return new_time_dict

def time_interval_check(start_time, end_time):
    first = time_interval_check_standard(start_time, end_time)
    second = time_interval_check_standard(time_shift(start_time, {'year':-1}), time_shift(end_time, {'year':-1}))
    if first or second:
        return True
    else:
        return False

def time_interval_check_standard(start_time,#= {"year": 2000, "month": 1, "day": 1, "hour":1, "minute":32},
        end_time):# = {"year": 2000, "month": 1, "day": 1, "hour":1, "minute":33}):
    print("times")
    print(start_time)
    print(end_time)
    current_time = datetime.datetime.now()
    start_time_temp = {}#start_time
    end_time_temp = {}#end_time
    # Converts 
    for time_piece in ["year", "month", "day", "hour", "minute"]:
        if not(time_piece in start_time):
            start_time_temp[time_piece] = int(eval("current_time." + time_piece))
        else:
            start_time_temp[time_piece] = int(start_time[time_piece])
        if not(time_piece in end_time):
            end_time_temp[time_piece] = int(eval("current_time." + time_piece))
        else:
            end_time_temp[time_piece] = int(end_time[time_piece])
    print(start_time_temp)
    print(end_time_temp)
    # handles the error of if the start time is labelled as happening later than the end time
    # usually only needing to error handle if the year not specified leads to Dec + 2 months = February
    for time_piece in ["year", "month", "day", "hour", "minute"]:
        start_time_piece = start_time_temp[time_piece]
        end_time_piece = end_time_temp[time_piece]
        if start_time_piece < end_time_piece:
            break
        elif start_time_piece > end_time_piece:
            while start_time_piece > end_time_piece:
                start_time_temp[time_piece] -= 1
            #make start_time_piece and end_time_piece equal, usually sets the years to be equal
    #if start_time_temp >= end_time_temp:
    #    for time_piece in ["year", "month", "day", "hour", "minute"]:
    #        if time_piece in start_time:
    #            start_time_temp[time_piece] -= 1
    #            break
    print(start_time_temp)
    print(end_time_temp)
    #
    start_datetime = datetime.datetime(year=start_time_temp["year"],
        month=start_time_temp["month"],
        day=start_time_temp["day"],
        hour=start_time_temp["hour"],
        minute=start_time_temp["minute"])
    end_datetime = datetime.datetime(year=end_time_temp["year"],
        month=end_time_temp["month"],
        day=end_time_temp["day"],
        hour=end_time_temp["hour"],
        minute=end_time_temp["minute"])
    print("Start Datetime")
    print(start_datetime)
    print("End Datetime")
    print(end_datetime)
    print("Current Datetime")
    print(current_time)
    if (start_datetime <= current_time) and (current_time <= end_datetime):
        return True
    else:
        return False

#example of use
    #if time_interval_check({"hour": 13}, {"hour": 20}):
    #    print("It is currently afternoon")
    #else:
    #    print("It ain't afternoon")
#print(time_shift({"minute":10}, {"minute":-20, "week":-1}))
#print(time_interval_check(
#    time_shift({"month": 5}, {"week": -5}), 
#    {"month": 5}))


