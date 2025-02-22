default restore_message = "hello"

label open_discord:
    $ webbrowser.open_new('https://discordapp.com/invite/RUdwW7q')
    return

label open_twitter:
    $ webbrowser.open_new('https://www.x.com/JustYuriDevTeam')
    return

label open_youtube:
    $ webbrowser.open_new('https://www.youtube.com/channel/UCHVJWOeTMXxxI-oL2xYyjbQ')
    return

init -1 style default:
    font gui.default_font
    size gui.text_size
    color gui.text_color
    outlines [(2, "#000000aa", 0, 0)]
    line_overlap_split 1
    line_spacing 1

init -1 style default_monika is normal:
    slow_cps 30

init -1 style edited is default:
    font "gui/font/VerilySerifMono.otf"
    kerning 8
    outlines [(10, "#000", 0, 0)]
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos
    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

init -1 style normal is default:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

init -1 style input:
    color gui.accent_color

init -1 style hyperlink_text:
    color gui.accent_color
    hover_color gui.hover_color
    hover_underline True

init -1 style splash_text:
    size 24
    color "#000"
    font gui.default_font
    text_align 0.5
    outlines []

init -1 style poemgame_text:
    yalign 0.5
    font "gui/font/Halogen.ttf"
    size 30
    color "#000"
    outlines []

    hover_xoffset -3
    hover_outlines [(3, "#cae", 0, 0), (2, "#a8c", 0, 0), (1, "#86a", 0, 0)]

init -1 style gui_text:
    font gui.interface_font
    color gui.interface_text_color
    size gui.interface_text_size


init -1 style button:
    properties gui.button_properties("button")

init -1 style button_text is gui_text:
    properties gui.button_text_properties("button")
    yalign 0.5


init -1 style label_text is gui_text:
    color gui.accent_color
    size gui.label_text_size

init -1 style prompt_text is gui_text:
    color gui.text_color
    size gui.interface_text_size

init -1 style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

init -1 style bar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)

init -1 style scrollbar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)
    unscrollable "hide"
    bar_invert True


init -1 style vscrollbar:
    xsize 18
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    unscrollable "hide"
    bar_invert True

init -1 style slider:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb "gui/slider/horizontal_hover_thumb.png"

init -1 style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"

init -1 style namebox_yuri:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

init -1 style say_label:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    outlines [(3, "#a679ff", 0, 0), (1, "#a679ff", 1, 1)]

init -1 style say_label_purple:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    outlines [(3, "#7e06ce", 0, 0), (1, "#7e06ce", 1, 1)]

init -1 style say_label_bluegreenish:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    outlines [(3, "#b0f8ef", 0, 0), (1, "#b0f8ef", 1, 1)]

init -1 style say_label_red:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    outlines [(3, "#ff0000", 0, 0), (1, "#ff0000", 1, 1)]

init -1 style say_label_orange:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    outlines [(3, "#fc7703", 0, 0), (1, "#fc7703", 1, 1)]

init -1 style say_label_blue:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    outlines [(3, "#87ceeb", 0, 0), (1, "#87ceeb", 1, 1)]

init -1 style say_label_pink:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    outlines [(3, "#ff8cfa", 0, 0), (1, "#ff8cfa", 1, 1)]

init -1 style say_label_green:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    outlines [(3, "#50c878", 0, 0), (1, "#50c878", 1, 1)]

init -1 style say_label_black:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    outlines [(3, "#010101", 0, 0), (1, "#010101", 1, 1)]

init -1 style say_label_dark_purple:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    outlines [(3, "#380c6b", 0, 0), (1, "#380c6b", 1, 1)]

init -1 style say_label_sky_blue:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    outlines [(3, "#58cced", 0, 0), (1, "#58cced", 1, 1)]
init -501 screen configuration(configurations):
    python: # Pre-Cache Options to preserver rendering order
        cache_render = []
        for configuration, options in configurations.items():
            cache = [ configuration.name, [0, []] ]
            cached_height = 0
            size = 0
            height = 0
            cache_index = 1
            index = 1
            option_should_shift = False
            option_can_shift = False
            for option in options:
                option_type = type(option)
                option_size = 4 if option_type == OptionSeparator else 2 if option_type == OptionBar else 0 if option_type == OptionTitle or option_type == OptionButton or option_type == OptionCheckbox else 1
                option_height = 0 if option_type == OptionButton or option_type == OptionCheckbox else 1
                option_should_shift = False if option_type == OptionButton or option_type == OptionCheckbox else True
                option_can_shift = option_can_shift or option_type == OptionButton or option_type == OptionCheckbox
                size += option_size
                
                if option_can_shift and option_should_shift:
                    index += 1
                    cached_height = cached_height if height < cached_height else height
                    cache[cache_index][0] = cached_height
                    height = 0
                    option_can_shift = False
                    cache[cache_index].append([])
                    size += 1

                if size > 4 or size == 4 and option_size <= 0:
                    size = option_size
                    cached_height = 0
                    height = 0
                    cache_index += 1
                    cache.append([0, []])
                    index = 1
                        
                height += option_height
                cache[cache_index][index].append(option)
                cache[cache_index][0] = cached_height
                if option_size > 0:
                    index += 1
                    cached_height = cached_height if height < cached_height else height
                    cache[cache_index][0] = cached_height
                    height = 0
                    option_can_shift = False
                    cache[cache_index].append([])
            cache_render.append(cache)
                
        for cache in cache_render:
            for cache_hbox in cache:
                if type(cache_hbox) == str:
                    continue
                cached_height = 0
                for cache_column in cache_hbox:
                    if type(cache_column) == int:
                        cached_height = cache_column
                        continue
                    else:
                        height = 0
                        for option in cache_column:
                            option_type = type(option)
                            option_size = 4 if option_type == OptionSeparator else 2 if option_type == OptionBar else 0 if option_type == OptionTitle else 1
                            height += 0 if option_type == OptionButton or option_type == OptionCheckbox else 1
                            if option_size > 0:
                                for amount in range(0, cached_height - height):
                                    cache_column.insert(0, ScreenSpacer())
                                break
                del cache_hbox[0]
    
    for cache in cache_render:
        null height (4 * gui.pref_spacing)
        vbox:  
            for cache_hbox in cache:
                if type(cache_hbox) == str:
                    label "{size=*1.25}" + cache_hbox + "{/size}":
                        style_prefix "slider"
                else:
                    hbox:
                        for cache_column in cache_hbox:
                            vbox:
                                for option in cache_column:
                                    $ option_type = type(option)
                                    if option_type == OptionSeparator:
                                        null height (4 * gui.pref_spacing)
                                    elif option_type == OptionTitle:
                                        $ option_label = option.title(option) if is_callable(option.title) else option.title
                                        label option_label:
                                            style_prefix "slider"
                                    elif option_type == OptionBar:
                                        $ option.init_action(option)
                                        vbox:
                                            python:
                                                option_label_type = type(option.labels)
                                                if option_label_type == str:
                                                    option_label = option.labels
                                                elif is_callable(option.labels):
                                                    option_label = option.labels()
                                                else:
                                                    option_label_size = len(option.labels)
                                                    option_label_index = int(option_label_size * ((option.value + 1) / option_label_size))
                                                    option_label = option.labels[option_label_index - 1]
                                            style_prefix "slider"
                                            label option_label
                                            bar value FieldValue(option, "value", min=option.min, max=option.max, offset=option.offset, step=option.step, action=Function(option.action if option.action else option.default_action, option)):
                                                xmaximum 350
                                    elif option_type == OptionButton:
                                        $ option.init_action(option)
                                        vbox:
                                            $ option_label = option.labels if type(option.labels) == str else option.labels[option.value]
                                            style_prefix "check"
                                            textbutton option_label action ActionButton(option)
                                    elif option_type == OptionCheckbox:
                                        $ option.init_action(option)
                                        vbox:
                                            $ option_label = option.labels if type(option.labels) == str else option.labels(option) if is_callable(option.labels) else option.labels[1 if option.value else 0]
                                            style_prefix "check"
                                            textbutton option_label action ActionCheckbox(option)
                                    elif option_type == OptionChecklist:
                                        $ option.init_action(option)
                                        $ option_label = option.label if type(option.label) == str else option.label(option) if is_callable(option.label) else option.label[option.value]
                                        label option.label
                                        vbox:
                                            style_prefix "check"
                                            for index in range(0, len(option.labels)):
                                                textbutton option.labels[index] action ActionChecklist(option, index)
                                    else:
                                        null height 50

