label control_panel:
    python:
        if not dev_access:
            renpy.call("save_and_quit_but_its_abrupt")
    menu:
        "Where to Go?"
        "Expression Hub":
            $persistent.costume = "school"
            $persistent.current_timecycle = "_day"
            $show_chr("standard")
            call screen make_expression
        "Dialogue Calling":
            call caller_loop
        "Active Menu":
            $call_dialogue(ch30_loop_type, "actives")
        "Ch30_Loop Jump":
            call ch30_loop
        "KS System":
            menu:
                "Show KS Points":
                    y "Sanity = [persistent.sanity_points], Karma = [persistent.karma_points]"
                "Alter Karma/Sanity":
                    call alter_ks
                "Nevermind":
                    $pass
        "Time_Tracker System":
            call alter_time_tracker
        "Seen Label Memory Deletion":
            python:
                forget_label = renpy.input("Which seen label do you want to forget?")
                if forget_label.strip() != "":
                    if renpy.seen_label(forget_label):
                        y("forgetting... [forget_label]")
                        del renpy.game.persistent._seen_ever[forget_label]
                    else:
                        y("I've never seen [forget_label] before.")
        "Close Game":
            jump save_and_quit
    jump control_panel

label caller_loop:
    menu:
        "Welcome to the Dialogue Loop"
        "Trigger Random Dialogue Type":
            menu:
                "Which Dialogue Type?"
                "Trigger Idle":
                    $call_dialogue(ch30_loop_type, "idles")
                "Trigger Greeting":
                    $call_dialogue(ch30_loop_type, "greetings")
                "Trigger Farewell":
                    $call_dialogue(ch30_loop_type, "farewells")
        "Reset Memory":
            $reset_memory()
        "Call To Dialogue":
            python:
                jumper = str(renpy.input("Which dialogue do you want to call to?"))
                if renpy.has_label(jumper):
                    renpy.call_in_new_context(jumper)
                else:
                    y(str(jumper) + " does not exist.")
        "Return To Control Panel":
            jump control_panel
    jump caller_loop

label alter_ks:
    menu:
        "Would you like to alter these values based on points or ks_convert_ names?"
        "Points":
            jump alter_1
        "ks_convert_":
            jump alter_2

label alter_1:
    menu:
        "All of the following increase the points by 10"
        "Increase Karma":
            $persistent.karma_points = persistent.karma_points + 10
        "Increase Sanity":
            $persistent.sanity_points = persistent.sanity_points + 10
        "Decrease Karma":
            $persistent.karma_points = persistent.karma_points - 10
        "Decrease Sanity":
            $persistent.sanity_points = persistent.sanity_points - 10
        "Reset Sanity and Karma to 0":
            $persistent.sanity_points = 0
            $persistent.karma_points = 0

        # --- New Custom Options ---
        "Custom Increase":
            jump custom_increase
        "Custom Decrease":
            jump custom_decrease
        # --- End of New Options ---

        "Return To Control Panel":
            "Huh. I suppose we don't need to do that."
            jump control_panel
    "Done."
    jump alter_1

label custom_increase:
    menu:
        "Which value to increase?"
        "Karma":
            jump custom_karma_increase
        "Sanity":
            jump custom_sanity_increase
        "Back":
            jump alter_1

label custom_decrease:
    menu:
        "Which value to decrease?"
        "Karma":
            jump custom_karma_decrease
        "Sanity":
            jump custom_sanity_decrease
        "Back":
            jump alter_1
label custom_karma_increase:
    python:
        amount = renpy.input("Enter amount to increase Karma (between -100 and 100):")
        try:
            amount = int(amount)
            if -100 <= amount <= 100:
                persistent.karma_points += amount
                y("Karma increased by [amount]. New Karma Points: [persistent.karma_points]")
            else:
                y("Invalid amount. Must be between -100 and 100.")
        except ValueError:
            y("Invalid input. Please enter a number.")
    jump alter_1

label custom_sanity_increase:
    python:
        amount = renpy.input("Enter amount to increase Sanity (between -100 and 100):")
        try:
            amount = int(amount)
            if -100 <= amount <= 100:
                persistent.sanity_points += amount
                y("Sanity increased by [amount]. New Sanity Points: [persistent.sanity_points]")
            else:
                y("Invalid amount. Must be between -100 and 100.")
        except ValueError:
            y("Invalid input. Please enter a number.")
    jump alter_1

