label purpleroomintro: #New Intro
    #Introduction of the Purple room
    #Requirements:
    #Karma level 5 and/or lovecheck is true
    #20 sessions ingame
    #Yuri asked player at least once if her knives freak him out, and he has to reply in a positive way (idle 30).
    $ show_chr("A-JBAAA-AAAA")
    y "I can't wait anymore! [player], I have something big to show you! I made a new location for us. I hope you'll like it..."
    if not persistent.bg == "yuri_kotatsu_1" or "yuri_table" or "yuri_desk" or "yuri_kotatsu_2" or "yuri_knives" or "yuri_bed":
        $tc_class.transition("yuri_desk", speed=3.0)

    y "It's my bedroom! Now I can talk to you from my own desk at home!"
    y "It's modeled after my 'real' room at home, albeit... a fair bit larger. I was never able to invite you over in the original game, perhaps because the files for it didn't exist outside of my own memories."
    $ show_chr("A-ABAAA-AMAM")
    y "That, and the fact that I considered my parents too embarrassing to introduce to you, especially when I wasn't certain if my feelings for you were mutual..."
    $ show_chr("A-JAAAA-AAAA")
    y "Anyway. Welcome to my refuge! I have my favorite notebooks and pens, headphones,  my book collection, my laptop... I can't tell you how many hours I've spent here, happily lost in my own little world."
    y "I was even able to code in a Kotatsu! It's the perfect size for serving tea."
    $ show_chr("A-ABAAA-AAAA")
    y "I must say, creating new locations is harder than one might think. Art assets are more time-consuming than difficult, but the coding... well. I wanted to show you a complete room *and* hallway, but unfortunately, it's still a work in progress."
    $ show_chr("A-AAAAA-AAAA")
    y "I'm so happy I can show you my little haven, though! I... it may sound silly, but I've dreamed of having someone over even just to read with them. And now you're here."
    $ show_chr("A-JBAAA-AAAA")
    y "Also... there's something I'm almost *more* excited to show you. My knife collection. I created a whole display for it, the kind I always dreamed of having!"
    $ show_chr("A-BCAAA-ABAB")
    y "I mean, if you're even interested to begin with. I can understand if knives aren't your cup of tea."
    $ show_chr("A-BCABA-ABAJ")

    #There should definitely be a lovecheck somewhere in here... will she only show the room if she has some trust in the player? I'd assume yes. 

    y "You know... I usually don't let other people into my bedroom, or show them my knives... but you've proven to me, time and time again, that I can trust you."
    $ show_chr("A-ACAAA-ABAE")
    y "So... would you like to see my collection?"
    menu:
        "Yes, of course!":
            $ show_chr("A-CAAAA-AAAA")
            y "Then please, follow me..."
            call preknife

        "Maybe not now.":
            $ show_chr("A-ABBAA-AAAA")
            y "Well... alright. Just tell me when you're ready."
            call ch30_loop

        "Are those dollhouses in your bookshelf?":
            $ show_chr("A-BDAAA-ADAA")
            y "Not exactly. They're book nooks! I was briefly into making miniatures as a hobby, and I created a few scenes inspired by the books I was reading at the time. Nothing specific, just vague fantasy locations." 
            $ show_chr("A-ADAAA-AFAA")
            y "The complete building on the upper right is actually from a kit I remember being gifted a long time ago, but I didn't attempt putting it together until right before my senior year of high school."
            $ show_chr("A-BFAAA-AFAA")
            y "It didn't turn out as well as the one you're looking at now... I didn't find the instructions to be very clear, and when I tried to undo the steps I had made in error I broke one of the largest pieces in the set."
            $ show_chr("A-BDAAA-ALAA")
            y "After that, I threw it away in frustration, but regretted it soon after. So, when I was thinking of how to decorate my room here, I realized I could recreate it as a perfect shelf display!"
            $ show_chr("A-CCAAA-ALAA")
            y "As for the diorama on the lower left, it's a secret underground room meant to be part of a castle. It's not modeled after any book or scene in particular, just something I made for fun."
            $ show_chr("A-ACAAA-ALAA")
            y "The room's not as detailed as it could be, but I like it that way–unanswered questions are wonderful for sparking inspiration."
            y "Can you see the little desk? Maybe the room is part of a spy network where intercepted messages are sent. Or it could be someone's hidden quarters, where a pair of lovers meet and leave notes for one another..." 

        "Where does that door lead?":
            $ show_chr("A-ADBAA-AAAA")
            y "Eventually, it will be a hallway, but I really wouldn't advise exploring. I'm looking forward to seeing your reaction, but I haven't gotten the code stable yet."
            menu:
                "I'll be looking forward to it.":
                    $ show_chr("A-ABAAA-AAAA")
                    y "I will too. I'm working hard on getting everything ready, and I hope to show you soon!"
                    menu:
                        "I really like your room, [persistent.yuri_nickname].":
                            $ show_chr("A-CCAAA-ALAA")
                            y "Thank you!"
                            $ show_chr("A-AAAAA-ALAA")
                            y "Would you let me see your bedroom, if you could? Or it, too, needs some work first?"
                            menu:
                                "I keep my room neat enough.":
                                    $ show_chr("A-CAAAA-ALAA")
                                    y "Doesn't a well-organized space feel nice? It's easy to work or relax in, and something about it is just so calming. It's not always easy to find the time or energy to put a room in order, but it's worth the effort."

                                "My room looks like a tornado hit it.":
                                    $ show_chr("A-ADAAA-ALAA")
                                    y "I know most people don't find cleaning to be an activity they enjoy, and private spaces such as the bedroom can get... chaotic. Worse, if there's too many things on the floor, it's difficult or impossible to vacuum."
                                    y "Would you like some help? I've heard good things about the Pomodoro method. You set a timer for a specific amount of time, say twenty minutes, and work until it goes off." 
                                    $ show_chr("A-ADAAA-AFAA")
                                    y "After that, you rest for a set time, then repeat until you're done. It's up to you if 'done' means 'finished with the task at hand' or just 'done for now regardless!'"
                                    $ show_chr("A-BDAAA-AFAA")
                                    y "And of course, there's apps for this! Pomodoro - Focus Timer is free, and a popular paid option is... ah... well, the iOS store calls it 'Unfilth Your Habitat'."
                                    $ show_chr("A-AAAAA-ALAA")
                                    y "If you need encouragement, just let me know. I'm always happy to cheer you on, [player]."
                                    #in a future update, add timer code? I found info on it here: https://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=52516&p=499010
                                    #Not sure if this dialogue is being kept

                                "So you did have parents?":
                                    $ show_chr("A-AFGAA-ALAA")
                                    y "I'd say 'of course', but I suppose that isn't actually a given for video game characters..."
                                    $ show_chr("A-ADAAA-ALAA")
                                    y "But yes, I have the sort of memories you might expect from a teenager. A mother, a father, and a much older sister. And yet... I actually can't remember any of their names, now that I think about it." 
                                    y "I mostly recall Mom and Dad not being concerned about my social life, or lack thereof, because I kept up my grades without being told to." 
                                    y "It was only over the last few months, since I joined the Literature Club, that they started asking me about friends at school. So when I mentioned you..." 
                                    $ show_chr("A-ABABA-AMAM")
                                    y "Truthfully, their reaction wasn't bad. Just—enthusiastic. I was afraid they'd scare you off, by insinuating things that might or might not be true." 
                                    y "So I made it a point not to invite you over until I had a better idea of how we both felt. And now that I do know..."
                                    $ show_chr("A-BDAAA-ALAA")
                                    y "It's somewhat unfortunate you don't get to see them officially but only time will tell how my parents would look like."

    $ show_chr("A-AAAAA-ALAA")
    y "..."
    y "Anyway, what would you like to do?"
    call ch30_loop