init -501 screen say(who, what): #dialogue window
    zorder 100
    style_prefix "say"

    window:
        id "window"

        text what id "what"

        if who is not None:

            window:
                style "namebox"
                text who id "who"

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

init -1 style window is default
init -1 style say_label is default
init -1 style say_dialogue is default
init -1 style say_thought is say_dialogue

init -1 style namebox is default
init -1 style namebox_label is say_label

init -1 style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox/textbox.png", xalign=0.5, yalign=1.0)

init -1 style yuri_txtbox:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox/textbox_y.png", xalign=0.5, yalign=1.0)

init -1 style window2:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox/textbox_m.png", xalign=0.5, yalign=1.0)

init -1 style window3:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox/textbox_n.png", xalign=0.5, yalign=1.0)

init -1 style window4:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox/textbox_s.png", xalign=0.5, yalign=1.0)

init -1 style windowgh:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox/textbox_gh.png", xalign=0.5, yalign=1.0)

init -1 style window_monika is window:
    background Image("gui/textbox/textbox_yuri.png", xalign=0.5, yalign=1.0)

init -1 style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

init -1 style say_label:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    outlines [(3, "#a679ff", 0, 0), (1, "#a679ff", 1, 1)]

init -1 style say_dialogue:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

init 499 image ctc:
    xalign 0.81 yalign 0.98 xoffset -5 alpha 0.0 subpixel True
    "gui/ctc.png"
    block:
        easeout 0.75 alpha 1.0 xoffset 0
        easein 0.75 alpha 0.5 xoffset -5
        repeat

init 499 image input_caret:
    Solid("#a679ff")
    size (2,25) subpixel True
    block:
        linear 0.35 alpha 0
        linear 0.35 alpha 1
        repeat

init -501 screen input(prompt):
    style_prefix "input"

    window:

        has vbox:
            xpos gui.text_xpos
            xanchor 0.5
            ypos gui.text_ypos

        text prompt style "input_prompt"
        input id "input"

init -1 style input_prompt is default

init -1 style input_prompt:
    xmaximum gui.text_width
    xalign gui.text_xalign
    text_align gui.text_xalign

init -1 style input:
    caret "input_caret"
    xmaximum gui.text_width
    xalign 0.5
    text_align 0.5

init -501 screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

define -1 config.narrator_menu = True

init -1 style choice_vbox is vbox
init -1 style choice_button is button
init -1 style choice_button_text is button_text

init -1 style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

init -1 style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

init -1 style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines []


init -1 python:
    def RigMouse():
        currentpos = renpy.get_mouse_pos()
        targetpos = [640, 345]
        if currentpos[1] < targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)

init -501 screen rigged_choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    timer 1.0/30.0 repeat True action Function(RigMouse)
init -501 screen guide_mouse(number):#
    timer 0.1 action Jump("ouija" + str(number))

init -1 style choice_vbox is vbox
init -1 style choice_button is button
init -1 style choice_button_text is button_text

init -1 style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

init -1 style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

init -1 style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines []

init -501 screen quick_menu():


    zorder 100

    if quick_menu:


        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.995


            if not config.allow_skipping:
                textbutton _("History") action ShowMenu('history')
                textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
                textbutton _("Auto") action Preference("auto-forward", "toggle")
                textbutton _("Settings") action ShowMenu('preferences')
            else:
                textbutton _("History") action ShowMenu('history')
                textbutton _("Auto") action Preference("auto-forward", "toggle")
                textbutton _("Settings") action ShowMenu('preferences')

default -1 quick_menu = True

init -1 style quick_button:
    properties gui.button_properties("quick_button")
    activate_sound gui.activate_sound

init -1 style quick_button_text:
    properties gui.button_text_properties("quick_button")
    outlines []

init -1 python:
    def FinishEnterName():
        if not player: return
        persistent.playername = player
        persistent.stutter_player = persistent.playername[:1] + "-" + persistent.playername
        renpy.hide_screen("name_input")
        renpy.jump_out_of_context("start")

init -501 screen navigation():
    if main_menu:
        vbox:
            xpos 30
            ypos 100
            style_prefix "navigation"
            hbox:
                if main_menu:
                    textbutton _("New Game") action Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName))

        vbox:
            xpos 30
            ypos 140
            style_prefix "navigation"
            hbox:
                if main_menu:
                    textbutton _("Settings") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]
        vbox:
            xpos 30
            ypos 180
            style_prefix "navigation"
            hbox:
                if main_menu:
                    textbutton _("Discord Server") action [Help("open_discord"), Show(screen="dialog", message="Join the Official Just Yuri Community!", ok_action=Hide("dialog"))]
        vbox:
            xpos 30
            ypos 220
            style_prefix "navigation"
            hbox:
                if main_menu:
                    textbutton _("Official X") action [Help("open_twitter"), Show(screen="dialog", message="Follow Just Yuri on X!", ok_action=Hide("dialog"))]
        vbox:
            xpos 30
            ypos 260
            style_prefix "navigation"
            hbox:
                if main_menu:
                    textbutton _("Official YouTube") action [Help("open_youtube"), Show(screen="dialog", message="Subscribe to Just Yuri's Channel!", ok_action=Hide("dialog"))]
        vbox:
            xpos 30
            ypos 300
            style_prefix "navigation"
            hbox:
                if main_menu:
                    textbutton _("Credits") action ShowMenu("about")

        vbox:
            xpos 30
            ypos 340
            style_prefix "navigation"
            hbox:
                if main_menu:
                    textbutton _("Quit") action Quit_no_farewell(confirm=not main_menu)

    else:
        vbox:
            xpos 30
            ypos 100
            style_prefix "navigation"
            hbox:
                if renpy.variant("pc"):
                    textbutton _("History") action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]

        vbox:
            xpos 30
            ypos 140
            style_prefix "navigation"
            hbox:
                if renpy.variant("pc"):
                    textbutton _("Settings") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]
        vbox:
            xpos 30
            ypos 180
            style_prefix "navigation"
            hbox:
                if renpy.variant("pc"):
                    textbutton _("Discord Server") action [Help("open_discord"), Show(screen="dialog", message="Join the Official Just Yuri Community!", ok_action=Hide("dialog"))]
        vbox:
            xpos 30
            ypos 220
            style_prefix "navigation"
            hbox:
                if renpy.variant("pc"):
                    textbutton _("Official X") action [Help("open_twitter"), Show(screen="dialog", message="Follow Just Yuri on X!", ok_action=Hide("dialog"))]
        vbox:
            xpos 30
            ypos 260
            style_prefix "navigation"
            hbox:
                if renpy.variant("pc"):
                    textbutton _("Official YouTube") action [Help("open_youtube"), Show(screen="dialog", message="Subscribe to Just Yuri's Channel!", ok_action=Hide("dialog"))]
        vbox:
            xpos 30
            ypos 300
            style_prefix "navigation"
            hbox:
                if renpy.variant("pc"):
                    textbutton _("Credits") action ShowMenu("about")
        vbox:
            xpos 30
            ypos 340
            style_prefix "navigation"
            hbox:
                if renpy.variant("pc"):
                    textbutton _("Mod List") action ShowMenu("mod_list")
        vbox:
            xpos 30
            ypos 380
            style_prefix "navigation"
            hbox:
                if renpy.variant("pc"):
                    textbutton _("Quit") action Quit_no_farewell(confirm=not main_menu)


init -1 style navigation_button is gui_button
init -1 style navigation_button_text is gui_button_text

init -1 style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

init -1 style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    font "gui/font/lhandw.ttf"
    color "#fff"
    outlines [(4, "#a679ff", 0, 0), (2, "#a679ff", 2, 2)]
    hover_outlines [(4, "#b9e", 0, 0), (2, "#b9e", 2, 2)]
    insensitive_outlines [(4, "#ecf", 0, 0), (2, "#ecf", 2, 2)]

