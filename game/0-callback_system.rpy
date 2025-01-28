#==================================================#
#  Just Yuri Mod - Callbacks File
#==================================================#
#  This file is responsible for running and 
#  handling events posted by renpy and submods.
#  
#  :D
#==================================================#

#==================================================#
#  How To Use Callbacks
#  
#  Callbacks are used in JY to allow developers to
#  execute special code when any event occurs
#  in game. JY comes with a few pre-registered
#  events listed below. JY also allows custom
#  events to be used as well.
#
#  1: Register the event id
#     To define a custom event, use
#     Callback.register(<id>). You may also pass in
#     callbacks after the id.
#
#  2: Register your callback functions
#     To register your own callback functions, use
#     Callback.register(<id>, *<callback functions>)
#     All callback functions must have only one
#     parameter.
#
#     That parameter will hold the event object which
#     keeps track of variables saved within it. All
#     functions will be able to change any variable
#     within the event to change the result of the
#     event.
#
#  3: Call the event id
#     You can call any event at anytime. Use
#     Callback.call(<id>, <event>) to call that id.
#     All callbacks registered with that event
#     will be called. You must pass the coresponding
#     EventObject on the second parameter or the
#     game will crash.
#
#  4: Stopping further event calls
#     If you want to stop the event from executing
#     further callbacks, set event.canceled to
#     True. If there are any more callbacks that
#     need to be fired, they will all be skipped.
#==================================================#

#==================================================#
#  Renpy Callbacks
#
#     _start: Called when the game has finished
#             loading
#
#     _label: Called when a renpy label has executed
#         Parameters
#           - label_name: The name of the label
#           - called: Whether this label was called
#
#     _quit: Called when the user quits the game
#            without saying goodbye
#
#     _safe_quit: Called when the user quits the game
#                 after saying goodbye
#
#     _exit: Called when the game closes for any
#            reason
#
#     _crash: Called durring the init phase if jy
#             has crashed last session
#
#     _tick: Called twenty times every second in
#            the background
#==================================================#
init -998 python:
    class CallbackObject:
        id = None  # The id of the callback
        callbacks = []  # The functions that get called when this callback is called

        def __init__(self, event_id, *callbacks):
            self.id = event_id
            self.callbacks = []

            if callbacks[0] != ():
                for callback in callbacks:
                    self.callbacks.append(callback)

        # Calls all functions registered while passing in a EventObject. EventObjects are used to pass parameters and get a result back.
        def call(self, event_object):
            for callback in self.callbacks:
                try:
                    callback(event_object)
                except:
                    print_error("Failed to execute event " + self.id + " as the function errored upon execution")
                    raise
                if event_object.canceled:
                    break
            return event_object

    # The Callback API
    class Callback:
        events = {}

        # Registers functions that get called by a specified callback id
        @staticmethod
        def register(event_id, *callbacks):
            if event_id in Callback.events:
                if callbacks[0] != ():
                    for callback in callbacks:
                        Callback.events[event_id].callbacks.append(callback)
            else:
                Callback.events[event_id] = CallbackObject(event_id, callbacks)

        # Calls all functions of a callback with a specified EventObject. EventObjects are used to pass parameters and get a result back.
        @staticmethod
        def call(event_object):
            if event_object.id in Callback.events:
                Callback.events[event_object.id].call(event_object)
            else:
                print_error("Failed to execute event " + str(event_object.id) + " as the event was not registered prior to calling it")
                raise NameError("Event id " + event_object.id + " was not registered prior to calling it")

    #==============================================#
    # Renpy Callbacks
    #==============================================#
    
    def callback_start():
        Callback.call(StartEvent())

    def callback_label(label_name, called):
        current_label = label_name
        event = LabelEvent(str(label_name), called)
        Callback.call(event)

        if event.label_name == "_quit":
            callback_quit()
            return
        if event.label_name == "save_and_quit":
            callback_safe_quit()
            return

    def callback_quit():
        persistent.crash = False
        Callback.call(QuitEvent())

    def callback_safe_quit():
        persistent.crash = False
        Callback.call(SafeQuitEvent())
        
    def callback_exit():
        Callback.call(ExitEvent())

    def callback_crash():
        Callback.call(CrashEvent())

    def callback_tick():
        Callback.call(TickEvent())
        
    #==============================================#
    # Main Callbacks
    #==============================================#

    #==============================================#
    # Renpy Events
    #==============================================#
    class EventObject:
        id = None  # The event id this event is used in
        canceled = False  # Whether the event should continue running

    class StartEvent(EventObject):
        id = "_start"

    class LabelEvent(EventObject):
        id = "_label"
        label_name = None
        called = False
        def __init__(self, label_name, called):
            self.label_name = label_name
            self.called = called

    class QuitEvent(EventObject):
        id = "_quit"

    class SafeQuitEvent(EventObject):
        id = "_safe_quit"

    class ExitEvent(EventObject):
        id = "_exit"

    class CrashEvent(EventObject):
        id = "_crash"

    class TickEvent(EventObject):
        id = "_tick"

    #==============================================#
    # Registering Callbacks
    #==============================================#
    Callback.register(StartEvent.id)
    Callback.register(LabelEvent.id)
    Callback.register(QuitEvent.id)
    Callback.register(SafeQuitEvent.id)
    Callback.register(ExitEvent.id)
    Callback.register(CrashEvent.id)
    Callback.register(TickEvent.id)
    
    if persistent.crash:
        callback_crash()