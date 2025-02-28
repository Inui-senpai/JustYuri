init -998 python:
    """
    Base Events
    _start
    _label
    _quit
    _safe_quit
    _exit
    _crash
    _tick

    JY Events
    karma: Runs whenever karma changes
    sanity: Runs whenever sanity changes
    gift: Runs whenever a gift is detected
    change_hair: Runs whenever Yuri's hair changes
    change_head_piece: Runs whenever Yuri's head piece changes
    change_music: Runs whenever the current background music changes
    change_outfit: Runs whenever Yuri's outfit changes
    change_presence: Runs whenever the Rich Discord Presence is updated
    change_room: Runs whenever the room changes to another room
    change_timecycle: Runs whenever the timecycle wants to change
    idle: Runs when Yuri returns to her idle state
    date: Runs when the player starts a date with Yuri
    dream: Runs when the player starts a dream with Yuri
    game: Runs when the player starts a game with Yuri
    talk_greeting: Runs when Yuri is about to greet the player
    talk_idle: Runs when Yuri is about to say an idle
    talk_topic: Runs when Yuri is about to talk to the player about a topic
    talk: Runs anytime Yuri begins any kind of dialogue
    """

    class StartEvent(Event):
        pass

    class LabelEvent(Event):
        def __init__(self, label_name, called):
            self.label_name = label_name
            self.called = called

    class QuitEvent(Event):
        pass

    class SafeQuitEvent(Event):
        pass

    class ExitEvent(Event):
        pass

    class CrashEvent(Event):
        pass
    class TickEvent(Event):
        ticks = 0

    callback_tick_event = TickEvent()

    # Fires anytime Yuri's karma changes
    class KarmaEvent(Event):
        def __init__(self, karma, resulting_karma, is_setting_karma):
            self.karma = karma
            self.resulting_karma = resulting_karma
            self.is_setting_karma = is_setting_karma

    # Fires anytime Yuri's sanity changes
    class SanityEvent(Event):
        def __init__(self, sanity, resulting_sanity, is_setting_sanity):
            self.sanity = sanity
            self.resulting_sanity = resulting_sanity
            self.is_setting_sanity = is_setting_sanity

    # Fires anytime the TimeCycle system wants to change the time id
    class TimeCycleEvent(Event):
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

    class TalkEvent(Event):
        def __init__(self, dialogue):
            self.label = str(label)
            self.original_label = str(label)
            self.dialogue = dialogue



    EventAPI.register(StartEvent)
    EventAPI.register(LabelEvent)
    EventAPI.register(QuitEvent)
    EventAPI.register(SafeQuitEvent)
    EventAPI.register(ExitEvent)
    EventAPI.register(CrashEvent)
    EventAPI.register(TickEvent)

    EventAPI.register(KarmaEvent)
    EventAPI.register(SanityEvent)
    EventAPI.register(TimeCycleEvent)
    EventAPI.register(TickEvent, callback_jy_tick)