init -501 screen main_menu():
    tag menu

    style_prefix "main_menu"

    if persistent.ghost_menu:
        add "white"
        add "menu_art_y_ghost"
        add "menu_art_n_ghost"
    else:
        add "menu_bg"
        add "menu_art_y"
        add "menu_art_n"
        frame
        use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "Alpha Revival: [alpha.version]":
                style "main_menu_version"

            text "Beta: [config.version]":
                style "main_menu_version"

    if not persistent.ghost_menu:
        add "menu_particles"
        add "menu_particles"
        add "menu_particles"
        add "menu_logo"
    if persistent.ghost_menu:
        add "menu_art_s_ghost"
        add "menu_art_m_ghost"
    else:
        if persistent.playthrough == 1 or persistent.playthrough == 2:
            add "menu_art_s_glitch"
        else:
            add "menu_art_s"
        add "menu_particles"
        if persistent.playthrough != 4:
            add "menu_art_m"
        add "menu_fade"

    key "K_ESCAPE" action Quit(confirm=False)

init -1 style main_menu_frame is empty
init -1 style main_menu_vbox is vbox
init -1 style main_menu_text is gui_text
init -1 style main_menu_title is main_menu_text
init -1 style main_menu_version is main_menu_text:
    color "#000000"
    size 16
    outlines []

init -1 style main_menu_frame:
    xsize 310
    yfill True

    background "menu_nav"

init -1 style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

init -1 style main_menu_text:
    xalign 1.0

    layout "subtitle"
    text_align 1.0
    color gui.accent_color

init -1 style main_menu_title:
    size gui.title_text_size

init -501 screen game_menu_m():
    $ persistent.menu_bg_m = True
    add "gui/menu_bg_m.png"
    timer 0.3 action Hide("game_menu_m")

init -501 screen game_menu(title, scroll=None):
    if main_menu:
        add gui.main_menu_background
    else:
        key "mouseup_3" action Return()
        add gui.game_menu_background

    style_prefix "game_menu"

    frame:
        style "game_menu_outer_frame"
        has hbox
        frame:
            style "game_menu_navigation_frame"
        frame:
            style "game_menu_content_frame"
            if scroll == "viewport":
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    yinitial 0.0
                    side_yfill True
                    has vbox
                    transclude

            elif scroll == "vpgrid":
                vpgrid:
                    cols 1
                    yinitial 1.0

                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    side_yfill True
                    transclude
            else:
                transclude
    use navigation

    if not main_menu and persistent.playthrough == 2 and not persistent.menu_bg_m and renpy.random.randint(0, 49) == 0:
        on "show" action Show("game_menu_m")
    vbox:
        xpos 30
        ypos 420
        style_prefix "navigation"
        hbox:
            textbutton _("Return") action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


init -1 style game_menu_outer_frame is empty
init -1 style game_menu_navigation_frame is empty
init -1 style game_menu_content_frame is empty
init -1 style game_menu_viewport is gui_viewport
init -1 style game_menu_side is gui_side
init -1 style game_menu_scrollbar is gui_vscrollbar
init -1 style game_menu_label is gui_label
init -1 style game_menu_label_text is gui_label_text
init -1 style return_button is navigation_button
init -1 style return_button_text is navigation_button_text
init -1 style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120
    background "gui/overlay/game_menu.png"

init -1 style game_menu_navigation_frame:
    xsize 280
    yfill True

init -1 style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

init -1 style game_menu_viewport:
    xsize 920

init -1 style game_menu_vscrollbar:
    unscrollable gui.unscrollable

init -1 style game_menu_side:
    spacing 10

init -1 style game_menu_label:
    xpos 50
    ysize 120

init -1 style game_menu_label_text:
    font "gui/font/lhandw.ttf"
    size gui.title_text_size
    color "#fff"
    outlines [(6, "#a679ff", 0, 0), (3, "#a679ff", 2, 2)]
    yalign 0.5

init -1 style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30

init -501 screen about():
    tag menu
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")

define -1 gui.about = ""

init -1 style about_label is gui_label
init -1 style about_label_text is gui_label_text
init -1 style about_text is gui_text

init -1 style about_label_text:
    size gui.label_text_size

init -501 screen save():
    tag menu
    use file_slots(_("Save"))


init -501 screen load():
    tag menu
    use file_slots(_("Load"))

init -1 python:
    def FileActionMod(name, page=None, **kwargs):
        if persistent.playthrough == 3 and renpy.current_screen().screen_name[0] == "save":
            return Show(screen="dialog", message="There's no point in saving anymore.\nDon't worry, I'm not going anywhere.", ok_action=Hide("dialog"))
        else:
            return FileAction(name)


init -501 screen file_slots(title):

    default page_name_value = FilePageNameInputValue()

    use game_menu(title):

        fixed:
            order_reverse True
            button:
                style "page_label"
                xalign 0.5
                input:
                    style "page_label_text"
                    value page_name_value
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing
                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    button:
                        action FileActionMod(slot)
                        has vbox
                        add FileScreenshot(slot) xalign 0.5
                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"
                        text FileSaveName(slot):
                            style "slot_name_text"
                        key "save_delete" action FileDelete(slot)
            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0
                spacing gui.page_spacing
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

init -1 style page_label is gui_label
init -1 style page_label_text is gui_label_text
init -1 style page_button is gui_button
init -1 style page_button_text is gui_button_text

init -1 style slot_button is gui_button
init -1 style slot_button_text is gui_button_text
init -1 style slot_time_text is slot_button_text
init -1 style slot_name_text is slot_button_text

init -1 style page_label:
    xpadding 50
    ypadding 3

init -1 style page_label_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

init -1 style page_button:
    properties gui.button_properties("page_button")

init -1 style page_button_text:
    properties gui.button_text_properties("page_button")
    outlines []

init -1 style slot_button:
    properties gui.button_properties("slot_button")

init -1 style slot_button_text:
    properties gui.button_text_properties("slot_button")
    color "#666"
    outlines []

init -501 screen preferences():
    tag menu

    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_("Settings"), scroll="viewport"):
        vbox:
            xoffset 50
            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")
                        #flag #Courtesy of Terra#2060
                        #if persistent.narrative != "a1p1_start":
                            #Some documentation on how this works:
                            #If you're trying to change a persistent variable, you have to do it the SetField way.
                            #Otherwise you can do it the SetVariable way.
                            #This button does two actions, it sets the variable to keep track of if the button has been pressed or not True, and then sets ..whatever other variable you wanted, to whatever you want it to be.
                            #imagebutton:
                                #idle "/gui/poemgame/y_sticker_1.png"
                                #action SetField(persistent, "buttonvar", True), SetField(persistent, "narrative", "a1p1_start")
                        #else:
                        #    imagebutton idle "/gui/poemgame/y_sticker_2.png" action NullAction()
                        #    #Once the button has been pressed, the image changes and will never change back. The button no longer does anything.

                if config.developer:
                    vbox:
                        style_prefix "radio"
                        label _("Rollback Side")
                        textbutton _("Disable") action Preference("rollback side", "disable")
                        textbutton _("Left") action Preference("rollback side", "left")
                        textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                if restore_message == "access":
                    vbox:
                        style_prefix "radio"
                        label _("Custom Assets")
                        if persistent.narrative == None:
                            textbutton _("Assets Missing..."):
                                action SetField(persistent, "narrative", "a1p1_start")
                        else:
                            textbutton _("Assets Ready") action Jump("reveal_asset_location")
                            textbutton _("JYCrypt") action Jump("jycrypt")

            null height (4 * gui.pref_spacing)
            hbox:
                style_prefix "slider"

                vbox:
                    if persistent.idle_frequency_factor <= 0.75:
                        label _("Idle Frequency: Frequent")
                    elif persistent.idle_frequency_factor >= 1.25:
                        label _("Idle Frequency: Hesitant")
                    else:
                        label _("Idle Frequency: Normal")
                    bar value FieldValue(persistent, "idle_frequency_factor", 1.3, offset=0.5, step=0.1):
                        xmaximum 350

                    if persistent.game_time_rate > 1:
                        label _("Game Time Cycle: " + str(persistent.game_time_rate) + "x Faster")
                    else:
                        label _("Game Time Cycle: Realtime")
                    bar value FieldValue(persistent, "game_time_rate", step=1, range=100):
                        xmaximum 350

                    label _("Text Speed")
                    bar value FieldValue(_preferences, "text_cps", range=180, max_is_zero=False, style="slider", offset=20)

                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")

                vbox:
                    if config.has_music:
                        label _("Music Volume")
                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:
                        label _("Sound Volume")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)

                    if config.has_voice:
                        label _("Voice Volume")
                        hbox:
                            bar value Preference("voice volume")
                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing
                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

                    if persistent.high_gpu == 0:
                        textbutton _("Space BG Bloom: On") action [SetField(persistent, "high_gpu", 1), Function(timecycle_transition, persistent.bg, "now", True)]:
                            style_prefix "check"
                    elif persistent.high_gpu == 1:
                        textbutton _("Space BG Bloom: Off") action [SetField(persistent, "high_gpu", 2), Function(timecycle_transition, persistent.bg, "now", True)]:
                            style_prefix "check"
                    else:
                        textbutton _("Space BG Bloom: Vid") action [SetField(persistent, "high_gpu", 0), Function(timecycle_transition, persistent.bg, "now", True)]:
                            style_prefix "check"

            use configuration(ConfigAPI.configurations)


    text "v[config.version]":
        xalign 1.0 yalign 1.0
        xoffset -10 yoffset -10
        style "main_menu_version"

