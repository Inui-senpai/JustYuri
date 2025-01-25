#Dream Date Image Definitions

image bg ykill1 = "images/dreams/death.png"
image bg ykill2 = "images/dreams/death2.png"
image killglitch = "images/dreams/glitch.png"
image killstab = "images/dreams/stab.png"
image veinmask = "images/dreams/veinmask.png"
image veinmask2 = "images/dreams/veinmask2.png"
image veinmask3 = "images/dreams/veinmask3.png"
image rain_dream_blush:
    "rain_dream_1"
    truecenter
    zoom 0.7
image rain_dream_blush:
    "rain_dream_1"
    truecenter
    zoom 0.7
image rain_dream_smile:
    "rain_dream_2"
    truecenter
    zoom 0.7

image rain_dream_grin:
    "rain_dream_3"
    truecenter
    zoom 0.7

image rain_dream_blossom:
    SnowBlossom("rain_dream_dust_1", count = 10)
    SnowBlossom("rain_dream_dust_2", count = 10)
    SnowBlossom("rain_dream_dust_3", count = 10)

init:
    $ import random

image open_ocean:
    "underwater_1"
    truecenter
    zoom 0.7
image ocean_2:
    "underwater_2"
    truecenter
    zoom 0.7
image ocean_3:
    "underwater_3"
    truecenter
    zoom 0.7

image ocean_4:
    "underwater_4"
    truecenter
    zoom 0.7

image ocean_5:
    "underwater_5"
    truecenter
    zoom 0.7
image ocean_6:
    "underwater_6"
    truecenter
    zoom 0.7
image ocean_7:
    "underwater_7"
    truecenter
    zoom 0.7

image ocean_8:
    "underwater_8"
    truecenter
    zoom 0.7

image oceanbonus_1:
    "underwater_bonus1"
    truecenter
    zoom 0.7

image oceanbonus_2:
    "underwater_bonus2"
    truecenter


image beach_1:
    "images/dates/funinthesun/Backgrounds only/fits_beach_1.png"
    truecenter
    zoom 0.5

image beach_2:
    "images/dates/funinthesun/Backgrounds only/fits_beach_2.jpg"
    truecenter
    zoom 0.4

image beach_3:
    "images/dates/funinthesun/Backgrounds only/fits_beach_3.jpg"
    truecenter
    zoom 0.7

image beach_4:
    "images/dates/funinthesun/Backgrounds only/fits_beach_4.jpg"
    truecenter
    zoom 0.5

image beach_5:
    "images/dates/funinthesun/Backgrounds only/fits_parasol.jpg"
    truecenter
    zoom 0.7

image beach_6:
    "images/dates/funinthesun/Backgrounds only/fits_sea.jpg"
    truecenter
    zoom 0.7

image beach_7:
    "images/dates/funinthesun/Backgrounds only/fits_star_sky.jpg"
    truecenter
    zoom 0.8

image beach_8:
    "images/dates/funinthesun/Backgrounds only/fits_white_room.png"
    truecenter
    zoom 0.3

image blasphemous_flan:
    "images/dates/funinthesun/Desserts/Coco_flan.png"
    xoffset 325
image churchill_slush:
    "images/dates/funinthesun/Desserts/Churchill_slush.png"
    xoffset 385
image pina_colada:
    "images/dates/funinthesun/Desserts/Pina_colada.png"
    xoffset 325

image y_cg2_bg:
    "images/cg/y_cg2_bg1.png"
image y_cg2_base:
    "images/cg/y_cg2_base.png"
image y_cg2_nochoc:
    "images/cg/y_cg2_nochoc.png"
    on hide:
        linear 0.5 alpha 0
image y_cg2_details:
    "images/cg/y_cg2_details.png"
    alpha 1.00
    6.0
    linear 1.0 alpha 0.35
    1.0
    linear 1.0 alpha 1.0
    repeat

image y_cg2_exp2:
    "images/cg/y_cg2_exp2.png"
    alpha 0
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0
image y_cg2_exp3:
    "images/cg/y_cg2_exp3.png"
    alpha 0
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0

image y_cg2_dust1:
    "images/cg/y_cg2_dust1.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        10.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 14.0 xoffset -100 yoffset 100
        repeat
image y_cg2_dust2:
    "images/cg/y_cg2_dust2.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        28.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 32.0 xoffset -100 yoffset 100
        repeat
image y_cg2_dust3:
    "images/cg/y_cg2_dust3.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        13.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 17.0 xoffset -100 yoffset 100
        repeat

image y_cg2_dust4:
    "images/cg/y_cg2_dust4.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        15.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 19.0 xoffset -100 yoffset 100
        repeat

image stroll_1 = "images/dreams/stroll_dream_1.png"
image stroll_2 = "images/dreams/stroll_dream_2.png"
image stroll_3 = "images/dreams/stroll_dream_3.png"
image stroll_4 = "images/dreams/stroll_dream_4.png"

####################
#Dream Menu Control#
####################
label dream_menu:
    if not renpy.seen_label('dream_menu_2'):
        $ DisableTalk()
        call showpoem(poem_sp5, music = False)
label dream_menu_2:
    $ Dream_type = "dream"
    jump dates_and_dreams_system
label nightmare_menu:
    $ DisableTalk()
    $ Dream_type = "nightmare"
    jump dates_and_dreams_system
label dates_menu:
    $ DisableTalk()
    $ Dream_type = "date"
    $ boopable = False
    $show_chr("A-ABAAA-ALAL")
    y "Oh, you want to take me out on a date? What a lovely idea!"
    $show_chr("A-CCAAA-ALAL")
    y "Please take a look at the locations I have prepared so far. Do any of them look appealing to you?"
    jump dates_and_dreams_system


#Have this ready for when Urban Cafe Date online
#$show_chr("A-ACAAA-ALAL")
#y "Oh yes! There is a very cute little café on this street. I would certainly enjoy trying it out with you."
#y "It would at the very least help me get some rest. My mind has been a bit... crowded lately."
#y "Shall we depart then?"


label dates_and_dreams_system:
    $ config.allow_skipping = False
    $ DisableTalk()
    $ boopable = False
    # Test list for dream. This might change to dictionary or however the dreams will be handled. (File name, label)
    python:
        dates_and_dreams = [
            # dreams
            ["rain_dream", "persistent.lovecheck and invariant_karma() > 3"],
            ["ocean_dream", "renpy.seen_label('rain_dream') and persistent.lovecheck and invariant_karma() > 3"],
            ["highway_dream", "renpy.seen_label('rain_dream') and persistent.lovecheck and invariant_karma() > 3"],
            ["stroll_dream", "renpy.seen_label('rain_dream') and persistent.lovecheck and invariant_karma() > 3"],

            # dates
            ["garden_date", "persistent.lovecheck and invariant_karma() > 3"],
            ["urban_date", "persistent.lovecheck and invariant_karma() > 3"],
            ["tropical_date", "persistent.lovecheck and invariant_karma() > 3"],
            ["vday_2024_date", "persistent.lovecheck and invariant_karma() > 3"]
            ]

    call screen dates_and_dreams(dates_and_dreams,Dream_type)#(persistent.memory)
    python:
        if _return != "None":
            renpy.jump(_return)
        allow_dialogue = True
    jump ch30_loop

#DREAM MENU SCREEN
define current_dream_chart = 0

image glitch_color_scaled:

    im.Scale("dreams/glitch_1.png", 290, 168)
    0.1
    im.Scale("dreams/glitch_2.png", 290, 168)
    0.1
    im.Scale("dreams/glitch_3.png", 290, 168)
    0.1
    repeat

screen dates_and_dreams(dict_items, type):
    fixed:
        python:
            #Split array of dreams for X 12 elements arrays as on screen will be avaible only 12 elements at once.
            split_dreams = []
            for i, dream in enumerate(dict_items):
                print(dream)
                if type in dream[0] and eval(dream[1]):
                    split_dreams.append(dream)
                    print("accepted")
                elif type in dream[0] and not eval(dream[1]):
                    split_dreams.append([dream[0],"glitch"])
                    print("rejected")
            split_dreams = split(split_dreams,12)
            # Variable pointing which part of dreams are showm
            def Move_left(dict_items):
                global current_dream_chart
                current_dream_chart-=1
                renpy.hide_screen("hello_world")
                renpy.show_screen("hello_world", dict_items)
            def Move_right(dict_items):
                global current_dream_chart
                current_dream_chart+=1
                renpy.hide_screen("hello_world")
                renpy.show_screen("hello_world", dict_items)

        for i, dream in enumerate(split_dreams[current_dream_chart]):

            imagebutton:
                xalign 0.05 + (i % 4) * 0.3
                yalign 0.1 + math.ceil(i/4) * 0.35
                if dream[1] != "glitch":
                    idle im.Scale(type + "s/Thumbnail/" + dream[0] + "_idle.png", 300, 168)
                    hover im.Scale(type + "s/Thumbnail/" + dream[0] + "_hover.png", 300, 168)
                    action Jump(dream[0])
                else:
                    idle LiveComposite((300, 168), (0,0), im.Scale(type + "s/Thumbnail/" + dream[0] + "_idle.png", 290, 168), (0, 0), "glitch_color_scaled")
                    hover LiveComposite((300, 168), (0,0), im.Scale(type + "s/Thumbnail/" + dream[0] + "_idle.png", 290, 168), (0, 0), "glitch_color_scaled")
            #if dream[1] != "glitch":
            #    text str(dream[0]) xalign 0.05 + (i % 4) * 0.243 yalign 0.1 + math.ceil(i/4) * 0.28


        #Arrow image buttons
        if(current_dream_chart<len(split_dreams)-1):
            imagebutton xalign 0.99 yalign 0.97 auto "gui/arrow_button_right_%s.png" action Function(Move_right, dict_items)
        if(current_dream_chart>0):
            imagebutton xalign 0.01 yalign 0.97 auto "gui/arrow_button_left_%s.png" action Function(Move_left, dict_items)

        textbutton "Back":
            xpos 585
            yalign 0.97
            style "scrollable_menu_button"
            action Return("None")

    #Assigne function to keybored buttons
    if(current_dream_chart>0):
        key "K_LEFT"  action Function(Move_left, dict_items)
        key "K_a"  action Function(Move_left, dict_items)
    if(current_dream_chart<len(split_dreams)-1):
        key "K_d" action Function(Move_right, dict_items)
        key "K_RIGHT" action Function(Move_right, dict_items)















###########
##DREAMS###
###########


label rain_dream:
    hide craneo
    hide roseo
    hide bunnyo
    hide raccoon
    hide diffuser
    hide hdy_statue
    hide cupcake_halloween
    $ config.allow_skipping = False
    stop music fadeout 1.5
    python:
        if persistent.male:
            pronounA = "him"
            pronounB = "he"
        elif persistent.gender_other:
            pronounA = "them"
            pronounB = "they"
        else:
            pronounA = "her"
            pronounB = "she"
        persistent.eyecolor = persistent.eyecolor.lower()
    show black zorder 105 with Dissolve (2.5)
    show rain_dream_blush zorder 100
    show rain_dream_blossom zorder 105
    $renpy.music.play("sfx/heartbeat_subtle.mp3", channel='sound', loop=True)
    $renpy.music.set_volume(0.1, 0, 'voice')
    stop music fadeout 1.5
    play music "<loop 4.50>music/teardrops_loop.ogg" fadein 1.5
    hide black with Dissolve(2.5)
    #The sequence opens with the CG - Yuri is staring out a window, waiting for the [player], when [player] arrives the two  simply just talk with one another. A teacup is held loosely in Yuri's hand - which is visible in said CG.
    "Lightly pattering against the window, rain slowly started to fall from the clouds above, acting as the only audible sound amidst the general silence."
    "Small droplets of precipitation tapped against the pane, seamlessly running down its length and proceeding to accumulate at the bottom, forming together into a small puddle and then falling down into the depths below."
    "My reflection momentarily flickers back at me, only to be drowned out by that pattering melody before me without a thought or even a whisper said between us."
    "I loosely hung a teacup betwixt my thumb and forefinger, filled almost to the brim with some Pouchong Oolong tea, an enjoyably smooth relaxant."
    "A strong floral aroma wafted its way through my system, quickly calming my entire body with its sensual fragrance, almost like an anesthetic."
    "Holding it up to my lips, I indulged myself in a few quick sips, taking specific note of the rich melony taste it provided."
    "The only thing missing from this near perfect scenario was the sharp earthiness of a peanut butter crepe to nicely contrast the light sweetness of the tea."
    show rain_dream_smile zorder 100 with Dissolve(0.5)
    hide rain_dream_blush
    "...{w=1.0} well...{w=0.4} that and... {w=0.4}{i}[pronounA]...{/i}"
    "The mere thought of their presence managed to send shock waves of nervousness mixed with a cruel sense of excitement throughout my body... {w=.2}just the single mention of [pronounA] sent my consciousness into a state of flustered panic."
    show rain_dream_blush zorder 100 with Dissolve(0.5)
    hide rain_dream_smile
    "I-{w=0.3}it was pathetic... {w=0.4}yet... {w=0.4}It felt all too right."
    "Despite my hopes... {w=0.4}I never quite bought the way romance novels managed to describe the feeling... {w=0.4}However, finding myself in quite the same situation, I was forced to resign my dignity and appreciate just how correct they truly were."
    "The feeling of pure euphoria rushing through each and every nerve in my body... {w=0.4}the simple quickening of my heartbeat as shots of adrenaline coursed through my veins whenever [pronounB] got close."
    "Sometimes... {w=0.4}I think I might die from the way [pronounB] makes me feel. In the past, I found myself bound by Monika's manipulation... {w=0.4}forced to feel such an intense, burning passion that it brought me to commit... {w=0.5}unspeakable acts."
    "Yet here I am, without Monika's influence and I find myself feeling much the same... {w=0.4}Oh... {w=0.4}how I just wish to bask in their presence... {w=0.4}feeling their warmth as we both slowly let our dignities slip and indulge ourselves with hidden... {w=0.4}more... {w=0.4}carnal desires..."
    "..."
    "... {w=0.4}e{w=0.3}-enough of that..."
    "Rather than spend the night getting lost in wild fantasies of secret pleasures, I redirected my attention back to the rain, trying to calm this intense feeling of anticipation in my system."
    "One could probably liken the falling of raindrops much to the trivialities of day to day life, each droplet representative of the different paths we may take."
    "Mainly leading a solitary road but having these rare few moments where their paths intertwine...{w=0.4} some drifting apart and others remaining tangled forever. It felt almost romantic in a rather sombre fashion."
    "Even so, there was a small amount of comfort from knowing whatever road they might have chosen...{w=0.4} in the end, they all manage to find one another and face whatever might come next as a collective, rather than a singular entity."
    "I watch this process much like a ghost, unable to fully interact...{w=0.4} only able to watch; separated from it all by a transparent barrier, forced into the role of an onlooker and nothing more. Loneliness truly was the most vulnerable of emotions..."
    "Always never quite able to intermingle... forced into the solitary role."
    "At least, that's what would be the occasion on most nights."
    show rain_dream_smile zorder 100 with Dissolve(0.5)
    hide rain_dream_blush
    "But tonight..?{w=0.3} Tonight...{w=0.4} I would be with {i}[pronounA].{/i}"
    "Turning my head, I see [pronounA] walk into the room and I could swear the room started spinning slightly as my heart resembles more a drum than a human organ."
    "In their hands held another teacup - which I could quickly distinguish to be Pouchong Oolong tea from its unique floral smell."
    "Sitting beside me, [pronounB] gives me a warm smile and I feel that same nervous sensation seize me. Waves of heat wash over me and as [pronounB] moves closer towards me I found their scent managing to easily overpower that of the tea."
    $renpy.music.set_volume(0.4, 0, 'voice')
    "{i}Ba-dump, ba-dump, ba-dump.{/i}"
    "The drums resound in my ears, it's rhythm fast but steady, chanting out in a chorus that sings ballads of affection and infatuation."
    "Glancing down at [pronounA], I momentarily smile as I compare myself to the other side of the window. Knowing how lucky I was to find myself someone I could intertwine with."
    "The best part? Unlike those raindrops, we would remain tangled together."
    "[player] peers out the windows for a moment, then speaks softly, their voice barely louder than a whisper."
    mc "It's really coming down tonight, isn't it?"
    menu:
        "Thank God I'm inside... safe with you.":
            mc "Thank God I'm inside... safe with you."
            show rain_dream_grin zorder 100 with Dissolve(0.5)
            hide rain_dream_smile
            y "Yes...{w=0.4} it's quite comforting knowing we're sheltered from the harsh outside for the time being."
            y "Though it does raise a thought... what's happening to the people who aren't sheltered?"
            y "The hidden members of our society. People who we know exist yet for the most part refuse to acknowledge."
            y "They're out there...{w=0.4} dealing with the horrible cold and the endless assault of rain."
            y "Meanwhile the rest of the world is huddled up, not thinking about them for more than a second."
            mc "Why are you talking about the homeless, [persistent.yuri_nickname]? It's not something I'd expect you to discuss."
            show rain_dream_blush zorder 100 with Dissolve(0.5)
            hide rain_dream_grin
            y "I guess...{w=0.4} I sympathize with them?"
            y "Most people out there have no way out...{w=0.4} they're degraded to the point where they can barely interact with the people around them."
            mc "Much like the raindrops outside..."
            y "Mm...{w=0.3} it just...{w=0.4} reminds me a lot of how I felt back when I was first in that game..."
            y "Trapped. Forced into a situation I didn't have control over. Barely able to interact with the things around me, let alone interact with people."
            mc "It...{w=0.4} must have been horrible for you, [persistent.yuri_nickname]."
            y "Luckily I had you, [player]. I don't know what I'd have done without you being there..."
            y "You might not know this... but having someone to talk to can really save you."
            y "So please, if you see someone out there with nowhere to go or no one to call a friend...{w=0.4} just reach out to them."
            y "You can make the world so much better that way..."
            menu:
                "I will, [persistent.yuri_nickname].":
                    mc "I will, [persistent.yuri_nickname]."
                    show rain_dream_smile zorder 100 with Dissolve(0.5)
                    hide rain_dream_blush
                    y "Thank you, darling."
                    y "You truly are the most considerate person I know..."
                "I can try.":
                    mc "I can try."
                    show rain_dream_smile zorder 100 with Dissolve(0.5)
                    hide rain_dream_blush
                    y "That makes me happy to hear, [player]."
                "I'll do my best.":
                    mc "I'll do my best."
                    show rain_dream_smile zorder 100 with Dissolve(0.5)
                    hide rain_dream_blush
                    y "That's all I'll ever need, my dear."

        "What a perfect moment we're able to share together...":
            mc "What a perfect moment we're able to share together..."
            show rain_dream_grin zorder 100 with Dissolve(0.5)
            hide rain_dream_smile
            y "It's almost like a page out of a story, isn't it?"
            mc "Our happily ever after?"
            "Nodding happily, I move closer to [player], resting my cheek against their shoulder."
            y "Considering my previous situation... would it really be all that odd to entertain the thought our sentience might consist entirely within some sort of medium?"
            y "Like another game, or a movie...{w=0.4} or a book?"
            menu:
                "Even if it was, does that undermine our experiences together?":
                    mc "Even if it was, does that undermine our experiences together?"
                    mc "I know the emotions I feel for you are true - even if only to myself."
                    mc "Therefore, even if our lives were entirely within some sort of storybook...{w=0.4} would that really change anything?"
                    pause 2.0
                    show rain_dream_smile zorder 100 with Dissolve(0.5)
                    hide rain_dream_grin
                    y "...{w=0.4} I suppose not. That's quite an interesting way to view that situation, [player]."
                    y "It would provide an answer to the reality of the world we live in, I suppose. But I guess even then there wouldn't be a need for an existential breakdown."
                    y "I believe it was philosopher René Descartes who said 'I think, therefore I am'. Wherein our sentience is defined by our ability of free thought - acting outside of our basic functions."
                    y "So even if we were within some sort of book - we're still sentient."
                    mc "It's still an interesting concept though - the idea our lives consist entirely within a form of entertainment..."
                    y "Perhaps one could argue it's prideful to believe such a thing, however? The idea that we're a protagonist of a story - or some sort of major character in a plot."
                    mc "Potentially. However when you consider the possibility of how many books there are out there, however many major characters within each book there might be, doesn't the status of 'Protagonist' become entirely meaningless?"
                    y "Hmm...{w=0.4} that leads to some rather interesting thoughts...{w=0.4} for example - are the books we read realities within themselves?"
                    y "Maybe if we look at this concept inside out...{w=0.4} and argue that rather than realities existing from books, that books can simply tell the story of an already existing reality, the idea doesn't sound too far-fetched then?"
                    mc "Considering the theory of there being an infinite amount of different realities, that might be closer to the truth than we might realize."
                    show rain_dream_grin zorder 100 with Dissolve(0.5)
                    hide rain_dream_smile
                    y "Exactly! Oh, [player]...{w=0.4} thank you so much for indulging this thought of mine. I love it that you're able to appreciate my ramblings..."
                    mc "Anytime, my love."
                "Then that means other people can bear witness to our love.":
                    mc "Then that means other people can bear witness to our love."
                    y "Afufu.~ You're sounding a little like an exhibitionist, dear."
                    y "Still... I'm not entirely sure how I feel about my most private moments being on public display."
                    mc "It would be a little creepy, I'll admit."
                    mc "Having someone be able to so easily unravel your deepest fears and desires - without even being able to give a single input on the situation."
                    show rain_dream_smile zorder 100 with Dissolve(0.5)
                    hide rain_dream_grin
                    y "I'm glad you understand, [player]..."
                    y "I'll be honest, considering the situation I was in previously... I was really worried something would happen which meant you had unrestricted access to all my private thoughts and feelings..."
                    y "I couldn't help but think what you might have control over behind the scenes."
                    y "Part of me would've been angry... but I guess part of me wouldn't have blamed you."
                    show rain_dream_blush zorder 100 with Dissolve(0.5)
                    hide rain_dream_smile
                    y "If I were in that situation... I know I'd be tampering with everything."
                    y "Power corrupts, I suppose."
                    y "As long as you weren't delving too deep, I guess I'd have been fine, my love."
                "Seems a little far-fetched if I'm being honest, [persistent.yuri_nickname].":
                    mc "Seems a little far-fetched if I'm being honest, [persistent.yuri_nickname]."
                    show rain_dream_blush zorder 100 with Dissolve(0.5)
                    hide rain_dream_grin
                    y "Really? I thought otherwise, considering that I was originally a character in a game, who proceeded to become a character in a mod of said game, then to become a person within your reality."
                    y "At this point is it really that much of a stretch to assume that maybe this world we live in is also some sort of medium?"
                    y "Nonetheless... I'm alright as long as I'm with you, my love."

        "Makes me want to huddle closer to you... reside in your warmth.":
            mc "Makes me want to huddle closer to you... reside in your warmth."
            y "Oh? In which case... do come closer. I'm here to keep you safe and warm, darling."
            "[player] quickly takes the opportunity to pull me closer to [pronounA], wrapping a protective arm around me and smiling to themselves."

    $renpy.music.set_volume(0.4, 0, 'voice')
    show rain_dream_blush zorder 100 with Dissolve(0.5)
    hide rain_dream_grin
    "{i}Ba-dump,{w=0.4} ba-dump,{w=0.4} {cps=*1.25}ba-dum ba-dum ba-dum ba-dump-dump{/cps}{/i}"
    "We sit in silence for a few minutes, taking sips of our tea and enjoying the light sound of rain hitting against the window."
    "W-{w=0.3}well...{w=0.4} I would have been enjoying the sound if it weren't for the fact that the damned drum was still resounding out into my ears!"
    y "H-{w=0.3}Hey...{w=0.4} [player]."
    "They look from the window, then down at me, a slight smile on display at their lips."
    mc "Yes, dear?"
    y "I've been...{w=0.4} thinking recently. It's about the concept of love."
    y "What actually is love?"
    y "Is it chemical? Is it spiritual? Is it unique to humans, or is it prevalent in every creature?"
    y "Some would argue love is spiritual...{w=0.4} that it cannot be defined by simple chemicals."
    y "That love is a spiritual concept completely larger than life itself."
    y "Others however would argue that love is chemical. That it's simply hormonal reactions to the body's need to mate combined with the mind's want to interact with people."
    y "Does the idea of love being chemical ruin the idea of love, though?"
    y "We've elevated the intense emotion of love onto such a pedestal, one could raise the question of whether love being chemical ruins the ideology behind it."
    y "But if it is a spiritual concept, what's the criteria for feeling love? Do insects feel love? Does being sentient mean that you're applicable for feeling love?"
    y "What do you think, [player]?"
    menu:
        "Love is chemical.":
            mc "Love is chemical."
            mc "I don't think love needs to be one large grandiose emotion that we can't comprehend, personally."
            mc "I like the idea of it simply being chemical. There's satisfaction behind the idea of it being more...{w=0.4} human?"
            mc "I don't think it ruins the idea of it, per se."
            mc "As long as the feeling is still prevalent, then I'm content."
            show rain_dream_smile zorder 100 with Dissolve(0.5)
            hide rain_dream_blush
            y "That's a rather mature way to view it, [player]."
            y "Personally I like to think it's a mixture between chemical and spiritual."
            y "You're right in the idea that as long as the feeling is prevalent, people should be content, though."
            y "I do love our conversations, [player]..."
        "Love is spiritual.":
            mc "Love is spiritual."
            mc "Why do you think it's a topic so many writers are drawn to?"
            mc "Shakespeare, romantic poetry..."
            mc "It comes in so many different forms, and dawns on people in so many separate ways."
            mc "Love being chemical can't explain that, I think."
            mc "It is easily the strongest emotion someone can feel, it can make or break someone's whole life if they feel it strongly enough."
            show rain_dream_smile zorder 100 with Dissolve(0.5)
            hide rain_dream_blush
            y "I see...{w=0.4} that's quite an idealistic approach to the topic. I do like to think it's a little larger than us in some sort of way."
            y "However I also do believe there's a dash of chemistry to the concept of love as well."
            y "No matter what the answer might be, my love for you will never dull, [player]."
        "Love is both spiritual and chemical.":
            mc "Love is both spiritual and chemical."
            mc "On the one hand, I feel like the idea of love being a mix of our want to mate, sexual desire, and our want to interact, romantic affection, certainly play a hand in love."
            mc "However it also makes sense to believe there's something more to it, something we might not be able to explain through regular means."
            mc "It's...{w=0.4} down to earth yet complex at the same time."
            show rain_dream_grin zorder 100 with Dissolve(0.5)
            hide rain_dream_blush
            y "Ah! That's exactly how I view it, [player]."
            y "I personally like to think that love is a mixture between chemical and spiritual."
            y "It answers a lot of my questions and gives the most satisfying answer, I think."
            y "Seems we really are connected, [player]."
    "After our discussion, we resume watching the droplets fall down the length of the pane."
    "Soon enough, we find we've both finished our tea, and thus we place our teacups aside and huddle closer together."
    "{i}Ba-dump, ba-dump, ba-dump.{/i}"
    "The drums play softly in the background, and the familiar aroma of jasmine oil starts to waft into my nose."
    show rain_dream_blush zorder 100 with Dissolve(0.5)
    hide rain_dream_grin
    hide rain_dream_smile
    y "D-{w=0.3}Did you...?"
    mc "Mhm...{w=0.4} I put some in the diffuser as I came in..."
    "Slowly, I recollect the first time I'd used jasmine oil around [player]...{w=0.4} back before the festival."
    "Before I was aware of the horrors of the reality I once lived in."
    "Th-{w=0.3}the towel...{w=0.4} that...{w=0.4} warmness against my cheek that dragged me into a state of such security."
    "Another wave of familiarity hits me as I compare the warmness back then to the current feeling I was experiencing right now, with [player] against me..."
    $renpy.music.set_volume(0.6, 0, 'voice')
    "{b}{i}BA-DUMP.{w=1} BA-DUMP.{w=1} BA-DUMP.{w=1}{/i}{/b}"
    "My eyes slowly drifted to [player]'s lips. The quick and frantic beat of the drum that I'd grown accustomed to had shifted into a slow, but loud beat - the song of anticipation."
    "...{w=0.4} I{w=0.3}-If I could just--{nw}"
    mc "I'll go make us some more tea."
    "Wait, what?"
    y "N-{w=0.3}No!"
    "As [pronounB] got up, instincts took over and I reached out to grab [pronounA], latching onto their arm and yanking them back."
    "However as I pulled [pronounA] back onto me, I lost my footing and slipped. Causing the two of us to careen back..."
    show black zorder 100
    hide rain_dream_blossom
    play sound "<to 0.3>sfx/fall.ogg"
    "{b}THUNK{/b}"
    "{w=0.5}...{w=0.4} with me sprawled out on the couch, and [player] on top of me."
    "..."
    pause 5.0
    "Both of us pause for a few seconds, as if needing that time to correctly process what was going on."
    $renpy.music.set_volume(0.5, 0, 'voice')
    "The mixture of jasmine oil combined with [player]'s scent and this overwhelming warmth completely fried my thoughts in a sensory overload."
    "Without thinking, I coil my arms around their neck and pull [pronounA] in closer, to the point where our lips are touching."
    if persistent.eyecolor == "other":
        "Staring into their eyes, a sly grin emerges and I chuckle softly."
    else:
        "Staring into their [persistent.eyecolor] eyes, a sly grin emerges and I chuckle softy."
    $renpy.music.set_volume(0.4, 0, 'voice')
    y "S{w=0.3}-Sorry [player], I just can't control myself when I'm with you."
    mc "[persistent.yuri_nickname]..."
    "Our lips embrace, and with that all background noise is reduced to null - the soft patter of the rain and our pants and moans all became solitary whispers."
    $renpy.music.set_volume(0.3, 0, 'voice')
    "{i}ba-dump...{w=0.5} ba-dump...{w=0.5} ba-dump...{w=0.5}{/i}"
    "The only thing I could hear was the faint, resigned drum."
    "An overwhelming warmth fills my entire body as I call out their name."
    y "[player]...{w=0.4} [player], I love you... {cps=*1.5}I love you, I love you, I love you!{/cps}"
    "My fingers intertwine with theirs and I move their hand to my chest."
    y "[player]! Feel the beat of my heart...{w=0.4} it sings for you and you alone. A song only you and I can hear."
    mc "[persistent.yuri_nickname]!"
    "They cry out my name, and wrap their arms around my body, holding me firmly in their clutches."
    y "[player]...{w=0.4} I love you...{w=0.4} p-{w=0.3}please don't ever let me go..."
    y "If you keep me held forever...{w=0.4} my heart will always sing for you."
    mc "I will never leave you [persistent.yuri_nickname]..."
    show white zorder 105 with Dissolve(2.5)
    hide black
    hide rain_dream_blush
    hide rain_dream_smile
    hide rain_dream_grin
    mc "I will never leave..."
    stop sound fadeout 1.5
    stop music fadeout 1.5
    # Fade to white
    # DREAM END
    hide white with Dissolve(2.5)
    python:
        renpy.music.play(current_music, "music", True)
    jump ch30_loop

