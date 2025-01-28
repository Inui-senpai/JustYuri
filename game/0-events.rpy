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

    def callback_jy_tick(event):
        TimeCycle.tick()
        
    Callback.register("_tick", callback_jy_tick)