label preknife:
    show black zorder 100 with Dissolve(2.5)
    $ tc_class.transition("yuri_knives", speed="now")
    hide yuri_sit
    show screen un_knife_wall()
    hide black zorder 100 with Dissolve(2.5)
    y "And here it is! Much nicer than the one in my memories—I doubt many teenagers have a display cabinet built directly into their bedroom walls."
    y "What do you think?"
    menu:
        "It's nice! What a great job you've done, [persistent.yuri_nickname]!":
            #karma +1
            karma 1
            y "Oh thank you! I put a lot of effort into it, I'm glad that you like it!"
    
        "It's quite... elegant. But still an amazing piece of work [persistent.yuri_nickname]!":
            #karma +2 (I think she respects honesty)
            karma 2
            y "...I guess you're right. Maybe I took it a bit too far?"
            y "Thank you for your feedback, I appreciate your honesty." 
    
        "It's...not very impressive, I must admit.":
            #karma -1
            karma -1
            y "...I see."

    hide screen un_knife_wall
    call screen knife_wall()

screen un_knife_wall():

    frame:
        imagebutton:
            xpos 350 ypos 102
            idle "bg/yuri_knives/knives/filet_idle.png"
            action NullAction()

        imagebutton:
            xpos 158 ypos 150
            idle "bg/yuri_knives/knives/butterfly_idle.png"
            action NullAction()

        imagebutton:
            xpos 346 ypos 208
            idle "bg/yuri_knives/knives/grater_idle.png"
            action NullAction()

        imagebutton:
            xpos 159 ypos 277
            idle "bg/yuri_knives/knives/empty_idle.png"
            action NullAction()

        imagebutton:
            xpos 352 ypos 331
            idle "bg/yuri_knives/knives/dagger1_idle.png"
            action NullAction()

        imagebutton:
            xpos 183 ypos 387
            idle "bg/yuri_knives/knives/kabar_idle.png"
            action NullAction()

        imagebutton:
            xpos 338 ypos 455
            idle "bg/yuri_knives/knives/dagger2_idle.png"
            action NullAction()

        imagebutton:
            xpos 204 ypos 527
            idle "bg/yuri_knives/knives/kukri_idle.png"
            action NullAction()

        imagebutton:
            xpos 807 ypos 96
            idle "bg/yuri_knives/knives/jagdkommando_idle.png"
            action NullAction()

        imagebutton:
            xpos 626 ypos 161
            idle "bg/yuri_knives/knives/saw_idle.png"
            action NullAction()

        imagebutton:
            xpos 802 ypos 222
            idle "bg/yuri_knives/knives/bowie_idle.png"
            action NullAction()

        imagebutton:
            xpos 648 ypos 284
            idle "bg/yuri_knives/knives/damascus_idle.png"
            action NullAction()

        imagebutton:
            xpos 814 ypos 358
            idle "bg/yuri_knives/knives/kunai_idle.png"
            action NullAction()

        imagebutton:
            xpos 650 ypos 412
            idle "bg/yuri_knives/knives/paring_idle.png"
            action NullAction()

        imagebutton:
            xpos 789 ypos 471
            idle "bg/yuri_knives/knives/kampfmesser_idle.png"
            action NullAction()

        imagebutton:
            xpos 675 ypos 524
            idle "bg/yuri_knives/knives/bone_idle.png"
            action NullAction()

