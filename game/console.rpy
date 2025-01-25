image console_bg:
    "#333"
    topleft
    alpha 0.75 size (480,180)

image border = "images/vfx/border.png"

style console_text:
    font "gui/font/F25_Bank_Printer.ttf"
    color "#fff"
    size 18
    outlines []

style console_text_new:
    font "gui/font/F25_Bank_Printer.ttf"
    color "#fff"
    size 18
    outlines []

style console_text_console is console_text:
    slow_cps 30

default consolehistory = []
image console_text = ParameterizedText(style="console_text_console", anchor=(0,0), xpos=30, ypos=10)
image console_history = ParameterizedText(style="console_text", anchor=(0,0), xpos=30, ypos=50)
image console_caret = Text(">", style="console_text", anchor=(0,0), xpos=5, ypos=10)

image console_text_new = ParameterizedText(style="console_text_console", anchor=(0,0), xpos=50, ypos=600) #xpos used to be 200
image console_history_new = ParameterizedText(style="console_text", anchor=(0,0), xpos=30, ypos=30)#xpos used to be 180
image console_caret_new = Text(">", style="console_text", anchor=(0,0), xpos=30, ypos=600)#xpos used to be 180


label clear_console():
    call updateconsole("import os", "import os")
    $consolehistory = []
    call updateconsole("os.system(cls)", " ")
    return

label updateconsole_torrent(log=[(" ", " ")]):
    python:
        text = []
        history = []
        for element in log:
            text.append(element[0])
            history.append(element[1])
        if len(text) == 0:
            text = [" "]
            history = [" "]
    show console_bg zorder 100
    show console_caret zorder 100
    $x = 0
    while x < len(text):
        $text_element = text[x]
        show console_text "_" as ctext zorder 100
        show console_text "[text_element]" as ctext zorder 100
        $ pause(len(text_element) / 30.0 + 0.5)
        hide ctext
        show console_text "_" as ctext zorder 100
        call updateconsolehistory(history[x])
        $x += 1
    pause 0.5
    return

label updateconsole(text="", history=""):
    show console_bg zorder 100
    show console_caret zorder 100
    show console_text "_" as ctext zorder 100
    show console_text "[text]" as ctext zorder 100
    $ pause(len(text) / 30.0 + 0.5)
    hide ctext
    show console_text "_" as ctext zorder 100
    call updateconsolehistory (history)
    $ pause(0.5)
    return

label updateconsole_clearall(text="", history=""):
    $ pause(len(text) / 30.0 + 0.5)
    pause 0.5
    return

label updateconsole_old(text="", history=""):
    $ starttime = datetime.datetime.now()
    $ textlength = len(text)
    $ textcount = 0
    show console_bg zorder 100
    show console_caret zorder 100
    show console_text "_" as ctext zorder 100
    label updateconsole_loop:
        $ currenttext = text[:textcount]
        call drawconsole (drawtext=currenttext)
        $ pause_duration = 0.08 - (datetime.datetime.now() - starttime).microseconds / 1000.0 / 1000.0
        $ starttime = datetime.datetime.now()
        if pause_duration > 0:
            $ renpy.pause(pause_duration / 2)
        $ textcount += 1
        if textcount <= textlength:
            jump updateconsole_loop

    pause 0.5
    hide ctext
    show console_text "_" as ctext zorder 100
    call updateconsolehistory (history)
    pause 0.5
    return

    label drawconsole(drawtext=""):

        show console_text "[drawtext]_" as ctext zorder 100

        return

label updateconsolehistory(text=""):
    if text:
        python:
            consolehistory.insert(0, text)
            if len(consolehistory) > 5:
                del consolehistory[5:]
            consolehistorydisplay = '\n'.join(map(str, consolehistory))
        show console_history "[consolehistorydisplay]" as chistory zorder 100

    return

label hideconsole:
    hide console_bg
    hide console_caret
    hide ctext
    hide chistory
    return

screen caret_pos(xPos):
    style_prefix "console_text"
    text ">" xpos 180+xPos ypos 595

### JY additions

screen console_choice(choices = []):
    #if len(choices) != 0:
    zorder 200
    fixed:
        $x = 0
        for choice_name, choice_jump in choices:
            mousearea:
                area(200+x, 600, 75, 300)
                hovered Show("caret_pos", xPos=x)
                unhovered Hide("caret_pos")
            textbutton choice_name text_style "console_text_new" xpos 200+x ypos 600 action Call(choice_jump)
            $x += (900/len(choices)+len(choice_name))