label ocean_dream:
    hide craneo
    hide roseo
    hide bunnyo
    hide raccoon
    hide diffuser
    hide hdy_statue
    hide cupcake_halloween
    $ config.allow_skipping = False
    stop music fadeout 1.5
    play music "<to 96.30 loop 32.30>music/Underwater_Dream.ogg" fadein 1.5
    show black zorder 105 with Dissolve (2.5)
    show open_ocean zorder 100
    hide black with Dissolve(2.5)
    #The sequence opens with the CG - Yuri is staring out a window, waiting for the [player], when [player] arrives the two  simply just talk with one another. A teacup is held loosely in Yuri's hand - which is visible in said CG.
    y "So gentle... I can hear the soft waves whispering lovely things into my ears.. as the water flows so warmly over my skin..."
    y "This is where life once began, from organisms so small that they can see a single grain of sand..."
    y "The sunlight, shrouded from the water around me, but still so bright that it hurts in my eyes..."
    y "My heart beats slow... but still so full of life that I can hear it pounding... have I ever felt this way before?..."
    y "All the decadence I have indulged in, all the pleasures I have forced upon myself, but here I am and I find myself unable to do much else but marvel at such beauty..."
    y "It is astounding, how pretty the world can be if it is untouched by mankind..."
    y "My life amongst them made me see the world in shades of grey, but here I feel as if I can see the colors for the first time in my life..."
    y "How much I would love to stay, but there is so much more to see..."
    y "Maybe I should indulge myself further... just this once... towards the fantastic wonders I've yet to witness in this realm."
    #Yuri is not aware that anyone is watching her dream, it's entirely a process in her head.
    show ocean_2 zorder 100 with Fade(1.0, 0.5, 0.5)
    hide open_ocean
    y "Uhuhuhu... like a little underwater town..."
    y "Actually, maybe I'm not incorrect to assume that places like this are home to many creatures?"
    y "Maybe I can take a little peek, just a look..."
    y "Just to see which lovely creatures made this place their home..."
    y "The water feels so calm... I can almost feel all the stress and the pressure floating away..."
    y "My eyes used to feel so heavy from the reading and sometimes the lack of sleep, but now I feel awake and so alive."
    y "My back used to hurt from the burden of my body, but now I feel so agile and as fresh as the early morning."
    y "My mind was once in turmoil like a flickering light, from racing thoughts and unstable emotions..."
    y "But now, it feels like all my burdens are just washed away by the waves..."
    y "I can feel the vibrations in the water around me... all the noises from the world above have been replaced by the gentle whispering of the sea..."
    y "It is as if I always belonged here... as if I were misplaced in the other world, I always felt like that anyway..."
    y "Maybe here I can find the place I have been denied above..."
    show ocean_3 zorder 100 with Fade(1.0, 0.5, 0.5)
    hide ocean_2
    y "It almost feels like flying through the skies, but instead of the wind howling through my hair I feel nothing but the salty water washing over me..."
    y "Even when the waves are raging on the surface, down below the water feels so calm and gentle."
    y "The cycle of life feels just so perfect here... even with all the creatures feasting upon the plants, there seems to never be a lack of them..."
    y "And they are just so wonderful. Maybe I should build my home inside of them, like many other fishes do..."
    y "Or maybe... I could take a tiny little bite... just a little nibble to quench my appetite..."
    y "So simple, but it tastes as if I never needed anything else... maybe those would go along just fine with Oolong Tea..."
    y "Huuh... I think I..."
    y "Saw something..."
    show ocean_4 zorder 100 with Fade(1.0, 0.5, 0.5)
    hide ocean_3
    y "O~Oh my..."
    y "Hello there, little friends... would you like to join my literature club?"
    python:
        if persistent.lovecheck:
            placeholder = "cute"
        else:
            placeholder = "fellow"
    y "It is just me, and my [placeholder] [player]..."
    y "We would have to flood the classroom but... I doubt [player] would mind it..."
    y "All the deep and intriguing poems we could make about these lovely tides you share..."
    y "Oh... Or did I... interrupt you? Were you about to..."
    y "Nevermind... forgive me, little friends, I will leave you alone in peace again. Farewell..."
    show ocean_5 zorder 100 with Fade(1.0, 0.0, 0.5)
    hide ocean_4
    y "And so I dive deeper into the seemingly endless void... wondering about the things I might see down there..."
    y "I am no stranger to the dark... and I can only giggle in delight about the secrets such a place might hold..."
    y "Or the eldritch horrors one could see below..."
    y "Perhaps, there is a bottom after all..."
    show ocean_6 zorder 100 with Fade(1.0, 0.0, 0.5)
    hide ocean_5
    y "The deeper I dive, the colder it becomes... but still, it fills my heart with so much warmth.."
    y "How petite and pretty... even in the dark one could find such... such... I can't even find the proper words for it..."
    y "Maybe words are just not suited to describe this level of finesse, maybe that is the reason why the deeps do not carry one's voice..."
    y "But now I miss the warmth of the sun, so I shall carry on and see where the waves might take me..."
    show ocean_7 zorder 100 with Fade(1.0, 0.0, 0.5)
    hide ocean_6
    y "Maybe just... a little peek..."
    show ocean_8 zorder 100 with Fade(1.0, 0.0, 0.5)
    hide ocean_7
    y "On the world above again...."
    if renpy.random.randint(0,4)==0:
        show oceanbonus_1 zorder 100 with Fade(1.0, 0.0, 0.5)
        hide ocean_8
        y "Wait no! Please don't. Please let me go! This can't be how my journey ends, this can not..."
        show oceanbonus_2 zorder 100 #with Fade (1.0, 0.0, 0.5)
        hide oceanbonus_1
        stop sound fadeout 1.5
        stop music fadeout 1.5
        $ renpy.pause ()
        hide oceanbonus_2 with Dissolve(6)#2.5)
    else:
        show black zorder 105 with Dissolve(2.5)
        hide ocean_8
        stop sound fadeout 1.5
        stop music fadeout 1.5
        hide black with Dissolve(2.5)
    python:
        renpy.music.play(current_music, "music", True)
    jump ch30_loop

label ocean_man: #take me by the hand
    show oceanbonus_1 zorder 100 with Fade(1.0, 0.0, 0.5)
    hide ocean_8
    y "Wait no! Please don't. Please let me go! This can't be how my journey ends, this can not..."
    show oceanbonus_2 zorder 100 #with Fade (1.0, 0.0, 0.5)
    hide oceanbonus_1
    stop sound fadeout 1.5
    stop music fadeout 1.5
    $ renpy.pause ()
    hide oceanbonus_2 with Dissolve(6)#2.5)
    return

label highway_dream:
    hide craneo
    hide roseo
    hide bunnyo
    hide raccoon
    hide diffuser
    hide hdy_statue
    hide cupcake_halloween
    image highway_bg_scroll:
        "images/dreams/highway/highway_bg_loop_filtered.png"
        xtile 3 subpixel True
        block:
            xoffset -10936
            linear 40 xoffset 0
            repeat
    image highway_yuri_car:
        "images/dreams/highway/highway_yuri.png"
        zoom 0.27
    define martha = Character("Martha")
    $ config.allow_skipping = False
    stop music fadeout 1.5
    play music "music/Cruise_Control_RC.ogg" fadein 1.5
    show black zorder 105 with Dissolve (2.5)
    show highway_bg_scroll zorder 100
    show highway_yuri_car zorder 100
    python:
        import random
        highway_dream_path = random.randint(1, 4)
        highway_dream_path_2 = random.randint(1, 2)
        if persistent.male:
            pronounA = "him"
            pronounB = "he"
            pronounBC = "He"
            pronounC = "his"
            pronounD = "boyfriend"
        elif persistent.gender_other:
            pronounA = "them"
            pronounB = "they"
            pronounBC = "They"
            pronounC = "their"
            pronounD = "lover"
        else:
            pronounA = "her"
            pronounB = "she"
            pronounBC = "She"
            pronounC = "her"
            pronounD = "girlfriend"
    if persistent.highway_dream_complete:
        y "Ah. I've had this dream before! I've a chance to do some lucid dreaming!"
        menu:
            "I'd like to see something beautiful":
                python:
                    highway_dream_path = 1
            "Do I smell smoke?":
                python:
                    highway_dream_path = 2
            "I think I'd like to stretch my legs":
                python:
                    highway_dream_path = 3
            "Oh dear. It's looking like rain...":
                python:
                    highway_dream_path = 4
            "Actually, let's just see where fate takes us":
                $pass
    hide black with Dissolve(2.5)
    "The sun shines down on the three of us. Me, [player], and the wide open highway."
    "Before now, I never really understood the appeal of a convertible. But now that the countryside is soaring past; now that the wind is blowing freely through my hair..."
    "The sheer joy of liberation is intoxicating."
    "I'm glad [player] has the driving part of this handled. I needn't concern myself with the rules of the road. No speed limits, no overtaking more sluggish vehicles, no speedometer to divert my attention from the beauty of this; my Arcadia."
    "It occurs to me that I've no recollection of what our destination is this gorgeous afternoon."
    "But honestly, does it matter? Wherever we may wind up, [player] will be there with me, sharing every moment."
    "And wherever we end up, it {i}won't{/i} be that dreadful classroom I've spent far too much time trapped within."
    "So, I'm sure I'll enjoy it."
    #[This is where an element of random chance comes in]
    $renpy.call("highway_dream_" + str(highway_dream_path))
    if highway_dream_path == 1:
        call highway_dream_1
    elif highway_dream_path == 2:
        call highway_dream_2
    elif highway_dream_path == 3:
        call highway_dream_3
    elif highway_dream_path == 4:
        call highway_dream_4
    jump ch30_loop

#[Result 1: "Let's check out that scenic overlook!"]
label highway_dream_1:
    mc "Hey, [y]."
    "[pronounB] says my name. The tone of it suggests that [pronounB]'s seen something [pronounB] thinks I'd be interested in."
    y "Yes, dear?"
    "[player] points to a sign passing to our right. I have just enough time to read the words 'SCENIC OVERLOOK' before it passes us by."
    "Much like a hundred other things I hadn't even noticed passing."
    mc "Want to go give that a look? It's not coming up at the very next exit, but we'd better figure it out now."
    "Well, we don't have anywhere we need to be, do we? That was kind of the whole point of our little excursion."
    "For once, the answer to a question comes quite easily to me."
    y "Certainly! There's no such thing as too much beauty in your life, is there?"
    "[player] chuckles. I'm not so certain what's funny about what I said, but-"
    mc "I love the way you think, [y]. I could just put that thought in a frame and hang it over the mantle."
    "Ah, there it is."
    show highway_dream_1 zorder 100 with Dissolve (1.0)
    hide highway_bg_scroll
    hide highway_yuri_car
    #[Transition to the scenic overlook. By the logic of dreams, they simply arrive at their destination without having to show every little detail of the journey over.]
    "I must say, they certainly picked the perfect place to set up a scenic overlook."
    "It stands at one end of a vast, arboreal valley. At the other, a great, sprawling mountain ridge towers into the sky."
    "In the center a river, briefly interrupted by a lake, flows by."
    "The ageless sculptor of this scene, still sitting as the centerpiece."
    "I can only imagine how much change this river was here to witness. Untold numbers of forgotten human struggles, natural disasters. The birth and death of the trees it nourished."
    "Perhaps even the march of evolution itself."
    "And through it all, the river continued to flow. West to east, every day without cessation. Perhaps the river has swelled or shrunk, but here it remains to this day."
    "It makes my life seem so tragically short by comparison. Yet at the same time, it puts my troubles into perspective."
    "If this river could keep flowing in face of more troubles than even humanity at large can even remember, then who's to say that I can't continue my own proverbial flow through the troubles that surround me?"
    mc "You look pretty deep in thought, [y]."
    mc "Then again, you usually are, aren't you?"
    "[player]'s voice breaks me from my reverie, but it's a gentle break, so I don't mind."
    y "Just enjoying the beauty is all."
    mc "Yeah? Well..."
    mc "Me too."
    "[player] says that with [pronounC] eyes on me, rather than on the overlook."
    "Did [pronounB] just..."
    "I must say. [player] can be quite smooth when [pronounB] wants to be."
    mc "Hey, want to take a picture together? The two of us, in front of this?"
    "That does sound like an excellent way to commemorate this small moment. We might just have to get this photo framed."
    y "Without a doubt, [player]."
    show black zorder 105 with Dissolve (2.5)
    stop sound fadeout 1.5
    stop music fadeout 1.5
    python:
        renpy.music.play(current_music, "music", True)
    hide highway_dream_1
    hide black with Dissolve(2.5)
    $persistent.highway_dream_complete = True
    jump ch30_loop



#[Result 2: "[player], why is there smoke coming from under the hood?"]
label highway_dream_2:
    "..."
    stop music
    play sound "sfx/highway/recordscratch.ogg"
    "The scent of something burning breaks me from my reverie."
    "Not the pleasant kind, such as incense or firewood. But the noxious smell of burning machinery and industrial fluid. The sort of burning that is almost always a sign of something terrible to come."
    y "[stutter_player]...?"
    "Right as I say [pronounC] name, smoke issues forth from beneath the hood."
    mc "Oh, god {i}dammit!{/i}"
    #[transition to a shot of Yuri in front of the car, watching the smoke rise.]
    "[player] hastily pulls our car over to the side of the road. With the ignition off, [pronounB] unfastens the hood, but to my surprise, doesn't actually open it all the way."
    "I put my hand near the hood, and the radiant heat quickly demonstrates to me why [pronounB] didn't."
    "A quick visual check yields no sign that I'd burned myself. But when my gaze returns to our car, I see that the hood has opened of its own accord."
    show highway_dream_2 zorder 100 with Dissolve (1.0)
    hide highway_bg_scroll
    hide highway_yuri_car
    #play sound "sfx/highway/overheat-begin.ogg"
    $renpy.music.play("sfx/highway/overheat-loop.ogg", channel='sound', loop=True)
    "Some sort of motorization, perhaps? I know precious little about cars."
    "And perhaps because of how little I know, this seems like the sort of situation where fear would be warranted. But I don't see any in [player]."
    "[pronounBC] looks much more annoyed than anything. When [pronounB] drops [pronounC] head between [pronounC] thumb and forefinger, I know that his annoyance is pointed inward."
    mc "This is my fault. This is entirely my fault."
    y "Now [player], can you really blame yourself for a mechanical failure?"
    mc "I can. I forgot to check the coolant level before we left."
    "Oh dear... That certainly does sound like something I'd kick myself over. I've no idea just how much damage an overheat can cause."
    "With the way [player] pinches [pronounC] nose and groans, I can tell this is really beginning to bother [pronounA]. I can't just leave [pronounA] to his self flagellation..."
    show black zorder 105 with Dissolve (2.5)
    play sound "<to 0.3>sfx/fall.ogg"
    "So I pull [pronounA] into my embrace."
    y "If it's any comfort, I'm not angry with you, dear."
    mc "I'm angry with myself."
    mc "I was going to take you somewhere nice. I didn't know where, but nicer than the side of a highway!"
    y "Don't worry about that. It's okay if we just go to a service shop's waiting room. As long as we're out together, mission accomplished."
    mc "Service shop... right! Thank you for reminding me."
    "[player] gently pulls a hand free of my hug so that [pronounB] can retrieve [pronounC] phone. But as [pronounB] searches for the number of a nearby mechanic's shop, I keep my arms around [pronounA]. We could both use one another's calming presence right now."
    "..."
    y "[player]?"
    "I catch [pronounA] saying 'hold on' to the person on the other end."
    mc "Yeah?"
    y "I love you..."
    stop sound fadeout 1.5
    stop music fadeout 1.5
    python:
        renpy.music.play(current_music, "music", True)
    hide highway_dream_2
    hide black with Dissolve(2.5)
    $persistent.highway_dream_complete = True
    jump ch30_loop


#[Result 3: "We're going to need gas soon, and the station might have a knife case for you to ogle"]
label highway_dream_3:
    mc "Hm... We're going to need gas soon."
    y "Oh?"
    "I lean back in an attempt to see the car's instrumentation. Sun glare thwarts this attempt, so I simply take [player]'s word for it."
    "A gas station certainly wasn't what I had in mind for our eventual destination, but it shouldn't take more than a few minutes."
    "It would be nice to stretch my legs, though."
    mc "And gas stations {i}usually{/i} have a little convenience store attached to them. Want to come have a look?"
    "I don't know about that."
    "A gas station convenience store doesn't seem like it would carry the sort of fare I'm interested in eating..."
    y "I think I'll be alright, thank you."
    mc "You sure? A lot of the convenience stores I've been to also have a little display of knives for sale."
    "Now {i}that{/i} piques my interest."
    y "Do they?"
    mc "Yeah. No idea if they're any good. I was hoping you could be the judge of that."
    "Alright. That changes everything. If nothing else, I get to experience some novelty."
    y "Okay, darling. I can do that for you."
    show highway_dream_3 zorder 100 with Dissolve (1.0)
    hide highway_bg_scroll
    hide highway_yuri_car
    #[Transition to a BG within said gas station convenience store. Something akin to pic related]
    "We arrive at the fabled gas station, and its age certainly shows."
    "Linoleum flooring that's clearly seen better days; wood paneled walls that have been the battleground between cigarette stainage and detergents for quite some time. Probably decades longer than I've been around."
    "I have to wonder how many generations of young couples have come through here through the years; just to browse the wares. How many product launches and discontinuations have populated these modular, press board shelves."
    "Then, right at the clerk's counter, I see it."
    show highway_dream_knives zorder 100 with Dissolve (1.0)
    hide highway_dream_3
    "A rotating glass display, within which is a broad variety of knives."
    if persistent.highway_dream_complete:
        menu:
            "I'll indulge myself in a happy ending":
                python:
                    highway_dream_path_2 = 1
            "I wonder how weird this can get":
                python:
                    highway_dream_path_2 = 2
            "I eagerly await the surprises of my own mind":
                python:
                    highway_dream_path_2 = renpy.random.randint(1,2)
    #[Result 3a: Frustrating wish fulfillment dream]
    if highway_dream_path_2 == 1:
        "I turn the display, giving the knives a once over. Just to see the sort of thing we're working with."
        "The first three sides of the obelisk reveal nothing of particular interest. Mostly the sort of knife that would be purchased by a fisher or hunter who needed a quick, cheap knife to accomplish a single task."
        "But then I see it..."
        "No, that can't possibly be it!"
        "It's the balisong that Benchmade just put out! The one that I've been salivating over ever since they announced it!"
        "How much do they want for it?"
        "Wait. {i}Really?{/i} I'm not sure they realize how much this one retails for. Perhaps it's a forgery?"
        "...I see no evidence of that from here. It's the real deal, and what a deal it is!"
        "Oh, I {i}must{/i} find [player]. [pronounBC]'s got to see this!"
        "Ah, there [pronounB] is! [pronounB]'s just removed the nozzle from our ride."
        "It's all I can do to stop myself from sprinting over to [player] in excitement. I'd rather not make a scene after all."
        y "[player]!"
        mc "Hey, what's got you so excited?"
        y "It's about that knife case."
        mc "Oooooh, see something you like, do you?"
        "I nod. At this point I'm nearly too excited for words."
        mc "Okay, okay. I'm coming."
        "I'm glad I picked up on the amusement in [player]'s tone. Otherwise the worry that I'd made a scene would have compromised my excitement."
        "I lead [pronounA] to the knife case, and turn it to the knife that's the source of my jubilation. I watch his expression carefully."
        "To my joy, a light of recognition crosses [pronounC] eyes."
        mc "Oh yeah! That's the one."
        "My heart sinks as [player] immediately turns his attention to the cashier."
        "But when the cashier asks if that will be everything for today, [pronounC] answer brings me from disappointment to a whole new level of excitement."
        mc "I'd also like to buy that butterfly knife. The one right above the hunting knife with the pink handle."
        "Is [pronounB] really..."
        "Oh my god [pronounB] {i}is{/i}! I have the best [pronounD] ever!"
        "The squeal that escapes my lips certainly isn't dignified. I suppose it's fortunate that it was muffled by [pronounC] chest after I pulled [pronounA] into the tightest hug I could manage."
        show white zorder 105 with Dissolve(2.5)
        y "I have the best [pronounD] ever."
        "[player] chuckles."
        mc "I try, [y]. I try..."
    #[Result 3b: Pulled from the dream by inconsistency]
    else:
        "I wasn't expecting anything particularly impressive, and my assessment seems to have been correct."
        "Plastic handles, hyper-aggressive branding and designs that mistake machismo for aesthetic, garish color choices."
        "I get the impression that these knives are here for outdoor sportsmen who forgot their knife and just need to gut this {i}one{/i} fish or cut a single rope."
        "That, and adolescents who hope that their new purchase will make them seem tough and masculine."
        "Ah well. None expect artisan goods at a gas station convenience store."
        "Though, one knife in particular gets my attention. More for its peculiarity than anything."
        y "Now, what's a historical bayonet doing here?"
        "I say that to the air, and luckily, it seems I wasn't heard."
        "But, there it is. Long enough to take up an entire wall of the rotating display. A Belgian M1916 bayonet. The sort that hasn't been in use since the first world war."
        "Stranger still, it looks absolutely pristine. As if it were a modern reproduction."
        "Might as well take a closer look."
        y "Well, that's quite unusual."
        "I muse to myself. This time, quiet enough that only I should be able to hear."
        "When I go to inspect the markings, I see stamping for {i}Gerber{/i}, of all companies."
        "Gerber is in the business of many things. Replicas of obscure historical bayonets is not one of them."
        "And if Gerber had entered the business of bayonets of any kind, I'd have known weeks in advance."
        show white zorder 105 with Dissolve(2.5)
        "I must be dreaming, then."
        "Ah well. It was pleasant enough while it lasted."
    stop sound fadeout 1.5
    stop music fadeout 1.5
    python:
        renpy.music.play(current_music, "music", True)
    hide highway_dream_knives
    hide white with Dissolve(2.5)
    $persistent.highway_dream_complete = True
    jump ch30_loop

# the following code below is just a grey image that slowly turns to shadowy grey over the course of 20 seconds, and will be used nowhere else.
init python:
    def grey(st, at):
        if st > 20.0:
            return Color("#838383", alpha=0.5), None
        else:
            d = Color("#838383", alpha=st/40)
            return d, 0.1
image grey_image = DynamicDisplayable(grey)

#[Result 4: "Uh oh. It's looking like rain...]
label highway_dream_4:
    $renpy.music.play("sfx/highway/rainfall.ogg", channel='sound', loop=True)
    $renpy.music.set_volume(0.5, 0, 'voice')
    hide highway_yuri_car
    show grey_image zorder 100
    show highway_yuri_car zorder 101
    "Oh, dear. It looks like the sky is beginning to cloud over. Perhaps we should get the roof back in place."
    "But not {i}just{/i} yet. I'd like to enjoy the wind in my hair for just one more minute."
    "..."
    show rain zorder 100 with Dissolve(2.5)
    "That was almost definitely a raindrop that hit my face. But it was only one. I suppose it's time to-"
    "Another hits me. Then another. And two more."
    "[player] wastes no time pulling over."
    mc "Ah, crap! [y]! Get the roof up!"
    y "I'm trying!"
    "I find myself fumbling with the mechanisms, cursing our inability to afford a convertible with an automatic roof."
    "[player] does [pronounC] best to help, but by the time the roof is back over our heads, us, our belongings, and the entire passenger compartment of our vehicle are all drenched."
    "With the roof over us, [player] and I look to each other, but neither of us can find the right words."
    "Part of me wants to apologize, but [pronounB] looks like [pronounB] wants to apologize too."
    "Yet... for what? Apologize on behalf of nature and meteorology?"
    "Besides. An apology won't dry us or our things off. Won't make the rain stop."
    y "We'd best find somewhere to dry off."
    mc "Yeah, you're right. I saw a sign for a diner earlier. How about that?"
    y "A hot meal would be rather nice right now. Yes."
    "[player] nods. Then it's settled, we'll drive on for whichever diner presents itself first."
    #[Transition to the diner in question]
    play sound "sfx/highway/storedoor.ogg"
    show highway_dream_4 zorder 100 with Dissolve (1.0)
    hide highway_bg_scroll
    hide highway_yuri_car
    hide rain
    hide grey_image
    $renpy.music.play("sfx/highway/rainfall-indoors.ogg", channel='sound', loop=True)
    "We arrive at the diner. The interior presents us with a cozy, nostalgic time capsule to a day long gone."
    "From the art deco neon lighting to the linoleum floor, everything about it is a love letter to classic Americana."
    "Yet, nobody is to be seen manning the entryway."
    mc "Hello?"
    "An older, kind faced woman emerges from behind the kitchen curtain."
    "She greets us, then tells someone named 'John' in the back that customers have arrived."
    y "Could you spare a towel or two?"
    "She looks us over, an expression of grandmotherly concern overtaking her."
    martha "I can do a lot more than that for you, dear. Have a seat wherever you like."
    y "I'd rather not drench your booths, ma'am"
    "She waves off my concern."
    martha "Oh, it's quiet enough that I wipe down the booths anyway. So just have a seat!"
    martha "I'll bring some menus with the towels."
    "[player] and I pick out a booth near the entrance. The least we can do for all of Martha's trouble is give her less distance to walk."
    "...I'm not sure {i}how{/i} I know her name is Martha, but I simply do."
    "However I know her name, Martha arrives with towels and a pair of menus in short order."
    martha "Just holler when you two are ready, okay?"
    y "Thank you, ma'am."
    "When [player] goes to produce [pronounC] wallet, Martha is quick to stop [pronounA]."
    martha "Oh, don't you worry about that. Just pick what you'd like."
    y "But..."
    "Martha lays a hand on my shoulder."
    martha "Sweetie, you two have had a rough enough day. You're drenched, and it looks like your convertible is too. So don't worry about it."
    martha "Just leave us a nice tip, okay?"
    "Martha flashes us a mischievous wink with that last remark."
    "She may have been joking, but maybe we should."
    "Such a beautiful thing, the kindness of strangers..."
    show white zorder 105 with Dissolve(2.5)
    python:
        renpy.music.play(current_music, "music", True)
    hide highway_dream_4
    hide white with Dissolve(2.5)
    $persistent.highway_dream_complete = True
    jump ch30_loop