screen knife_wall():
    frame:
        imagebutton:
            xpos 350 ypos 102
            idle "bg/yuri_knives/knives/filet_idle.png"
            hover "bg/yuri_knives/knives/filet_hover.png"
            action Jump("Filet")

        imagebutton:
            xpos 158 ypos 150
            idle "bg/yuri_knives/knives/butterfly_idle.png"
            hover "bg/yuri_knives/knives/butterfly_hover.png"
            action Jump("Butterfly")

        imagebutton:
            xpos 346 ypos 208
            idle "bg/yuri_knives/knives/grater_idle.png"
            hover "bg/yuri_knives/knives/grater_hover.png"
            action Jump("Grater")

        imagebutton:
            xpos 159 ypos 277
            idle "bg/yuri_knives/knives/empty_idle.png"
            hover "bg/yuri_knives/knives/empty_hover.png"
            action Jump("Empty")

        imagebutton:
            xpos 352 ypos 331
            idle "bg/yuri_knives/knives/dagger1_idle.png"
            hover "bg/yuri_knives/knives/dagger1_hover.png"
            action Jump("Dagger1")

        imagebutton:
            xpos 183 ypos 387
            idle "bg/yuri_knives/knives/kabar_idle.png"
            hover "bg/yuri_knives/knives/kabar_hover.png"
            action Jump("Kabar")

        imagebutton:
            xpos 338 ypos 455
            idle "bg/yuri_knives/knives/dagger2_idle.png"
            hover "bg/yuri_knives/knives/dagger2_hover.png"
            action Jump("Dagger2")

        imagebutton:
            xpos 204 ypos 527
            idle "bg/yuri_knives/knives/kukri_idle.png"
            hover "bg/yuri_knives/knives/kukri_hover.png"
            action Jump("Kukri")

        imagebutton:
            xpos 807 ypos 96
            idle "bg/yuri_knives/knives/jagdkommando_idle.png"
            hover "bg/yuri_knives/knives/jagdkommando_hover.png"
            action Jump("Jagdkommando")

        imagebutton:
            xpos 626 ypos 161
            idle "bg/yuri_knives/knives/saw_idle.png"
            hover "bg/yuri_knives/knives/saw_hover.png"
            action Jump("Saw")

        imagebutton:
            xpos 802 ypos 222
            idle "bg/yuri_knives/knives/bowie_idle.png"
            hover "bg/yuri_knives/knives/bowie_hover.png"
            action Jump("Bowie")

        imagebutton:
            xpos 648 ypos 284
            idle "bg/yuri_knives/knives/damascus_idle.png"
            hover "bg/yuri_knives/knives/damascus_hover.png"
            action Jump("Damascus")

        imagebutton:
            xpos 814 ypos 358
            idle "bg/yuri_knives/knives/kunai_idle.png"
            hover "bg/yuri_knives/knives/kunai_hover.png"
            action Jump("Kunai")

        imagebutton:
            xpos 650 ypos 412
            idle "bg/yuri_knives/knives/paring_idle.png"
            hover "bg/yuri_knives/knives/paring_hover.png"
            action Jump("Paring")

        imagebutton:
            xpos 789 ypos 471
            idle "bg/yuri_knives/knives/kampfmesser_idle.png"
            hover "bg/yuri_knives/knives/kampfmesser_hover.png"
            action Jump("Kampfmesser")

        imagebutton:
            xpos 675 ypos 524
            idle "bg/yuri_knives/knives/bone_idle.png"
            hover "bg/yuri_knives/knives/bone_hover.png"
            action Jump("Bone")

    textbutton "Back":
        xpos 585
        yalign 0.97
        style "scrollable_menu_button"
        action Call("room_back")

