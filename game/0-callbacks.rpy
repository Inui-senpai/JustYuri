#==================================================#
#  Just Yuri Mod - Callbacks File
#==================================================#
#  This file is responsible for running and 
#  handling events posted by renpy and submods.
#  
#  :D
#==================================================#

init -999 python:
    def callback_start():
        print("A: START")
    def callback_label(label_name, called):
        print("B: " + str(label_name))
        if label_name == "_quit":
            callback_quit()
            return
        if label_name == "save_and_quit":
            callback_safe_quit()
            return
    def callback_quit():
        persistent.crash = False
        print("C: Quit")

    def callback_safe_quit():
        persistent.crash = False
        print("C: Safe Quit")

    def callback_exit():
        print("D: EXIT")

    def callback_crash():
        print("E: FUCK")

    if persistent.crash:
        callback_crash()