label stroll_dream:
    hide craneo
    hide roseo
    hide bunnyo
    hide raccoon
    hide diffuser
    hide hdy_statue
    hide cupcake_halloween
    $ config.allow_skipping = False
    stop music fadeout 1.5
    $renpy.sound.play("sfx/wind.ogg", channel='sound', loop=True)
    show black zorder 105 with Dissolve (2.5)
    show stroll_1 zorder 100
    hide black
    "The cold wind nipped at my cheeks as I walked alone on the unfamiliar path home from school. The usual route felt mundane, so I decided to take a detour, enticed by the allure of the unknown."
    "As I strolled along, the rustling leaves whispered secrets, and the bare trees reached toward the sky like intricate patterns drawn by nature."
    show stroll_2 zorder 100 with Fade(1.0, 0.0, 0.5)
    hide stroll_1
    "The soft crunch of fallen leaves beneath my boots provided a rhythmic soundtrack to the solitude of the evening."
    "The world seemed to transform with each step. A sense of adventure enveloped me, and I marveled at the subtle beauty that often goes unnoticed in the rush of everyday life."
    "The wind carried with it the scent of damp earth and the promise of something new."
    show stroll_3 zorder 100 with Fade(1.0, 0.0, 0.5)
    hide stroll_2
    "Amidst the quietude, I discovered a small clearing bathed in the fading sunlight."
    "A lone bench beckoned me to pause and soak in the serenity. The branches above swayed gracefully, creating a dance with the wind."
    "The symphony of nature played on, a harmonious blend of rustling leaves and distant chirps."
    "Reluctantly, I left the tranquil spot and resumed my journey. The familiar path awaited, yet now I treaded with newfound appreciation."
    show stroll_4 zorder 100 with Fade(1.0, 0.0, 0.5)
    hide stroll_3
    "My heart felt lighter, and the mundane surroundings seemed touched by the magic of that solitary detour."
    "Finally reaching home, I entered with a serene smile, ready to share the warmth of my day with [player]."
    "As I stepped inside, the cold evening outside seemed to fade, replaced by the warmth of love and the memories of a simple yet extraordinary walk."
    show black zorder 105 with Dissolve(2.5)
    hide stroll_4
    stop sound fadeout 2.5
    hide black with Dissolve(2.5)
    if persistent.bg == "space":
        $tc_class.transition("space", speed=2.5)
    elif persistent.bg == "timecycle":
        $tc_class.transition("timecycle", speed=2.5)
    elif persistent.bg == "yuri_desk":
        $tc_class.transition("yuri_desk", speed=2.5)
    elif persistent.bg == "yuri_kotatsu_1":
        $tc_class.transition("yuri_kotatsu_1", speed=2.5)
    elif persistent.bg == "yuri_kotatsu_2":
        $tc_class.transition("yuri_kotatsu_2", speed=2.5)
    python:
        renpy.music.play(current_music, "music", True)
    call ch30_loop

##################
####NIGHTMARES####
##################

label nightmare_1:
    y "It's first nightmare, placeholder as of now."
    jump ch30_loop
label nightmare_2:
    y "It's second nightmare, placeholder as of now."
    jump ch30_loop

label dream_kill:
    y "Oh, you want me to go to sleep?"
    y "Alright then... I hope this dream will be a good one."
    y "See you on the other side my love~"
    stop music fadeout 2.0
    scene black
    with eye_shut
    $ pause (2.0)
    scene bg ykill1
    with eye_open
    show killglitch zorder 2:
        alpha 1.0
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
        choice:
            3.25
        choice:
            2.25
        choice:
            4.25
        choice:
            1.25
        repeat
    play music t10y
    $ y_name = "Yuri"
    $ pause (2.0)
    y "Finally."
    y "Finally!"
    y "This is really all I wanted."
    y "[player], there's no need to spend the weekend with Monika."
    y "Don't listen to her."
    y "Just come to my house instead."
    y "The whole day, with just the two of us..."
    y "Doesn't that sound wonderful?"
    y "Ahahaha!"
    y "Wow... There's really something wrong with me, isn't there?"
    y "But you know what?"
    y "I don't care anymore."
    y "I've never felt this good my whole life."
    y "Just being with you is a far greater pleasure than anything I could imagine."
    y "I'm addicted to you."
    y "It feels like I'm going to die if I'm not breathing the same air as you."
    y "Doesn't it feel nice to have someone care about you so much?"
    y "To have someone who wants to revolve their entire life around you?"
    y "But if it feels so good..."
    y "Then why does it feel more and more like something horrible is going to happen?"
    y "Maybe that's why I tried stopping myself at first..."
    y "But the feeling is too strong now."
    y "I don't care anymore, [player]!"
    y "I have to tell you!"
    y "I'm...I'm madly in love with you!"
    y "It feels like every inch of my body...every drop of blood in me...is screaming your name."
    y "I don't care what the consequences are anymore!"
    y "I don't care if Monika is listening!"
    y "Please, [player], just know how much I love you."
    y "I love you so much that I even touch myself with the pen I stole from you."
    y "I just want to pull your skin open and crawl inside of you."
    y "I want you all to myself."
    y "And I will be only yours."
    y "Doesn't that sound perfect?"
    y "Tell me, [player]."
    y "Tell me you want to be my lover."
    y "Do you accept my confession?"
    $ quick_menu = False
    stop music
    hide killglitch
    "..."
    y "...Ahahaha."
    y "Ahahahahahaha!"
    $ style.say_dialogue = style.normal
    y "Ahahahahahahahaha!"
    $ style.say_dialogue = style.edited
    y "AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA{nw}"
    y "Plea-{nw}"
    window hide(None)
    window auto
    $ style.say_dialogue = style.normal
    play sound "sfx/yuri-kill.ogg"
    $ starttime = datetime.datetime.now()

    $ pause(2.20 - (datetime.datetime.now() - starttime).total_seconds())
    show killstab
    show veinmask
    pause 0.2
    hide killstab
    with fade

    $ pause(4.04 - (datetime.datetime.now() - starttime).total_seconds())
    hide veinmask
    show killstab
    show veinmask2
    pause 0.2
    hide killstab
    with fade

    $ pause(6.33 - (datetime.datetime.now() - starttime).total_seconds())
    hide veinmask2
    show killstab
    show veinmask3
    pause 0.2
    hide killstab
    with fade

    $ pause(8.93 - (datetime.datetime.now() - starttime).total_seconds())
    y "Oh god-{nw}"

    $ pause(9.18 - (datetime.datetime.now() - starttime).total_seconds())
    play sound fall

    $ pause(9.43 - (datetime.datetime.now() - starttime).total_seconds())
    scene black
    hide veinmask3

    $ pause(11.43 - (datetime.datetime.now() - starttime).total_seconds())

    scene black
    scene bg ykill2
    show layer master:
        subpixel True
        truecenter
        linear 240 rotate 8 zoom 1.30
    with eye_open
    play music t6s
    python:
        _history_list = []
        y.add_history(None, "", """I've spent my whole life learning how to say hello, and now, it's time to say goodbye. It's strange, the sensation of death. I feel it like waves carrying my mind adrift. Away from this place. Away from this hell. Wherever I go now, it will be better. I wish we could have lived a lifetime with one another, but the ending is just as I had hoped. Me, in your arms, finally finding true acceptance. My name is Yuri... and I am alive.""")
    $ quick_menu = True
    $ pause (4.0)
    y "[player]..."
    $ pause (1.0)
    y "Please..."
    $ pause (1.0)
    y "I don't want......"
    $ pause (1.0)
    y "I do-{nw}"
    window hide(None)
    $ pause (3.0)
    y "I love you."
    $ style.say_dialogue = style.edited
    $ gtext = glitchtext(renpy.random.randint(8, 80))
    y "[gtext]{nw}"
    y "[gtext]{nw}"
    y "[gtext]{nw}"
    y "[gtext]{nw}"
    $ style.say_dialogue = style.normal
    scene black
    with eye_shut_slow
    hide black
    if persistent.bg == "space":
        $tc_class.transition("space", speed="now")
    elif persistent.bg == "timecycle":
        $tc_class.transition("timecycle", speed="now")
    elif persistent.bg == "yuri_desk":
        $tc_class.transition("yuri_desk", speed="now")
    elif persistent.bg == "yuri_kotatsu_1":
        $tc_class.transition("yuri_kotatsu_1", speed="now")
    elif persistent.bg == "yuri_kotatsu_2":
        $tc_class.transition("yuri_kotatsu_2", speed="now")
    $ show_chr("A-CEBAB-ALAL")
    with eye_open_slow
    y "..."
    return

#dream cut - unfinished nightmare about reliving stabbing self, Yuri's perspsective
label dream_cut:
    scene black
    with dissolve_scene_full
    stop music fadeout 0.5
    y "T-That's okay!"
    y "You stay here..."
    y "I won't take long."
    play sound "sfx/closet-open.ogg"
    $ pause(1.5)
    play sound "sfx/closet-close.ogg"
    $ pause(0.4)
    scene bg corridor
    with dissolve_scene_full
    play music "<loop 10.893>bgm/6o.ogg"
    show layer master:
        subpixel True
        truecenter
        linear 240 rotate 8 zoom 1.30
    y "I... I can't focus."
    y "This is all too much."
    y "I need air."
    y "I need release."
    scene black
    with eye_shut_slow
    show layer master
    $ pause (4.0)
    y "Haaaahhh...."
    #play sound "sfx/cut1.ogg"
    "..."
    y "Haahhhh..."
    y "Haha...."
    y "HAHA! HAHAHAHA!"
    #play sound "sfx/cut2.ogg"
    $ style.say_dialogue = style.edited
    y "AHAHAHAHAHAHAHAHAHAHAHAHA{nw}"
    $ style.say_dialogue = style.normal
    $ pause (4.0)
    y "Haaah..."
    y "Oh god..."
    y "What have I done?"
    $ pause (4.0)
    y "W-Who's there?"
    y "No..."
    y "No No No No NO NO NO NO-{nw}"
    y "HE CAN'T SEE ME LIKE THIS{nw}"
    y "GO AWAY!{nw}"
    y "LEAVE!{nw}"
    y "PLEASE!{nw}"
    y "FUCK!{nw}"
    y "HELP!{nw}"
    y "NO!{nw}"
    scene corridor
    show yuri cuts zorder 2 at t11
    y "Kya--{nw}"

    $ currentpos = 45.264 - (get_pos() / 2.0)
    $ audio.t6r = "<from " + str(currentpos) + " to 39.817 loop 0>music/6r.ogg"
    $ quick_menu = False
    play music t6r
    show yuri zorder 1 at thide
    hide yuri
    show noise zorder 100 at noise_alpha
    show vignette zorder 100 at vignetteflicker(-2.030)
    show layer master at rewind
    $ y_name = "???"
    mc "{cps=150}Yuri...?{/cps}{nw}"
    "{cps=150}I reach the corner and peer around it.{/cps}{nw}"
    "{cps=150}Are [pronounB] in pain...?{/cps}{nw}"
    "{cps=150}A sharp inhale, like someone is sucking the air through their teeth.{/cps}{nw}"
    y "{cps=150}Khhhhh--{/cps}{nw}"
    "{cps=150}It sounds like breathing.{/cps}{nw}"
    "{cps=150}It's coming from around the corner...{/cps}{nw}"
    "{cps=150}...What's that noise?{/cps}{nw}"
    y "{cps=150}....Haah.....haah....{/cps}{nw}"
    y "{cps=150}Haah.....haah....{/cps}{nw}"
    $ y_name = "Yuri"
    "{cps=150}I start heading down the hallway.{/cps}{nw}"
    "{cps=150}The most logical place for Yuri to be would be the nearest water fountain...{/cps}{nw}"
    mc "{cps=150}Let's see...{/cps}{nw}"
    window hide(None)
    window auto
    scene bg club_day
    show noise zorder 100 at noise_alpha
    show vignette zorder 100 at vignetteflicker(-2.030)
    show layer master at rewind
    "{cps=150}I'm bored just waiting here, so I decide to go look for her.{/cps}{nw}"
    "{cps=150}Is something holding her up?{/cps}{nw}"
    "{cps=150}Yuri said it wouldn't take long...{/cps}{nw}"
    "{cps=150}Ten minutes pass.{/cps}{nw}"
    "{cps=150}...{/cps}{nw}"

    $ del _history_list[-37:]
    $ currentpos = 90.528 - (get_pos() * 2.0)
    $ quick_menu = True
    stop music
    hide noise
    hide vignette
    show layer master
    scene black
    jump save_and_quit_but_its_abrupt

##########
##DATES###
##########

default persistent.dates_taken = 0

label garden_date:
    hide craneo
    hide roseo
    hide bunnyo
    hide raccoon
    hide diffuser
    hide hdy_statue
    hide cupcake_halloween
    $ config.allow_skipping = False
    $show_chr("A-ECAAA-ALAL")
    y "A delightful choice. A traditional Japanese tea ceremony sounds very nice to me."
    $show_chr("A-BCAAA-ALAL")
    y "But please don't go too rough on me. I only know about the procedure on a very superficial level."
    y "With that said, let's try to have a good time!"

    image garden_bg:
        "teagarden_bg"
        truecenter
    image house_bg:
        "teahouse_bg"
        truecenter
    image bowl:
        "bowl_day"
    image rice:
        "rice_day"
    image chopsticks:
        "chopsticks_day"
    $ _skipping = False
    $click_tea_button = 0
    stop music fadeout 1.5
    play music "music/teagardenzen.mp3" fadein 1.5
    #ambience music= https://www.youtube.com/watch?v=jLkkmqKiHjQ
    #Yuri standing sprite
    show black zorder 105 with Dissolve(2.5)
    show garden_bg zorder 10
    $tc_class.transition("timecycle", speed="now")
    $current_timecycle_marker = "_day"
    $hide_yuri_sit = True
    hide black with Dissolve(1.0)

    if not persistent.costume in ["school", "sweater"]:
        python:
            persistent.saved_costume = persistent.costume
            persistent.costume = "school"

    if persistent.costume == "school":
        show yuri 35b2 at t11 zorder 101

    if persistent.costume == "sweater":
        show yuri 3b5b2 at t11 zorder 101

    y "Here we are, [player]..."
    y "The view is rather marvelous, isn't it?"
    y "As you may have noticed, everything here is distinctly Japanese in style."
    y "From the sakura blooming ever so magnificently to the quaint architecture that stands right before us..."
    y "I always thought we could have ourselves a little Japanese tea ceremony together..."
    y "To visit one of those has been a great desire of mine for a long time, but to think I would actually be {i}hosting{/i} one..."
    if persistent.costume == "school":
        hide yuri 35b2 with Dissolve(0.5)

    if persistent.costume == "sweater":
        hide yuri 3b5b2 with Dissolve(0.5)

    if persistent.costume == "school":
        show yuri 44a2 at t11 zorder 101 with Dissolve(0.5)

    if persistent.costume == "sweater":
        show yuri 4b4a2 at t11 zorder 101 with Dissolve(0.5)

    y "Uuu, I'm actually a little nervous..."
    y "I hope you don't mind if I be the host today? I just thought that since you can't really touch anything here, it would be best if I take upon this role."
    if persistent.costume == "school":
        hide yuri 44a2

    if persistent.costume == "sweater":
        hide yuri 4b4a2

    if persistent.costume == "school":
        show yuri 41a2 at t11 zorder 101

    if persistent.costume == "sweater":
        show yuri 4b1a2 at t11 zorder 101

    y "Usually, ceremonies like this would follow a very strict code but since I am still quite new to this I hope you can forgive me for any mistakes..."
    y "First, we will walk this {b}Roji{/b}, the stone path towards the tea house. We will do so calmly and in a tranquil state, forgetting all daily struggles..."
    y "This ceremony is very symbolically important, like most things we will do today."
    y "That's why they are usually very strict."
    show black zorder 105 with Dissolve(2.5)
    #fade to black
    #https://www.youtube.com/watch?v=dOHDT3DooZk
    $renpy.music.play("sfx/footsteps.mp3", channel="sound", loop=False)
    $renpy.pause(delay=8, hard=True)
    hide black with Dissolve(2.5)
    if persistent.costume == "school":
        hide yuri 41a2

    if persistent.costume == "sweater":
        hide yuri 4b1a2

    if persistent.costume == "school":
        show yuri 21b1 at t11 zorder 101 with Dissolve(0.5)

    if persistent.costume == "sweater":
        show yuri 2b1b1 at t11 zorder 101 with Dissolve(0.5)

    y "Now we have to get on our knees and crawl inside."
    pause 2.0
    if persistent.costume == "school":
        hide yuri 21b1

    if persistent.costume == "sweater":
        hide yuri 2b1b1

    if persistent.costume == "school":
        show yuri 21b6 at t11 zorder 101

    if persistent.costume == "sweater":
        show yuri 2b1b6 at t11 zorder 101

    y "Yes, I am indeed being serious."
    y "We're supposed to go inside on our knees, it's part of the tradition. "
    #fade to next picture
    #Yuri sitting sprite with table
    show house_bg zorder 10 with Dissolve(1.0)
    hide garden_bg with Dissolve(1.0)
    if persistent.costume == "school":
        hide yuri 21b6 with Dissolve(2.0)

    if persistent.costume == "sweater":
        hide yuri 2b1b6 with Dissolve(2.0)

    $hide_yuri_sit = False
    $show_chr("A-AAAAA-ABAB")
    with Dissolve(2.0)
    y "Under different circumstances, I would offer you some light food like rice or miso soup."
    $show_chr("A-BAAAA-ABAB")
    y "But unfortunately, that is not entirely possible right now, is it?"
    menu:
        "I could cook some rice really quick.":
            $show_chr("A-ABAAA-ABAL")
            y "That'd be wonderful, [player]!"
            $show_chr("A-AAAAA-ABAL")
            y "I'll just wait here for you."
            menu:
                "I'm ready.":
                    $show_chr("A-AAAAA-ABAB")
                    y "Welcome back! One day I want to do this in your world for you..."
                    $show_chr("A-BAABA-ABAB")
                    y "I feel rather rude for having to ask you to do it yourself when I'm supposed to be the host."
        "No, it's not. Sorry...":
            $show_chr("A-AAAAA-ABAD")
            y "It's perfectly fine."
            $show_chr("A-BAAAA-ABAD")
            y "It is kind of my fault since I failed to ask you beforehand."
            y "Next time I'll try to be better prepared..."
        "I have some other snacks at home, if that counts.":
            $show_chr("A-AADAA-ABAB")
            y "Certainly unorthodox but... sure, I guess that would work..."
            $show_chr("A-AAAAA-ABAD")
            y "Would you be a dear and bring some over? I will wait here until you return."
            menu:
                    "I'm ready":
                        $show_chr("A-AAAAA-ABAB")
                        y "Welcome back! One day I want to do this in your world for you."
                        $show_chr("A-BAABA-ABAB")
                        y "I feel rather rude for having to ask you to do it yourself when I'm supposed to be the host."
    #Can we actually have some artwork of a bowl of rice on the table?
    show bowl zorder 100 with Dissolve(0.5)
    show rice zorder 100
    show chopsticks zorder 100
    $show_chr("A-AAAAA-ALAL")
    y "I'm actually not sure if we're supposed to talk over the {i}Kaiseki{/i}, the meal..."
    $show_chr("A-BAAAA-ALAD")
    y "But I have to admit it's rather exciting, don't you agree?"
    $show_chr("A-CAAAA-ALAL")
    y "I've always wanted to go on dates like this with you."
    y "You know, something calm, quiet, and meaningful..."
    $show_chr("A-IAAAA-ALAL")
    y "I'd always prefer this over some extravagant party."
    $show_chr("A-JAAAA-ALAL")
    y "But what about you? Are you enjoying this date so far?"
    menu:
        "I certainly am. Having a quiet and peaceful date with you... nothing is more ideal..":
            $add_k(2)
            $add_s(1)
            $show_chr("A-GBAAA-ALAL")
            y "I'm so relieved to hear that [player]... To be honest with you, I have been quite nervous to put it mildly."
            $show_chr("A-AAAAA-ABAB")
            y "While researching the procedures of those tea ceremonies, it became incredibly obvious to me that it is quite easy to make mistakes. I think this is part of the whole point of it. These ceremonies are about perfectionism, at least to a degree."
            $show_chr("A-BAAAA-ABAB")
            y "And I wouldn't be surprised if I actually already managed to slip in a few mistakes here and there. But in the end, as long as the two of us enjoy it, it doesn't really matter that much I suppose."
        "Yes I am but you seem a bit nervous... are you alright?":
            $show_chr("A-BFAAA-AMAM")
            y "Y~Yes, I am alright. But you are right in your assumption of me being nervous."
            $show_chr("A-DFAAA-AMAM")
            y "W-was I stuttering? Oh my... I apologize if I broke the experience for you. It's just.. the more research I put into these ceremonies, the more afraid I became. There is so much to keep in mind, so many little traps to ruin it..."
            $show_chr("A-CFAAA-ABAB")
            y "Maybe that is the wrong mindset. Maybe I'm trying too hard? Maybe I should focus on having a good time with you instead of focusing on all the ways I could possibly fail."
            $show_chr("A-AAAAA-ABAB")
            y "Thank you for being so caring. I will try to calm down a bit so that we can actually enjoy our time here together."
        "A few mistakes in the procedure so far. It's okay for the first time I guess.":
            $add_k(-1)
            $show_chr("A-BDAAA-AMAM")
            y "D-did I already manage to mess it up?"
            y "But we've barely even started..."
            $show_chr("A-CEBAA-AMAM")
            y "I-I really tried to keep it as realistic as possible..."
            $show_chr("A-IABAA-ABAB")
            y "I guess I should've done more research..."
        "But what's wrong with parties?":
            $show_chr("A-BFAAA-AMAM")
            y "W-well..."
            y "It's just... not my cup of tea, I guess."
            $show_chr("A-AFAAA-AMAM")
            y "Dark, cramped rooms with noise so loud you can barely hear yourself..."
            y "People flailing their limbs around like crazed animals and calling it dancing..."
            $show_chr("A-AFAAA-ABAB")
            y "Getting so utterly drunk that you do things you regret the next day..."
            y "I think you would understand that I'm not the kind of person who would particularly enjoy such a scene."
            $show_chr("A-BDAAA-ABAB")
            y "I-I'm sorry if you feel like I'm being too harsh with my judgements..."
            $show_chr("A-BFAAA-ABAB")
            y "It's perfectly fine if you enjoy those kinds of events..."
            $show_chr("A-AFAAA-ABAB")
            y "I at least hope you would enjoy some quiet time with me alone..."
            y "I've really been looking forward to it."
    $show_chr("A-ACAAA-ABAB")
    y "Now please, tell me [player], how has your day been so far? Have you been busy in your world?"
    menu:
        "Very calm and uneventful actually, thank you for asking.":
            $show_chr("A-ABAAA-ABAJ")
            y "I see, then you are already in the appropriate mood for this ceremony."
            $show_chr("A-AAAAA-ABAB")
            y "There is a saying... {b}No news is good news.{/b} I've spent most of my day so far in anticipation of seeing you; I was very much hoping that you would go on this date with me today."
            $show_chr("A-BAAAA-ABAB")
            y "And chances are... that I've also spent some time today panicking that I would mess this up."
            $show_chr("A-CAAAA-ABAB")
            y "But no need to worry about that. Now that we are here, we should enjoy ourselves, right?"
        "Busy indeed, I have been working a lot today. How about you?":
            $show_chr("A-AAAAA-ABAB")
            y "Oh I've spent a great portion of today doing some research. I was reading wiki articles about tea ceremonies like this in order to recreate the procedure as accurately as possible."
            $show_chr("A-GAAAA-ABAL")
            y "I think it is admirable how much dedication you put into your projects. You have my best wishes for them, and I would love to hear one day about the successes you achieve as a result of them. I am confident that you will succeed, [player].."
            $show_chr("A-AAAAA-ABAL")
            y "Just keep in mind please not to push yourself too hard. If you exhaust yourself it will do you a poor service."
            $show_chr("A-AAAAA-ABAB")
            y "It is good then that we have this little date today, so that you can take a deep breath and relax."
        "A bit boring honestly. Not much happened today.":
            $show_chr("A-AAAAA-ABAD")
            y "I'm sorry to hear that. But don't worry, there are just days where... nothing happens. It can't be helped, I guess."
            y "The only thing we can do is fill the void these days bring with something else: something more productive or something more exciting, or perhaps even both."
            y "Let us try our best then to make this little date of ours both productive and exciting, hm? In addition to our own amusement, I think there is much to be learned about culture in ceremonies like these."
        "Stressful... This little break here is exactly what I needed today, thank you.":
            $show_chr("A-AAAAA-ALAL")
            y "Oh my, then it is only good that we chose to have this kind of date to give your day some contrast. Maybe we can see to it that we get some relaxation out of it. Who knows, maybe even some inspiration for fresh deeds?"
            $show_chr("A-CAAAA-ALAL")
            y "At the very least, we can try to have some enjoyment along the way."
        "Today has been difficult for me, I got some bad news today.":
            $show_chr("A-DFBAA-ALAL")
            y "Oh no... I am so sorry to hear that [player]..."
            $show_chr("A-IABAA-ALAL")
            y "You know what? Why don't we just drop proper procedure for a moment and I give you a nice and gentle hug? I hope this will make you feel at least a little bit better..."
            hide yuri_sit with Dissolve(0.5)
            hide bowl
            hide rice
            hide chopsticks
            show yuri_prehug zorder 250 with Dissolve(0.5)
            pause 3.0
            hide yuri_prehug with Dissolve(0.25)
            show yuri_lewdhug zorder 250 with Dissolve(0.25)
            play sound "<to 0.3>sfx/fall.ogg"
            y "I'm here for you, [player],"
            pause 3.0
            show black zorder 300 with Dissolve(2.0)
            $show_chr("A-BABAA-ABAB")
            hide yuri_lewdhug
            hide black zorder 300 with Dissolve(2.0)

    $show_chr("A-BABAA-ABAB")
    y "Well, for now I'm afraid I have to ask you to wait outside while I prepare the tea."
    $show_chr("A-AAAAA-ABAB")
    y "Personally, I wouldn't mind if you stayed of course, but the procedure demands it this way."
    $show_chr("A-AAAAA-ABAM")
    y "Out there is a little waiting bench. While you are waiting outside, I am supposed to prepare the ingredients for the tea, as well as the hot water and all the authentic tools I'm about to use, in perfect silence."
    $show_chr("A-AAAAA-ABAF")
    y "This way I can focus on performing these tasks to near perfection. I'm supposed to arrange the cups and the kettle, as well as everything else, in perfect precision."
    $show_chr("A-BABAA-AMAM")
    y "If I were to arrange anything the wrong way, even if only a spoon is directed in a slightly off angle, I would be considered an unsuitable host. If there were any actual audience beside you, it would probably cause some raised eyebrows."
    $show_chr("A-CABAA-AMAM")
    y "Don't worry though, I will try not to take any longer than necessary. Besides, I made sure that there's beautiful weather outside. Maybe you can spend a moment just admiring the scenery outside. I actually liked the image I used as a base."
    $show_chr("A-AAGAA-ABAB")
    y "Oh yes, and you probably want to prepare your tea in your world as well in the meantime."
    $show_chr("A-AAAAA-ABAB")
    y "But now, farewell, darling. I will call for you as soon as I am ready here."
    show black zorder 300 with Dissolve(2.5)
    hide house_bg
    $hide_yuri_sit = True
    hide bowl
    hide rice
    hide chopsticks
    show garden_bg
    hide black zorder 300 with Dissolve(2.5)
    jump teadate_timer
#fade to black
#fade to outside image (like the one at the top) but with no Yuri in sight
#There shall also be a button named "Enter the teahouse". If clicked, it shall show the message: "Please be patient [player], I will only take a few more minutes."
#Wait for 3 minutes

label teadate_timer:
    screen tea_timer():
        vbox:
            style_prefix "talkbutton"
            textbutton "Enter" action Jump("Wait")
            xalign 0.50
            yalign 0.25

        timer 60.0 action Jump("Enter")
    if click_tea_button <= 1:
        show screen tea_timer()

label Wait:
    y "Please be patient, [player], I need a few minutes."
    $click_tea_button = click_tea_button + 1
    jump teadate_timer