show screen knife_wall()

label room_back:
    if persistent.first_knife:
        $ tc_class.transition("yuri_desk", speed="now")
        $ show_chr("A-AAAAA-AAAA")
        y "Now then, what would you like to do?"
        $ persistent.first_knife = False
    else:
        $ tc_class.transition("yuri_desk", speed="now")
        pass

    call ch30_loop

label Kampfmesser: #This is meant to be for the left displays's top left most knife. Black handle.
    y "Ah, the Kampfmesser 2000! A fine piece of military equipment..."
    y "The Kampfmesser - quite literally translating to 'combat knife' - is the standard combat knife of Germany's Bundeswehr, the Defense Force of the country."
    y "It's been made famous by its 'unorthodox' design, at least in terms of military knives; it has a design similar to that of a Tanto, which is highly unusual for military-based knives in large numbers."
    y "As such, due to the blade's popularity, several offshoots have been designed and sold...different materials for the blade, or even changes to better suit different environments, like the desert."
    y "But, I prefer to have the original as a nice showpiece to represent the entire line. It's not to say that the others are any less interesting..."
    y "It's just that I don't think I'd ever have enough room to properly display every single variant, you see. It's also not very engaging to listen to. The last thing I want to do is bore you..."
    menu:
        "Don't be silly, [persistent.yuri_nickname]. I'd love to hear more about them and anything else you know.":
            y "Oh, really? Then, allow me..."
            y "This is the basic variant of the Kampfmesser 2000. It's often just referred to as the KM2000, for brevity's sake."
            y "As I said, there have been several variants produced for a variety of different situations and environments."
            y "The KM1000 is essentially just a KM2000 without the coating, leaving the blade a nice, non reflective silver. Good if you don't want to worry about the coating being damaged overtime, I suppose...but the coating is good for corrosive resistance. These are special use case knives, I believe."
            y "Going on from there, there's the KM3000, which abandons the tanto-style point in favor of an almost spear-like tip. An odd choice, I suppose. The tanto style tip was fairly iconic amongst the Kampfmesser brand."
            y "I'm sure it has its uses, but...well. I think my preference is known, yes? The tanto design allows the knife's tip to double as a pry bar due to the strength of the design...but, moving on from that..."
            y "Both of these have further variants with sand colored scabbards and grips. As you could probably guess, they're for use in desert environments; they saw some popularity in Afghanistan."
            y "I mentioned this before, but it seems like the knives themselves didn't change much for the hot environment..."
            y "There's also a KM4000. Eickhorn received requests from the German Armed Forces for further-expanded multi-functionality in their knives, and this was their response. It goes back to the tanto-style tip, but also includes a complete saw-back alongside an actual wire cutter!"
            y "All of these offshoots and variants born from a single knife. They're ultimately the same at heart, just with a few alterations."
            y "The blades themselves are comprised of Böhler N695. It's a particular type alloy designed to hold an edge better than previous 1.4110 steel. Though you could also find knives being produced with 1.4125..."
            y "Going further, the knives come in partially serrated or straight edge variants for a variety of use cases, depending on what you see yourself needing more. Many people opt for the partially serrated versions. Having a saw on hand is...well, handy."
            y "And before I forget, an interesting trait they all seem to share is located in the handle of the knife itself. In the bottom is a glass breaker tip; a solid lug of metal designed for exactly what it sounds like."
            y "It's actually the end of the knife blade! The knives are full tang; that is to say, one solid, complete piece of steel. In this situation, it feels like no part of the metal goes to waste!"
            y "The Kampfmesser family is incredibly diverse in their several approaches to what's essentially the same blade. I appreciate their work in making sure that there's a little something for everyone..."

        "It's okay, [persistent.yuri_nickname]. You don't have to go into a history lesson about every variation.":
            y "Quite. If I did, we'd be here for a while, I believe..."
            y "Ah, but I'm rambling again. My apologies, [player]."
            y "Is there any other blade of which you'd have me speak on?"
    call screen knife_wall()

