#==================================================#
#  Just Yuri Mod - Callbacks File
#==================================================#
#  This file is responsible for running and 
#  handling events posted by renpy and submods.
#  
#  :D
#==================================================#

#==================================================#
#  How To Use Events
#  
#  Events are used in JY to allow developers to
#  execute special code when any event occurs
#  in game. JY comes with a few pre-registered
#  events listed below. JY also allows custom
#  events to be used as well.
#
#  1: Register the event
#     To define a custom event, use
#     EventAPI.register(<event>). You may also pass in
#     callbacks after the event if you wish.
#     All events must extend from the Event class and
#     must have a unique event id
#
#     - See 1-events.rpy for examples
#
#  2: Register your callbacks
#     To register your own callback methods, use
#     EventAPI.register(<event>, *<callback>)
#     All callback method must have only one
#     parameter used for the expected event.
#
#     The event parameter holds the event object which
#     keeps track of variables saved within it. All
#     methods will be able to change any variable
#     within the event to change the result of the
#     event.
#
#  3: Call the event
#     You can call any event at anytime. Use
#     EventAPI.call(<event>) to call that event.
#     All callbacks registered with that event
#     will be called.
#
#  4: Stopping further event calls
#     If you want to stop the event from executing
#     further callbacks, call event.cancel().
#     If there are any more callbacks that needs
#     to be fired, they will be skipped.
#==================================================#

init -999 python:
    class Event:
        id = None
        canceled = False
        def cancel(self):
            self.canceled = True

    class EventHandler:
        event = None
        callbacks = []

        def __init__(self, event : Event, callbacks):
            self.event = event
            self.callbacks = []
            self.register(callbacks)

        def register(self, callbacks):
            print_debug("Registering " + str(len(callbacks)) + " callback(s) for event " + self.event.id)
            for callback in callbacks:
                if callback and not callback in self.callbacks and type(callback) != tuple:
                    print_debug("  - Registering callback: " + repr(callback))
                    self.callbacks.append(callback)

        def call(self, event : Event):
            for callback in self.callbacks:
                try:
                    callback(event)
                except BaseException as exception:
                    print("Failed to execute event " + self.event.id + " as the function errored upon execution")
                    print_error(exception, new_traceback=False)

    class EventAPI:
        event_handlers = {}

        @staticmethod
        def register(event: Event, *callbacks):
            if not event.id in EventAPI.event_handlers:
                EventAPI.event_handlers[event.id] = EventHandler(event, callbacks)
            else:
                EventAPI.event_handlers[event.id].register(callbacks)

        @staticmethod
        def call(event: Event):
            if event.id in EventAPI.event_handlers:
                EventAPI.event_handlers[event.id].call(event)
            else:
                print_error(NameError("Failed to execute event " + str(event.id) + " as the event was not registered prior to calling it"))

        @staticmethod
        def contains(id):
            return id in EventAPI.event_handlers    

    #==============================================#
    # Renpy Callbacks
    #==============================================#
    def callback_start():
        EventAPI.call(StartEvent())

    def callback_label(label_name, called):
        global current_label; current_label = label_name
        event = LabelEvent(str(label_name), called)
        EventAPI.call(event)

        if event.label_name == "_quit":
            callback_quit()
            return
        if event.label_name == "save_and_quit":
            callback_safe_quit()
            return

    def callback_quit():
        persistent.crash = False
        EventAPI.call(QuitEvent())

    def callback_safe_quit():
        persistent.crash = False
        EventAPI.call(SafeQuitEvent())
        
    def callback_exit():
        EventAPI.call(ExitEvent())

    def callback_crash():
        EventAPI.call(CrashEvent())

    def callback_tick():
        EventAPI.call(callback_tick_event)
        callback_tick_event.ticks += 1
    
init -998 python:
    if persistent.crash:
        crashed = True
        callback_crash()
    else:
        crashed = False
        persistent.crash = True
        renpy.save_persistent()