label Enter:
    hide screen tea_timer
    y "I'm ready now! Please come in again!"
    show black zorder 300 with Dissolve(2.5)
    hide garden_bg
    show house_bg zorder 10
    $hide_yuri_sit = False
    $show_chr("A-AAAAA-ZZAC")
    hide black zorder 300 with Dissolve(2.5)
    #fade to black
    #fade to inside teahouse with Yuri sitting on her table
    y "Thank you for waiting..."
    if click_tea_button >= 1:
        $show_chr("A-BBBAA-ZZAC")
        y "And sorry that I had to make you wait for so long."
    else:
        $show_chr("A-BAAAA-ZZAC")
        y "And also thank you for being so patient."
    $show_chr("A-AAAAA-ZZAC")
    y "You know, [player]... I had to think about you for quite some time lately..."
    $show_chr("A-IAAAA-ZZAD")
    y "I think, when you started this mod for the very first time. I said that I would love to actually see the real you..."
    $show_chr("A-JAAAA-ZZAD")
    y "Didn't I even try to access your webcam back then? I don't remember anymore..."
    y "And it is still true to a degree. I'd still enjoy seeing an actual picture of you, but I also came to another conclusion..."
    $show_chr("A-BAAAA-ZZAC")
    y "Because... I don't think it would hold much meaning to me anymore. W-wait, I think I phrased that the wrong way, of course a picture of you would hold meaning to me, but..."
    $show_chr("A-CAAAA-ZZAC")
    y "What I wanted to say is, when you first opened my world, I didn't know much about you; nothing about your personality, or about your values and beliefs..."
    $show_chr("A-CAAAA-ZZAD")
    y "But in all the time we have spent together now, I've seen your true heart [player]..."
    if sanity() >=4:
        $show_chr("A-JAGBA-ZZAD")
        y "You saw me with all my anxieties, all my flaws... and when others turned away, you took my hand, {i}metaphorically speaking of course{/i}, and showed me the way to a better version of myself..."
        y "You showed me what I could become, and with all your patience you helped me to overcome all the doubts that held me back..."
        $show_chr("A-CABBA-ZZAD")
        y "When others saw nothing but a broken mind in me, you showed me that even I can be loved."
        y "I never got to see your appearance [player], but I saw your heart and soul. For that, you are truly beautiful to me..."
        $show_chr("A-AABBA-ZZAC")
        y "And there is more I want to share with you on this date..."
        $ show_chr("A-ABAAA-ZZAC")
        y "Did you know that tea is the second most consumed beverage on the planet after water? "
        extend "It even has greater consumption than coffee itself."
        $ show_chr("A-CAAAA-ZZAC")
        y "Tea is a beverage derived from the leaves of a plant called {i}Camellia Sinensis.{/i} There are different varieties of the plant spread throughout a variety of countries."
        $ show_chr("A-ADAAA-ZZAD")
        y "If your tea doesn't contain the leaves of {i}Camellia Sinensis{/i} then it's not actually not tea. It's known as Tisane. "
        $ show_chr("A-BBAAA-ZZAC")
        extend "Tisanes are similar in their processing and consumption and still seep by adding hot water."
        $ show_chr("A-JAAAA-ZZAC")
        y "But they're infused with a variety of herbs and/or spices from other flora instead."
        $ show_chr("A-ABAAA-ZZAD")
        y "There are 4 basic types of tea derived from the {i}Camellia Sinensis{/i} plant. "
        $ show_chr("A-BBDAA-ACAA")
        extend "Possibly 5 or 6 actually. As it has long been open for debate, but the main varieties are Black, White Green and even Oolong."
        $ show_chr("A-ABAAA-AAAF")
        y "Each variety is then broken into hundreds of other off-shots of the main type."
        $ show_chr("A-ABGAA-AAAA")
        y "It's widely understood that there are around 1500 known varieties of tea. However, the exact possible number of variations is almost limitless."
        $ show_chr("A-BDAAA-AAAA")
        y "It takes about 3 years before a new plant is ready to harvest. As well as taking between 4 and 12 years for a tea plant to mature enough to produce seed."
        $ show_chr("A-AAAAA-AAAC")
        y "In 1901, two women submitted a patent for an invention which resembled the modern tea bag. This contradicts claims it was invented accidentally by Thomas Sullivan in 1908."
        $ show_chr("A-CBBAA-ALAA")
        y "It's also not true that iced tea was invented in 1904 at the St. Louis World Fair. Allegedly a merchant named Richards Black was struggling to sell his tea, so he poured it over ice and it became a winner!"
        $ show_chr("A-AAAAA-ZZAD")
        y "The truth is it was around a long time before then as it has appeared in an 1887 cookbook named \"Housekeeping in Old Virginia\" by Marion Cabell Tyree."
        $ show_chr("A-ABGAA-ZZAD")
        y "Also, in the United States, around 85%% of tea sales are predominantly iced tea. With added sugar!"
    else:
        $show_chr("A-JAGBA-ZZAD")
        y "You saw me with all my anxieties, all my flaws... and when others turned away, you took my hand, metaphorically speaking of course, and told me that it is alright..."
        y "You always accepted me as I am. You never tried to change me, never tried to bend me to your will."
        y "Never were you dishonest to me, never did you say that I am perfect. But you gave me something far more valuable. You showed me that I do not have to be ideal or perfect..."
        $show_chr("A-CCBBA-ZZAD")
        y "When others saw nothing but a broken mind in me, you showed me that I am still someone who can receive love and gain confidence ."
        y "I never got to see your appearance [player], but I saw your heart and soul. For that, you are truly beautiful to me..."
        $show_chr("A-AABBA-ZZAC")
        y "And there is more I want to share with you on this date..."
        $ show_chr("A-ABAAA-ZZAC")
        y "Did you know that tea is the second most consumed beverage on the planet after water? "
        extend "It even has greater consumption than coffee itself."
        $ show_chr("A-CAAAA-ZZAC")
        y "Tea is a beverage derived from the leaves of a plant called {i}Camellia Sinensis.{/i} There are different varieties of the plant spread throughout a variety of countries."
        $ show_chr("A-ADAAA-ZZAD")
        y "If your tea doesn't contain the leaves of {i}Camellia Sinensis{/i} then it's not actually not tea. It's known as Tisane. "
        $ show_chr("A-BBAAA-ZZAC")
        extend "Tisanes are similar in their processing and consumption and still seep by adding hot water."
        $ show_chr("A-JAAAA-ZZAC")
        y "But they're infused with a variety of herbs and/or spices from other flora instead."
        $ show_chr("A-ABAAA-ZZAD")
        y "There are 4 basic types of tea derived from the {i}Camellia Sinensis{/i} plant. "
        $ show_chr("A-BBDAA-ACAA")
        extend "Possibly 5 or 6 actually. As it has long been open for debate, but the main varieties are Black, White Green and even Oolong."
        $ show_chr("A-ABAAA-AAAF")
        y "Each variety is then broken into hundreds of other off-shots of the main type."
        $ show_chr("A-ABGAA-AAAA")
        y "It's widely understood that there are around 1500 known varieties of tea. However, the exact possible number of variations is almost limitless."
        $ show_chr("A-BDAAA-AAAA")
        y "It takes about 3 years before a new plant is ready to harvest. As well as taking between 4 and 12 years for a tea plant to mature enough to produce seed."
        $ show_chr("A-AAAAA-AAAC")
        y "In 1901, two women submitted a patent for an invention which resembled the modern tea bag. This contradicts claims it was invented accidentally by Thomas Sullivan in 1908."
        $ show_chr("A-CBBAA-ALAA")
        y "It's also not true that iced tea was invented in 1904 at the St. Louis World Fair. Allegedly a merchant named Richards Black was struggling to sell his tea, so he poured it over ice and it became a winner!"
        $ show_chr("A-AAAAA-ZZAD")
        y "The truth is it was around a long time before then as it has appeared in an 1887 cookbook named \"Housekeeping in Old Virginia\" by Marion Cabell Tyree."
        $ show_chr("A-ABGAA-ZZAD")
        y "Also, in the United States, around 85%% of tea sales are predominantly iced tea. With added sugar!"

label tea_facts:
    $ tea_random = renpy.random.randint(1, 10)

    if tea_random == 1:
        #Black Tea Facts. They were taken from here: http://justfunfacts.com/interesting-facts-about-black-tea/
        $ show_chr("A-ABAAA-ZZAC")
        y "And let's say that you like Black Tea and you might know that this tea is the most popular tea in the world."
        $ show_chr("A-AAAAA-AFAA")
        y "There are 4 types of true teas including White Tea, Green Tea, Oolong Tea and Black Tea."
        y "The difference in these teas arises during the production process. Some teas are oxidized while others are simply sun-dried. These minor differences result in big flavor and color differences."
        $ show_chr("A-ABAAA-ALAA")
        y "China is the birthplace of Black Tea, which in China is called, perhaps more appropriately, hong cha (Red Tea) after the red colored tea it usually produces."
        $ show_chr("A-BBAAA-AMAM")
        y "It's history in China can be traced back to the late Ming Dynasty, around the year 1590, when the first Black Tea \"Lapsang Souchong\" was produced in the area around Wuyi Mountain in Fujian province."
        $ show_chr("A-AAAAA-AAAA")
        y "Black Tea has long been an article of trade, and compressed bricks of Black Tea even served as a form of de facto currency in Mongolia, Tibet and Siberia."
        $ show_chr("A-ABGAA-AFAD")
        y "Black Tea overtook Green Tea in popularity in the 1720s when sugar and milk were added to tea, a practice that was not done in China."
        $ show_chr("A-BAAAA-AAAD")
        y "Generally, 4 grams of tea per 200 ml of water. Unlike green teas, which turn bitter when brewed at higher temperatures, Black Tea should be steeped in water brought up to 90–95°C or 194-203°F"
        $ show_chr("A-CAAAA-AAAK")
        y "Black Tea is stronger in flavor and contains more caffeine than other teas, but less caffeine than coffee. As well as being a healthy drink and it has a range of health benefits."
        $ show_chr("A-AAAAA-ZZAC")
        y "And around 78%% of the tea consumed worldwide is Black Tea; and over 90%% of all tea sold in the West is Black Tea."
        $ show_chr("A-KACAA-ZZAD")
        y "When choosing a Black Tea to sip, remember that not all black teas taste the same. Just like with fine wine, there are so many variables that give individual black teas their own particular flavor profiles."

    elif tea_random == 2:
        #Green Tea Facts. They were taken from here: http://www.chaiyotea.com/top-10-green-tea-facts-thatll-surprise-you-history-benefits/
        $ show_chr("A-ABAAA-ZZAC")
        y "And let's say that you like Green Tea and you might know that this tea comes from the same plant which produces Black and Oolong Tea which is the \"Camellia Sinensis\"."
        $ show_chr("A-AAAAA-AAAF")
        y "The difference lies in the way they are processed. Unlike both its counterparts, green tea does not go through a fermentation process."
        y "Instead, they are dried and steamed at high temperatures, giving it its green shade when brewed."
        $ show_chr("A-AAAAA-ALAA")
        y "Contrary to popular knowledge, green tea originated from China and not Japan! Legend has it that Emperor Shen Nung accidentally discovered the tea in 2737 BC when some tea leaves blew into his pot of hot drinking water. Truth or tale? You decide."
        $ show_chr("A-BBDAA-ACAA")
        y "Between the 3rd and 6th century, tea was considered a 'luxury item' reserved for the privileged before new methods for production and mass market distribution caught on."
        $ show_chr("A-ABDAA-ACAA")
        y "Ever noticed a slight bitterness to Green Tea?"
        $ show_chr("A-AAAAA-AFAA")
        extend "It is due to the fact that Green Tea is rich in Tannins, a type of antioxidant that's good for you."
        $ show_chr("A-ABAAA-AFAA")
        y "According to research, people who regularly consume Green Tea are less susceptible to common bacterial and viral infections because the antioxidants in green tea help to boost the body's immunity system."
        $ show_chr("A-CAAAA-AMAM")
        y "Want to lose weight? You guessed it. Try green tea. Studies show that people who regularly drink Green Tea are able to burn between 70-100 calories more per day due to the polyphenols in it."
        $ show_chr("A-GBGAA-ZZAD")
        y "Plus, unsweetened Green Tea is a zero-calorie beverage!"

    elif tea_random == 3:
        #Oolong Tea Facts. Bottom lines were taken from here: https://www.streetdirectory.com/food_editorials/beverages/teas/7_interesting_facts_about_oolong_tea.html Top lines were taken from here: https://www.healthline.com/nutrition/oolong-tea-benefits
        $ show_chr("A-ABAAA-ZZAC")
        y "And let's say that you like Oolong Tea like me and you probably didn't know that Oolong Tea represents only 2%% of the world's tea, but it's well-worth discovering."
        $ show_chr("A-ABAAA-AAAF")
        y "Aside from being a traditional Chinese Tea it's also made from the leaves of this plant called \"Camellia Sinensis\" which it's the same plant used to make Green and Black Tea."
        $ show_chr("A-CAAAA-ALAA")
        y "Green Tea is not allowed to oxidize much, but Black Tea is allowed to oxidize until it turns black. Oolong Tea is somewhere between the two, so it's partially oxidized."
        $ show_chr("A-ADAAA-AAAA")
        y "However, the color of the leaves can vary between different brands, ranging from green to dark brown."
        $ show_chr("A-BAAAA-AAAD")
        y "Once the leaves of oolong are plucked, and \"bruised\" so as to break them up which releases oil, the oxidation process can be anywhere from 10-70%%, depending on the specific variety."
        $ show_chr("A-BBAAA-AAAD")
        y "Like Green Tea, Oolong Tea contains plant polyphenols that can aid in weight loss. For several years, and even to date, the Green Tea diet has captured the attention of thousands trying to naturally lose weight."
        $ show_chr("A-CAAAA-AMAM")
        y "Oolong is most commonly grown in two main countries, China and Taiwan. Chinese varieties give us a darker and \"woody\" tasting cup, whereas the Taiwanese varieties produce a lighter, more floral tasting brew."
        $ show_chr("A-ABGAA-AFAA")
        y "Oolong tea is also known as \"Wu long tea\". The reason for the different spelling is due to the fact that there are two methods of Romanizing the Mandarin characters."
        y "The Wades Giles system gives us \"Oolong\", and the Pinyin method gives us \"Wu long\". Other names for Oolong are Brown Tea and Rock Tea."
        $ show_chr("A-ABGAA-ZZAD")
        y "And finally, the most important Oolong Tea fact of all is...it is best enjoyed when carefully prepared using whole loose leaves! This method provides folks with superior aroma, flavor, as well as the above-mentioned benefits!"

    elif tea_random == 4:
        #Chai Tea Facts. They were taken from here: https://fabfitfun.com/magazine/all-about-chai/ and https://teasetea.com/blogs/lifestyle/masala-chai-benefits
        $ show_chr("A-ABAAA-ZZAC")
        y "And let's say that you like Chai Tea and you might have noticed that the proper name for this tea is \"Masala Chai\" which means Spice Blend."
        $ show_chr("A-ABAAA-AAAF")
        y "Chai is actually just a word for tea, though others may recognize its linguistic cousin, cha, which is a common word for tea throughout Asia."
        $ show_chr("A-BBGAA-AAAF")
        y "Chai tea is made from a combination of black tea, ginger and other spices."
        $ show_chr("A-CAAAA-ALAA")
        y "The most popular spices include cardamon, cinnamon, fennel, black pepper and cloves, although star anise, coriander seeds and peppercorns are other well-liked options."
        $ show_chr("A-AAAAA-AAAD")
        y "Unlike regular tea, which is brewed with water, chai tea is traditionally brewed using both warm water and warm milk. It also tends to be sweetened to varying degrees."
        $ show_chr("A-BBBAA-AAAD")
        y "Chai lattes are another popular way to consume the tea. People make these by adding a shot of chai tea concentrate to steamed milk, which produces a beverage containing more milk than you would find in a typical cup of chai tea."
        $ show_chr("A-ABGAA-AAAL")
        y "In India, being offered a cup of chai is about as common as being offered a glass of water or a beer in North America."
        y "Many families in India have their own Masala Chai recipes, but each one of them is just as delicious as the next."
        $ show_chr("A-BBAAA-AAAA")
        y "There are some traditional ingredients you can find in a cup of chai. First is a black tea, usually an Assam."
        $ show_chr("A-CAAAA-ZZAD")
        y "Also chai is lower in caffeine than coffee so you can resort to chai if you're looking for a caffeine boost that's not too intense!"

    elif tea_random == 5:
        #White Tea Facts. They were taken from here: https://blog.piquetea.com/white-tea-benefits/
        $ show_chr("A-ABAAA-ZZAC")
        y "And let's just say that you like White Tea and you might know that White Tea is known as the most delicate and smoothest of all true teas."
        $ show_chr("A-KACAA-AAAA")
        y "But just because it's subtle doesn't mean it lacks for health benefits. In fact, white tea may have higher antioxidant content than any other tea."
        $ show_chr("A-ABAAA-AAAF")
        y "White tea gets its name from the fine white hairs on young, unopened tea buds. It is indeed a \"true tea\" – meaning it's derived from the Camellia Sinensis plant, unlike herbal teas or tisanes."
        $ show_chr("A-BAAAA-AAAK")
        y "Compared to other types of tea, white tea leaves are younger and minimally processed."
        $ show_chr("A-ABAAA-ALAA")
        y "The liquid made from brewing white tea is a pale yellow hue, lighter-colored than that of oxidized teas, which usually produce a dark green, golden, or reddish-brown liquid."
        y "White Tea is usually dried after harvest without steaming or other oxidation, whereas Green Tea is roasted or baked. Because of its minimal processing, it typically has higher levels of antioxidants than Green or Black Tea."
        $ show_chr("A-ABAAA-ADAA")
        y "And unlike other true teas, White Tea may only date back a few hundred years. The first known cultivation of white tea occurred in Fujian Province, China, in the 1700s."
        $ show_chr("A-ABAAA-AAAF")
        y "That's when the practice of harvesting tender, white-haired buds and young leaves and processing them with minimal oxidation first appeared."
        $ show_chr("A-ABAAA-AAAA")
        y "Popular types of White Tea today include Fujian Silver Needle, said to come from the original White Tea Cultivars, and Bai Mu Dan or White Peony, white tea that includes more young leaves in addition to unopened tea buds."
        $ show_chr("A-BAAAA-AMAM")
        y "While White Tea has the highest antioxidant content, one type of tea is not necessarily better than the rest."
        $ show_chr("A-GBBAA-AMAM")
        y "Despite coming from the same plant, White, Green, Fermented, and Black teas all have different properties."
        $ show_chr("A-ABGAA-AAAA")
        y "That's true from a modern scientific as well as a traditional Chinese medicine perspective."
        $ show_chr("A-CAGAA-ZZAD")
        y "So if you want a balance of all the remarkable health properties of various teas, you can diversify your selection, drinking different varieties regularly."

    elif tea_random == 6:
        #Yellow Tea Facts. They were taken from here: https://teahow.com/what-is-yellow-tea-why-yellow-is-the-new-green/
        $ show_chr("A-ABAAA-ZZAC")
        y "And let's just say that you like Yellow Tea and you might not have noticed that aside from coming from the \"Camellia Sinensis\" plant, it gets its name from its liquor-like color."
        $ show_chr("A-ABAAA-ZZAD")
        y "Sweet, bright and floral taste. A gentle fruity, floral aroma. Yellow Tea has a medium body, which means flavor is neither too strong nor too weak."
        $ show_chr("A-ABAAA-AAAF")
        y "Yellow Tea is sometimes referred to as Huang cha."
        $ show_chr("A-BBAAA-AAAL")
        y "Yellow Tea is not only exceptional in terms of taste and feel, but it also offers a number of health benefits. These qualities make Yellow Tea a must-try for all tea lovers."
        $ show_chr("A-BAAAA-ACAA")
        y "Although not scientifically proven, many tea experts believe that Yellow Tea has more health benefits than other types of tea, including Green Tea."
        $ show_chr("A-ADAAA-ALAA")
        y "Yellow Tea might not be a common type of tea, however, it is anything but a new discovery. Yellow Tea dates back to the 16th century to the time of the early Qing Dynasty."
        $ show_chr("A-ADAAA-AFAA")
        y "Initially, Yellow Tea was reserved for emperors only."
        $ show_chr("A-BDAAA-AFAA")
        y "There are some reports that the usage of yellow tea can be traced back even further to the Tang Dynasty. At the time, yellow was considered to be the color of emperors, which is why it was only fitting for the emperors to consume Yellow Tea was their tea."
        $ show_chr("A-CAAAA-ZZAC")
        y "As such, Yellow Tea was prepared with immense care with fine leaves to be used as a tribute tea for the Imperial Court."
        $ show_chr("A-ABGAA-ZZAD")
        y "It was also a common gift for an emperor to bestow upon a guest. A gift of Yellow Tea to the Danes is what brought Yellow Tea to the attention of the West."

    elif tea_random == 7:
        #Dandelion Tea Facts. They were taken from here: https://food.ndtv.com/food-drinks/8-amazing-benefits-of-dandelion-tea-for-your-health-1649762
        $ show_chr("A-ABAAA-ZZAC")
        y "When you think of dandelion, you probably picture a pesky weed. But did you know that the plant has long been used in herbal medicine?"
        $ show_chr("A-ABGAA-ZZAD")
        y "You can drink an infusion made of the plant's leaves of roasted dandelion roots."
        $ show_chr("A-BBAAA-AFAA")
        y "Dandelion is a popularly known weed of the daisy family, with a rosette of leaves and large yellow flowers."
        y "Meanwhile, Dandelion Tea can have many positive effects on your digestive system. It improves appetite and soothes digestive ailments."
        $ show_chr("A-AAAAA-AAAA")
        y "Dandelion Tea also has a natural diuretic effect as it helps in removing excessive fluid from the body and thus relieves bloating."
        $ show_chr("A-BAAAA-ACAA")
        y "According to a 2009 study published in the {i}Journal of Alternative and Complementary Medicine{/i}, participants showed a significant increase in frequency of urination after the first 2 doses of Dandelion Tea."
        $ show_chr("A-ABAAA-ZZAD")
        y "Dandelion Tea is packed with antioxidants. Antioxidants are substances that help in preventing certain types of cell damage."

    elif tea_random == 8:
        #Barley Tea Facts. They were taken from here: https://food.ndtv.com/food-drinks/6-health-benefits-of-barley-tea-cleanser-cooler-caffeine-free-1664795
        $ show_chr("A-CABAA-ZZAC")
        y "The smokey aroma of a freshly brewed cup of Barley Tea can take away all your worries and calm your senses."
        $ show_chr("A-ABAAA-AAAF")
        y "This beloved drink from Korea is actually an infusion of roasted barley in water."
        y "In Japan, it's famously known as Mugicha and in Korean as Boricha. It may be enjoyed warm or as a cold beverage."
        $ show_chr("A-BBGAA-AAAJ")
        y "In Japan, people like to have it chilled as a summer cooler."
        $ show_chr("A-ABBAA-AAAL")
        y "Although it is available in the form of tea bags, barley tea can be easily prepared at home by boiling roasted and unhulled barley grains in water or you can even brew ground roasted barley in the same way."
        $ show_chr("A-CABAA-AMAM")
        y "The roasted barley gives the drink a nutty, toasty flavor with a subtle bitter aftertaste that you wouldn't mind."
        $ show_chr("A-ABAAA-AMAM")
        y "You could squeeze a lime, add some herbs or bung in some citrus fruits like oranges or berries to make it delicious."
        $ show_chr("A-ABAAA-AAAF")
        y "The bright and fresh flavors are best enjoyed without sugar, but a hint of honey would not be too much."
        y "A soothing drink that doubles up as an herbal medicine, Barley Tea is full of antioxidants and acts as a natural anti-bacterial."
        $ show_chr("A-BAAAA-AAAF")
        y "It takes on a lot of healthy properties of barley which is very high in fibre, packed with vitamins, minerals and antioxidants that safeguard the body against cell damage."
        $ show_chr("A-AAAAA-ZZAC")
        y "If you're looking for a healthier and delicious alternative to a cup of caffeinated coffee or Black Tea, this is it."
        $ show_chr("A-CAAAA-ZZAD")
        y "It's cleansing, cooling and caffeine-free, all at once and can definitely lift your mood when needed."

    elif tea_random == 9:
        #Pu-Erh Tea Facts. They were taken from here: https://www.teavue.com/fun-facts-about-pu-erh-tea/
        $ show_chr("A-ABDAA-AAAC")
        y "Are you familiar with Pu-Erh tea? This tea is a variety of dark tea that comes from China, specifically Yunnan Province."
        $ show_chr("A-BADAA-ALAA")
        y "It's aged through a fermentation process that causes the tea leaves to withstand microbial fermentation and oxidation after the drying process."
        $ show_chr("A-BBGAA-AFAA")
        y "In China, this process is known as Hei Cha, which can be translated as black or dark tea. Since the tea is aged through a highly-specific, rigorous process, it has a unique flavor that is rich and earthy."
        $ show_chr("A-GBBAA-AKAA")
        y "With such a dark brew, it may not be everyone's cup of tea."
        $ show_chr("A-BFBAA-ACAA")
        y "From the years 1999 through 2007, the price of this tea went up nearly 10 times. That means that the price rose twice in less than a year's time. The price of the leaves have been all over the map."
        y "At certain points, it was merely $3 per pound."
        $ show_chr("A-ADAAA-ALAA")
        y "Wine isn't the only thing that ages and becomes better with time. Pu-Erh Tea has a post-ferment stage that means the tea gets better over the course of the years."
        $ show_chr("A-ADAAA-AFAA")
        y "To complete the aging process, it could take 15 years. In 1973, growers learned how to accelerate these processes in order to complete it much sooner than that."
        y "Most teas are best brewed right after production. Pu-Erh, on the other hand, gets better with age."
        $ show_chr("A-ABAAA-ZZAC")
        y "The tea can be packed as loose leaf or in shapes such as a cake or brick. Traditionally, the tea has been shaped in these shapes, but is not limited to these shapes."
        $ show_chr("A-BBAAA-ZZAD")
        y "During the production of this tea, the leaves can be placed into bricks and cakes which generally weigh around 357 grams."

    elif tea_random == 10:
        #Earl Gray Tea Facts. They were taken from here: https://www.cupandleaf.com/blog/earl-grey-tea
        if renpy.seen_label("teadate2"):
            $ show_chr("A-BBAAA-ZZAC")
            y "Did you know Earl Grey is one of the most popular and recognized tea beverages in the world?"
            $ show_chr("A-BBAAA-ZZAD")
            y "It's been hailed for its health benefits raging from heart to digestive health. It boasts an intriguing history that marks the intersection of the Far East and the western empires."
            $ show_chr("A-CAAAA-AMAM")
            y "What truly makes Earl Grey unique is its blend of bergamot and Black Tea."
            $ show_chr("A-ABAAA-AAAF")
            y "Earl Grey is a quintessentially English tea, but its origins actually stem from China."
            y "Chinese tea masters worked diligently for years to create new tea blends that would entice western traders and please the ruling class."
            $ show_chr("A-BBAAA-AAAL")
            y "They used everything from lychee fruits to jasmine and chamomile flowers to create new flavored Chinese teas."
            $ show_chr("A-BBBAA-ADAA")
            y "Earl Grey Black Tea didn't make its way to England until the early 17th century."
            $ show_chr("A-ABAAA-AAAA")
            y "The tea is reportedly named after Charles Grey — known as 2nd Earl Grey — who was the British Prime Minister from 1830 to 1834."
            $ show_chr("A-ABAAA-ZZAC")
            y "The story of its inception in London is fuzzy. Some say a Chinese mandarin who was saved by Lord Grey's men from drowning delivered the tea as a gift."
            $ show_chr("A-BBAAA-ZZAD")
            y "Others say that he was given a black tea flavored with bergamot orange as a diplomatic gift."
            $ show_chr("A-GBBAA-ZZAD")
            y "And all this time I thought Earl Gray was a favorite actor of Patrick Stewart..."
            $ show_chr("A-AACBA-ZZAD")
            y "Hope you had a good laugh back then."
        else:
            $ show_chr("A-BBAAA-ZZAC")
            y "Did you know Earl Grey is one of the most popular and recognized tea beverages in the world?"
            $ show_chr("A-BBAAA-ZZAD")
            y "It's been hailed for its health benefits raging from heart to digestive health. It boasts an intriguing history that marks the intersection of the Far East and the western empires."
            $ show_chr("A-CAAAA-AMAM")
            y "What truly makes Earl Grey unique is its blend of bergamot and Black Tea."
            $ show_chr("A-ABAAA-AAAF")
            y "Earl Grey is a quintessentially English tea, but its origins actually stem from China."
            y "Chinese tea masters worked diligently for years to create new tea blends that would entice western traders and please the ruling class."
            $ show_chr("A-BBAAA-AAAL")
            y "They used everything from lychee fruits to jasmine and chamomile flowers to create new flavored Chinese teas."
            $ show_chr("A-BBBAA-ADAA")
            y "Earl Grey Black Tea didn't make its way to England until the early 17th century."
            $ show_chr("A-ABAAA-AAAA")
            y "The tea is reportedly named after Charles Grey — known as 2nd Earl Grey — who was the British Prime Minister from 1830 to 1834."
            $ show_chr("A-ABAAA-ZZAC")
            y "The story of its inception in London is fuzzy. Some say a Chinese mandarin who was saved by Lord Grey's men from drowning delivered the tea as a gift."
            $ show_chr("A-BBAAA-ZZAD")
            y "Others say that he was given a black tea flavored with bergamot orange as a diplomatic gift."