label Kabar: #This is meant for the knife to the right of the one above. The KA-BAR; Left display, top row, middle.
    y "Oh, yes, the famous USN Mark 2 Utility Knife. Many military enthusiasts know this blade well; you've almost certainly encountered it through some form of media."
    y "You may know it better by its contemporary name; The Ka-Bar!"
    y "A combat knife first adopted by the United States Marine Corp, and later the Navy. It first saw service in November of 1942, after Marines complained about their previous blade of choice, the Mark I trench knife..."
    y "It was designed both to be used for combat, but also as a tool. The environments many soldiers found themselves in proved to be much more amiable with this at their sides."
    y "There's a funny story about the trademark name KA-BAR I recall reading once."
    y "Apparently, the company that owns the trademark received a letter sometime in the 1920s from a fur trapper."
    y "The trapper claimed that he had used one of their blades to finish off a wounded bear that had assaulted him after his rifle had jammed."
    y "The letter was quite illegible, however; only fragments of the phrase 'kill a bear' could be read, which came out as 'ka bar'. The company found this to be high praise, as well as a great advertising point."
    y "As such, the brand 'KA-BAR' was established; a knife good enough to kill even a bear."
    y "Now, of course, this report leaves much to be discussed. Of course, the biggest question is; did it actually kill a bear?"
    y "Who knows? I'm certainly not about to find out...and I hope you aren't, either, [player]!"
    y "Hehe...that was fun. Is there any other knife you'd like me to talk about?"
    call screen knife_wall()

label Bowie: #This is meant for the pair of Bowie Knives in the right display's bottom row.
    y "Oh, my, the Bowie Knife...quite hard to miss, isn't it, [player]?"
    y "It's an almost comically large blade, going up to 30cm...that's to say, 12 inches in length."
    y "The history behind it is quite funny, too. It was originally made for a man named Jim Bowie for use in a duel."
    y "I believe the duel is known as the Sandbar Fight. Quite a sordid affair it ended up being..."
    y "It was less a 'duel' and more a brawl between a large number of participants. Guns were drawn, shots fired, and well..."
    y "The knife has a fascinating history, is the point of this all. Bowie even managed to win with the knife despite having been shot, stabbed, and nearly beaten to death."
    y "The blade itself carries along that same spirit of hardiness. You'd be hard pressed to find a situation in which this pretty number wouldn't help...be it through intimidation or force. How did that line go? 'That's not a knife...{i}THIS{/i} is a knife'?"
    y "Not that I'm saying you should go and pick fights! Or put yourself in a situation in which a fight could be picked to begin with!"
    y "No, no...please, be safe! Knife or no knife!"
    y "Goodness...sorry about that. I worry for you, from time to time, is all."
    y "Was there any other piece of my collection you'd like to discuss?"
    call screen knife_wall()