label gpu_toggle(setting):

init -1 style pref_label is gui_label
init -1 style pref_label_text is gui_label_text
init -1 style pref_vbox is vbox

init -1 style radio_label is pref_label
init -1 style radio_label_text is pref_label_text
init -1 style radio_button is gui_button
init -1 style radio_button_text is gui_button_text
init -1 style radio_vbox is pref_vbox

init -1 style check_label is pref_label
init -1 style check_label_text is pref_label_text
init -1 style check_button is gui_button
init -1 style check_button_text is gui_button_text
init -1 style check_vbox is pref_vbox

init -1 style slider_label is pref_label
init -1 style slider_label_text is pref_label_text
init -1 style slider_slider is gui_slider
init -1 style slider_button is gui_button
init -1 style slider_button_text is gui_button_text
init -1 style slider_pref_vbox is pref_vbox

init -1 style mute_all_button is check_button
init -1 style mute_all_button_text is check_button_text

init -1 style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

init -1 style pref_label_text:
    font "gui/font/RifficFree-Bold.ttf"
    size 24
    color "#fff"
    outlines [(3, "#a679ff", 0, 0), (1, "#a679ff", 1, 1)]
    yalign 1.0

init -1 style pref_vbox:
    xsize 225

init -1 style radio_vbox:
    spacing gui.pref_button_spacing

init -1 style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

init -1 style radio_button_text:
    properties gui.button_text_properties("radio_button")
    font "gui/font/Halogen.ttf"
    outlines []

init -1 style check_vbox:
    spacing gui.pref_button_spacing

init -1 style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

init -1 style check_button_text:
    properties gui.button_text_properties("check_button")
    font "gui/font/Halogen.ttf"
    outlines []

init -1 style slider_slider:
    xsize 350

init -1 style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

init -1 style slider_button_text:
    properties gui.button_text_properties("slider_button")

init -1 style slider_vbox:
    xsize 450










init -501 screen history():
    tag menu




    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                text h.what

        if not _history_list:
            label _("The dialogue history is empty.")


init -1 style history_window is empty

init -1 style history_name is gui_label
init -1 style history_name_text is gui_label_text
init -1 style history_text is gui_text

init -1 style history_text is gui_text

init -1 style history_label is gui_label
init -1 style history_label_text is gui_label_text

init -1 style history_window:
    xfill True
    ysize gui.history_height

init -1 style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

init -1 style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

init -1 style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

init -1 style history_label:
    xfill True

init -1 style history_label_text:
    xalign 0.5

image input_caret:
    Solid("#a679ff")
    size (2,25) subpixel True
    block:
        linear 0.35 alpha 0
        linear 0.35 alpha 1
        repeat

screen input(prompt):
    style_prefix "input"


    window:
        vbox:
            xalign .5
            yalign .5
            spacing 30

            text prompt style "input_prompt"
            input id "input"

style input_prompt:
    xmaximum gui.text_width
    xcenter 0.5
    text_align 0.5

style input:
    caret "input_caret"
    xmaximum gui.text_width
    xcenter 0.5
    text_align 0.5