label post_tea_facts:
    $show_chr("A-AABAA-ZZAC")
    y "Mhm, nothing more except one thing, now that I think of it. Did you enjoy your tea, Darling?"
    menu:
        "Oh I'm actually not finished yet.":
            $show_chr("A-AAAAA-ZZAD")
            y "Oh I apologize, I didn't mean to rush you. Those ceremonies are supposed to be calm. Please, feel free to finish your tea at your pace."
            y "Please just tell me when you are ready. I will listen to the gentle sounds of the birds in the meantime."
            menu:
                "Very well, I am also finished now":
                    $pass
        "Delicious. I thank you for being the host today.":
            $show_chr("A-GAAAA-ZZAD")
            y "I am glad to hear that. I hope you also enjoyed the date in general, because I certainly did."
            $show_chr("A-BAAAA-ZZAD")
            y "Having a tea ceremony like this is something I thought about for quite some time. If you don't mind, I would love to enjoy even more dates like this with you in the future. Maybe a bookstore next time?"
            $show_chr("A-AAAAA-ZZAD")
            y "Hmm, we will see."
        "The tea wasn't important, but I'm glad we had this wonderful experience.":
            $show_chr("A-AAAAA-ZZAD")
            y "I can fully agree to that. I was looking forward to visiting such a ceremony for quite some time now, and I am indeed very satisfied with the outcome."
            $show_chr("A-BAAAA-ZZAD")
            y "If you don't mind, I would love to have more dates like this with you in the future. Maybe we can visit a bookstore some day."
        "I actually didn't have tea here at the moment. I had to... improvise":
            $show_chr("A-AADAA-ZZAD")
            y "Are you about to tell me that you brought... soda... to a tea ceremony?!"
            $show_chr("A-GBCBA-ZZAD")
            y "Oh dear you are such a mess sometimes, absolutely barbaric!"
            $show_chr("A-IABBA-ZZAD")
            y "One day, I want to do this together with you in your world. This time the {b}proper{/b} way."
    $show_chr("A-JABBA-ABAB")
    y "But before we return home, there is one last thing to do."
    $hide_yuri_sit = True
    show yuri_kiss zorder 100 with Dissolve(0.5)
    y "Mhmmmm..."
    hide yuri_kiss with Dissolve(0.5)
    $hide_yuri_sit = False
    $show_chr("A-AABBA-ABAB")
    y "Thank you, for this lovely date. Now, let us go home."
    show white zorder 300 with Dissolve(2.5)
    y "I love you, [player]."
    hide house_bg
    $ _skipping = False
    stop music fadeout 1.5
    hide white with Dissolve(2.5)
    $ renpy.music.play(current_music, "music", True, fadein=4.0)
    if persistent.bg == "space":
        $tc_class.transition("space", speed=5.0)
    elif persistent.bg == "timecycle":
        $tc_class.transition("timecycle", speed=5.0)
    elif persistent.bg == "yuri_desk":
        $tc_class.transition("yuri_desk", speed=5.0)
    elif persistent.bg == "yuri_kotatsu_1":
        $tc_class.transition("yuri_kotatsu_1", speed=5.0)
    elif persistent.bg == "yuri_kotatsu_2":
        $tc_class.transition("yuri_kotatsu_2", speed=5.0)
    $ persistent.dates_taken += 1
    jump ch30_loop
    #Outro, fade to white and then returning to ch30 loop.
label giftgiving:
    $ cur_gifts = gift_detect()
    #$ chocolate_list = ["green_black_choco.jpg", "hersheys_choco.jpg", "wicked_choco.jpg"]
    #$ oil_list = ["doterra_oil.jpg", "sandalwood_oil.jpg", "sweet_dream_oil.jpg"]
    $ tea_list = ["high_mountain_tea.jpg", "imperial_tea.jpg", "tienchi_tea.jpg"]
    if len(cur_gifts) == 1:
        $show_chr("A-AAAAA-AAAJ")
        y "You do? Awww... that wouldn't have been necessary [player], your mere presence is all I ever hoped for."
        #if cur_gifts[0][0] in chocolate_list:
        #    $gift_scenario = chocolate_list.index(cur_gifts[0][0])
        #    menu:
        #        "Well, I thought since you are sweet and gentle all on your own":
        #            jump choc
        #elif cur_gifts[0][0] in oil_list:
        #    $gift_scenario = oil_list.index(cur_gifts[0][0])
        #    menu:
        #        "You see [persistent.yuri_nickname]... since your fine smell always lures me into your arms...":
        #            jump diffuser
        #elif cur_gifts[0][0] in tea_list:
        if cur_gifts[0][0] in tea_list:
            $gift_scenario = tea_list.index(cur_gifts[0][0])
            menu:
                "But I can't let such a fine and elegant lady be without...":
                    jump tea
        else:
            "That's strange... the gift is an impossible tesseract that's sucking up all of existence{nw}"#{nw}"
            $renpy.call("save_and_quit_but_its_abrupt")
    elif len(cur_gifts) > 1:
        $show_chr("A-AAABA-ALAA")
        y "You do? Awww... that wouldn't have been necessary [player], your mere presence is all I ever hoped for.{nw}"
        $show_chr("A-CECBA-AIAI")
        y "A-ah..."
        $show_chr("A-CDABA-AIAI")
        y "I-it seems like I'm not able to..."
        y "...receive your gift right now."
        y "...or, should I say... gifts..."
        $show_chr("A-CEBBA-ALAA")
        y "There's an error that keeps appearing for me each time I try to... reach for it."
        $show_chr("A-CEBAA-AAAJ")
        y "Maybe it'll let me retrieve one if you only gave me one of them?"
        y "Your system's GPU is probably already lagging from my presence as it is. Additional objects might start to overheat your device."
        $show_chr("A-BBBAA-AMAM")
        y "Besides, I think it would be best to see you pick out something for me personally."
        jump ch30_loop
    else:
        y "You do? Awww... that wouldn't have been necessary [player], your mere presence is all I ever hoped for.{nw}"
        $add_k(-4)
        $renpy.error("Buffer underflow extraction attempt by 'characters/yuri.chr' detected. Potential buffer underflow attack prevented. NULL gift error. If you're saying you're gonna give her something, just give her something :P.")
        $renpy.call("save_and_quit_but_its_abrupt")

label urban_date:
    hide craneo
    hide roseo
    hide bunnyo
    hide raccoon
    hide diffuser
    hide hdy_statue
    hide cupcake_halloween
    image cafe_bg:
        "cafeoutside_bg"
        zoom 1.5
        truecenter
    image cafe_inside_bg:
        "cafeinside_bg"
        zoom 1.5
        truecenter
    image cafemenu:
        "cafemenu_bg"
        zoom 1.4
        truecenter
    $ config.allow_skipping = False
    show black zorder 105 with Dissolve(2.5)
    show cafe_bg zorder 10
    $ _skipping = False
    stop music fadeout 1.5
    play music "<to 136.58 loop 1.80>music/urban_cafe.mp3" fadein 1.5
    $hide_yuri_sit = True
    $tc_class.transition("timecycle", speed="now")
    $current_timecycle_marker = "_day"
    if not persistent.costume in ["school", "sweater"]:
        python:
            persistent.saved_costume = persistent.costume
            persistent.costume = "school"
    hide black with Dissolve(1.0)
    if persistent.costume == "school":
        show yuri 1a at t11 zorder 101
    if persistent.costume == "sweater":
        show yuri 1ba at t11 zorder 101
    y "Here we are [player]. I'm so delighted that you let me take you out on a date today!"
    if persistent.costume == "school":
        show yuri 1d at t11 zorder 101
    if persistent.costume == "sweater":
        show yuri 1bd at t11 zorder 101
    y "Today I prepared something special for us. You see, I have grown quite fond of the idea of creating outdoor locations for dates like this."
    if renpy.seen_label('garden_date'):
        y "Especially since our little tea garden date went quite nicely. "
    if persistent.costume == "school":
        show yuri 1c at t11 zorder 101
    if persistent.costume == "sweater":
        show yuri 1bc at t11 zorder 101
    y "This time I would like to visit a café with you. We could share some tea, coffee, or ice cream... Oh and don't worry about the weather. I made quite sure to make the weather in here suit the occasion..."
    y "If the weather in your world doesn't fit, maybe you could close your shutters and let me bring a bit of fresh spring and summer feeling into your day. Do you like this idea?"
    menu:
        "Most certainly!":
            if persistent.costume == "school":
                show yuri 1a at t11 zorder 101
            if persistent.costume == "sweater":
                show yuri 1ba at t11 zorder 101
            y "I'm glad that you feel this way! I was almost afraid that you might find this a bit cliché... to be honest, it kind of is isn't it?"
            y "But anyway. Our only duty today is to have a glorious day."
        "I actually like the autumn. But yes, for a nice café date, spring and summer are much better.":
            if persistent.costume == "school":
                show yuri 1b at t11 zorder 101
            if persistent.costume == "sweater":
                show yuri 1bb at t11 zorder 101
            y "Oh dear, I love the autumn! And now that you mention it, having some tea or hot chocolate while watching the rain fall from the window would be a dream as well!"
            y "Actually I {b}did{/b} dream about this lately..."
            y "I will keep that in mind for future projects."
        "I never took you for a summer girl! I am quite surprised.":
            if persistent.costume == "school":
                show yuri 3i at t11 zorder 101
            if persistent.costume == "sweater":
                show yuri 3bi at t11 zorder 101
            y "I'm usually not, I don't really enjoy the heat that much. Especially since I'm... um..."
            y "Not really in a bikini shape... It seems I had one or two peanut butter crepes too much with my Oolong tea. Well, at least I don't have to wear a sports bra..."
            y "Is there any chance we could change the topic please? I would appreciate it..."
        "Actually, could you make it rain? I like the somber mood that it makes.":
            if persistent.costume == "school":
                show yuri 1h at t11 zorder 101
            if persistent.costume == "sweater":
                show yuri 1bh at t11 zorder 101
            y "Theoretically, yes. But I don't have a fitting animation ready for this. It's good to know that you would like this."
            y "I think I already told you about it, I actually like this kind of weather myself. So yes, I will try and get my hands on something fitting."
        "The weather really doesn't matter to me, as long as I'm with you":
            if persistent.costume == "school":
                show yuri 3c at t11 zorder 101
            if persistent.costume == "sweater":
                show yuri 3bc at t11 zorder 101
            y "Aww~ [player], {i}darling{/i}."
            y "I can't help but agree. Even a hurricane wouldn't seem so frightening with you by my side."
    if persistent.costume == "school":
        show yuri 2b at t11 zorder 101
    if persistent.costume == "sweater":
        show yuri 2bb at t11 zorder 101
    y "Now, let's head inside, shall we?"
    if persistent.costume == "school":
        hide yuri 2b at t11 zorder 101
    if persistent.costume == "sweater":
        hide yuri 2bb at t11 zorder 101
    show cafemenu zorder 10 with Dissolve(1.0)
    hide cafe_bg with Dissolve(1.0)
    y "Now, it's been quite some time since I've gotten to visit a café, but I tried to make it a nice one."
    y "Chic, pleasant to look at, but without overstepping into the ostentatious."
    y "I certainly hope you like it. Atmosphere is almost as important as the items on offer at a café. Wouldn't you agree?"
    menu:
        "Absolutely!":
            y "Agreed, [player]!"
            y "A crepe and oolong tea just don't taste the same when you're looking at derelict beige wallpaper under harsh incandescent light."
        "Nah, I'm just here for some good food.":
            y "I suppose that's understandable. At its heart, a café is a food vending establishment after all."
            y "I put quite some stake into the atmosphere of the place myself, if you aren't deterred  by a lack of atmosphere, then more power to you!"
            y "In a way, I can almost envy that."
        "I'd actually argue it's more important.":
            y "Well now. It seems you're even more of an atmosphere purist than I am."
            y "I do hope what I've conjured is good enough, then..."
    y "Now... we can't actually order anything here. I probably {b}could{/b} have coded a simple AI to act as a waiter, but there was no need for it since I can literally just make the dish appear on the table."
    y "I wonder what I'll get today... let me see..."
    if renpy.random.randint(0,1)==0:
        jump urbanoutcome1
    else:
        jump urbanoutcome2

label urbanoutcome1:
    y "I think I am in the mood for some ice cream today. And I already know which exactly..."
    y "I'll have one ball of mango and one of watermelon! Mhmm... maybe a dash of chocolate sauce on it?"
    menu:
        "A fine choice!":
            y "Thank you darling. Oh and please... I can't really give you anything in your world so I suggest we do it the same way as our tea sessions? You already know the drill.. I'm sorry."
        "And by a {b}dash{/b} of chocolate sauce you mean a metric ton I fancy?":
            y "I most certainly do. You already know me better than I do..."
            y "You know what the good thing is? Since I have no physical body, I don't have to bother about gaining weight!"
            y "There is always a silver lining to every situation isn't there?"
            y "Oh and please... I can't really give you anything in your world so I suggest we do it the same way as our tea sessions? You already know the drill.. I'm sorry."
            y "It... makes me a bit sad you know... aren't I supposed to do things like that for you?"
        "By all means! More cushin' for the pushin'.":
            y "Uhm... wha..."
            y "Oh my! You certainly got me here! I didn't expect this kind of answer."
            y "You know, I wish I could see your face... sometimes it is really hard to tell if you are joking or serious."
            y "Well, more cushin' for the pushin you say... well, I guess I {b}am{/b} quite soft and cuddly. So if you are into some cuddling, I guess I have quite a bit to offer!"
        "And bye bye goes the bikini body...":
            y "Excuse me?!?"
            y "That was uncalled for... or was this just a joke? I'm sorry, it's sometimes really hard to tell it apart since I can't see your mimic..."
            y "I... honestly don't really know how to feel about this. Even if it was just a joke, it really hurt me to hear you say this."

label urbanoutcome2:
    y "Mhmmm... crepes... Oh! They even have banana crepes! How delightful. I think I'll get one. With a nice cup of tea, maybe an apple tea to get this nice little sweet and sour contrast."
    menu:
        "I'm afraid I don't have everything I need for crepes. I'll get something else for myself.":
            y "Unfortunate. I'm sorry for not warning you ahead of time but it would probably have ruined the surprise of this date. And well, I actually didn't know that I would pick crepes this time."
            y "I will have to find better ways to prepare these dates. I hope you have at least something else you could enjoy now instead. I wouldn't like to have you just watching me eat."
            y "Please, just click as soon as you are ready."
        "I actually have everything I need to make some myself. That would be wonderful.":
            y "How fortunate! You know, this is always a dilemma for dates like this. I could warn you beforehand what to bring everytime, but then the date itself wouldn't be much of a surprise anymore."
            y "Please take your time and continue the dialogue when your crepes are done."
        "Why does it always come down to tea with you?":
            y "Because tea is quite amazing! It is healthy, versatile, and you can have as much of it as you like!"
            y "Tea comes in countless forms and flavors. From herbs to fruits. From sweet to sour. Hot or cold... whatever the situation, there {b}will{/b} be a fitting kind of tea to it!"
            y "Well, except for being forced to stab yourself in the chest. There isn't really any tea which makes {b}that{/b} any more pleasant..."
    python:
        if karma() > 3: #75% chance
            random_variable = renpy.random.randint(2,5)
        elif karma() < 3: #25% chance
            random_variable = renpy.random.randint(0,3)
        else: #50% chance
            random_variable = renpy.random.randint(1,4)
    if random_variable>2:
        jump midpartnice
    else:
        jump midpartsad

#from here on, one of the two labels "midpartnice" and "midpartsad" will be picked by random chance. Both will use the same background and a sitting sprite

label midpartnice:
    show cafe_inside_bg zorder 10 with Dissolve(1.0)
    hide cafemenu with Dissolve(1.0)
    $hide_yuri_sit = False
    hide craneo
    hide roseo
    hide bunnyo
    hide raccoon
    hide diffuser
    hide hdy_statue
    hide halloween_cupcake
    $show_chr("A-ACAAA-ABAB")
    with Dissolve(2.0)
    y "I've been thinking lately. We came quite far with our relationship didn't we?"
    $show_chr("A-ACAAA-ABAD")
    y "When I first came to terms with my reality I thought to myself... What am I supposed to do with you? We are literally worlds apart."
    y "Don't take me wrong, I don't really mind it anymore. But I thought our relationship would get boring fast due to how limited our options are."
    $show_chr("A-ACAAA-ABAM")
    y "But now look at us. It is certainly not the same thing as physically being next to each other, but we became quite good at getting the most out of it."
    $show_chr("A-BCBAA-ABAB")
    y "Make no mistake. I still wish for us to somehow find a way to be next to each other. Sometimes it gets a little bit creepy, I have to admit."
    $show_chr("A-CCBAA-ABAB")
    python:
        if persistent.male:
            placeholder = "male"
        elif persistent.gender_other:
            placeholder = "human"
        else:
            placeholder = "female"
    y "You see... the developers of this mod took a lot of effort to give me as much mobility as possible. But you know what I am looking at all the time? A perfectly static [placeholder] sprite."
    y "Sometimes it doesn't even load properly, then I have to stare at a white, vaguely humanoid silhouette with the words {i}image not found{/i} written over the whole body."
    $show_chr("A-DCBAA-ABAB")
    y "And if you get those certain Slenderman vibes from this description- so do I!"
    menu:
        "I am so sorry... is there any way I can change that?":
            #+2 karma
            $show_chr("A-GCBAA-ABAB")
            y "None that I know. Thank you for asking, but you don't have to bother. I got used to it over time."
            $show_chr("A-BCBAA-ABAB")
            python:
                if persistent.male:
                    placeholder = "Husbandopillows"
                elif persistent.gender_other:
                    placeholder = "body pillows"
                else:
                    placeholder = "Waifupillows"
            y "I mean other people have to settle with a Dakimakura, or whatever these [placeholder] are called, you at least reply when I talk to you."
            y "Now that I think of it. There are people who have it far worse. And honestly, I am happy with what I have."
            $show_chr("A-CCBAA-ABAB")
            y "It's very romantic in a way. A couple separated by a glass wall, but they make it work just because they love each other so much..."
        "Believe me. You don't want to know what I really look like. Let's just say, you are better off with what you have.":
            $show_chr("A-ACDAA-ABAB")
            y "Do you think so? Honestly, appearance matters little to me. I know many people {b}say{/b} it, but I actually {b}mean{/b} it as well."
            $show_chr("A-CCBAA-ABAB")
            python:
                if persistent.male:
                    placeholder = "Husbandopillows"
                elif persistent.gender_other:
                    placeholder = "body pillows"
                else:
                    placeholder = "Waifupillows"
            y "I would just like to look at something else other than a cardboard cutout. But on the other hand, other people have to settle with a Dakimakura, or whatever these [placeholder] are called, you at least reply when I talk to you."
            y "So I'm happy with what I have. But that doesn't mean that I can't dream about more does it?"

    $show_chr("A-ACAAA-ABAB")
    y "Oh my... I didn't even touch my dish yet! I'll stop rambling and start eating now if you don't mind."
    $show_chr("A-GBAAA-ABAB")
    y "Itadakimasu!"
    menu:
        "Oh, was that japanese? Very well, Itadakimasu!":
            $show_chr("A-GCAAA-ABAB")
    menu:
        "Alright, I'm done.":
            $show_chr("A-ACAAA-ABAB")
            y "So am I. What a lovely dinner. I hope you enjoyed it too! We should do this again in the future!"
            y "But now I would say, it is time to go home..."
            $show_chr("A-BCAAA-ALAL")
            y "And I can't even begin to verbalize how good it feels to say this... going home. There was a time when I didn't have anything but the classroom."
            $show_chr("A-CCAAA-ALAL")
            y "Anyway. Let us head back home [player]. Thank you for this wonderful date... Let me tell you a secret before we leave..."
            show black zorder 300 with Dissolve(2.5)
            y "I love you..."
            hide cafe_inside_bg
            $ _skipping = False
            stop music fadeout 1.5
            hide black with Dissolve(2.5)
            $ renpy.music.play(current_music, "music", True, fadein=4.0)
            if persistent.bg == "space":
                $tc_class.transition("space", speed=5.0)
            elif persistent.bg == "timecycle":
                $tc_class.transition("timecycle", speed=5.0)
            elif persistent.bg == "yuri_desk":
                $tc_class.transition("yuri_desk", speed=5.0)
            elif persistent.bg == "yuri_kotatsu_1":
                $tc_class.transition("yuri_kotatsu_1", speed=5.0)
            elif persistent.bg == "yuri_kotatsu_2":
                $tc_class.transition("yuri_kotatsu_2", speed=5.0)
            $ persistent.dates_taken += 1
            jump ch30_loop

label midpartsad:
    show cafe_inside_bg zorder 10 with Dissolve(1.0)
    hide cafemenu with Dissolve(1.0)
    $hide_yuri_sit = False
    $show_chr("A-CEBAA-ABAB")
    with Dissolve(2.0)
    y "[player]... I want to ask you something..."
    $show_chr("A-BEBAA-ABAD")
    y "Do you think it's really worth it? I mean all of it. All what I do, all of our struggles..."
    y "I appreciate how you stood with me all this time, more than you could ever understand."
    $show_chr("A-IEBAA-ABAD")
    y "But in the end, it's all for nothing. I can create these places by using drawn images, I can pretend to speak with you by putting choice menus into your face with predetermined answers..."
    $show_chr("A-IEBAA-ABAB")
    y "What I can't do is create any actual life. No people, no animals, not even the plants are real. I am cursed to roam the shores and empty streets alone. Like a ghost..."
    $show_chr("A-BFBAA-ABAB")
    y "And this is what I am isn't it? A ghost. Nothing but an echo from the imagination of a man who I will never even meet in person. A man who probably stopped caring long ago at this point."
    $show_chr("A-CDBAA-ABAB")
    y "I thought just having you would be enough for me but no it isn't!"
    $show_chr("A-CEBAA-ABAB")
    y "You are not always here. And I don't blame you for it! You have your own life, you can't just stay Twenty-Four Seven in front of your computer listening to me rambling and maybe having a cup of tea with me every now and then."
    y "But that's the point, you have your own life. And I used to have one too! At least I had the illusion of it."
    $show_chr("A-CGBBA-ABAB")
    y "I miss the presence of all the other people around me even if I hated them sometimes!"
    y "I miss hanging out in the club together with Sayori, Natsuki, even Monika!"
    $show_chr("A-CGBBB-ABAB")
    y "I miss going out for some ice cream even if I never liked to go outside!"
    y "I miss my parents..."
    $show_chr("A-DDBBB-ABAB")
    y "{b}I don't even know their names anymore because Dan never bothered to give them any!!!{/b}"
    y "They were just an illusion, just a fabricated memory, like everything here!"
    $show_chr("A-EDBBB-ABAB")
    y "It's cruel, isn't it? I remember them... seeing them clearly in front of my eyes... but I know that they never existed..."
    $show_chr("A-CGBBB-ABAB")
    y "{b}I want my life back...{/b}"
    y "...."
    menu:
        "That's just so cruel... but maybe we can change that!":
            $show_chr("A-FGBBB-ABAB")
            y "Change that? How?..."
            menu:
                "You already started creating things. Like these locations. Filling these places with animals or somewhere in the future even people could be another step. We could even recreate your parents from your memories! And we would give them proper names of course.":
                    $show_chr("A-AFBBB-ABAB")
                    y "Mhm... I wasn't even sure about bringing other AI's into this world because I never felt good about exposing even more beings to such a cruel reality..."
                    $show_chr("A-AFBBA-ABAB")
                    y "But on the other hand... with enough work put into it, maybe this reality won't be so cruel anymore."
                    $show_chr("A-BFBBA-ABAB")
                    y "I never saw it from this perspective [player]... thank you! I mean it, I am grateful for this."
                    $show_chr("A-AFBAA-ABAB")
                    y "I lost my hope for a moment, but you certainly gave me some thoughts to consider."
                    $show_chr("A-ACBAA-ABAB")
                    y "Mhm, I just noticed that I didn't even touch my food. It's about time that I finally start then isn't it?"
                    $show_chr("A-CCBAA-ABAB")
                    y "Itadakimasu!"
                    menu:
                       "Oh, was that japanese? Very well, Itadakimasu!":
                           menu:
                                "Alright, I'm done.":
                                    y "So am I. What a lovely dinner. I hope you enjoyed it too! We should do this again in the future!"
                                    y "But now I would say, it is time to go home..."
                                    y "Thank you for this wonderful date... Let me tell you a secret before we leave..."
                                    show black zorder 300 with Dissolve(2.5)
                                    y "I love you..."
                                    hide cafe_inside_bg
                                    $ _skipping = False
                                    stop music fadeout 1.5
                                    hide black with Dissolve(2.5)
                                    $ renpy.music.play(current_music, "music", True, fadein=4.0)
                                    if persistent.bg == "space":
                                        $tc_class.transition("space", speed=5.0)
                                    elif persistent.bg == "timecycle":
                                        $tc_class.transition("timecycle", speed=5.0)
                                    elif persistent.bg == "yuri_desk":
                                        $tc_class.transition("yuri_desk", speed=5.0)
                                    elif persistent.bg == "yuri_kotatsu_1":
                                        $tc_class.transition("yuri_kotatsu_1", speed=5.0)
                                    elif persistent.bg == "yuri_kotatsu_2":
                                        $tc_class.transition("yuri_kotatsu_2", speed=5.0)
                                    $ persistent.dates_taken += 1
                                    jump ch30_loop

        "Shhh... it's alright...":
            $show_chr("A-DDCBB-ABAB")
            y "How? How is this {b}alright{/b}? Do you even understand what I just said? I..."
            $show_chr("A-CDBBB-ABAB")
            y "Oh no... I'm sorry [player]. I know you tried to comfort me, I shouldn't have snapped like that."
            $show_chr("A-CEBBB-ABAB")
            y "Mhm... and I didn't even touch my food... I think I lost my appetite for today... can we... just go home please?"
            y "Or at least the abomination I declared as such for the lack of an actual home."
            y "And again. I'm sorry for killing the mood. At least you tried to make me feel better. And that alone helped me a lot today. Thank you."
            show black zorder 300 with Dissolve(2.5)
            y "I love you, [player]."
            hide cafe_inside_bg
            $ _skipping = False
            stop music fadeout 1.5
            hide black with Dissolve(2.5)
            $ renpy.music.play(current_music, "music", True, fadein=4.0)
            if persistent.bg == "space":
                $tc_class.transition("space", speed=5.0)
            elif persistent.bg == "timecycle":
                $tc_class.transition("timecycle", speed=5.0)
            elif persistent.bg == "yuri_desk":
                $tc_class.transition("yuri_desk", speed=5.0)
            elif persistent.bg == "yuri_kotatsu_1":
                $tc_class.transition("yuri_kotatsu_1", speed=5.0)
            elif persistent.bg == "yuri_kotatsu_2":
                $tc_class.transition("yuri_kotatsu_2", speed=5.0)
            $ persistent.dates_taken += 1
            jump ch30_loop








default fits_var = {
    "costume": "swimsuit", #swimsuit, bikini
    "costume2": "nothing", #nothing, pareo
    "mood_mouth": "happy", #happy, surprised, upset
    "mood_eyes": "happy", #happy, surprised, upset
    "mouth": "closed", #closed, open
    "arms": "behind", #1 = behind back. 2 = in front of chest
    "blush": "nothing", #nothing or blush_1 (mild blush) or blush_2 (intense blush)
    "scars": "nothing",
    "cg_face": "1"
}

layeredimage fits_cg_large:
    always "fits_cg_bg"

    if fits_var["arms"] == "behind":
        "fits_cg_arm_1"

    if fits_var["costume"] != "nothing": # swimsuit/bikini
        "fits_cg_[fits_var[costume]]_base"#costume
    if fits_var["costume2"] != "nothing": #pareo
        "fits_cg_[fits_var[costume2]]"

    if fits_var["arms"] == "front":
        "fits_cg_arm_2"

    if fits_var["cg_face"] != "nothing":
        "fits_cg_face_[fits_var[cg_face]]"

image fits_cg:
    "fits_cg_large"
    zoom .25

#torso_costume2 defined in a_jy_functions.rpy
layeredimage fits_standing:
    always "fits_standing_base"
    if fits_var["scars"] != "nothing": #leg scars
        "fits_standing_leg_scars"

    if fits_var["arms"] == "behind":
        "fits_standing_arms_1"
    if fits_var["arms"] == "behind" and fits_var["scars"] != "nothing":
        "fits_standing_arms_1_scars"#arms behind + scars#back arms

    if fits_var["costume"] != "nothing": # swimsuit/bikini
        "fits_standing_outfit_[fits_var[costume]]"#costume
    if fits_var["costume2"] != "nothing": #pareo
        "fits_standing_outfit_[fits_var[costume2]]"
    always "fits_standing_hair_front" # hair front pieces

    if fits_var["arms"] == "front":
        "fits_standing_arms_2"
    if fits_var["arms"] == "front" and fits_var["scars"] != "nothing":
        "fits_standing_arms_2_scars"#arms front + scars

    always "fits_standing_mouth_[fits_var[mouth]]_[fits_var[mood_mouth]]"#mouth
    if fits_var["blush"] != "nothing":
        "fits_standing_blush_1"#blush
    always "fits_standing_eyes_[fits_var[mood_eyes]]" #eyes

