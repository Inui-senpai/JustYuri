init -998 python:
    # Fires anytime Yuri's karma changes
    class KarmaEvent(EventObject):
        id = "karma"
        karma = 0
        original_karma = 0

        def __init__(self, karma):
            self.karma = karma
            self.original_karma = karma

    # Fires anytime Yuri's sanity changes
    class SanityEvent(EventObject):
        id = "sanity"
        sanity = 0
        original_sanity = 0

        def __init__(self, sanity):
            self.sanity = sanity
            self.original_sanity = sanity

    # Fires anytime the TimeCycle system wants to change the time id
    class TimeCycleEvent(EventObject):
        id = "timecycle"
        hour = minute = second = 0

        def __init__(self):
            self.hour = int(TimeCycle.hour)
            self.minute = int(TimeCycle.minute)
            self.second = int(TimeCycle.second)

        def get_time_id(self):
            if self.hour > 20 or self.hour < 5:
                return "night"
            elif self.hour < 7:
                return "sunrise"
            elif self.hour < 20:
                return "day"
            else:
                return "sunset"

    def callback_jy_tick(event):
        TimeCycle.tick()

    Callback.register(KarmaEvent.id)
    Callback.register(SanityEvent.id)
    Callback.register(TimeCycleEvent.id)
    Callback.register(TickEvent.id, callback_jy_tick)