init -501 screen name_input(message, ok_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        input default "" value VariableInputValue("player") length 20 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'.-_ 1234567890"

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action

init -501 screen dialog(message, ok_action):

    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action

init 499 image confirm_glitch:
    "gui/overlay/confirm_glitch.png"
    pause 0.02
    "gui/overlay/confirm_glitch2.png"
    pause 0.02
    repeat

init -501 screen confirm(message, yes_action, no_action):

    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        if in_sayori_kill and message == layout.QUIT:
            add "confirm_glitch" xalign 0.5

        else:
            label _(message):
                style "confirm_prompt"
                xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

init -1 style confirm_frame is gui_frame
init -1 style confirm_prompt is gui_prompt
init -1 style confirm_prompt_text is gui_prompt_text
init -1 style confirm_button is gui_medium_button
init -1 style confirm_button_text is gui_medium_button_text

init -1 style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

init -1 style confirm_prompt_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"

init -1 style confirm_button:
    properties gui.button_properties("confirm_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

init -1 style confirm_button_text is navigation_button_text:
    properties gui.button_text_properties("confirm_button")

init -501 screen fake_skip_indicator():
    use skip_indicator

init -501 screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox:
            spacing 6

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

transform -1 delayed_blink(delay, cycle):
    alpha .5

    pause delay
    block:

        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat

init -1 style skip_frame is empty
init -1 style skip_text is gui_text
init -1 style skip_triangle is skip_text

init -1 style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

init -1 style skip_text:
    size gui.notify_text_size

init -1 style skip_triangle:


    font "DejaVuSans.ttf"

init -501 screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')

transform -1 notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

init -1 style notify_frame is empty
init -1 style notify_text is gui_text

init -1 style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

init -1 style notify_text:
    size gui.notify_text_size

# Scrolable menu - testing
define prev_adj = ui.adjustment()
define gui.side_menu_button_width = 375
define gui.side_menu_button_height = 55
define gui.side_menu_button_tile = False
define gui.side_menu_button_borders = Borders(25, 5, 25, 5)

define gui.side_menu_button_text_font = gui.default_font
define gui.side_menu_button_text_size = 18
define gui.side_menu_button_text_idle_color = "#000"
define gui.side_menu_button_text_hover_color = "#fa9"

style side_menu_button is choice_button:
    properties gui.button_properties("side_menu_button")

style side_menu_button_text is choice_button_text:
    properties gui.button_text_properties("side_menu_button")

define gui.scrollable_menu_button_tile = False
define gui.scrollable_menu_button_width = 120
define gui.scrollable_menu_button_height = 45
define gui.scrollable_menu_button_borders = Borders(25, 5, 25, 5)

define gui.scrollable_menu_button_text_font = gui.default_font
define gui.scrollable_menu_button_text_size = gui.text_size
define gui.scrollable_menu_button_text_layout = "nobreak"
define gui.scrollable_menu_button_text_idle_color = "#000"
define gui.scrollable_menu_button_text_hover_color = "#fa9"

style scrollable_menu_button is choice_button:
    properties gui.button_properties("scrollable_menu_button")

style scrollable_menu_button_text is choice_button_text:
    properties gui.button_text_properties("scrollable_menu_button")

define current_topic_place = 0

transform anim_with_old(lin, xp, yp, zo, al, lin_old, xp_old, yp_old, zo_old, al_old):
    linear lin_old xpos xp_old ypos yp_old zoom zo_old alpha al_old
    linear lin xpos xp ypos yp zoom zo alpha al

transform anim(lin, xp, yp, zo, al):
    linear lin xpos xp ypos yp zoom zo alpha al

#screen to call three_choice_menu which has 3 controlable types of buttons
#args
#1, 2, 3, items for each button types
screen three_choice_menu(dict_items, current_list, three_below_button_items, side_button_items,first_run, cur_wheel_num):

    python:
        #put current list into local variable
        scroll_button_items = current_list
        persistent.marker3 = scroll_button_items
        if len(scroll_button_items) < 3:
            scroll_button_items.append(scroll_button_items[0])
            scroll_button_items.append(scroll_button_items[1])
        #Function which move the buttons in the wheel
        def change_to_left(dict_items, scroll_button_items, three_below_button_items, side_button_items, num, turn, cur_wheel_num):
            global current_topic_place
            current_topic_place += num
            renpy.hide_screen("three_choice_menu")
            renpy.show_screen("three_choice_menu", dict_items, scroll_button_items, three_below_button_items, side_button_items,turn, cur_wheel_num)
        #Function which move from one wheel to another
        def move_to_other_wheel(dict_items, new_topics, three_below_button_items, side_button_items, cur_wheel_num):
            global current_topic_place
            current_topic_place = 0
            if cur_wheel_num == 0:
                new_topics = list(new_topics)  # Convert to a list
                for i, item in enumerate(new_topics):
                    new_topics[i] = [item, 0]
            renpy.hide_screen("three_choice_menu")
            renpy.show_screen("three_choice_menu", dict_items, new_topics, three_below_button_items, side_button_items, "", cur_wheel_num)

    #Assigne function to keybored buttons
    key "K_LEFT"  action Function(change_to_left, dict_items, scroll_button_items, three_below_button_items, side_button_items, -1, "right", cur_wheel_num)
    key "K_RIGHT" action Function(change_to_left, dict_items, scroll_button_items, three_below_button_items, side_button_items, 1, "left", cur_wheel_num)
    key "K_a"  action Function(change_to_left, dict_items, scroll_button_items, three_below_button_items, side_button_items, -1, "right", cur_wheel_num)
    key "K_d" action Function(change_to_left, dict_items,scroll_button_items, three_below_button_items, side_button_items, 1, "left", cur_wheel_num)

#Scroll button objects
    fixed:
        xpos 0 ypos 0

        #viewport:
        #    xadjustment prev_adj


        #Arrow image buttons
        imagebutton xalign 0.99 yalign 0.98 auto "gui/arrow_button_right_%s.png" action Function(change_to_left, dict_items, scroll_button_items, three_below_button_items, side_button_items, 1, "left", cur_wheel_num)
        imagebutton xalign 0.01 yalign 0.98 auto "gui/arrow_button_left_%s.png" action Function(change_to_left, dict_items, scroll_button_items, three_below_button_items, side_button_items, -1, "right", cur_wheel_num)
        if cur_wheel_num > 0:
            textbutton "Back":
                xpos 585
                yalign 0.85
                style "scrollable_menu_button"
                action Function(move_to_other_wheel, dict_items, dict_items.keys(), three_below_button_items, side_button_items, 0)

    fixed:
        area (120, 640, 1200, 75)

        viewport:
            xadjustment prev_adj

            has hbox

            python:
                global current_topic_place
                if current_topic_place >= len(scroll_button_items):
                    current_topic_place = 0
                elif current_topic_place < 0:
                    current_topic_place = len(scroll_button_items) - 1

            for i, i_topic in enumerate(range(current_topic_place - 2, current_topic_place + 3)):

                if first_run == "right":
                    $ i_topic += 1
                elif first_run == "left":
                    $ i_topic -= 1

                if i_topic < 0:
                    $ i_topic += len(scroll_button_items)
                elif i_topic >= len(scroll_button_items):
                    $ i_topic -= len(scroll_button_items)

                if i == 0:
                    if first_run == "right":
                        if i_topic-1 < 0:
                            $ temp_i_topic = len(scroll_button_items) - 1
                        else:
                            $ temp_i_topic = i_topic - 1
                        textbutton scroll_button_items[temp_i_topic][0]:
                            at anim_with_old(0.5, 0, 17, 0.4, 0.3, 0, -20, 20, 0, 0)
                            style "side_menu_button"
                            xsize 320
                            ysize 75
                            if cur_wheel_num == 0:
                                action Function(move_to_other_wheel, dict_items , dict_items[scroll_button_items[temp_i_topic][0]], three_below_button_items, side_button_items, 1)
                            else:
                                action Return(scroll_button_items[temp_i_topic][1])
                    textbutton scroll_button_items[i_topic][0]:
                        if first_run == "left":
                            at anim_with_old(0.5, -20,20,0, 0, 0, 0, 17, 0.4, 0.3)
                        elif  first_run == "right":
                            at anim_with_old(0.5, 10, 10, 0.65, 0.5, 0, 0, 17, 0.4, 0.3)
                        else:
                            at anim(0, 0, 17, 0.4, 0.3)
                        if cur_wheel_num == 0:
                            action Function(move_to_other_wheel, dict_items , dict_items[scroll_button_items[i_topic][0]], three_below_button_items, side_button_items, 1)
                        else:
                            action Return(scroll_button_items[i_topic][1])
                        style "side_menu_button"
                        xsize 320
                        ysize 75
                elif i == 1:
                    textbutton scroll_button_items[i_topic][0]:
                        if first_run == "left":
                            at anim_with_old(0.5, 0, 17, 0.4, 0.3, 0, 10, 10, 0.65, 0.5)
                        elif  first_run == "right":
                            at anim_with_old(0.5, 20, 0, 1, 1, 0, 10, 10, 0.65, 0.5)
                        else:
                            at anim(0, 10, 10, 0.65, 0.5)
                        if cur_wheel_num == 0:
                            action Function(move_to_other_wheel, dict_items , dict_items[scroll_button_items[i_topic][0]], three_below_button_items, side_button_items, 1)
                        else:
                            action Return(scroll_button_items[i_topic][1])
                        style "side_menu_button"
                        xsize 320
                        ysize 75
                elif i == 2:
                    textbutton scroll_button_items[i_topic][0]:
                        if first_run == "left":
                            #linear lin xpos xp ypos yp zoom zo alpha al
                            at anim(0.5, 10, 10, 0.65, 0.5)
                        elif  first_run == "right":
                            at anim(0.5, 30, 10, 0.65, 0.5)
                        if cur_wheel_num == 0:
                            action Function(move_to_other_wheel, dict_items , dict_items[scroll_button_items[i_topic][0]], three_below_button_items, side_button_items, 1)
                        else:
                            action Return(scroll_button_items[i_topic][1])
                        style "side_menu_button"
                        xpos 20
                        xsize 320
                        ysize 75
                elif i == 3:
                    textbutton scroll_button_items[i_topic][0]:
                        if first_run == "left":
                            at anim_with_old(0.5, 20, 0, 1, 1, 0, 30, 10, 0.65, 0.5)
                        elif  first_run == "right":
                            at anim_with_old(0.5, 40, 17, 0.4, 0.3, 0, 30, 10, 0.65, 0.5)
                        else:
                            at anim(0, 30, 10, 0.65, 0.5)
                        if cur_wheel_num == 0:
                            action Function(move_to_other_wheel, dict_items , dict_items[scroll_button_items[i_topic][0]], three_below_button_items, side_button_items, 1)
                        else:
                            action Return(scroll_button_items[i_topic][1])
                        style "side_menu_button"
                        xsize 320
                        ysize 75
                elif i == 4:
                    textbutton scroll_button_items[i_topic][0]:
                        if first_run == "left":
                            at anim_with_old(0.5, 30, 10, 0.65, 0.5, 0, 40, 17, 0.4, 0.3)
                        elif  first_run == "right":
                            at anim_with_old(0.5, 60, 20, 0, 0, 0, 40, 17, 0.4, 0.3)
                        else:
                            at anim(0, 40, 17, 0.4, 0.3)
                        if cur_wheel_num == 0:
                            action Function(move_to_other_wheel, dict_items , dict_items[scroll_button_items[i_topic][0]], three_below_button_items, side_button_items, 1)
                        else:
                            action Return(scroll_button_items[i_topic][1])
                        style "side_menu_button"
                        xsize 320
                        ysize 75
                    if first_run == "left":
                        if i_topic+1 >= len(scroll_button_items):
                            $ i_topic -= len(scroll_button_items)
                        textbutton scroll_button_items[i_topic+1][0]:
                            at anim_with_old(0.5, 40, 17, 0.4, 0.3, 0, 60, 20, 0, 0)
                            style "side_menu_button"
                            xsize 320
                            ysize 75
                            if cur_wheel_num == 0:
                                action Function(move_to_other_wheel, dict_items , dict_items[scroll_button_items[i_topic+1][0]], three_below_button_items, side_button_items, 1)
                            else:
                                action Return(scroll_button_items[i_topic+1][1])

#Three button objects
    fixed:
        $ temp = 0
        for i_caption,i_label in three_below_button_items:
            if i_caption != "":
                textbutton i_caption:
                    xpos 35 + 400 * temp
                    yalign 0.85 - 0.116 * (temp % 2)
                    style "choice_button"
                    action Return(i_label)
            $ temp += 1

#Side button objects
        #fixed:
        #    area (35, 40, 400, 1000)

        #    viewport:

        #        has vbox
        #        $temp = side_button_items[:7]
        #        for i_caption,i_label in temp:
        #            textbutton i_caption:
        #                style "side_menu_button"
        #                action Return(i_label)
        #            null height 20

        #fixed:
        #    area (875, 40, 400, 1000)

        #    viewport:

        #        has vbox
        #        $temp = side_button_items[7:14]
        #        for i_caption,i_label in temp:
        #            textbutton i_caption:
        #                style "side_menu_button"
        #                action Return(i_label)
        #            null height 20

#expression = "0-0ab00-a1a1"
default headIterator = 0
default eyesIterator = 0
default mouthIterator = 0
default eyebrowsIterator = 0
default blushIterator = 0
default cryIterator = 0
default upLIterator = 0
default lowLIterator = 0
default upRIterator = 0
default lowRIterator = 0
default bothIterator = 0
default costumeIterator = 0
default spriteIterator = 0
default timecycleIterator = 0
default glassesIterator = 0
default nekoIterator = 0
default positionIterator = 0
default botharmsIterator = 0
default temp_code = "A-AAAAA-AAAA"

default headList = ["A","B"]
#0 = forward facing
default timecycle0List = ["_sunrise","_day","_sunset","_night"]#["","_sunrise","_day","_sunset","_night"]
default glasses0List = ["nothing", "glasses_1", "glasses_2"]
default neko0List = ["nothing", "cat_ears", "raccoon_ears"]

default eyes0List = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]
default mouth0List = ["A","B","C","D","E","F","G","H","I","J","K","L", "M", "N", "O"]
default eyebrows0List = ["A","B","C","D","E","F","G"]
default blush0List = ["A","B","C"]
default cry0List = ["A","B"]
#1 = side facing
default eyes1List = ["A","B"]
default mouth1List = ["A"]
default eyebrows1List = ["A"]
default blush1List = ["A","B"]
default cry1List = ["A"]

default upLList = ["A"]
default lowLList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]#,,"P","Q","R","S", "T"]
default upRList = ["A"]
default lowRList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]#,,"P","Q","R","S", "T"]
default botharmsList = ["A", "B", "C", "D"]