label Jagdkommando: #This is about the Jagdkommando knife
    y "Ah, the Jagdkommando tri-dagger... Amongst the most dangerous knives in the world."
    y "A 7-inch twisted blade made from 6AL-4V Titanium, with a grenade-like handle, which is also made from the same material."
    y "Regarding comfort and handling, it isn't the best, but the handle does give the user a solid grip."
    y "The blade is hollowed, which further enhances its menacing looks and reduces the overall weight of the dagger."
    y "The name comes from the Austrian Special Forces Operation group, and it lives up to its elite namesake."
    y "The dagger comes with a custom hard-coated 6061-T6 tubular sheath to protect the blade and the user, and has storage for a compass as well!"
    y "The very unique style of this knife intrigues me a lot, and I've read many things about its capabilities."
    y "Although, as you can see, [player], this is only a safe, dull knife, since the actual one is illegal in many countries."
    y "If there was someone who'd be unfortunate enough to be stabbed by it, no doctor could even stitch the penetrated area because of the twisted blades making a pyramid-shaped wound that, even if it was stitched from the surface, wouldn't staunch bleeding, thus making it an internal wound."
    y "Its sturdiness is top-notch, as well, therefore the durability and reliability sky-rocket to a very high point, and when combined with the grip it offers, you could even stab through bricks, if you're powerful enough."
    y "But, despite this only being a dull knife, I still like it for its aesthetics and overall appearance, not that I don't like my other knives, too...!"
    y "{cps=500}Oh no I'm being embarrassing again!-{/cps}{nw}" #(very fast, barely any time for the player to even read it)
    y "I'm glad that you love knives as much as I do, [player]."
    if persistent.lovecheck:
        y "I love you."
    else:
        pass
    call screen knife_wall()

label Bone:
    y "Have you ever read about knives made from bone? They've been used to create blades in many cultures, and not just in the distant past." 
    y "I read a study recently about people in the Sepik region of New Guinea, who made them for use in battle as recently as the 1970s." 
    y "There doesn't seem to be a special name for these weapons, so anthropologists are just calling them 'bone daggers.'"
    y "Many such pieces have elaborate patterns etched into them, but others are strictly utilitarian."
    y "What's especially fascinating is that the bones they're made from are acquired from two completely different sources."
    y "One is cassowaries, a very large type of flightless bird common to the area, and the second is... their own ancestors."
    y "According to scholars, the daggers of human origin were sourced from the femurs of men who had proven themselves in battle, often the warriors' own fathers, or other highly respected men in the community." 
    y "Thus, taking a part of them with you into battle was seen as a way to add their strength to your own."
    y "As for cassowary daggers, the birds are rightly seen as powerful creatures—you can really see their dinosaur ancestry when you look at them!" 
    y "Wielding a part of one is also thought to imbibe you with their strength, but the ones made of human bone are held in much higher regard." 
    y "A study showed that while human and cassowary femurs are basically equal in strength, the process of carving them into blades is different depending on the source." 
    y "Cassowary bones are shaved down more, making them thinner but consequently weaker. In contrast, human bones are cut to keep their natural curvature, resulting in a thicker but stronger blade, and feature decorative etching as well."
    y "I was actually lucky enough to acquire a bone dagger of my own! Oh, don't worry, it is from a cassowary, not a human. At least... that's what its plain appearance and overall thin profile point to it being."
    y "Although I did buy it online, so it's impossible to say for sure..."
    call screen knife_wall()

label Filet:
    y "One of the first knives I ever bought for myself. It's actually a fillet knife, meant for filleting and preparing fish."
    y "It typically features a long, flexible blade with a sharp point, allowing it to maneuver around bones and remove skin from fish effectively."
    y "It's not the highest quality, but it is still genuinely useful, unlike some others I bought."
    y "Many traditional Japanese dishes involve fish, so knowing how to debone them is a useful skill."
    y "The shape of this knife's handle is actually very practical, as you do not want to risk your fingers coming into accidental contact with the sharp blade if the job happens to get slippery."
    y "I was able to get Natsuki talking about cooking/baking once. It was quite enjoyable, up until I asked if she ever made healthy food. That... wasn't where I had intended the conversation to go."
    y "Predictably, it didn't end well, either."
    call screen knife_wall()

