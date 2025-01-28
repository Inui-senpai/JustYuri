init -996 python:
    # The TimeCycle API
    class TimeCycle:
        year = month = day = hour = minute = second = 0
        ticks = 0

        @staticmethod
        def tick():
            if TimeCycle.ticks % 20 == 0:
                TimeCycle.second += 1 * persistent.game_time_rate
                while TimeCycle.second > 59:
                    TimeCycle.second -= 60
                    TimeCycle.minute += 1
                    if TimeCycle.minute > 59:
                        TimeCycle.minute -= 60
                        TimeCycle.hour += 1
                        if TimeCycle.hour > 23:
                            TimeCycle.hour -= 24

                print(TimeCycle.get_time_id() + ", " + str(TimeCycle.hour) + ":" + str(TimeCycle.minute) + ":" + str(TimeCycle.second))
            TimeCycle.ticks += 1

        @staticmethod
        def get_time_id():
            if TimeCycle.hour > 20 or TimeCycle.hour < 5:
                return "night"
            elif TimeCycle.hour < 7:
                return "sunrise"
            elif TimeCycle.hour < 20:
                return "day"
            else:
                return "sunset"

        @staticmethod
        def reset_time():
            now = datetime.datetime.today()
            TimeCycle.year = now.year
            TimeCycle.month = now.month
            TimeCycle.day = now.day
            TimeCycle.hour = now.hour
            TimeCycle.minute = now.minute
            TimeCycle.second = now.second


    TimeCycle.reset_time()