default costumeList = [
    "school", "sweater", "lab", "valentines", "pyjama"#, "pinkdress"
]
default spriteList = ["yuri_sit", "yuri_stand"]
#default sprite = ["Beta Yuri", "Alpha Yuri", "Standing Yuri"]
default positionList = ["t11", "t21", "t22", "t31", "t32", "t33"]
default position_marker = "t11"
screen make_expression():
    # Scroll button objects
    fixed:
        xpos 0
        ypos 0
        viewport:
            xadjustment prev_adj

        python:

            def addToClipBoard(text):
                import os
                command = 'echo ' + text.strip() + '| clip'
                os.system(command)

            def update(type, step_size=1):
                global current_timecycle_marker, headIterator, eyesIterator, mouthIterator, eyebrowsIterator, blushIterator, cryIterator, upLIterator, lowLIterator, upRIterator, lowRIterator, bothIterator, costumeIterator, spriteIterator, positionIterator, botharmsIterator, temp_code, timecycleIterator, glassesIterator, nekoIterator, position_marker

                # Define a helper function to avoid repetition
                def update_iterator(iterator_type, list_type, step):
                    iterator = globals().get(iterator_type + "Iterator")
                    if iterator is None:
                        return 0  # or handle the error as you see fit

                    iterator = (iterator + step) % len(globals().get(list_type))
                    globals()[iterator_type + "Iterator"] = iterator
                    return iterator

                if type in ["upL", "lowL", "upR", "lowR", "head", "costume", "sprite", "position", "botharms"]:
                     update_iterator(type, type + "List", step_size)

                else:
                    head_iterator = globals().get("headIterator")
                    if head_iterator is None:
                        head_iterator = 0
                    update_iterator(type, type + str(head_iterator) + "List", step_size)

                # Ensure all iterators are within bounds. Refactor this loop for efficiency
                for element in ["head", "eyes", "mouth", "eyebrows", "blush", "cry", "upL", "lowL", "upR", "lowR", "costume", "sprite", "position"]:
                    if element in ["upL", "lowL", "upR", "lowR", "head", "costume", "sprite", "position", "botharms"]:
                        globals()[element + "Iterator"] = globals().get(element + "Iterator") % len(globals().get(element + "List"))
                    else:
                        head_iterator = globals().get("headIterator")
                        if head_iterator is None:
                            head_iterator = 0

                        globals()[element + "Iterator"] = globals().get(element + "Iterator") % len(globals().get(element + str(head_iterator) + "List"))


                if type == "botharms":
                    temp_code = (str(headList[headIterator]) + "-"
                                 + str(eval("eyes" + str(headIterator) + "List")[eyesIterator])
                                 + str(eval("mouth" + str(headIterator) + "List")[mouthIterator]) +
                                 str(eval("eyebrows" + str(headIterator) + "List")[eyebrowsIterator]) +
                                 str(eval("blush" + str(headIterator) + "List")[blushIterator]) +
                                 str(eval("cry" + str(headIterator) + "List")[cryIterator]) +
                                 "-ZZA" +
                                 str(botharmsList[botharmsIterator]))
                else:
                    temp_code = (str(headList[headIterator]) + "-"
                                 + str(eval("eyes" + str(headIterator) + "List")[eyesIterator])
                                 + str(eval("mouth" + str(headIterator) + "List")[mouthIterator]) +
                                 str(eval("eyebrows" + str(headIterator) + "List")[eyebrowsIterator]) +
                                 str(eval("blush" + str(headIterator) + "List")[blushIterator]) +
                                 str(eval("cry" + str(headIterator) + "List")[cryIterator]) +
                                 "-" +
                                 str(upLList[upLIterator]) +
                                 str(lowLList[lowLIterator]) +
                                 str(upRList[upRIterator]) +
                                 str(lowRList[lowRIterator]))

                persistent.costume = costumeList[costumeIterator]

                if tc_class.bg_timecycle[persistent.bg]:
                    renpy.log(1)  # Use renpy.log instead of print_debug
                    current_timecycle_marker = timecycle0List[timecycleIterator]
                else:
                    renpy.log(2) # Use renpy.log instead of print_debug
                    current_timecycle_marker = "_space"

                persistent.face1 = glasses0List[glassesIterator]
                persistent.head1 = neko0List[nekoIterator]
                if persistent.head1 == "raccoon_ears":
                    persistent.head2 = "raccoon_tail"
                else:
                    persistent.head2 = "nothing"

                if spriteList[spriteIterator] == "yuri_stand":
                    if persistent.yuri_beta:
                        renpy.hide("yuri_sit")
                    else:
                        renpy.hide("yuri_sit_alpha")
                else:
                    renpy.hide("yuri_stand")

                show_chr(temp_code, str(spriteList[spriteIterator]), [str(positionList[positionIterator])])
                position_marker = positionList[positionIterator]

        # Text label
        text "CURRENT CODE: [temp_code] , [spriteIterator], [position_marker]" xpos 450 yalign 0.90 size 30

        # Buttons
        textbutton "Head" xpos 50 yalign 0.10 style "choice_button" xmaximum 125 ymaximum 35 action Function(update, "head") alternate Function(update, "head", -1)

        textbutton "Timecycle" xpos 200 yalign 0.10 style "choice_button" xmaximum 125 ymaximum 35 action Function(update, "timecycle") alternate Function(update, "timecycle", -1)
        text "TIMECYCLE: [current_timecycle_marker]" xpos 200 yalign 0.15 size 15
        textbutton "Glasses" xpos 200 yalign 0.25 style "choice_button" xmaximum 125 ymaximum 35 action Function(update, "glasses") alternate Function(update, "glasses", -1)
        textbutton "Neko" xpos 200 yalign 0.33 style "choice_button" xmaximum 125 ymaximum 35 action Function(update, "neko") alternate Function(update, "neko", -1)


        textbutton "Eyes" xpos 50 yalign 0.25 style "choice_button" xmaximum 125 ymaximum 35 action Function(update, "eyes") alternate Function(update, "eyes", -1)
        textbutton "Mouth" xpos 50 yalign 0.33 style "choice_button" xmaximum 125 ymaximum 35 action Function(update, "mouth") alternate Function(update, "mouth", -1)
        textbutton "Eyebrows" xpos 50 yalign 0.41 style "choice_button" xmaximum 125 ymaximum 35 action Function(update, "eyebrows") alternate Function(update, "eyebrows", -1)
        textbutton "Blush" xpos 50 yalign 0.49 style "choice_button" xmaximum 125 ymaximum 35 action Function(update, "blush") alternate Function(update, "blush", -1)
        textbutton "Cry" xpos 50 yalign 0.57 style "choice_button" xmaximum 125 ymaximum 35 action Function(update, "cry") alternate Function(update, "cry", -1)

        #textbutton "UpL" xpos 125 yalign 0.80 style "choice_button" xmaximum 125 ymaximum 35 action Function(update, "upL")
        textbutton "BothArms" xpos 200 yalign 0.80 style "choice_button" xmaximum 125 ymaximum 35 action Function(update, "botharms") alternate Function(update, "botharms", -1)
        textbutton "LowL" xpos 50 yalign 0.72 style "choice_button" xmaximum 125 ymaximum 35 action Function(update, "lowL") alternate Function(update, "lowL", -1)
        #textbutton "UpR" xpos 625 yalign 0.80 style "choice_button" xmaximum 125 ymaximum 35 action Function(update, "upR")
        textbutton "LowR" xpos 50 yalign 0.80 style "choice_button" xmaximum 125 ymaximum 35 action Function(update, "lowR") alternate Function(update, "lowR", -1)

        textbutton "Costume" xpos 50 yalign 0.95 style "choice_button" xmaximum 125 ymaximum 35 action Function(update, "costume") alternate Function(update, "costume", -1)

        # END Buttons
        textbutton "COPY_CODE" xpos 250 yalign 0.99 style "choice_button" action Function(addToClipBoard, temp_code)
        textbutton "DONE" xpos 700 yalign 0.99 style "choice_button" action Jump("control_panel")

        # sprite changer section
        textbutton "Background" xpos 1100 yalign 0.31 style "choice_button" xmaximum 125 ymaximum 35 action ui.callsinnewcontext("timecycleswitch")
        textbutton "Sprite" xpos 1100 yalign 0.49 style "choice_button" xmaximum 125 ymaximum 35 action Function(update, "sprite") alternate Function(update, "sprite", -1)
        #text "Design: [sprite]" xpos 550 yalign 0.85 size 30
        textbutton "Position" xpos 1100 yalign 0.40 style "choice_button" xmaximum 125 ymaximum 35 action Function(update, "position") alternate Function(update, "position", -1)


