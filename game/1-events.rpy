init -998 python:
    class StartEvent(Event):
        id = "_start"

    class LabelEvent(Event):
        id = "_label"
        label_name = None
        called = False
        def __init__(self, label_name, called):
            self.label_name = label_name
            self.called = called

    class QuitEvent(Event):
        id = "_quit"

    class SafeQuitEvent(Event):
        id = "_safe_quit"

    class ExitEvent(Event):
        id = "_exit"

    class CrashEvent(Event):
        id = "_crash"

    class TickEvent(Event):
        id = "_tick"

    # Fires anytime Yuri's karma changes
    class KarmaEvent(Event):
        id = "karma"
        karma = 0
        original_karma = 0

        def __init__(self, karma):
            self.karma = karma
            self.original_karma = karma

    # Fires anytime Yuri's sanity changes
    class SanityEvent(Event):
        id = "sanity"
        sanity = 0
        original_sanity = 0

        def __init__(self, sanity):
            self.sanity = sanity
            self.original_sanity = sanity

    # Fires anytime the TimeCycle system wants to change the time id
    class TimeCycleEvent(Event):
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
        DetectionAPI.tick()
        TimeCycle.tick()


    Callback.register(StartEvent.id)
    Callback.register(LabelEvent.id)
    Callback.register(QuitEvent.id)
    Callback.register(SafeQuitEvent.id)
    Callback.register(ExitEvent.id)
    Callback.register(CrashEvent.id)
    Callback.register(TickEvent.id)

    Callback.register(KarmaEvent.id)
    Callback.register(SanityEvent.id)
    Callback.register(TimeCycleEvent.id)
    Callback.register(TickEvent.id, callback_jy_tick)