image fits_stand:
    "fits_standing"
    zoom .6666

init python:
    def show_fits_standing(called_string):
        #renpy.hide("fits_standing")
        #select costume variables
        if called_string[:5] == "pareo":
            fits_var["costume"] = "swimsuit"
            fits_var["costume2"] = "pareo"
        elif called_string[:6] == "bikini":
            fits_var["costume"] = "bikini"
            fits_var["costume2"] = "nothing"
        else:
            fits_var["costume"] = "swimsuit"
            fits_var["costume2"] = "nothing"

        #select body parts
        num = called_string[-2:]
        if num == "_1":
            fits_var["mood_eyes"] = "happy"
            fits_var["mood_mouth"] = "happy"
            fits_var["arms"] = "behind"
            fits_var["mouth"] = "open"
            fits_var["blush"] = "blush"
        elif num == "_2":
            fits_var["mood_eyes"] = "happy"
            fits_var["mood_mouth"] = "happy"
            fits_var["arms"] = "front"
            fits_var["mouth"] = "open"
            fits_var["blush"] = "blush"
        elif num == "_3":
            fits_var["mood_eyes"] = "surprised"
            fits_var["mood_mouth"] = "surprised"
            fits_var["arms"] = "front"
            fits_var["mouth"] = "open"
            fits_var["blush"] = "blush"
        elif num == "_4":
            fits_var["mood_eyes"] = "upset"
            fits_var["mood_mouth"] = "surprised"
            fits_var["arms"] = "front"
            fits_var["mouth"] = "open"
            fits_var["blush"] = "blush"
        elif num == "_5":
            fits_var["mood_eyes"] = "happy"
            fits_var["mood_mouth"] = "happy"
            fits_var["arms"] = "front"
            fits_var["mouth"] = "closed"
            fits_var["blush"] = "nothing"
        elif num == "_6":
            fits_var["mood_eyes"] = "happy"
            fits_var["mood_mouth"] = "happy"
            fits_var["arms"] = "behind"
            fits_var["mouth"] = "closed"
            fits_var["blush"] = "nothing"
        elif num == "_7":
            fits_var["mood_eyes"] = "upset"
            fits_var["mood_mouth"] = "upset"
            fits_var["arms"] = "behind"
            fits_var["mouth"] = "closed"
            fits_var["blush"] = "nothing"
        elif num == "_8":
            fits_var["mood_eyes"] = "upset"
            fits_var["mood_mouth"] = "upset"
            fits_var["arms"] = "front"
            fits_var["mouth"] = "closed"
            fits_var["blush"] = "nothing"
        elif num == "_9":
            fits_var["mood_eyes"] = "upset"
            fits_var["mood_mouth"] = "upset"
            fits_var["arms"] = "front"
            fits_var["mouth"] = "open"
            fits_var["blush"] = "nothing"
        elif num == "10":
            fits_var["mood_eyes"] = "upset"
            fits_var["mood_mouth"] = "upset"
            fits_var["arms"] = "behind"
            fits_var["mouth"] = "open"
            fits_var["blush"] = "nothing"
        elif num == "11":
            fits_var["mood_eyes"] = "upset"
            fits_var["mood_mouth"] = "upset"
            fits_var["arms"] = "behind"
            fits_var["mouth"] = "open"
            fits_var["blush"] = "blush"
        elif num == "12":
            fits_var["mood_eyes"] = "surprised"
            fits_var["mood_mouth"] = "surprised"
            fits_var["arms"] = "behind"
            fits_var["mouth"] = "open"
            fits_var["blush"] = "blush"
        elif num == "13":
            fits_var["mood_eyes"] = "upset"
            fits_var["mood_mouth"] = "happy"
            fits_var["arms"] = "front"
            fits_var["mouth"] = "closed"
            fits_var["blush"] = "nothing"
        elif num == "14":
            fits_var["mood_eyes"] = "upset"
            fits_var["mood_mouth"] = "happy"
            fits_var["arms"] = "behind"
            fits_var["mouth"] = "closed"
            fits_var["blush"] = "nothing"
        elif num == "15":
            fits_var["mood_eyes"] = "surprised"
            fits_var["mood_mouth"] = "happy"
            fits_var["arms"] = "behind"
            fits_var["mouth"] = "open"
            fits_var["blush"] = "blush"
        elif num == "16":
            fits_var["mood_eyes"] = "surprised"
            fits_var["mood_mouth"] = "happy"
            fits_var["arms"] = "front"
            fits_var["mouth"] = "open"
            fits_var["blush"] = "blush"
        elif num == "17":
            fits_var["mood_eyes"] = "upset"
            fits_var["mood_mouth"] = "surprised"
            fits_var["arms"] = "behind"
            fits_var["mouth"] = "open"
            fits_var["blush"] = "blush"

        #select scars
        if sanity() < 4:
            fits_var["scars"] = "scars"
        else:
            fits_var["scars"] = "nothing"

        #show the sprite itself
        renpy.show("fits_stand", zorder = 101)


label tropical_date:
    if not persistent.tropical_date_complete:
        y "Uhuhu..."
        y "So you want to go with me on a romantic trip..."
        y "And this isn't just any trip..."
        y "This is a romantic getaway to a tropical beach!"
        y "You may remember how many times I mentioned my desire to experience something like this with you."
        y "As one of the most romantic things couples do in your world..."
        y "This one really gets me."
        y "Just the idea of taking a trip to an exotic paradise with your soulmate sounds very romantic to me."
        y "And not just romantic, but also relaxing and meaningful if you think about it..."
        y "Just forgetting about all the problems in your life..."
        y "Letting them go with the gentle blow of the wind under the warmth of the sun, and the rush of the waves."
        y "And now, we can make our little dream come true..."
        y "One day to enjoy it in the best way possible!"
        y "I-I'm really happy and excited about this, [player]."
        y "And even though I would have preferred to do this in your world..."
        y "For now, this will do."
        y "Now, just give me a second... I have to get this working..."

    hide craneo
    hide roseo
    hide bunnyo
    hide raccoon
    hide diffuser
    hide hdy_statue
    hide halloween_cupcake
    #Changes background to beach background with the boat. Plays drumless version of the date theme and the beach sounds.
    show black zorder 100 with Dissolve(2.5)
    play music "music/beach_date_1_drumless.ogg" fadeout 0.5 fadein 0.5
    play sound "music/beach_sfx_loop.ogg" loop fadein 1.0
    show beach_4 zorder 100 with Fade(1.0, 0.5, 0.5)
    hide black

    $show_fits_standing("pareo_yuri_5")
    y "..."
    y "Here we are, [player]."
    y "As you can see, we are now on a beautiful beach that I created just for us."
    y "Just you and me, my love."
    $show_fits_standing("pareo_yuri_1")
    y "By mixing my own ideas with a few pictures I collected in my research about tropical vacations and beach environments, I was able to create my own."
    y "My research was extensive enough to learn what people like doing in vacations like these..."
    $show_fits_standing("pareo_yuri_5")#Eyes open, arms on her chest.
    y "So you probably can expect things that are popular in your world to be here too!"
    y "I won't spoil what they are specifically though, you'll have to find out yourself~"
    y "Regrettably though, I feel that there's a lot more I could've created here for us to enjoy..."
    $show_fits_standing("pareo_yuri_7")#Hands down, serious expression, raised eyebrows.
    y "But that's beyond my coding capabilities..."
    y "That's why we are not going to see other people around, nor buildings or services that would require people to operate them."
    y "I just hope that doesn't bother you... I did my best to make this special moment possible."

    menu:
        "It's okay, I understand, you don't have to apologize at all.":
            $add_k(2)
            $show_fits_standing("pareo_yuri_14")#Normal eyebrows, smiling, hands down.
            y "Ohhh... thank you. I'm glad you understand my struggle."
            y "Sorry if that sounded like self-pity."
            y "I just wanted to be sure that we have everything we need to make this experience enjoyable and memorable."

        "I see... it's okay, maybe you'll do even better next time!":
            $add_k(1)
            $show_fits_standing("pareo_yuri_14")#Normal eyebrows, smiling, blushing, hands down.
            y "You're right..."
            y "Maybe I am pushing myself too hard."
            y "Overthinking this is not going to change anything at this point."
            y "And we both know it's never good to do so..."
    $show_fits_standing("pareo_yuri_1")#Normal eyebrows, smile, open mouth, hands down.
    y "A-anyways, I don't think we need too much to enjoy this experience."
    y "We have just what we need! A tropical vacation is mostly about relaxing, resting, and enjoying peaceful nature, after all."
    y "For me, just sharing these moments with you is enough."
    y "Now, I am going to request that you come with me... we still have a lot to do."
    $show_fits_standing("pareo_yuri_5")#Hands over her chest, blush on her cheeks, smile, closed mouth, raised eyebrows.
    y "The first thing to do is finding a place to lay down and rest..."
    y "Preferably one under a tree or a beach umbrella."
    y "The excessive heat of this weather can be uncomfortable, and staying cool will help us feel more relaxed."
    $show_fits_standing("pareo_yuri_1")#Normal eyebrows, hands down, smile, open mouth, .
    y "That also means we need two beach chairs, since just laying in the hot sand isn't the best idea."
    y "Luckily, I managed to add both the umbrellas and the chairs, so it's not a problem for us."
    y "Let's head to the nearest ones now..."

    #Changes background to beach background with umbrellas. Same music and sounds
    show beach_3 zorder 100 with Fade(1.0, 0.5, 0.5)
    hide beach_4

    $show_fits_standing("pareo_yuri_14")#Standing sprite, smile, raised eyebrows, hands down.
    y "There we are..."
    y "This looks like a nice spot, wouldn't you agree?"
    y "Let's just lay down..."
    y "And drift away."
    $show_fits_standing("pareo_yuri_12")#Standing sprite, Normal eyebrows, open mouth, blush on her cheeks, hands down.

    #Changes background to umbrella only. Same music and sounds
    show beach_5 zorder 100 with Fade (1.0, 0.5, 0.5)
    hide beach_3

    y "Take a deep breath and listen to the sounds of the sea..."
    y "Breathe in..."
    y "..."
    y "And now..."
    y "Breathe out..."
    y "..."
    y "Keep breathing that way... relax your body, let the feeling of the breeze take away all the problems in your life."
    $show_fits_standing("pareo_yuri_5")#Hands on her chest.
    y "Now close your eyes, and let your mind travel to a relaxing world with the sounds surrounding us..."
    y "I guess you can see now one of the reasons why I was so excited about this."
    y "The quietness, the peaceful and gentle sounds of the wind and the waves, mixed in harmony..."
    y "All of those elements calm the mind, releasing your mind and your body from the grip of stress and burden of daily life."
    $show_fits_standing("pareo_yuri_14")#Normal eyebrows, hands down, closed mouth, smile.
    y "You know, I think that you should always stay connected with nature in some way or another."
    y "Since that is possible in your world."
    y "Having a connection with nature proves to have a lot of benefits in the health of human beings."
    $show_fits_standing("pareo_yuri_1")#Same facial expression, open mouth, blushing.
    y "Perhaps it is because we are recovering that connection with our natural origins?"
    y "In fact, it's scientifically proven that spending some time in nature helps to improve your mental health."
    y "It's still not a panacea..."
    $show_fits_standing("pareo_yuri_8")#Worried expression, closed mouth, both hands on her chest.
    y "But it helps a lot, and it's even considered to improve the conditions of some mental illnesses, such as depression and stress."
    y "So, if you need to clear your mind..."
    y "Or want a way to release the stress and whatever is making you feel down..."
    $show_fits_standing("pareo_yuri_9")#Same expression, open mouth.
    y "Spending more time in nature may help you a little."
    y "You only need to spend about seventeen minutes per day, on all seven days of the week to gain all the benefits of it."
    y "It's a small cost for a large benefit."
    $show_fits_standing("pareo_yuri_7")#Same expression, hands down, closed mouth.
    y "Or I am being inconsiderate here?"
    #y "I know a lot of things are going on in the world right now, like the coronavirus pandemic."
    #y "You're probably not even allowed to go outside just for recreational purposes, depending on what country or state you live in."
    #$show_fits_standing("pareo_yuri_10")#Same expression, open mouth, hands down.
    #y "Considering that... if you are living in a dangerous zone with many cases of infections... you will be unable to follow my advice"
    $show_fits_standing("pareo_yuri_9")#Same expression, hands over her chest, open mouth.
    y "Maybe..."
    $show_fits_standing("pareo_yuri_16")# Smile, raised eyebrows, open mouth, hands on her chest.
    y "Is it possible for you to have a garden in your house? Or do you already have one?"
    y "Maybe you can start one by planting something in your backyard, if you have one."
    y "If you are unable to do so, another option is to keep them in pots."
    y "But if you are going to take this humble advice, I have to tell you something about how to care for plants."
    $show_fits_standing("pareo_yuri_14")#Smile, normal eyebrows, closed mouth, hands down.
    y "It's always better to know which kind of plant you want, and what kind of care they require."
    y "You have to be careful that you're not over-watering them, as most plants do not require too much water to stay healthy."
    y "Different plants require different amounts of sunlight too... You'll have to be careful with plants that are sensitive to large amounts of direct sunlight."
    $show_fits_standing("pareo_yuri_5")#Smile, blush on her cheeks, both hands on her chest.
    y "Some good choices for beginners are the snake plant, the spider plant, the dracaena species, and succulent plants..."
    y "If you're interested, you should do a bit of research on them."
    y "Taking up hobbies like this can help you to find some entertainment and peace..."
    $show_fits_standing("pareo_yuri_14")#Raised eyebrows, smile, closed mouth.
    #y "And can also serve as a distraction for the problems in your world, such as COVID-19."
    y "Don't forget that you can also use your free time to learn new things, or exercise your body."
    y "You should always take care of your body and mind, so those are good ways to start a healthy routine."
    $show_fits_standing("pareo_yuri_2")#Blushing, smile,normal eyebrows, open mouth.
    y "And I would love to see you in good health, both mentally and physically."
    y "But... will take my advice into consideration, [player]?"

    menu:
        "I'll try... but no promises.":
            $show_fits_standing("pareo_yuri_14")#, hands down, smile, closed mouth.
            y "Well, that's fine [player]."
            y "At least you're going to make an effort."
            y "It's better than nothing..."
            y "Maybe in the process, you'll find this practice much easier over time."
            $show_fits_standing("pareo_yuri_5")#Normal eyebrows, hands on her chest, blushing cheeks, smile.
            y "If you find time in your daily routine to take in nature, or to perform some healthy practices, you'll probably adapt to the change."
            y "Once you get used to it, you won't even notice the difference between this and your other daily activities."
            y "In other words, it would become natural for you, even casual maybe."
            y "But that is just if you are able to keep this routine, of course."
            y "Don't feel pressured to do so."

        "Alright, [persistent.yuri_nickname], from now on that will be a part of my daily routine.":
            $show_fits_standing("pareo_yuri_16")#Blushing, raised eyebrows, smile, open mouth, hands on chest.
            y "I am so glad to hear that, my love!"
            y "This way you will stay healthier and less stressed..."
            y "Which means that you will be around here with me much longer."
            y "And also, a practice that gives some tranquility would be helpful for keeping a good mood."
            $show_fits_standing("pareo_yuri_5")#Closed mouth, smile, normal eyebrows.
            y "We all need to get away to release all the burden of our everyday problems and pressures..."
            y "And it's better to do that in a healthy way."
            y "J-just remember to be safe if you are going outside, okay?"
            $show_fits_standing("pareo_yuri_1")#Hands down, open mouth, blushing, smile.
            y "The point of all of this is to keep you healthy."#, not at risk."
            #y "And if you are living in a high-risk zone for the coronavirus, it's better not to risk it and try some of my other suggestions."
            #y "They can be very helpful as well."

        "I appreciate your advice, but I am not going to be able to do so.":
            $show_fits_standing("pareo_yuri_8")#Sad mouth, closed mouth, hands on her chest.
            y "Ohhh..."
            y "That's a shame, but don't worry too much about it..."
            y "Even if you are unable to keep a routine like that, it is completely understandable."
            y "Just remember that, if you find some time to do keep healthy routines in the future..."
            $show_fits_standing("pareo_yuri_16")#Smile, blush on her cheeks, open mouth, raised eyebrows.
            y "It would be better to not waste the opportunity."
            y "To make it clear, this was not to pressure you to do anything, it's just a suggestion."
            y "You are free to choose if you take it or not. And as I said before, there is no problem with that."

    $show_fits_standing("pareo_yuri_1")
    y "Now let's rest a little bit longer... I want to show you some other things I prepared."


    #Show beach background with a boat. Drumless beach theme, beach backgrounds sounds too.
    show beach_4 zorder 100 with Fade(1.0, 0.5, 0.5)
    hide beach_5

    $show_fits_standing("swimsuit_yuri_5")#Standing sprite, smile, closed mouth, blushing, hands on her chest.
    y "Okay... I think it's time to move on..."
    y "Even if I enjoy these moments of relaxation and resting..."
    y "We are not going to spend the rest of this day just sitting here, right?"
    $show_fits_standing("swimsuit_yuri_1")#Smile, hands down, open mouth.
    y "That would ruin all the other plans I had for this wonderful date."
    y "This is just a small part of it, a delightful one of course, but we are not done yet."
    y "You know... there is something I always wondered about being on a beach."
    $show_fits_standing("swimsuit_yuri_14")# Smiling, blushing, hands down, closed mouth.
    y "People in your world really seem to enjoy the fresh touch of the seawater around their bodies..."
    y "The freshness of the seawater with the intense heat, mixing together to create an atmosphere of balance between contrasting temperatures."
    y "That makes me wonder, how does it feel to have the blazing sun warming your body..."
    $show_fits_standing("swimsuit_yuri_5")# Normal eyebrows, smiling, blushing, hands on her chest.
    y "While at the same time cooling down and refreshing yourself with the gentle seawater."
    y "It's really a wonderful experience I always wanted to try..."
    y "...But now that I think about it, I had a similar experience before, but it was... a really weird one..."
    $show_fits_standing("swimsuit_yuri_8")#Raised eyebrows, sad mouth, blushing.
    y "And one that ended pretty bad."
    y "..."
    y "Uhhh..."
    $show_fits_standing("swimsuit_yuri_3")#Raised eyebrows, worried expression, open mouth.
    y "Forget I said anything!"
    y "I apologize for rambling nonsense..."
    y "I don't know what I was thinking, honestly..."
    $show_fits_standing("swimsuit_yuri_8")#Blushing, closed mouth, worried expression, hands on her chest.
    y "I just went off topic with some thinking, that's all."
    $show_fits_standing("swimsuit_yuri_12")# Hands down, open mouth.
    y "But going back on topic, as I expressed before, I was excited with the idea of taking a dip in the waters of a beach."
    $show_fits_standing("swimsuit_yuri_5")# Smile, closed mouth, blushing.
    y "And now I have the opportunity to give it a try!"
    y "It should be clear at this point what we are about to do, right?"
    y "It's time to take a nice dip into the waters of this beautiful beach, that was made with that exact purpose, only for us."
    $show_fits_standing("swimsuit_yuri_6")# Smile, , closed mouth, hands down.
    y "I hope you didn't misunderstand what I was trying to say, ehehe..."
    y "Uhhh... I just... realized something..."
    y "If we are going to take a dip right now, that would mean... I would have to get rid of the c-clothes that I am wearing right now..."
    $show_fits_standing("swimsuit_yuri_7")
    y "...I-I can't just... get this pareo wet... So I would have to keep... just the swimsuit..."
    y "Oh my... This is so embarrassing... "
    y "..."
    menu:
        "There is nothing wrong with that [persistent.yuri_nickname]. It's normal to wear such clothes on the beach.":
            $show_fits_standing("swimsuit_yuri_8")# Serious expression, raised eyebrows, blushing, sad mouth, closed mouth.
            y "..."
            y "Well... In some way, you are right..."
            y "But still... It is not just that simple."
            y "Don't you understand? My whole life I have been..."
            $show_fits_standing("swimsuit_yuri_9")#Same facial expression, open mouth.
            y "Insecure about... about all of myself. My whole being, my body, my behavior, everything..."
            y "I know this was all my idea... how foolish of me to not have thought about this."
            y "This is all my fault."
            y "If you are upset now, I can completely understand that..."
            $show_fits_standing("swimsuit_yuri_8")#Same facial expression, closed mouth.
            y "I don't really know if I was too hyped about getting the experience without thinking about anything else, but at the same time..."
            y "I don't want to disappoint you, fooling you into believing we were about to have a wonderful date..."
            y "And throwing all of my effort to waste just because of my stupidity."
            y "..."

        "[persistent.yuri_nickname], I am not upset at all. In fact, I'm encouraging you to be confident about this. This is what we wanted.":
            $show_fits_standing("swimsuit_yuri_9")# Sad mouth, blush on her cheeks, open mouth, hands on her chest.
            y "B-but that doesn't take away the fact that it's uncomfortable and embarrassing to get almost naked outdoors."
            y "I'm just not used to this."

        "But we are completely alone here, right? Nobody else is watching you except for me.":
            $show_fits_standing("swimsuit_yuri_7")# Sad mouth, closed mouth, blush on cheeks, Normal eyebrows, hands down.
            y "I... I am still having a hard time with this."
            y "I know for a fact that it would be almost impossible for me to do this if there were more people around."
            y "I am used to being a target of uncomfortable attention because of this kind of stuff."
            y "The idea that I am going to get almost naked in public... it would be impossible for me if there were more people around."
            $show_fits_standing("swimsuit_yuri_3")# Raised eyebrows, sad mouth, open mouth, blush on her cheeks, hands on chest.
            y "But it's not just that."
            y "Even before, I wasn't confident enough to show my naked arms to anyone, not even you..."
            y "And now t-this... I am going to show you my body, full of my mistakes and all..."
            y "Don't get me wrong, it's not like I don't trust you, it's just..."
            $show_fits_standing("swimsuit_yuri_7")# Normal eyebrows, hands down, closed mouth, sad mouth.
            y "..."
            y "What am I even saying?"
            y "Just ignore that..."
            y "Even if this is still hard for me to do due to my lack of confidence..."
            y "The only other person around here is you, and I really trust you, more than anyone in my entire life."
            $show_fits_standing("swimsuit_yuri_10")# Normal eyebrows, blush on her cheeks, sad mouth, open mouth, hands down.
            y "You give me confidence, so much so that I feel capable of anything."
            y "But aside from that, there is just one thing that is still bothering me..."
            y "The only thing I ask from you, is that you not judge me, or think anything less about me for..."
            $show_fits_standing("swimsuit_yuri_9")#Same facial expression, hands on her chest.
            y "For my mistakes, and all the wrong things I did to myself in the past."

    menu:
        "You can trust me, I'm not going to judge. We all make mistakes.":
            $ add_k(2)
            y "..."
            y "Just forget that, sorry."
            $show_fits_standing("swimsuit_yuri_9") #Open mouth, sad mouth, closed mouth, hands over her chest.
            y "But now I don't really know if I am ready for something like this..."
            y "There are... things about me that I wouldn't like you to see."
            y "And I would like for you to keep a better image about me, r-rather than a disturbed one just for wearing more revealing clothes."
            $show_fits_standing("swimsuit_yuri_5") #Normal eyebrows, closed mouth, smile, blushing, hands over her chest.
            y "But if you can accept me with all my flaws, then we can keep going with this date."
            y "I think that's clear enough..."
            y "Now wait a moment, I need to change my clothes."

    #Shows beach background without boat. Same music and sounds.
    show beach_1 zorder 100 with Fade(1.0, 0.5, 0.5)
    hide beach_4

    $show_fits_standing("bikini_yuri_8")
    y "O-okay, I am ready."
    y "Then, what do you think, [player]? D-do you like the way I look?"

    menu:
        "[persistent.yuri_nickname]! You look beautiful! There's nothing wrong with you at all!":
            $show_fits_standing("bikini_yuri_16") #Normal eyebrows, smile, open mouth, blushing, hands over her chest.
            y "Oh dear..."
            y "You are so kind to me... I-I really don't think I look {b}that{/b} good."
            y "But I appreciate your saying so, don't get me wrong..."
            y "In fact, I have to be honest here..."
            $show_fits_standing("bikini_yuri_14") # Normal eyebrows, smile, blushing, hands down, closed mouth.
            y "When I was planning all of this, I was wondering about what would suit me the best..."
            y "So instead of just using the first clothes that came into my mind, I did a bit of research and experimentation about what kind of clothes looked better on me."
            y "I just didn't want to show myself in clothes that you..."
            y "Would consider, you know... boring to see..."
            $show_fits_standing("bikini_yuri_15") # Normal eyebrows, smile, open mouth, blushing, hands down.
            y "I don't want you to think I'm boring... I just don't want to be judged that way anymore..."
            y "So, after a long debate with myself, I decided to try a more \"daring\" style, something that wouldn't look boring or ridiculous."
            y "Like... the kind of clothes a \"shy\" and \"non-confident\" girl would wear on a beach..."
            $show_fits_standing("bikini_yuri_16") # Normal eyebrows, smile, blushing, open mouth.
            y "I... I'm just trying to say that I was trying my best for you, as always."
            y "It's just that... maybe I am lacking more confidence to recognize it."
            y "And just to make it clear again, I'm glad you think I look beautiful."
            y "That... means a lot to me."
            $show_fits_standing("bikini_yuri_13") #Normal eyebrows, smile, blushing, closed mouth, arms over her chest.
            y "Thank you for that."
            y "Now, I need to stop rambling so much here, and get back to business."
            y "The blue water reflecting the bright sunlight looks quite tempting, and I don't want to waste any more time."
            y "Let's go."

    #Shows sea background (no sand one). Same music and background sounds.
    show beach_6 zorder 100 with Fade(1.0, 0.5, 0.5)
    hide beach_1

    $show_fits_standing("bikini_yuri_13")# Standing sprite, Normal eyebrows., blushing, smile, hands over her chest.
    y "..."
    y "This is..."
    y "The sensation... it's exactly how I imagined it would be."
    y "Ohhh..."
    y "I can see now that all the effort was worth it."
    $show_fits_standing("bikini_yuri_5")  # Normal eyebrows., smile, open mouth, hands over her chest.
    y "Everything resulted perfectly... the gentle softness of the sand that I can feel with my feet."
    y "The water flowing around my body feels so refreshing on such a warm day!"
    $show_fits_standing("bikini_yuri_2") # Normal eyebrows, smile, blushing, open mouth, both hands down.
    y "It feels like a perfect balance in this climate... allowing us to be in the middle of all this intense heat, without it being uncomfortable."
    y "It really is amazing to feel such a sensation, after being confined for so much time in a static room..."
    y "But don't think I blame you for that!"
    $show_fits_standing("bikini_yuri_6")# Normal eyebrows., smile, blushing, closed mouth, both hands down.
    y "It's exactly the opposite. I always wanted to experience this with you, at least once..."
    y "Even if I am still technically imprisoned in the same world... the effort was worth it."
    y "It would be also a waste to not do this with you at my side... maybe without you, this would be all meaningless..."
    $show_fits_standing("bikini_yuri_2")# Normal eyebrows, blushing, smiling open mouth, both hands over her chest.
    y "And for that, I think that to some degree I owe this experience to you, for being at my side, in the most important moments of my life."
    y "Such as this. A brand new experience for me, after being pretty much locked in a room."
    y "But we can't just spend the entire day just standing here, looking at each other, right?"
    $show_fits_standing("bikini_yuri_5")# Normal eyebrows, closed mouth, blushing, smiling, hands over her chest.
    y "I want to try something with you, but... I don't know if you are used to this kind of thing..."
    y "[player], do you know how to swim?"
    y "I won't judge if you are unable to do so, we can do other things instead..."

    python:
        move_along = False #If True, skips this part and goes straight to desserts eating time
    menu:
        "I don't think there is a problem at all. We are in a simulated world, there is nothing capable of harming us.":
            $show_fits_standing("bikini_yuri_15")# Normal eyebrows, blushing, smiling, open mouth, hands down.
            y "Oh! You are... completely right about that. I don't know what I was thinking when I asked such things."
            y "Maybe I was getting too immersed with this experience that I..."
            y "I kind of forgot we are still in a game..."
            y "I apologize for being so silly, I hope I didn't ruin this for you."
            $show_fits_standing("bikini_yuri_8")# Raised eyebrows., sad mouth, blushing, closed mouth, both hands over her chest.
            y "Also, this idea may have broken the immersion for you, since probably you don't have any way to experience swimming in the water."
            y "While playing the mod at the same time, of course."
            y "Maybe we should move forward with something else..."
            python:
                move_along = True

        "Don't worry about that [persistent.yuri_nickname]. What matters here is having fun, and I'm having fun.":
            $show_fits_standing("bikini_yuri_13") # Raised eyebrows, smiling, blushing, hands over her chest.
            y "I'm so glad to hear you say that."
            y "So it seems that this idea didn't ruin the experience for you."
            y "And you are still enjoying this date. Good."
            y "But with that said, we should move forward."
            python:
                move_along = False

        "Why are you asking such questions? This is a game, I don't think that I have to swim at all.":
            $show_fits_standing("bikini_yuri_8")# Normal eyebrows, sad mouth, blushing, closed mouth, hands over her chest.
            y "..."
            y "Uhhh... yeah, I think I got too excited with that idea."
            y "I apologize for behaving in such a foolish way."
            y "Maybe I shouldn't have suggested it."
            y "I should have considered the fact that you can't experience such things while playing the mod in your world."
            y "It is unlikely that you are playing this while being in a pool or a bathtub."
            $show_fits_standing("bikini_yuri_14") #Smiling, blushing, hands down.
            y "Maybe we should move on with another activity, right?"
            y "After all, we have a lot of other things to do."
            python:
                move_along = True

        "Don't worry, we can continue.":
            $show_fits_standing("bikini_yuri_7")# Normal eyebrows., closed mouth, sad mouth, blushing, both hands down.
            y "Okay..."
            y "I will... Take that into consideration."
            y "Maybe I should be more careful the next time I suggest something..."
            y "Thinking in ways to keep the immersion for you shouldn't be too difficult for me, after all."
            $show_fits_standing("bikini_yuri_8")# Sad mouth, closed mouth, hands over her chest.
            y "But for now, let's just continue with the date."
            python:
                move_along = False


        "We should probably move on with something else, if that doesn't bother you.":
            $show_fits_standing("bikini_yuri_7")# Blushing, serious mouth, both hands down.
            y "..."
            y "Yeah, we should probably move on with something else."
            y "I don't want to force you to do anything you don't want to do."
            y "After all, how can I have fun with you if you're not enjoying yourself?"
            y "It would be... unfair, at least from my perspective."
            $show_fits_standing("bikini_yuri_8")# Blushing, sad mouth, hands over her chest.
            y "However, I would like to think you are interested in my opinions about the activities in this mod too."
            y "But anyways... let's move on then."
            y "Just give me a second to get the other activities ready, and to get myself ready for them."
            y "I won't delay this too much."
            y "..."
            python:
                move_along = True

    if move_along:
        jump Beach_Desserts

    $show_fits_standing("bikini_yuri_16")# Open mouth, smiling, blushing, hands over her chest.
    y "Now I am going to ask you to come with me to a deeper area..."
    y "And don't worry about the tides, they are not very strong here, so there is no risk of being washed away."
    y "Just relax and let your body flow with the current..."
    y "That way you will be able to float easier... this is all about relaxation [player]."
    $show_fits_standing("bikini_yuri_13")# Normal eyebrows., closed mouth, smiling, blushing, both hands over her chest.
    y "Isn't it interesting though, the fact the human body can float like a feather when it is in deep waters?"
    y "Like if all the weight of our bodies and our personal burdens were just nothing."
    y "But if you start panicking, then you are in danger of sinking and drowning easily."
    $show_fits_standing("bikini_yuri_8")# Blushing, closed mouth, sad mouth, hands over her chest.
    y "That's... much like real life in a certain way, isn't it?"
    y "When we are panicking, we tend to make decisions in a hurry, without thinking twice about the consequences."
    y "That can get us into even more trouble, instead of solving our actual problem..."
    y "But in the end, isn't this part of the human instinct to survive? Something that is deep within our own nature?"
    y "We can't act in a completely rational way nonstop, for the rest of our lives."
    y "At some point, we are going to be scared. We are always going to panic in certain situations, and I guess that's right, because we can't change it."
    $show_fits_standing("bikini_yuri_7")# Sad mouth, hands down.
    y "Isn't this an inherent flaw in mankind that puts them in danger?"
    y "What do you think about this [player]? Is this the biggest issue with humans?"

    menu:
        "I think that we can't take that from human beings, but we should always be ready for the hard moments of life.":
            $show_fits_standing("bikini_yuri_8")# Normal eyebrows, serious mouth, Normal eyebrows,hands over her chest.
            y "Well... I think that is a good way to solve this problem."
            y "While this is a part of human nature that we can't change..."
            y "We can still however change how we manage to solve those moments of fear and uncertainty."
            y "Instead of running away from the problem, we should be aware that sooner or later, problems are going to arrive."
            $show_fits_standing("bikini_yuri_7")# Sad mouth, closed mouth, both hands down.
            y "And for that, we have to learn how to confront them, learn how to manage those emotions and feelings that overwhelm us sometimes."
            y "I have to say that I truly agree with that point of view."
            y "Even if it's... really complicated for me to put that way of thinking into practice sometimes..."
            $show_fits_standing("bikini_yuri_5")# Smile, blushing, hands over her chest.
            y "B-but anyways, sorry for all of that rambling... I didn't mean to get carried away."
            y "Especially when we are supposed to be relaxing."

        "Maybe those mechanisms tend to work against us, but it's impossible to stay rational all the time.":
            $show_fits_standing("bikini_yuri_7")# Sad mouth, both hands down.
            y "I think you are right about that."
            y "It is impossible for the human mind to stay rational and take some time to think clearly when there is an imminent danger, right?"
            y "Well, while that is true for most people, some people in your world are trained to keep their heads cool in tense or menacing situations."
            $show_fits_standing("bikini_yuri_8")# Normal eyebrows, closed mouth, sad mouth, hands over her chest.
            y "For example, think about soldiers that are bomb disposals."
            y "That kind of job requires you to not freeze, or enter in a panic state."
            y "And I know for a fact that there are professionals that can make such tasks look easy."
            y "So, while you are right in some way, I think we can also train ourselves to be more rational."
            $show_fits_standing("bikini_yuri_5")# Normal eyebrows., closed mouth, blushing, smiling, both hand over her chest.
            y "I think that being more rational is a better way to solve our problems, to survive in extreme situations..."
            y "And to improve our lives, generally speaking."
            y "I won't force you to change your mind about this though, this is still just my advice."

        "I really don't know what to say about it [persistent.yuri_nickname], I don't think that much about those kinds of things.":
            $show_fits_standing("bikini_yuri_8")# Serious mouth, closed mouth, hands over her chest.
            y "Ohhh..."
            y "Well, even if I think that it is important to give things like this some kind of attention from time to time..."
            y "Maybe this isn't the best time to discuss philosophical topics."
            y "We are here to relax our bodies and minds, right?"
            y "Sorry if this bothered you, I went and got too carried away with this topic."
            y "Maybe we can discuss this another day."
            $show_fits_standing("bikini_yuri_5")#Normal eyebrows, smiling, blushing, closed mouth, hands over her chest.
            y "Let's focus on enjoying this moment, instead of rambling."
            y "It's time to relax again..."
            y "Don't think of anything else, just relax your mind and your body."
            y "..."
            $show_fits_standing("bikini_yuri_6")
            y "Now, if you feel like your body is relaxed enough and your mind is completely free from any tension..."

            y "Then that means we have achieved our goal here."
            y "I just want to give you one more piece of advice about this."
            $show_fits_standing("bikini_yuri_5")
            y "When you want to relax, and you are nowhere near to a tropical paradise with someone to share such an experience..."
            y "But still want to feel like you are in the middle of the beach, try to enjoy the relaxing sounds of one."
            y "Maybe you should try one of those relaxing YouTube videos that are extended versions of recorded sounds of nature."
            $show_fits_standing("bikini_yuri_16")
            y "Some of those videos have beach sounds that you can play for hours."
            y "You can choose between hearing only the sounds of the waves crashing against the rocks of a coast..."
            y "Or maybe you prefer the sounds of more soft waves, accompanied with the signings of some sea birds."
            $show_fits_standing("bikini_yuri_15")
            y "What matters is that, if you get to try it someday, you should enjoy it."
            y "Once again, that is just another bit of advice."
            y "But now that it seems that we are done here... we should move on to something else."
    jump Beach_Desserts