init -1 python:
    def split(arr, size):
        arrs = []
        while len(arr) > size:
            pice = arr[:size]
            arrs.append(pice)
            arr   = arr[size:]
        arrs.append(arr)
        return arrs

screen messagebox(message):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), [Hide('messagebox'), Return(True)]]
    frame:
        has vbox:
            xalign .5
            yalign .5
            spacing 30
        label _(message):
            style "confirm_prompt"
            xalign 0.5
        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action [Hide('messagebox'), Return(True)]

screen compliments(items):
    style_prefix "choice"

    fixed: #or frame, window
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True

            side_yfill True

            vbox:
                for i in items:
                    textbutton i[0] action Jump(i[1]) xpos 430 ypos 25
                    null
screen mod_settings(mod_id):
    tag menu
    use game_menu(_("Mod List"), scroll="viewport"):
        vbox:
            xoffset 50
            use configuration(ConfigAPI.mod_configurations[mod_id])
            

screen mod_list():
    tag menu
    use game_menu(_("Mod List"), scroll="viewport"):
        vbox:
            xoffset 50
            style_prefix "about"
            label "{size=*1.25}" + "Mod List" + "{/size}":
                style_prefix "slider"
            if submods.mod_count == 0:
                text "You have no submods installed. Submods can be installed under game/submods."
            else:
                if submods.mod_count == 1:
                    text "You have a submod installed. You can view it below."
                else :
                    text "You have " + str(submods.mod_count) + " submods installed. You can view them below."
            vbox:
                ypos 20
                spacing 60
                for mod_id in submods.mods:
                    vbox:
                        $submod = submods.mods[mod_id]
                        hbox:
                            add submod.icon
                            vbox:
                                xpos 10
                                label submod.name:
                                    style_prefix "slider"
                                text "{size=*0.7}Version: " + submod.version + "{/size}"
                                text "{size=*0.7}ID: " + submod.id + "{/size}"
                            if submod.id in ConfigAPI.mod_configurations:
                                textbutton "{size=*0.7}" + _("Open Settings") + "{/size}" action ShowMenu("mod_settings", submod.id):
                                    style_prefix "slider"

                        if submod.description:
                            text submod.description
                        if len(submod.dependencies) > 0:
                            label "Dependencies"
                            for dependency in submod.dependencies:
                                text "  > " + dependency
                null


screen about():
    tag menu

    hbox:
        add "label_credits"

    use game_menu(_("Credits"), scroll="viewport"):
        style_prefix "about"

        vbox:
            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"
