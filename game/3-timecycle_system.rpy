init -996 python:
    # The TimeCycle API
    class TimeCycle:
        year = month = day = hour = minute = second = 0
        time_id = "night"
        ticks = 0

        @staticmethod
        def tick():
            if TimeCycle.ticks % 20 == 0:
                print("Time ID: " + TimeCycle.time_id + ", Time: " + str(TimeCycle.hour) + ":"  + str(TimeCycle.minute) + ":" + str(TimeCycle.second))
                # Tick game time based on game time rate
                if persistent.game_time_rate > 0:
                    TimeCycle.second += 1 * persistent.game_time_rate
                    while TimeCycle.second > 59:
                        TimeCycle.second -= 60
                        TimeCycle.minute += 1
                        if TimeCycle.minute > 59:
                            TimeCycle.minute -= 60
                            TimeCycle.hour += 1
                            if TimeCycle.hour > 23:
                                TimeCycle.hour -= 24
                            
                            #Run the TimeCycle event for every hour where the time id will change
                            event = TimeCycleEvent()
                            if TimeCycle.time_id == "night":
                                if TimeCycle.hour == 5:
                                    Callback.call(event)
                            elif TimeCycle.time_id == "sunrise":
                                if TimeCycle.hour == 7:
                                    Callback.call(event)
                            elif TimeCycle.time_id == "day":
                                if TimeCycle.hour == 20:
                                    Callback.call(event)
                            elif TimeCycle.time_id == "sunset":
                                if TimeCycle.hour == 21:
                                    Callback.call(event)
                            TimeCycle.hour = min(event.hour, 23)
                            TimeCycle.minute = min(event.minute, 59)
                            TimeCycle.second = min(event.second, 59)
                            if TimeCycle.time_id != event.get_time_id():
                                TimeCycle.set_time_id()
                                timecycle_transition("timecycle")
                            TimeCycle.reset_date()

            TimeCycle.ticks += 1
        @staticmethod
        def set_time(hour = None, minute = None, second = None):
            TimeCycle.hour = min(hour, 23) if hour != None else TimeCycle.hour
            TimeCycle.minute = min(minute, 59) if minute != None else TimeCycle.minute
            TimeCycle.second = min(second, 59) if second != None else TimeCycle.second


        @staticmethod
        def set_time_id():
            if TimeCycle.hour > 20 or TimeCycle.hour < 5:
                TimeCycle.time_id = "night"
            elif TimeCycle.hour < 7:
                TimeCycle.time_id = "sunrise"
            elif TimeCycle.hour < 20:
                TimeCycle.time_id = "day"
            else:
                TimeCycle.time_id = "sunset"
        
        @staticmethod
        def reset_date():
            now = datetime.datetime.today()
            TimeCycle.year = now.year
            TimeCycle.month = now.month
            TimeCycle.day = now.day

        @staticmethod
        def reset_time():
            now = datetime.datetime.today()
            TimeCycle.hour = now.hour
            TimeCycle.minute = now.minute
            TimeCycle.second = now.second

        @staticmethod
        def reset():
            now = datetime.datetime.today()
            TimeCycle.year = now.year
            TimeCycle.month = now.month
            TimeCycle.day = now.day
            TimeCycle.hour = now.hour
            TimeCycle.minute = now.minute
            TimeCycle.second = now.second

    TimeCycle.reset()
    TimeCycle.set_time(hour=4)
    TimeCycle.set_time_id()