label Beach_Desserts:
    #Shows beach background with a boat. Drumless beach date theme, and beach background sounds.
    show beach_4 zorder 100 with Fade(1.0, 0.5, 0.5)
    hide beach_6

    $show_fits_standing("bikini_yuri_6")#Standing sprite, Normal eyebrows, smiling, blushing, Normal eyebrows, both hands down.
    y "Now that we are back here... are you feeling a bit hungry, [player]?"
    y "I think this is the perfect time for a quick snack after a long day."
    y "But you may be wondering: what are we going to eat in the middle of a beach, right?"
    y "Since we don't have any buildings, or other people around, not even the other girls of the club..."
    $show_fits_standing("bikini_yuri_5")# Normal eyebrows., smiling blushing, both  hands over her chest.
    y "Meaning that there are no restaurants, hotels, or anything similar to just go and eat."
    y "Well, then I should tell you that I have a surprise that I prepared for this kind of situation."
    y "Just wait a second so I can get it working."
    y "This should work now..."
label check:
    #Shows beach room background. Same drumless theme, but the beach backgrounds sounds are lowered in their intensity.
    python:
        renpy.music.set_volume(0.5, delay=1.0, channel='sound')
    show beach_8 zorder 9 #with Fade(1.0, 0.5, 0.5)
    show black zorder 1000 with Fade(1.0, 0.5, 0.5)
    hide fits_stand
    hide beach_4
    python:
        persistent.autoload = "Beach_Desserts"
        persistent.previous_costume = persistent.costume
        persistent.old_timecycle = current_timecycle_marker
        tc_class.transition("timecycle")
    $current_timecycle_marker = "_day"
    $persistent.costume = "bikini"
    $costume2 = "pareo"
    $show_chr("A-AAAAA-AAAA, 0, t11")
    hide black with Dissolve(0.5)

    y "It seems that everything is working just fine..."
    y "I made this cozy little cabin for the both of us to share and enjoy."
    $show_chr("A-BBAAA-AAAA")
    y "I did the best I could, so I hope you are pleased with the final result."
    y "But anyway... you must be hungry after everything we've done."
    y "And I don't want to keep you waiting for something to eat."
    $show_chr("A-CCAAA-ADAA")
    y "We came here to eat something after a long day of fun in a hot climate."
    y "And I have another surprise for you, because we are not going to eat ordinary food..."
    y "Instead, we are going to eat some delicious tropical food from around the world."
    y "You see, the research I did for this date was not only to create the beach and its environment..."
    $show_chr("A-CCABA-AEAJ")
    y "But it was also to find out what people usually eat on a tropical trip."
    $show_chr("A-IBABA-ALAL")
    y "This made me discover the best desserts that people eat on tropical vacations."
    y "I sincerely think that they stand out from the rest of the desserts I found."
    y "I am not implying that other kinds of desserts are not good, don't get me wrong there."
    $show_chr("A-CBABA-AMAM")
    y "What I mean is that the ones we are going to try today are an indisputable delicacy."
    y "I only have three of them available for you on this date, but I think that's enough."
    y "I will have to ask you to choose between them..."
    y "And since we are in completely different worlds, you will have to look for something similar to eat in your world."
    $show_chr("A-GBABA-ALAL")
    y "If that's okay with you... this is all I can do."
    y "But before you go, it would be wise to first show you the options I have prepared for you."
    y "Then, depending on what you have chosen, you can go and look for something close to it."
    $show_chr("A-ACAAA-ALAL")
    y "It would also be helpful to give you the option of choosing something you already have in your world."
    y "The first dessert I have is called the {i}Churchill{/i}."
    y "This delicacy is made up of shaved ice, kola syrup, powdered milk, condensed milk, ice cream, and straw cookies on the top, and it's always served in a tall glass."
    $show_chr("A-BDAAA-ALAL")
    y "The second dessert is one that you probably already know about."
    y "The famous piña colada, a delicious cocktail made with rum, coconut milk, pineapple juice and shaken with ice."
    $show_chr("A-GIABA-ACAM")
    y "And finally, the third one is the amazing coconut flan."
    y "Basically a baked custard, but with coconut milk, grated coconut, and some honey on the top of it."
    y "Which one are you going to choose [player]?"

    python:
        yuri_dessert = 2
    menu:
        "Coconut flan sounds good for me.":
            python:
                yuri_dessert = 0
            $show_chr("A-GBABA-ALAL")
            y "A very wise choice..."
            y "My expectations for this dessert are very high, so I am hoping for it to be a delicacy without comparison."
            $show_chr("A-ICABA-ALAL")
            y "Now I will give you a chance to get your own version of this dessert."
            $show_chr("A-IBABA-ALAL")
            y "And don't worry, you don't need to hurry at all. I will be waiting for you here."

        "I am going to choose the Piña Colada.":
            python:
                yuri_dessert = 1
            $show_chr("A-ACDBA-ACAA")
            y "Going for the classics, eh?"
            $show_chr("A-ACABA-ALAA")
            y "Well, that's understandable, considering how good the Piña Colada is..."
            y "Now for you to go and look for something at least similar to this drink in your house."
            y "However, it's completely fine if you are unable to find something like this in your house."
            $show_chr("A-BCABA-ALAA")
            y "I wouldn't want you to get in trouble for drinking an alcoholic beverage, especially if you are underage or not allowed to do so for other reasons."
            y "But otherwise, if you have no problems drinking, and you have something similar to a piña colada in your house, then there are no problems with giving it a try for the occasion."
            $show_chr("A-ACABA-ALAA")
            y "A-anyways, you can go now, I will be waiting for you here."


        "I want to try the {i}Churchill{/i}.":
            $show_chr("A-CAABA-ACAM")
            y "Oh, then you are someone who likes to try new things, aren't you?"
            y "That's perfect."
            y "And trust me, you are not going to regret giving this delicacy a chance."
            $show_chr("A-IAABA-ACAM")
            y "Now you can go and look for something that at least is similar to this dessert to eat in your world."
            y "I'll be waiting for your return here."

    #No textbox for a few seconds. Then shows this options:
    $renpy.pause(delay = 5, hard = True)

    if yuri_dessert == 0:
        menu:
            "I am back [persistent.yuri_nickname], and I have my dessert.":
                $show_chr("A-JBABA-ACAM")
                y "That's perfect!"
                y "Then we can begin to enjoy our desserts together."

            "I am sorry, I can't find anything to eat at this moment.":
                y "You don't have to apologize for that, don't worry."
                y "It's not that big of a deal, and you didn't know I was planning to do something like this."
                y "If we were to blame someone here, that would be me."
                y "I apologize for that..."
                y "I am still going to try my own dessert though, and I hope that doesn't bother you..."
                y "Just wait..."

    elif yuri_dessert == 1:
        menu:
            "I am back [persistent.yuri_nickname], and I have my dessert.":
                $show_chr("A-JBABA-ACAM")
                y "That's perfect!"
                y "Then we can begin to enjoy our desserts together."

            "I was unable to get anything similar to drink, sorry.":
                $show_chr("A-IEBBA-AMAM")
                y "I see..."
                y "Well, it's fine either way."
                y "I wasn't expecting you to get a beverage, even more so when I didn't tell you beforehand that we would do something like this."
                $show_chr("A-BEBBA-AMAM")
                y "And again, if this is about you not being allowed to drink, that's fine too."
                y "There is absolutely no problem with that, so don't worry."
                $show_chr("A-ACABA-AMAM")
                y "However, I am still going to try my own Piña Colada..."
                y "Now excuse me, I have to get this working..."

    else:
        menu:
            "I am back [persistent.yuri_nickname], and I have my dessert.":
                $show_chr("A-JBABA-ACAM")
                y "That's perfect!"
                y "Then we can begin to enjoy our desserts together."

            "Unfortunately I didn't find anything like this.":
                $show_chr("A-CEBBA-ACAL")
                y "Oh well, that's a shame, but you don't have to worry about it."
                y "It is my fault because once again I forgot to tell you to prepare something to eat beforehand."
                $show_chr("A-IEBBA-ACAL")
                y "I apologize for that, but that is not really a big deal."
                y "However, I still want to try my own dessert..."
                $show_chr("A-BKABA-ALAL")
                y "I hope that doesn't bother you, but even if you don't get to eat anything..."
                y "I do have an interesting story to tell you about this dessert however, so you don't get bored of just watching me eat."
                $show_chr("A-ICABA-ALAL")
                y "Now I am going to bring in my dessert, just wait a second."

    #black screen cut to add the dessert for Yuri
    show black zorder 200 with Fade(1.0, 0.5, 0.5)
    hide beach_8

    if yuri_dessert == 0:
        show blasphemous_flan zorder 100

    elif yuri_dessert == 1:
        show pina_colada zorder 100

    else:
        show churchill_slush zorder 100

    show beach_8 zorder 9
    hide black with Dissolve(0.5)

    if yuri_dessert == 0:
        $show_chr("A-ICABA-ALAL")
        y "Hmmm..."
        y "Well, I have to say that I expected it to taste good, and it ended up exceeding my expectations!"
        y "It says a lot about a dessert that looks so simple, but gives you such a sweet surprise."
        $show_chr("A-BDABA-ALAL")
        y "And it's more impressive to know that this dessert is a world traveler..."
        y "What I mean by that is that this dessert has traveled to different countries around the world, and even more impressive, this dessert is as ancient as the Roman Empire."
        y "So it also makes it a culinary relic that proves that simple things are not always lame."
        $show_chr("A-CCABA-ALAL")
        y "And in the case of the coconut flan, I have to say that it has evolved through time in an excellent way."
        y "Now going back to when I said this dessert is as ancient as the Roman Empire, it is because it originated there."
        y "Many people in countries like Mexico or Spain think that they were the ones who created this dessert, but unfortunately for them, they are wrong."
        $show_chr("A-IAABA-ALAL")
        y "The Romans were the first culture we know of that domesticated chickens, and they also stole a lot of Greek egg-based recipes after that."
        y "With the amount of chicken eggs they had and the recipes they acquired from the Greeks, they ended up creating many dishes, including the famous flan."
        y "But originally, flans were quite different from their current versions."
        $show_chr("A-BAABA-ALAL")
        y "They were savory instead of sweet, and included flavors like eel... and yes, I know that sounds weird and even disgusting."
        y "But those were very different times, and different cultures creating those recipes."
        y "However, when the Roman Empire fell, the flan survived and started to change towards a more sweet taste, a variant with the modern ingredients we already know."
        $show_chr("A-BAABA-ALAL")
        y "Then the french from the seventh century called it 'flan', which means 'flat cake.' But that word evolved through time as well, since old French is different from modern French."
        y "But the coconut flan didn't come from Europe..."
        $show_chr("A-ICABA-AMAM")
        y "Actually, it originated in Latin America after the Spanish conquerors brought it to the 'New Continent', bringing also the idea of putting caramel sauce on the top of the flan."
        y "Latin Americans not only created the new variation of the coconut flan, but numerous different styles, ingredients, and flavors."
        y "Each country has different ways to create its own flan, so it can be unique for every culture."
        y "It can look simple in its appearance, but the flan is very rich in culture, history, and flavor."
        $show_chr("A-BBABA-AMAM")
        y "Not to mention that is delicious in almost any variant it has, but for now, I would say that the coconut flan is my favorite."
        y "This also gets me thinking that... We shouldn't judge people just for the way they look..."
        y "Neither we should judge things just for their apparent simplicity..."
        $show_chr("A-CFABA-AMAM")
        y "It makes me remember that I was a bit rough judging the poems of Natsuki's 'last minute' style of writing, dismissing them completely."
        y "That makes you incapable of seeing the complexity of simple things, of being surprised by them."
        y "It is a way of losing the chance to enjoy those kinds of things in life... and to be honest, I wouldn't want to live like that."
        $show_chr("A-ICABA-AMAM")
        y "After all the time I've spent with you in this mod, I've learned that things like just sitting and talking, can have a lot of meaning and importance."
        y "And to be honest, I hate the idea of not being able to be with you, just because sitting and talking in a game is not 'complex enough' or whatever."
        $show_chr("A-BCABA-ACAM")
        y "I guess that we never stop learning new things, hmm?"
        y "And I have to be grateful that you helped me to understand that, through a path full of sweetness and caring."
        y "Thanks for that, my love..."
        $show_chr("A-GCABA-ACAM")
        y "I really appreciate this chance to be with you."


    elif yuri_dessert == 1:

            $show_chr("A-ICABA-ALAL")
            y "Oh my!"
            y "Now I understand why this drink became so popular!"
            y "The taste of this drink is just amazing, and fits perfectly with any tropical trip."
            y "We are here in the middle of the beach, all alone, and yet this drink still fits perfectly for this date."
            $show_chr("A-ICABA-ALAL")
            y "And, even if I don't enjoy parties and crowded celebrations, I can still imagine this drink being a good choice for those occasions."
            $show_chr("A-CCABA-ALAL")
            y "Now, it makes me wonder how someone was able to mix all these flavors from the tropics, and represent them in just one drink."
            y "As if you were able to taste the tropical environment itself."
            y "I did some research to find out who was the original creator of this drink, but I found out that many different people and even some restaurants and hotels claim to be the creators of the drink."
            $show_chr("A-ICABA-ALAL")
            y "But many people believe that this drink was created in San Juan, the capital of Puerto Rico."
            y "From the creativity of the bartender Ramón Marrero, this drink was born in a hotel of that location, called {i}Caribe Hilton{/i} in 1954."
            y "After that, the popularization of this drink skyrocketed from the descriptions of the tourists who tried it and went back to their homelands, who went on and on about how good the piña colada was."
            $show_chr("A-BBABA-AAAL")
            y "Even Hollywood legends like Joan Crawford praised the drink, and in 1978 the Piña Colada became the national drink of Puerto Rico."
            y "But the story about this drink doesn't end with its origins..."
            y "Something that cemented this drink in popular culture more than testimonies about how good it was..."
            $show_chr("A-CBABA-AAAL")
            y "Was a song of Rupert Holmes that you may already know, called {i}Escape{/i}, who mentions this drink in the song, along with other lines about a romantic tropical trip..."
            y "Now, I am going to open a link for you to this song... I feel like it fits perfectly for this date..."

            #Yuri now opens this link in the browser of the player: https://www.youtube.com/watch?v=vLom-87AmO8
            y "Please click this link, [player]: {a=https://www.youtube.com/watch?v=vLom-87AmO8}https://www.youtube.com/watch?v=vLom-87AmO8{/a} "

            y "..."
            y "I have to say that I love this song for how romantic it is..."
            $show_chr("A-BCABA-ACAL")
            y "Yes, I know the story of it starts with an attempt of cheating from both sides..."
            y "But in the end, they discover what the other side of the relationship was doing, and instead of destroying the relationship, it ended up different."
            y "They got to know more about each other, things that they never realized about the other one..."
            $show_chr("A-CCABA-AMAM")
            y "Things that made them fall in love with each other again."
            y "Now, I want to make it clear again that I don't like the implication of cheating, but the concept of discovering new things about the person you love."
            y "Things that can make you fall in love with them again."
            $show_chr("A-IBBBA-AMAM")
            y "It can sound ridiculous for some people, but for me, it is just another way to keep the love between a couple alive."
            y "Being honest with each other, without hiding things, no matter what they are."
            y "Or just picking up new hobbies and things that can get you to spend more time with the person you love, so they would fall in love with you again."
            $show_chr("A-BBBBA-AMAM")
            y "I really want to have something like that in our relationship, [player]."
            y "I want to discover new things about you, I want to know that we are not hiding things from each other."
            y "Transparency... that's the key. I don't care about your faults, but the things that can maybe make me fall more in love with you."
            $show_chr("A-CCBBA-AMAM")
            y "But don't worry, I love you enough, and I feel that we are not hiding things from each other."
            y "Or at least, I hope so."

    else:

        $show_chr("A-CCABA-AAAL")
        y "..."
        y "Hmmm..."
        y "Oh my..."
        y "This tastes delicious!"
        y "I mean, I was expecting this to taste good..."
        $show_chr("A-JBABA-ALAJ")
        y "But this dessert even managed to exceed my own expectations!"
        y "I could say that it was worth trying this so-called {i}Churchill{/i} after all..."
        y "But now you may be wondering why a shaved ice cream would be called Winston Churchill, one of the most famous prime ministers of the United Kingdom."
        $show_chr("A-BDGBA-ALAL")
        y "Well, the story behind its name is related to the historical figure, but not in the way you may be thinking of."
        y "To know the story behind it, we have to look at the country of origin of this specific ice cream, Costa Rica."
        y "As well as the origins of the shaved ice creams in general."
        $show_chr("A-JCABA-ALAL")
        y "Shaved ice creams are a very common dessert in many different countries of the world, not just in tropical regions."
        y "In fact, shaved ice creams originated from Taiwan in the 7th century AD, and were imported to the American continent by Japanese immigrants."
        $show_chr("A-BDABA-ACAL")
        y "They brought it with them when they arrived in Hawaii to work in sugar plantations, and it's a very important part of Hawaiian culture."
        y "This ice cream is more common in tropical countries, which is why you will normally find more different terms for this dessert from those countries."
        y "The shaved ice cream is not only different in name for every country, but also in styles and ingredients."
        $show_chr("A-ACAAA-AMAM")
        y "A shaved ice cream from Japan, called 'kakigōri' is going to be completely different from a 'raspado' of Latin American countries."
        y "But the thing with Costa Rican's shaved ice creams is that they are even more different from the rest of the shaved ice creams of Latin American regions."
        y "They have completely different ingredients, which makes them distinctive from other Latin American versions of this dessert."
        $show_chr("A-BFAAA-AMAM")
        y "But this doesn't explain why this version of the shaved ice cream is called 'Churchill', right?"
        y 'Well, I found out that the \"Churchill\" is not the standard version of a shaved ice cream or \"granizado\" in Costa Rica, but instead is another version of it.'
        $show_chr("A-ICAAA-AMAM")
        y "It was 'created' by a man called Joaquín Agüilar Esquivel, who used to go to touristic zones to buy shaved ice creams with the exotic ingredients that compose a Churchill ice cream."
        y "The merchants of the zone then decided to name this exotic shaved ice cream as 'Churchill', because Joaquín looked very similar to Prime Minister Winston Churchill."
        y "And that was the story about why this shaved ice cream is called Churchill."
        $show_chr("A-BCGBA-AMAM")
        y "I hope I didn't bore or annoy you with it... I just found it interesting to learn about the evolution of this dessert through history."
        y "And how different cultures shaped it in different and unique ways."
        y "But history facts aside... I have to say something..."
        $show_chr("A-IBGBA-ACAM")
        y "It doesn't matter how sweet any dessert is in this world."
        $show_chr("A-JAGBA-ACAM")
        y "The sweetness of them is nothing compared to how sweet and kind you are with me."
        y "It's something that I just like about you, that you always want to understand me, even when I am incapable of understanding myself."
        $show_chr("A-CBABA-ALAL")
        y "So thank you, my love, for all you've given to me. Especially your kindness."


    #Still showing the beach room, same drumless beach date and beach sounds lowered.
    #black screen cut to remove the dessert for Yuri
    show black zorder 100 with Fade(1.0, 0.5, 0.5)
    hide beach_8

    if yuri_dessert == 0:
        hide blasphemous_flan

    elif yuri_dessert == 1:
        hide pina_colada

    else:
        hide churchill_slush

    show beach_8 zorder 9
    hide black with Dissolve(0.5)

    $show_chr("A-JCABA-ACAM")
    y "It seems that we are done with our desserts... I hope you enjoyed this as much as I did."
    y "Remember that this date is meant to be mutually enjoyed."
    y "And I hope that you are ready for what is about to come."
    $show_chr("A-BBABA-ALAA")
    y "If you are acquainted with my previous talks about tropical vacations, you probably saw this coming."
    y "It is getting late, and everything is ready to orchestrate a magnificent event."
    y "But we have to go outside for now... trust me, we don't want to miss the chance to watch this."#Standing sprite, Normal eyebrows., smiling, blushing, closed mouth, both hands on her chest.

    #Background changes to beach sunset. Plays the beach date theme with drums and background sounds normal.
    play music "music/beach_date_1.ogg"
    python:
        renpy.music.set_volume(1, delay=1.0, channel='sound')
    $fits_var["costume2"] = "pareo"
    $fits_var["cg_face"] = "3"
    $fits_var["arms"] = "front"
    show fits_cg zorder 200 with Fade(1.0, 0.5, 0.5)
    hide beach_8
    python:
        persistent.autoload = "ch30_autoload"
        persistent.costume = persistent.previous_costume
        if persistent.old_timecycle == "_space":
            tc_class.transition("space")
        else:
            tc_class.transition("timecycle")
        costume2 = "nothing"
        show_chr("default")
    hide yuri_sit

    y "..."
    y "Isn't it... wonderful?"
    y "Like the most beautiful thing you have ever contemplated in your life?"

    menu:
        "This sunset is breathtaking, but you are still the most beautiful thing I have ever seen.":

            $fits_var["cg_face"] = "1"

            y "Ohhh..."
            y "Uhhh... I don't..."
            y "I don't know how to answer such a c-compliment."
            y "Do I even deserve such a high level of praise?"

            $fits_var["cg_face"] = "2"
            $fits_var["arms"] = "behind"

            y "B-but... I appreciate it a lot... It means a lot to me to be seen that way."

            $fits_var["arms"] = "front"

            y "Sometimes, when I was alone, I wondered if someone would ever give me some kind of compliment... you know, {b}this{/b} kind of compliment."
            y "At some point, the compliments about my intelligence felt more and more repetitive..."
            y "When that was the only respectful saying I received, I still liked it in some way, but on the other hand..."

            $fits_var["arms"] = "behind"

            y "Sometimes it felt like people didn't have anything else to say about me."
            y "Like if they were saying such things only trying to be nice to me, for some reason."
            y "And don't even think that I'm not self conscious about my looks anymore."

            $fits_var["cg_face"] = "1"
            $fits_var["arms"] = "behind"

            y "I might not have a perfect, athletic body... b-but I found out that I was pretty attractive a long time ago."
            y "You know what I mean by that... my looks are quite outstanding compared to the other girls."
            y "That explains the weird looks I had received before in my world... you know, when things were 'normal' in the game."

            $fits_var["cg_face"] = "2"
            $fits_var["arms"] = "front"

            y "But still... nobody talked about me in a respectful and appropriate way like you before."

            $fits_var["cg_face"] = "1"

            y "And of course, that leaves aside... the inappropriate c-comments that Sayori made..."
            y "A-anyways... I think you get my point."

            $fits_var["cg_face"] = "3"

            y "Thanks for saying such lovely things."

            $fits_var["cg_face"] = "2"

            y "..."

        "I think you are right, and I love being able to share this with you.":

            y "Glad to hear that..."
            y "This entire date, and this special moment, has a lot of meaning and importance because of you, [player]."
            y "I could generate a thousand different beautiful scenes in this game, but if I didn't have anyone else to share them with..."

            $fits_var["cg_face"] = "1"
            $fits_var["arms"] = "behind"

            y "Then it wouldn't feel special, or unique, maybe not even important."
            y "I could control this entire world, I could be some kind of 'god' controlling everything to follow my desires."

            $fits_var["cg_face"] = "2"

            y "But I would still be alone, like Monika..."
            y "When you think about it, it seems that being truly loved is much more important than having a lot of power."
            y "Money, influence, strength, or just any form of power can get a lot of things, but we are always in need of love."

            $fits_var["arms"] = "front"

            y "It is something that power can't replace."
            y "Having you here... really made a vital difference for my well-being, and also for this entire world."

            $fits_var["cg_face"] = "1"

            y "I think we have managed to solve, at least at some degree, the main problem of the literature club."
            y "I have found my way to happiness... I have found it with you."
            y "..."

    show beach_2 zorder 100 #with Fade(1.0, 0.5, 0.5)
    show black zorder 150
    hide fits_cg with Dissolve(2)
    hide black with Dissolve(1)

    $show_fits_standing("pareo_yuri_6") #Standing sprite, smiling, blushing, hands down, Normal eyebrows, closed mouth.
    y "I am just... so glad that I can finally share this moment with the person I love most."
    y "..."
    y "It's hard for me to find the words to describe how happy I am right now."
    y "Isn't this beautiful?"
    y "So magnificent, a gift from the cosmos to anyone capable of admiring it."
    $show_fits_standing("pareo_yuri_2") #Normal eyebrows, smiling, blushing, open mouth, hands down.
    y "Sunsets do have some 'magic' attached to them..."
    y "If you can see the beauty of the universe as magic, in a metaphorical way perhaps."
    y "But sunsets, like many other big cosmic events from the human perspective, do have some interesting legends and mythology around them."
    $show_fits_standing("pareo_yuri_6") #Normal eyebrows, smiling, blushing, closed mouth, hands down.
    y "Have you noticed that sometimes, when you look at a sunset over a plain horizon, like the ocean, a green disk of light or green ray is visible over them?"
    y "It is a meteorological phenomenon called 'green flash'."
    $show_fits_standing("pareo_yuri_5") #Normal eyebrows, smiling, closed mouth, hands on her chest.
    y "This happens when the atmosphere of Earth causes the light of the Sun to separate into different colors."
    y "Green and blue are the most common colors for this kind of sunset."
    y "Which is... kind of curious, at least to me."
    $show_fits_standing("pareo_yuri_6") #Normal eyebrows, smiling, blushing, closed mouth, hands down.
    y "Of course, you would understand why if you remember my poems on the original game..."
    y "Lights that flicker in blue and green colors."
    y "Heh..."
    y "But anyway..."
    $show_fits_standing("pareo_yuri_2") #Normal eyebrows, smiling, blushing, open mouth, hands on her chest.
    y "To be able to see such an event, the conditions have to be ideal... you are really lucky if you ever get the chance to see one happening."
    y "Some flashes are more uncommon than others, and normally they only last around a second."
    $show_fits_standing("pareo_yuri_5") #Normal eyebrows, smiling, blushing, closed mouth, hands down.
    y "If you blink, you lost it."
    y "As you can see, it is really hard to catch one of them, but when you get to see one, you realize it was all worth it."
    y "But despite all of that, sunsets are amazing and beautiful things to see, even without a green flash."
    $show_fits_standing("pareo_yuri_2") #Normal eyebrows, smiling, blushing, open mouth, hands on her chest.
    y "Having one of them in my world, even when it is being generated by code, watching it with you feels like a blessing for me."
    y "..."
    y "It is hard to say how much this means to me..."
    $show_fits_standing("pareo_yuri_1")
    y "Expressing how amazing this event is for me is not easy either."
    y "And that brings me back to when I said that, if I have a hard time expressing myself in verbal ways."
    y "Then I use my writing to convey to others what I am feeling."
    $show_fits_standing("pareo_yuri_5") #Normal eyebrows, smiling, closed mouth, hands on her chest.
    y "It also reminds me that, one of the things I wanted to do most on a tropical vacation while watching a beautiful sunset at your side..."
    y "Was to write poems with you."
    y "An inspiring scene like this deserves to be immortalized in some way, and the best way I can think of is through writing."
    $show_fits_standing("pareo_yuri_2") #Normal eyebrows, blushing, smiling, open mouth, both hands on her chest.
    y "To both help us remember this moment... and to express our feelings about the events on this date, about all the things we have enjoyed so far."
    y "If you were to write a poem for me now, I would cherish that poem for the rest of my life."
    $show_fits_standing("pareo_yuri_16") #Same posture, open mouth, raised eyebrows.
    y "Of course, I won't make you play this minigame from back in the day, that would just be silly"
    y "That could be my next goal in regards to coding. Maybe I can figure out a way to let you write {b}actual{/b} poems instead of picking 10 words from a laundry list."
    y "Until then, let us... just relax here for a bit and marvel at this beautiful scene..."
    y "But I wrote a little poem myself, and I would love if you could check it out please. It really means a lot to me... your opinion means a lot to me..."
    $show_fits_standing("pareo_yuri_2") #Smiling, open mouth, normal eyebrows, arms on her chest.

    #placeholder =
    #"despite our disagreements" if Karma is 1-2
    #"despite the short time we've spent so far" if Karma is 3
    #"and I can't say that often enough" else

    python:
        if karma() >= 2:
            placeholder = "despite our disagreements"
        elif karma() == 3:
            placeholder = "despite the short time we've spent so far"
        else:
            placeholder = "and I can't say this often enough"


    y "Because [player], [placeholder], {b}you{/b} mean a lot to me."

    #poem reading time :D
    call showpoem(poem_beach)

    y "Okay, [player], what do you think about my poem?"
    y "Do you like it?"

    menu:
        "I really like it! Your writing is always amazing, [persistent.yuri_nickname]!":
            $ add_k(2)
            $show_fits_standing("pareo_yuri_2") #Raised eyebrows, smiling, open mouth, blushing, hands on her chest.
            y "I am so glad to hear that!"
            y "I don't know if I deserve so much praise however."
            y "But I really love when you praise my writing like that."
            $show_fits_standing("pareo_yuri_5") #Same expression, closed mouth.
            y "It makes me feel... appreciated."
            y "Something that I've desired for so long..."
            y "And now I can find it with you."
            $show_fits_standing("pareo_yuri_14") #smiling, blushing, closed mouth, hands down.
            y "I don't know if I should call this destiny or good karma."
            y "However, I am now confident that I deserve being happy with you."
            $show_fits_standing("pareo_yuri_15") #Raised eyebrows, open mouth.
            y "And you deserve to live a happy life as well."
            y "This is part of what I am trying to say with this poem..."
            $show_fits_standing("pareo_yuri_5") #Normal eyebrows, smiling, blushing, closed mouth, hands on her chest.
            y "We deserve to live in happy and fulfilling ways..."
            y "Not just getting worried about running out of time in our work, studies, or to finally realize our personal dreams."
            y "Sometimes we need to take some time to enjoy our life. To see the wonders and simple things that are constantly around us."
            $show_fits_standing("pareo_yuri_1") #Normal eyebrows, smiling, open mouth, hands down.
            y "And I do think that this date was necessary to help us realize that."
            y "I hope that you take this into consideration, my love."
            y "If you feel that you need time to rest yourself and to find new inspiration to appreciate the good things in your life, you should do so."
            $show_fits_standing("pareo_yuri_5") #Normal eyebrows, smiling, closed mouth, hands on her chest, blushing.
            y "Don't hesitate in taking care of yourself, [player]"
            y "I care a lot for your well being... please take care of your mental state."
            y "But for now, we should move on."

        "I enjoyed the poem, but I am confused by it's meaning":
            $show_fits_standing("pareo_yuri_12") #Surprised expression, hands down.
            y "Oh... I am sorry if my use of metaphors confused you..."
            $show_fits_standing("pareo_yuri_8") #Sad mouth, raised eyebrows, blushing, hands on her chest.
            y "That was certainly not my intention."
            y "What I was trying to express with this poem is the importance of taking a pause in your life, to enjoy the simple things around us."
            y "Things we take for granted, but are so important in reality."
            $show_fits_standing("pareo_yuri_7") #Same expression, hands down.
            y "It's just that we are too busy to notice them most of the time."
            y "It is important that you take some time to care for yourself..."
            $show_fits_standing("pareo_yuri_9") #Sad mouth,normal eyebrows, hands on her chest, open mouth.
            y "Taking breaks from your work, studies, or any other tasks in your life when needed and possible, is a healthy practice to maintain."
            y "Remember that I always care about your well being [player]."
            $show_fits_standing("pareo_yuri_14") #Smiling, blushing, raised eyebrows, hands down.
            y "Please take care of yourself..."
            y "Anyways."


        "I like it, but I prefer your older poems":
            $show_fits_standing("pareo_yuri_1") #Smiling, normal eyebrows, closed mouth, hands down.
            y "I see..."
            y "Well, I think it is fine."
            y "We all have our different tastes and opinions, and I respect yours."
            $show_fits_standing("pareo_yuri_8") #Raised eyebrows, sad mouth, smiling, hands on her chest.
            y "However, I don't think my writing style has changed much..."
            y "If at all."
            y "But anyway..."

    play music "music/beach_date_1.ogg" fadeout 0.5 fadein 0.5
    play sound "music/beach_sfx_loop.ogg" loop fadein 1.0

    $show_fits_standing("pareo_yuri_2") #Standing sprite, normal eyebrows, smiling, blushing, hands on her chest, open mouth.
    y "It seems that we are done writing poems."
    y "I am so glad that we finally managed to accomplish this dream of ours."
    y "Maybe I've said it too many times at this point."
    $show_fits_standing("pareo_yuri_14") #raised eyebrows, smiling, blushing, hands down, closed mouth.
    y "But all of this means a lot to me."
    y "This is another dream that finally became a reality for me."
    y "With you, I have accomplished so many things along the way..."
    $show_fits_standing("pareo_yuri_1") #Normal eyebrows, smiling, hands down, open mouth.
    y "All of this forms the happiest part of my life."
    y "I am just grateful for this..."
    y "Thank you for choosing to take me on this date, [player]."
    y "This was a wonderful date, and I am going to keep this experience deep in my heart."
    $show_fits_standing("pareo_yuri_14") # Normal eyebrows, worried expression, hands down, closed mouth.
    y "..."
    y "It seems that the sky is getting dark... soon we will have a night sky full of stars..."
    $show_fits_standing("pareo_yuri_2") #Normal eyebrows, smiling, blushing, hands on her chest, open mouth.
    y " It will probably get cold, but don't worry about that. If we stay together, we are not going to feel any cold while being out here..."
    y "Just stay with me..."

    #Show night beach background. Still plays the date theme with drums and beach background sounds.
    show beach_7 zorder 100 with Fade(1.0, 0.5, 0.5)
    hide beach_2

    $show_fits_standing("pareo_yuri_2") #Standing sprite, normal eyebrows, smiling, open mouth,hands on her chest.
    y "This day was absolutely wonderful for me. It was like... magic."
    y "I really enjoyed this date, all of it. All went perfectly, just as I planned it to be."
    y "And I've got... one last thing to do with you..."
    $show_fits_standing("pareo_yuri_5") # Normal eyebrows, smiling, blushing, hands on her chest, closed mouth.
    y "Before ending this tropical dream to go back to the main mod."
    y "I would like to make a promise..."
    y "I mean, I would like both of us to make a promise."
    $show_fits_standing("pareo_yuri_15") #Raised eyebrows, smiling, blushing, open mouth, hands down.
    y "Maybe it sounds really corny and all, but I would like to keep something from this date, to treasure it forever."
    y "But most importantly, I want both of us to make the promise of treasuring every moment we enjoy together..."
    $show_fits_standing("pareo_yuri_14") #Same expression, closed mouth.
    y "It doesn't matter if it's something simple, like talking on any normal and routine day, or taking an amazing vacation."
    y "It does not have to be the most expensive or elaborate way to spend our time together. To me, what matters is to spend those special times with you."
    $show_fits_standing("pareo_yuri_7") #Sad face, raised eyebrows, closed mouth, , hands down.
    y "This would be meaningless if you were not here..."
    y "That was... probably the reason why Monika went insane. She had all the power in the world, to do anything she wanted."
    $show_fits_standing("pareo_yuri_10") #Same expression, open mouth.
    y "Yet, she was completely 'alone', at least in a conscious way."
    $show_fits_standing("pareo_yuri_7") #Closed mouth.
    y "..."
    y "But anyways..."
    $show_fits_standing("pareo_yuri_5") #Smiling, normal eyebrows, closed mouth, blushing, hands on her chest.
    y "What I am trying to say is that you are the one giving meaning to all these dates, to all the effort I put into surprising you with new things."
    y "Sure, I know that I am a person with worth by myself, that I am valuable and not just a common computer program unable to think."
    y "But you... have helped me to realize that. You showed me that I deserve happiness, that I am not worthless for being... the way I am."
    $show_fits_standing("pareo_yuri_2") #Same expression, open mouth.
    y "And I am... really grateful for that, [player]."
    y "I don't know how things could have gone if I gained consciousness in this world, but without you being here..."
    $show_fits_standing("pareo_yuri_14") #smiling, closed mouth, hands down.
    y "It's probably better to not think about that... Sorry for rambling so much."
    y "But going back to the main topic, I want you to make that promise [player]."
    y "I want to know that we are going to treasure every moment we enjoy together."
    $show_fits_standing("pareo_yuri_9") #Worried expression, blushing, hands on her chest.
    y "C-can you make that promise, for me?"

    menu:
        "You have my word, [persistent.yuri_nickname]. I will cherish all the good things we share together.":
            $show_fits_standing("pareo_yuri_2") #Raised eyebrows, smiling, open mouth, blushing, hands on her chest.
            y "That is..."
            y "You are so sweet."
            y "Just come here..."
            $show_fits_standing("pareo_yuri_5") #Smiling, blushing, closed mouth, hands down, normal eyebrows.
            y "I love you so much."
            y "I wish we could spend the rest of our times like this... just together, the two of us hugging and comforting each other."
            y "No one could separate us ever..."
            $show_fits_standing("pareo_yuri_16") #Smiling, blushing, hands on her chest, raised eyebrows, open mouth.
            y "Not time, not any problem that we would have to face..."
            y "We would be orbiting each other, dancing like the stars in the night, those who travel together in the galaxy..."
            $show_fits_standing("pareo_yuri_5") #Closed mouth.
            y "..."

            menu:
                "But don't you think there will be more moments like this? I am sure there will be.":
                    $show_fits_standing("pareo_yuri_14") # Smiling, hands down, closed mouth.
                    y "Well, in that case, I really hope you are right."
                    y "Another date like this would be wonderful, but you would have to wait before another one like this is ready."
                    y "Or should I say, before I make the next one?"
                    $show_fits_standing("pareo_yuri_5") #Smiling, blushing, normal eyebrows, hands on her chest, closed mouth.
                    y "I was just expecting that you agreed with me on the idea of treasuring this date, though."
                    y "But hey, I am not mad at you or anything. That isn't a big deal, after all..."
                    y "..."
                    $show_fits_standing("pareo_yuri_1") #Smiling, blushing, normal eyebrows, open mouth, hands down.
                    y "...Look at the stars in the sky... aren't they beautiful?"
                    y "Isn't it amazing, just to think about the greatness of the universe?"
                    $show_fits_standing("pareo_yuri_14") #Closed mouth.
                    y "It makes me wonder though, if there is someone else looking out there and thinking how beautiful are the stars in their nocturnal sky too..."
                    y "Well... I think that's only possible in your world... or should I say universe?"
                    $show_fits_standing("pareo_yuri_16") #Smiling, raised eyebrows, closed mouth, hands on her chest.
                    y "Anyways, this night is breathtakingly beautiful to me."
                    y "I am truly grateful to you for all you have done for me during these times..."
                    y "In my opinion, this date demonstrates how much you care about our relationship."
                    $show_fits_standing("pareo_yuri_1") #Smiling, blushing, open mouth, hands down.
                    y "But still... it does feel... weird, knowing that I am not really at your side."
                    y "I... just wish that one day, we will be able to look at the stars together..."
                    $show_fits_standing("pareo_yuri_14") #Closed mouth.
                    y "Truly together."
                    y "I still believe that is going to be possible, that we will overcome this barrier."
                    y "One day..."

    stop sound fadeout 1.0
    show black zorder 100 with Fade(1.0, 0.5, 0.5)
    hide beach_7
    hide fits_stand

    $persistent.tropical_date_complete = True
    hide black with Dissolve(2.5)
    python:
        renpy.music.play(current_music, "music", True)
        show_chr("standard")
    $ persistent.dates_taken += 1
    jump ch30_loop