#[erased] and MAS \n
            text (
                """{b}CURRENT HEAD DEVS{/b}

                Dandyfoot117
                Third Project Director.
                Head Dev.
                Producer.
                Coding Lead.
                QA Lead.
                Writer.
                BugSquasher.
                Coder.
                HDY Implementation.
                Tropical Date Implementation.

                *alura
                Head Dev.
                Art Lead.
                Artist.

                Sword Stance
                Head Dev.
                Writing Lead.
                Writer/Editor.

                Dr. Medic
                Producer.
                Head Dev.
                PR Lead.
                QA Lead.
                Tester.
                General Input and Helper.

                {b}CURRENT DEVS{/b}

                Shoujo Havoc
                Commissioned Artists.
                Merch Art.
                Logo V2 Maker.
                \"https://www.shoujohavoc.com/\"

                Unknownpony
                Tetris Maker.
                Renpy & Python Coder.
                First Version of Khet.

                Kurisu
                Ideas.
                Artist.
                Editor.

                Kesian
                Commissioned Artist.
                Writer.

                Trainer
                Support.
                Dev Counselor.
                MacOS Build Helper.

                Darkskull \"Kenshin\" Dawn Zenith
                Main Coder (In majority of the stuff).
                Chocolate Date Implementation.
                Valentines 2024 Date Implementation.
                Windy Stroll Dream Implementation.
                And many more...

                Ego/J.M.O/Nemesis
                Ex Head Dev.
                Ex Art Lead
                Backgrounds.
                Art Creation.
                Art Editing.

                Yuri's Husband
                Coder.
                Tester.

                PalaKeda
                Commissioned Artists.
                \"https://www.deviantart.com/palakeda\"

                Buglax/Ultima Atulos Maxim
                Tester.

                OFFLUCK
                Coder.

                SquadalaGuy
                General Input and Project Ideas.

                Veus
                Tester.

                C.Sub-Zero
                Tester.

                Slovenly_dilettante
                Coder.
                Writer.

                Yuri's Thighs
                Coder.
                Writer.
                Tester.

                Hbjennings
                Tester.

                Kyle Ren
                Coder.
                Tester.


                {b}CURRENT VERIFIED{/b}

                Emilia/Bonnie (EYLO)
                Verified Writer.

                Envy
                Verified Writer.
                Verified Coder.

                Jill Natalie Stingray
                Verified Artist.
                Verified Art Editor.
                Verified Tester.

                Mrr7782
                Verified Coder.

                Just hotdog yuri
                HDY writing.

                Logan the Spooky
                Verified Writer.

                mcl.exe
                Verified Writer.
                Verified Tester.

                Pancake
                Verified Writer.

                Bailey
                Ex-Tester.
                HDY Writer.

                DaFluffyPengu
                NSFW writer.
                Verified Writer.

                Toast
                Verified Artist.
                Verified Art Editor.

                {b}ASSETS{/b}

                Chibi Yuri Sprites by Mouhantain
                Edits by Seanm0451
                \"https://www.reddit.com/user/Mouhantain/\"

                H4D35
                Eternity Writing and Editing.
                Producer.

                MorteNexus for Sweater Shimejis.

                Monika After Story Dev Team
                \"https://www.monikaafterstory.com/\"
                for allowing previous use of some of their Monika sprites and the initial Menu code before Unknown's retooling, as well as the past Talk button.


                {b}EX-DEVS{/b}

                Poosi
                Original Owner.
                Creator of Just Yuri.
                One of its Main Programmers.
                Gatherer of the Original Team.

                Motion
                Lead Writer and Editor in Original Team. One of the Establishing Figures Behind the Insanity Dialogue.

                Fjord
                Original Yuri Artwork.
                The Base Sprite Made from Scratch in its Earliest Incarnation.

                Primus
                Base Code Structure of Just Yuri Space Classroom.
                Maker of the Very Base Code of JY.

                Dio/Cronks/Chronos/Algol/Ouroboros/Pyracmon/Dalekette/Diosynechis
                Second Project Director.
                Head Dev.
                Lead Writer.
                Lead Coder.
                Narrative Writer.
                Lead Member of Original Team.
                Alpha and Overhaul Writer and Coder.
                Expression System Coder.
                Timecycle Coder.
                Writer of the Dark Intro.

                b1g int3ll3ct
                Head Dev.
                Code Lead.
                General Project Manager.
                MC Dialogues Remover.
                Dialogue Coder.
                Hot Dog Yuri Creator.

                Dalek
                Head Dev.
                Eternity Lead.
                Writer Lead.
                Old Bugsquasher.

                StephenHCE117/Clifford
                Clifford-PartMascot.
                Head Dev.
                Producer.
                Merch Manager.
                Public Relations.
                Ex-Community Server Administrator.
                NSFW Lead.
                Large Investor/Donator.

                Blizzard-The Angel of Ice
                Head Dev.
                Stability Lead.
                Head Counselor.

                Spooky MrMcgee
                Head Dev.
                Everything.

                SlightlyAmiss
                Audio Engineer Lead.
                Song Designer.
                Teardrops (Just Yuri's Rain Dream Theme).

                Leodecraprio
                Audio Engineer.
                Song Designer.
                SFX Designer.
                Starset (Just Yuri's Sunset Song).
                Enotronics (Just Yuri's Night Song).
                Eternity (Just Yuri's Sunrise Song).
                Introversion (Just Yuri's Day Song).
                Stagnant Air (Just Yuri Overhaul Release Songs).
                Hot Date (April Fools 2019 Song).

                belwynn
                In-House Counselor.
                Yuri Emulation Expert.
                Poem Writer.
                Ex-Community Server Staff.
                Treasurer Lead.

                Bryce
                Head Dev.
                QA Lead.

                FaithHW
                Art Lead.
                Writing.
                Suggestions.
                Testing Lead.

                Angon
                Commissioned Artists.
                Yuri Sprite Art.
                CG Art.

                Seanm0451
                Head Dev.
                Art Lead.
                Chibi Project Lead.

                profGRob
                Head Dev.
                Narrative Writer.
                Lead.
                Ex-Community Server Staff.

                SyntheticGoat
                Tester.
                General input and help.
                HKLS revamp pioneer.
                Current Community Server Owner.

                Ryuse
                Touching Up Yuri Artwork.
                The one who Split the Yuri Artwork into its Different Pieces.

                Lolika
                Maker of the yh1.ogg (Hello Again...).
                yins.ogg (Hello Again... Insane Variant) Just Yuri Theme.

                0Blueaura/Seba
                Maker of the Custom Timecycle BG 3D Room as well as the Timecycle Variations and Purple Room variants.
                Fixer of the Yuri Sprite's Errors.
                The One Who Resized the Majority of the Timecycle Images.
                Recolored the GUI Pictures to Purple, Aside From those Contributed by CPG.
                The Purple Room.

                Tooru
                Artist Who Made the Shy Poses.
                Both Standard & Blushing.

                theneworchestra
                Adjustments in Music.
                Fellow Writer of Dialogue.

                Chernov
                Early Sane Yuri Dialogue Writer.
                Master of the Expression Delivery in the Early Days.

                ! OhYeahYuri !
                Renpy & Python Programming.

                erased
                Contributions Overall.
                The Boop Code Mechanic.

                Phathom
                Enhance Resolution of Old Yuri Sprites up to Excellent Levels.
                Reason the Sprites Actually Look Sharp Today.

                Madman with a Labcoat
                Writing & Coding.

                Not Cuddles
                Yupee Sprites.
                Coding for Yupee.

                The Community
                Original Helper.
                Organizer of Initial Yuri Traits List.

                Toni
                Editing on Multiple Art Pieces for Improvement, Including the Eyes, Precision Bug Testing, Starting Work on Sweater Yuri Assets.

                DarkChocolateYuri
                Yuri Emulation Expert.
                Yuri RolePlay Help.
                Ideas.

                Vinyl Flames
                Ideas.
                Dialog Writing.

                Bardinal
                Testing.
                Ex-Community Server Staff.

                Redd
                Testing.
                Eternity Writing.
                Ex-Community Server Staff.

                InfiniteDeer
                Commissioned Artists.
                Art and Ideas.

                NormallyAverage
                Art.
                Art Editing.
                Suggestions.

                Symbol Games
                Ren'Py & Python Coding.

                Motion
                Early Founder of Insanity Writing.
                Yuri Emulation Expert.

                judg3THJudg3
                Yupee Sprites.
                Coding for Yupee.

                Lord Catsius
                Programing.
                Bug Fixes.

                MarKreations Studios
                NSFW Writer.

                TailRadish
                Writer/Editor.

                LilyAnon
                Ideas.
                Writing.
                Community Server Help.

                Hunny Fox
                Writer.
                Suggestions.
                Bug Testing.
                Community Server Staff.

                R3b0rnMike
                Eternity Writer/Editor.

                Three
                Ren'Py & Python Coding.
                Mac and Linux Port.

                Ishtar's Throne
                Testing.
                Ideas.
                Eternity Writing.

                Zeus Krazy
                Art Edits.
                Helper in Coding Writing for the Pre-Space.
                Particularly in the Natsuki Scenes.

                Wandering Comet
                Pencil Artist.

                Paradox
                Former Co-Head of Narrative.
                Writer.

                Aussie_Mantis
                Dev Counselor.
                Community Server Staff.

                toast
                Art Editor.

                TBirdTrevino
                Bug Testing.
                End User Support.
                Community Server Staff.

                Acrinym
                Website Design.

                Icicle C Cold
                Yuri Emulation Expert.
                Commissioned Editor.

                Miguel
                Yandere.
                Tester.
                Community Server Staff.

                Sariel
                Python Coder.

                imunkaea
                Commissioned Artist.
                Maker of NSFW Yuri Art Back in the Day.
                SFW/NSFW Yuri Arts And Sprites Today.
                Rain Dream CG.
                Tropical Date Sprites.

                Fen
                Ex Head Dev.
                Eternity Writer.

                NullCase
                Writer.
                Tester.
                General all Round Helper.

                YuriHuggu
                Writer.
                Tester.

                Crystalline
                Writer.

                Hugh Mungus
                Tester.

                YourUberDriver
                Tester.
                Writer.

                Tuna
                Art Editor.

                huangstilk
                Commissioned Artists.
                \"https://www.deviantart.com/sandiegoappletrees/gallery\"

                jaebot
                Commissioned Artists.
                \"https://heenaem.wixsite.com/portfolio\"

                notRohan
                Art Editor.

                Lethe
                Progenitor God Ruptured Heaven.
                Community Server Staff.
                Art Editor.
                The Yuri Dead CGs in their Early Days.
                An Art Editor in their own Right.
                Timecycle Versions of Hug.
                Community Server Staff.

                Cpl. Corgi
                Writer/Editor.
                Writer of the Highway Dream.

                Delstraw
                Writer.
                Writer of the Tropical Date.

                Bucket Man
                Writer.
                HDY Writer.


                {b}EX-VERIFIED{/b}

                Gravard
                For Writing Idle 67.

                Juri
                Verified Writing.
                Bugsquashing.

                Picugaming.
                Documentation and Testing.

                Spare

                theGalacticBlaze

                Are You Lying?

                ATLAS

                Evathing.Gov
                Verified Writer.
                Ideas.

                JADE
                Eternity Writer.

                Isabelle
                Support.
                Ideas.

                Dark Chocolate
                Ideas.
                Yuri Coon.

                JustME
                LogoV1 Design.

                Sovietsmoke
                Bugsquasher.

                _OatZ
                Ideas.
                Insanity Writing.

                Yami Bakura
                Writer.
                Ideas.

                SharkBerry
                Art.

                oceansurvivr
                Writing.

                dokibrandondoki
                Mac Testing.

                Otelo2
                Writing.
                Coding.
                Starting Spanish Translation.

                Retro R3AP3R
                Pencil Artist.

                BananaMan
                Community Server Staff.

                rambo_tan
                Testing.
                Ideas.

                KJ
                Large Investor/Donator."""
                )