label Butterfly:
    y "As you likely know, this is a folding knife, also known as a butterfly knife."
    y "In addition to its obvious use as a weapon, it makes a lovely multi-use tool; many professions all but require keeping one folded in your pocket."
    y "Consequently, I find butterfly knives are very often designed to be both beautiful and functional. I actually own more than one, but this is by far the most appealing."
    y "It originated in the Philippines and gained popularity worldwide due to its unique flipping and spinning techniques."
    y "Butterfly knives are often used for tricks, flipping, and display purposes rather than as practical cutting tools."
    y "While illegal in some jurisdictions due to safety concerns and association with criminal activities, butterfly knives are legal and widely collected in many places."
    call screen knife_wall()

label Grater:
    y "That... is a stylized vegetable peeler. I bought it at a craft fair, so it has some hope of actually being food-safe, but mostly I was taken by its elegantly simple design."
    y "I didn't realize what it was until I read the care instructions later!"
    y "While it's not uncommon in fiction to see full-sized swords with cutouts like this one, on the grounds that it makes the blade lighter, it's actually the opposite of practical in real life."
    y "Such a design only makes the blade significantly weaker."
    y "Real swords are actually much lighter than you might expect; contrary to what some movies would have you believe, they're not made by pouring molten metal into molds."
    y "Instead, the blades are formed by folding."
    y "This process involves heating the metal and then pounding it into shape, many times over, which removes impurities in the material and greatly strengthens the blade."
    y "It's truly an art form."
    y "Also, grater knives are essential tools in culinary tasks such as garnishing, baking, and adding flavor to dishes."
    y "They come in various sizes and styles, including handheld graters, box graters, and rotary graters."
    call screen knife_wall()

label Dagger1:
    y "...I must confess I'm not immune to the 'rule of cool.' I saw it, I liked it, and thus I bought it. It's functional as a letter opener, but nothing more."
    call screen knife_wall()

label Dagger2:
    y "Just an impulse purchase, I'm afraid. I saw it and was reminded of a blade in one of the books I was reading, and I couldn't resist. I actually bought two that day... and then one of them broke when I attempted to actually use it, and it hit the cutting board." 
    y "I wish I was joking! At that point, I realized decorative blades likely shouldn't be used on food regardless."
    call screen knife_wall()

label Empty:
    y "This spot here is for the kitchen knife I have within me if you were curious."
    y "You pretty much know what a kitchen knife works for so I won't go into much detail."
    call screen knife_wall()

label Kunai:
    y "I'm guessing you're familiar with this one: it's a kunai!"
    y "Media portrayals would have you believe it's exclusively used as a weapon, but historically it was more of a multi-use tool, most commonly for farming or stonework."
    y "It's likely not coincidental that the kunai somewhat resembles a masonry trowel."
    y "In fiction, you see them used largely as throwing weapons, but from what I've read, they were more practical for stabbing or slashing."
    y "Another common use in media is climbing aids, stabbing them into a cliff or even a stone wall to scale it."
    y "As simple as the design is, the kunai is suited to many different functions. In terms of weaponry, the loop at the end allows them to be tied to poles as makeshift spears; the handle can also be wrapped to provide a better grip."
    y "Originally used as a farming implement for digging, planting, and prying, kunai knives later became associated with ninja warriors and popular culture."
    y "Kunai knives are known for their simple and utilitarian design, featuring a sturdy blade and a looped handle for improved grip and control."
    y "In modern times, kunai knives are often used in martial arts training, cosplay, and as decorative or collectible items."
    call screen knife_wall()

label Paring:
    y "Just a paring knife, for preparing fruits and vegetables. It's actually one of the highest quality blades I own; I inherited rather than bought it. If you're curious, it originally belonged to..."
    y "..."
    y "...I can't remember who. I really, really dislike being confronted with reminders that virtually every memory I have, prior to that one week in the club, is false."
    y "...anyway."
    y "It is designed for tasks that require precision and control, such as peeling, trimming, and shaping fruits and vegetables."
    y "Paring knives come in various styles, including straight-edge, serrated, and bird's beak (curved) blades, each suited to different cutting techniques."
    y "They are essential tools for chefs and home cooks alike, facilitating delicate and intricate culinary preparations with ease."
    call screen knife_wall()