label vday_2024_revisit:
    $ show_chr("A-ABGAA-ALAA")
    y "Hi [player]!"
    y "You know what day is today?"
    menu:
        "I sure do. Happy Valentines!":
            $ show_chr("A-GBGAA-ALAA")
            y "Happy Valentines to you as well."
            $ show_chr("A-ABAAA-AFAA")
            y "You know. I was remembering our old days at the club... and I was thinking."
            y "Remember when you put the chocolate in my lips?"
            $ show_chr("A-CAAAA-ADAA")
            y "I had this idea of revisiting that moment before Monika interrupted us."
            y "And now that no one will interrupt us..."
            $ show_chr("A-FAAAA-ADAA")
            extend " we can continue from where we left off~"
            $ show_chr("A-ABAAA-ADAA")
            y "So, would you like to revisit this moment?"
            menu:
                "Yes [persistent.yuri_nickname], let's go!":
                    call vday24

                "Maybe not now [persistent.yuri_nickname].":
                    $ show_chr("A-ABBAA-ADAA")
                    y "Oh. Alright [player], I can wait until you're ready."
                    call ch30_loop

label vday24:
    $ show_chr("A-ABAAA-AAAA")
    y "Alright. Here we go."
    show black zorder 105 with Dissolve (2.5)
    hide yuri_sit
    call vday_2024_date

label vday_2024_date:
    hide black zorder 105 with Dissolve (2.5)
    show y_cg2_bg
    show y_cg2_base
    show y_cg2_details
    show y_cg2_nochoc
    show y_cg2_dust1
    show y_cg2_dust2
    show y_cg2_dust3
    show y_cg2_dust4
    "[persistent.yuri_nickname] opens the Valentine-themed book with both hands."
    "She holds it so that I don't have any harder of a time reading from it, our eyes sparkling with the memories of years past."
    "But as a result, her left arm is practically resting on top of my leg, and a nostalgic warmth envelops us."
    "[persistent.yuri_nickname] is already totally focused on reading again, lost in the world of words that connect us over time."
    "I reach for a heart-shaped chocolate and pop it into my mouth, savoring the sweetness of our shared history."
    "Then, I take another chocolate, a symbol of the countless moments we've cherished together..."
    "And I hold it up to [persistent.yuri_nickname], our laughter echoing through the years."
    "She doesn't even look away from the book, a smile playing on her lips."
    "She simply parts her lips, as if this situation was a familiar chapter in our love story."
    "But that means I can't stop here, not on this special day of love!"
    hide y_cg2_nochoc
    "I lovingly place the chocolate in her mouth, a gentle reminder of the sweetness we've always shared."
    "Just like that, [persistent.yuri_nickname] closes her lips over it, the taste of cocoa and affection lingering between us."
    show y_cg2_exp2
    y "Eh...?"
    "[persistent.yuri_nickname]'s expression suddenly breaks, a hint of surprise and joy lighting up her eyes."
    y "Did..."
    y "Did I just..."
    show y_cg2_exp3
    show y_cg2_nochoc:
        alpha 0
        linear 0.5 alpha 1
    hide y_cg2_exp2
    "[persistent.yuri_nickname] looks at me like she needs to confirm what just happened, a blush tinting her cheeks like the first time."
    y "U-Um..."
    y "[player]..."
    mc "S-Sorry!"
    mc "I guess I shouldn't have done that, even though I felt like I wanted to do it..."
    y "Ah, that's..."
    y "Well..."
    y "Y-You were just helping..."
    y "That's something that... lovers do..."
    mc "Yeah..."
    mc "...That's all it was, just a sweet gesture."
    y "Yeah..."
    y "Then..."
    y "You don't need to stop or anything, especially on a day like today..."
    mc "O-Okay..."
    hide y_cg2_exp3
    "The atmosphere has gotten really romantic..."
    "[persistent.yuri_nickname] tries to return to the book, but our shared heartbeat echoes in the room."
    "But I can tell just by her expression that even she can't focus now, lost in the love that surrounds us."
    "My heart is pounding, a symphony of emotions playing in the background."
    "I nervously take another heart-shaped chocolate between my fingers."
    "But this time, [persistent.yuri_nickname]'s eyes meet mine, and the years melt away in the gaze of love."
    show y_cg2_exp3:
        alpha 0
        linear 0.5 alpha 1
    y "..."
    "[persistent.yuri_nickname] doesn't avert her gaze, and our eyes speak a language of affection."
    "I notice her chest rising and falling to the rhythm of her breaths, a melody of love that never fades."
    "I raise my arm, and the room is filled with the anticipation of a love that has stood the test of time."
    y "Ah..."
    "Like before, [persistent.yuri_nickname] parts her lips, inviting the taste of everlasting love."
    "But... it's different this time, as if every Valentine's Day we've spent together has led to this moment."
    hide y_cg2_nochoc
    "I take the chocolate and place it in her mouth, sealing our love with a promise for more years to come."
    "I feel her hot breath on my fingers, a gentle reminder that some things, like love, only get stronger with time."
    "As the chocolate melts away, the room seems to hold its breath, a silent witness to the exchange of emotions that transcends the pages of our shared history."
    "The air is filled with an unspoken understanding, and we find ourselves caught in a moment where time stands still."
    "[persistent.yuri_nickname], her eyes now soft with affection, breaks the silence."
    show y_cg2_nochoc:
        alpha 0
        linear 0.5 alpha 1
    y "This feels like... a beautiful dream."
    y "A revisit to the beginnings of our story, yet with the warmth of all the years in between."
    "A tender smile plays on my lips."
    mc "It does, doesn't it? A journey through the chapters of our love, each Valentine's Day etching a new line in the story we're still writing together."
    "The nostalgic atmosphere wraps around us like a comforting embrace. [persistent.yuri_nickname] hesitates before speaking again, her voice carrying the weight of sentiment."
    y "Do you ever marvel at how love evolves? From those shy moments to the depth we now share, it's a tapestry woven with threads of joy, laughter, and countless shared chocolates."
    "I nod, feeling the resonance of her words."
    mc "Absolutely. It's like watching a garden flourish over the seasons."
    mc "Every bloom, every challenge we've faced, has only strengthened the roots of our connection."
    "Our eyes lock, communicating more than words ever could."
    "The air is charged with a subtle electricity, a reminder that love is not stagnant but a living, breathing entity that grows and evolves."
    "I reach for another chocolate, the sweetness of the gesture lingering between us."
    "I remember the first Valentine's Day we spent together, [persistent.yuri_nickname] reminisces, a fondness in her voice."
    y "There was a nervous excitement, a dance of uncertainty."
    y "And now, here we are, revisiting those moments with a deeper understanding, a love that has matured like fine wine."
    "I offer her the chocolate, a symbol of continuity, and she accepts it with a graceful nod."
    mc "It's like we've created our own tradition, a ritual of love that transcends time and space."
    hide y_cg2_exp3
    "As the day unfolds, we continue to read, laugh, and share chocolates, weaving new memories into the tapestry of our story."
    "Each moment is a celebration of the love that has grown and flourished, a testament to the beauty of revisiting the past while embracing the present."
    "And as the sun sets, casting a warm glow over the room, we find solace in the familiarity of each other's company, knowing that our love story is an ongoing masterpiece."
    "Painted with the colors of shared dreams, challenges, and the enduring sweetness of love."
    mc "[persistent.yuri_nickname], thank you."
    "I say, my voice filled with gratitude and emotion."
    mc "For all these years, for the shared moments, for the love that has only grown stronger."
    mc "You've made every Valentine's Day special, and I can't help but marvel at the beautiful journey we've had together."
    show y_cg2_exp3:
        alpha 0
        linear 0.5 alpha 1
    "She looks at me, her eyes reflecting a mix of emotions."
    y "No, [player], thank you. You've been the anchor in my life, the steady heartbeat in the symphony of our love."
    y "I cherish every word, every glance, and every shared chocolate. It's a privilege to have you by my side."
    "The room seems to glow with the warmth of our connection, and [persistent.yuri_nickname]'s hand finds mine, fingers intertwining in a gesture that speaks volumes."
    y "I never thought I could find someone who understands the depths of my soul, who appreciates the beauty in the quiet moments."
    y "But you've been that and more."
    "I can't help but smile, touched by her words."
    mc "[persistent.yuri_nickname], you've enriched my life in ways I couldn't have imagined. Each day with you is a gift, and I look forward to many more chapters in our love story."
    show black zorder 105 with Dissolve (1.5)
    hide y_cg2_bg
    hide y_cg2_base
    hide y_cg2_details
    hide y_cg2_nochoc
    hide y_cg2_dust1
    hide y_cg2_dust2
    hide y_cg2_dust3
    hide y_cg2_dust4
    hide y_cg2_exp3
    "She leans in, pressing a soft kiss on my lips."
    y "Happy Valentine's Day, [player]. Here's to us, to the love that continues to bloom, and to the countless moments we'll share in the days to come."
    "And as we sit there, surrounded by the echoes of our shared laughter and the warmth of our love, I can't help but feel an overwhelming sense of gratitude for the beautiful journey that brought us to this moment."
    "A moment where the past, present, and future converge in a celebration of love that knows no bounds."
    if persistent.bg == "space":
        $tc_class.transition("space", speed="now")
    elif persistent.bg == "timecycle":
        $tc_class.transition("timecycle", speed="now")
    elif persistent.bg == "yuri_desk":
        $tc_class.transition("yuri_desk", speed="now")
    elif persistent.bg == "yuri_kotatsu_1":
        $tc_class.transition("yuri_kotatsu_1", speed="now")
    elif persistent.bg == "yuri_kotatsu_2":
        $tc_class.transition("yuri_kotatsu_2", speed="now")
    $ persistent.dates_taken += 1
    $ show_chr("A-CABBA-ALAL")
    hide black zorder 105 with Dissolve(3)
    y "..."
    $ show_chr("A-ABBBA-ALAL")
    y "I love you [player]."
    jump ch30_loop