label custom_karma_decrease:
    python:
        amount = renpy.input("Enter amount to decrease Karma (between -100 and 100):")
        try:
            amount = int(amount)
            if -100 <= amount <= 100:
                persistent.karma_points += amount  # Use += for decrease as well (amount will be negative)
                y("Karma decreased by [amount]. New Karma: [persistent.karma_points]")
            else:
                y("Invalid amount. Must be between -100 and 100.")
        except ValueError:
            y("Invalid input. Please enter a number.")
    jump alter_1

label custom_sanity_decrease:
    python:
        amount = renpy.input("Enter amount to decrease Sanity (between -100 and 100):")
        try:
            amount = int(amount)
            if -100 <= amount <= 100:
                persistent.sanity_points += amount # Use += for decrease as well (amount will be negative)
                y("Sanity decreased by [amount]. New Sanity: [persistent.sanity_points]")
            else:
                y("Invalid amount. Must be between -100 and 100.")
        except ValueError:
            y("Invalid input. Please enter a number.")
    jump alter_1

label alter_2:
    menu:
        "Alter Karma or Sanity?"
        "Karma":
            menu:
                "Karma Level 5":
                    $persistent.karma_points = lvl_to_point(5)
                "Karma Level 4":
                    $persistent.karma_points = lvl_to_point(4)
                "Karma Level 3":
                    $persistent.karma_points = lvl_to_point(3)
                "Karma Level 2":
                    $persistent.karma_points = lvl_to_point(2)
                "Karma Level 1":
                    $persistent.karma_points = lvl_to_point(1)
                "Nevermind":
                    "Huh. I suppose we don't need to do that."
        "Sanity":
            menu:
                "Sanity Level 5":
                    $persistent.sanity_points = lvl_to_point(5)
                "Sanity Level 4":
                    $persistent.sanity_points = lvl_to_point(4)
                "Sanity Level 3":
                    $persistent.sanity_points = lvl_to_point(3)
                "Sanity Level 2":
                    $persistent.sanity_points = lvl_to_point(2)
                "Sanity Level 1":
                    $persistent.sanity_points = lvl_to_point(1)
                "Nevermind":
                    "Huh. I suppose we don't need to do that."
        "Return to Control Panel":
            jump control_panel
    "Done."
    jump alter_2

label alter_time_tracker:
    menu:
        "Show Current In_Game Time":
            y "[persistent.ingame_time]"
        "Set In_Game Time":
            $ingame_time_seconds_temp = 3600*int(renpy.input("Number of Hours?\n"))
            $ingame_time_days_temp = int(renpy.input("Number of Days?"))
            $persistent.ingame_time = datetime.timedelta(seconds = ingame_time_seconds_temp, days = ingame_time_days_temp)
            y "[persistent.ingame_time]"
    jump control_panel

#label ip_tracer:
#    "Warning: You are about to allow the Just Yuri mod to find and send info of your current IP address to a reference website to determine your current location."
#    "The following piece of code requires an internet connection to work properly."
#    menu:
#        "Do you wish to continue in using this function?"
#        "Yes":
#            "Very well."
#            "Continue on to the next dialogue to begin testing the ip tracer."
#        "No":
#            jump superdeluxe
#    python:
#        if renpy.file("foundyou.txt"):
#            f = open(config.basedir + "/game/foundyou.txt", "r")
#            location_data = []
#            for line in f:
#                location_data.append(line)
#            city = location_data[0]
#            latitude = location_data[1]
#            longtitude = location_data[2]
#            y("Your guessed city is " + city + ".")
#            y("Your guessed latitude and longtitude are (" + latitude + ", " + longtitude + ").")
#    "This concludes the ip_tracer test."
#    jump superdeluxe
#
#label complete_deletion:
#    "Warning: The following action may delete both the current version of this mod and the persistent file if everything goes right. Otherwise, only an error should pop up"
#    menu: 
#        "Do you wish to test Yuri Panic?"
#        "Yes":
#            call updateconsole ("Inducing panic state...", "Panic state induced.")
#            call updateconsole ("Persistent file deletion detected...", "/yuri.chr aberrations enhanced.")
#            python:
#                if renpy.windows:
#                    os.remove(os.path.expandvars("%APPDATA%") + "\RenPy\JustYuri\persistent")
#                if renpy.linux:
#                    os.remove(os.path.expandvars("%APPDATA%") + "\RenPy\JustYuri\persistent")
#                if renpy.macintosh:
#                    os.remove("~/Library/RenPy/JustYuriOverhaul/persistent")
#            $shutil.rmtree(config.basedir + "/game")
#            "Please report back to Pyracmon the success of the following procedure."
#            $renpy.call("save_and_quit_but_its_abrupt")
#        "No":
#            jump ch30_loop