label Damascus:
    y "This one is very special: it's Damascus steel!"
    y "Damascus steel, from which Damascus knives are derived, has a rich history dating back centuries."
    y "The origins of Damascus steel production can be traced to the Middle East, particularly the regions of Syria and Iran, as early as the 3rd century AD."
    y "Historical Damascus steel was renowned for its exceptional strength, sharpness, and resilience, making it highly sought after for swords, knives, and other weapons."
    y "The unique patterning in Damascus steel is created through a process of layering and forging different types of steel alloys, resulting in a distinctive rippled or wavy appearance."
    y "Modern Damascus knives are crafted using pattern welding techniques that replicate the aesthetics of traditional Damascus steel."
    y "These knives are constructed from layers of high-carbon and low-carbon steel alloys, which are forge-welded and manipulated to create intricate patterns."
    y "The layering process not only enhances the visual appeal of the knife but also contributes to its strength, durability, and edge retention."
    y "Damascus knives are prized possessions among collectors, chefs, and knife enthusiasts for their craftsmanship, performance, and historical significance."
    y "The sharpness and durability of Damascus steel allow for precise and effortless cutting, making it a preferred choice among professional chefs and home cooks."
    y "Damascus knives are often used for preparing meats, vegetables, fruits, and other ingredients with precision and finesse."
    y "While prized for their beauty and craftsmanship, Damascus knives are also functional tools that excel in both performance and aesthetics."
    call screen knife_wall()

label Kukri:
    y "The kukri knife is a traditional Nepalese blade characterized by its distinctive inwardly curved edge."
    y "It serves as both a utility tool and a weapon, widely used by the Nepalese Gurkha soldiers and various ethnic groups in Nepal."
    y "The kukri features a heavy, forward-weighted blade designed for chopping, slicing, and hacking through tough materials."
    y "Its unique shape and weight distribution make it efficient for cutting wood, clearing brush, and even combat situations."
    y "The kukri often holds cultural and religious significance in Nepal and is commonly used in ceremonies and rituals."
    call screen knife_wall()

label Saw:
    y "The saw knife is a versatile cutting tool that combines the functionality of a knife with a serrated edge similar to that of a saw."
    y "It is commonly used in outdoor activities such as camping, hiking, and survival situations for cutting through wood, bone, and other tough materials."
    y "Saw knives may feature a fixed or folding blade design, with the serrated portion typically located near the handle for increased control and precision."
    y "The serrated edge allows for more aggressive cutting action compared to traditional knife edges, making saw knives ideal for tasks that require cutting through fibrous or hard materials."
    y "Folding saw knives are popular among outdoor enthusiasts for their portability and safety features, as the blade can be folded into the handle when not in use."
    y "In survival situations, saw knives can be crucial for gathering resources, constructing shelters, and improvising tools for hunting and fishing."
    call screen knife_wall()

label purple_a1:
    $ show_chr("A-AAAAA-AAAA")
    y "Hmm, okay [player]."
    $ show_chr("A-ABAAA-ALAA")
    y "Did one or more of my knives got your interest?"
    y "Or did you forgot the name of it?"
    $ show_chr("A-CBAAA-ALAA")
    y "Well, I don't think that matters."
    $ tc_class.transition("yuri_knives", speed="now")
    hide yuri_sit
    call screen knife_wall()

label purple_a2:
    $ show_chr("A-AAAAA-AAAA")
    y "I don't see why not."
    y "Surely you want to take a look at the rest of the room anyway."
    if persistent.bg == "yuri_kotatsu_1":
        menu:
            "To the front side of the Kotatsu.":
                y "Alright."
                $ tc_class.transition("yuri_kotatsu_2", speed=3.0)

            "To the desk.":
                y "Alright."
                $ tc_class.transition("yuri_desk", speed=3.0)
    elif persistent.bg == "yuri_kotatsu_2":
        menu:
            "To the back side of the Kotatsu.":
                y "Alright."
                $ tc_class.transition("yuri_kotatsu_1", speed=3.0)

            "To the desk.":
                y "Alright."
                $ tc_class.transition("yuri_desk", speed=3.0)

    elif persistent.bg == "yuri_desk":
        menu:
            "To the back side of the Kotatsu.":
                y "Alright."
                $ tc_class.transition("yuri_kotatsu_1", speed=3.0)

            "To the front side of the Kotatsu.":
                y "Alright."
                $ tc_class.transition("yuri_kotatsu_2", speed=3.0)