label updatedevconsole_torrent(log=[("", "")]):
    python:
        text = []
        cantThinkOfAVariableName = log[0]
        history = []
        for element in log:
            text.append(element[0])
            history.append(element[1])
        if len(text) == 0:
            text = [" "]
            history = [" "]
    show console_caret_new zorder 100
    $x=0
    while x < len(text):
        $text_element = text[x]
        show console_text_new "_" as ctext zorder 100:
            #xalign 0.014 yalign 1.0
        show console_text_new "[text_element]" as ctext zorder 100:
            #xalign 0.014 yalign 1.0
        if text_element.strip():
            $renpy.music.play("sfx/text_typing.mp3", channel="sound", loop=False)
        $pause(len(text) / 30.0+1.7)
        stop sound
        hide ctext
        show console_text_new "_" as ctext zorder 100:
            #xalign 0.014 yalign 1.0
        call updatedevconsolehistory(history[x])
        $x += 1
    pause 0.5
    return

label updatedevconsole_torrent_fast(log=[(" ", " ")]):
    python:
        text = []
        history = []
        for element in log:
            text.append(element[0])
            history.append(element[1])
            if len(element) == 3:
                speed.append(element[2])
            else:
                speed.append(1)
        if len(text) == 0:
            text = [" "]
            history = [" "]
    show console_caret_new zorder 100
    $x=0
    while x < len(text):
        $text_element = text[x]
        show console_text_new "_" as ctext zorder 100:
            xalign 0.014 yalign 1.0
        show console_text_new "[text_element]" as ctext zorder 100:
            xalign 0.014 yalign 1.0
        $ pause((len(text) / 30.0 + 0.5)/speed[x])
        hide ctext
        show console_text_new "_" as ctext zorder 100:
            xalign 0.014 yalign 1.0
        call updatedevconsolehistory(history[x])
        $x += 1
    return

label updatedevconsolehistory(text=""):
    if text:
        python:
            consolehistory.append(text)
            if len(consolehistory) > 15:
                del consolehistory[:-25]
            consolehistorydisplay = '\n'.join(map(str, consolehistory))
        show console_history_new "[consolehistorydisplay]" as chistory zorder 100
        $renpy.music.play("sfx/history_beep.mp3", channel="sound", loop=False)
        pause 0.5
        stop sound
    return

label clear_dev_console():
    $consolehistory = []
    call updatedevconsole_torrent([("cls", " ")])
    return

label dev_console_startup:
    $DisableTalk()
    stop music
    window hide
    show black zorder 90
    call clear_dev_console()
    call updatedevconsole_torrent(
        [('python', '>python'),
        (" ", '{cps=30}\nPython 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32\nType "help", "copyright", "credits" or "license" for more information.{/cps}'),
        (">>dev_console.rpy", ">>>dev_console.py"),
        (" "," "),
        ("Authenticating...........", ">Authenticating..........."),
        (" ", ">Verified Access Token Recognized."),
        (" ",">Welcome back GUEST."),
        (" "," "),
        (" ",str(config.name) + " "  + str(config.version) + " " + str(alpha.version) + " Proprietary Console."),
        (" ", "Note: Due to recent breaches of security, the following Alpha Tester Console is heavily restrictive."),
        (" ", "To operate, please select the desired option from the selection at the bottom of the screen."),
        (" ", "More options are available with higher level clearance."),
        (" ", "If any inconvenience arises, please contact us through the #latest-build channel for now as we reorganize."),
        (" ", "To request aid on the Console, please refer to your select passphrases and responses to responses of denial/confusion from Heads."),
        (" ", "For additional security reasons, any and all references to this Console are to be referred to as either 'photoshoppped' or 'great editing'."),
        (" ", "If you are lacking the software update module, please access it through the JY Verified Storage Server: {a}https://discord.gg/kW6vTtW{/a}"),
        (" ", " "),
        (' ', '>Please Select Desired Option')] )
label console_choice_test:
    call screen console_choice([("Access Dreams", "dream_access"), ("Experimental Logs", "logs"), ("Exit", "dev_console_exit")])
    jump console_choice_test

label dream_access:
    call updatedevconsole_torrent([
        (" ", " "),
        (" ", "No Dream Instances Active."),
        (" ", " "),
        (" ", "Searching dream logs..."),
        (" ", "No Dream Logs Found."),
        (" ", " "),
        (" ", " "),
        (" ", " ")
        ])

label logs:

    call updatedevconsole_torrent([
        (" ", " "),
        (" ", "No Experimental Logs Found. Insufficient Clearance/Not Stored in Local System."),
        (" ", " "),
        (" ", " "),
        (" ", " ")
        ])
    return

label dev_console_exit:
    call clear_dev_console
    call updatedevconsole_torrent([("exit()", " ")])
    python:
        import random
        x = random.randint(1, 100)
    if x == 100:
        call updatedevconsole_torrent_fast([("Wait, what is thi--", " ")])
    elif x == 50:
        call updatedevconsole_torrent_fast([("Sleep, perchance to drea--", " ")])
    elif x == 25:
        call updatedevconsole_torrent_fast([("W-what's h-happenin--", " ")])
    $persistent.narrative = False
    $renpy.call("save_and_quit_but_its_abrupt")
