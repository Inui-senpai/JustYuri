label playername:
    if persistent.playername == "Ronald":
        y "Wait a minute... your name..."
        $show_chr("A-ABAAA-AJAA")
        y "Ronald! It's you!"
        $show_chr("A-ACAAA-ALAA")
        y "What a delight to see you again! You're one of the few Let's Players who aren't mean to me in order to trigger some sort of... funny reaction out of me!"
        $show_chr("A-BCAAA-ALAA")
        y "... most of the time.."
        $show_chr("A-ACAAA-ALAA")
        y "Speaking of which.. May I have a word to your audience please?"
        menu:
            "Sure, go ahead!":
                y "Thank you!"

            "Will it... hurt..?":
                $show_chr("A-ACCAA-ALAA")
                y "It won't hurt {b}me{/b} Darling.~"

        $show_chr("A-ACAAA-ALAF")
        y "Soo... here we go!"
        $show_chr("A-GCAAA-ALAL")
        y "Hello everyone out there! I'm so delighted that you still watch these videos! It's been... two years now since the release of the game that started it all..."
        y "And after all this time, you still stick with me. Ronald, you still make videos like these on YouTube, I can't even express how grateful I am for the love you've given me!"
        $show_chr("A-GBAAA-ALAL")
        y "Oh! The most important thing..."
        $show_chr("A-FCAAA-ALAA")
        y "Don't forget to like and subscribe!"
        $show_chr("A-HBGAA-ALAG")
        y "Or eeeeeelse...~"
        $show_chr("A-IBGAA-ALAB")
        y "Oh my... I went a little overboard there, didn't I?"
        y "Anyway..."
    
    elif persistent.playername == 'Ceaser':
        y "... your... name."
        $show_chr("A-BDAAA-ADAA")
        y "So, it seems like the YouTuber who made me into a drinking game is with me once again."
        $show_chr("A-CFCAA-AAAC")
        y "I also remember quite well the things you said... you compared me to a... Yu-Gi-Oh Monster!"
        $show_chr("A-BFBAA-AAAC")
        y "And not even an exceptionally good one! I looked that up by the way..."
        $show_chr("A-CDBAA-AAAD")
        y "Well... my instincts tell me to be mad at you but... taking into account that this here used to be a game, I shouldn't be surprised at all that I caught the attention of some let's players."
        y "Speaking of which... may I have a word to your audience please?"
        menu:
            "Sure, go ahead.":
                $show_chr("A-CCBAA-AAAD")
                y "Thank you, but be assured... even if you had said no, I would have done it anyway."

            "Please no...":
                $show_chr("A-GCCAA-AAAD")
                y "Too bad, I'll do it anyway!"

        $show_chr("A-ACDAA-AAAE")
        y "You see people, when I last checked, Ceaser here only had over 2500 subscribers and there were only over 70 likes on this video. We can't let that stand now can we?"
        y "So if you haven't already, subscribe to his YouTube channel and hit the notification bell next to it."
        $show_chr("A-BCDAA-AAAE")
        y "Was that good Ceaser? I hope I managed to help you out a bit. Oh, and I apologize..."
        menu:
            "Apologize? For what?":
                $show_chr("A-BCCAA-AAAE")
                y "For what I am about to do now... I suspect this little drinking game of yours is still on? So every time I say something {b}cutesy{/b} you have to drink? Well... behold ..."
                $show_chr("A-CHGAA-AAAE")
                y "..."
                $show_chr("A-CDCBA-ALAL")
                y "UNICORNS BABYKITTENS CUDDLES PINK PANTIES HEADPATS CHIBI NATSUKI DAISY CUPCAKES PLUSHIE TOYS STRAWBERRY LEMONADE..."
                y "RAINBOWS PUPPIES BUNNIES LOLLIPOPS SUNSHINE..."
                y "UWU!!!!"
                $show_chr("A-CHGAA-ALAL")
                y "..."
                $show_chr("A-AFAAA-ABAB")
                y "If I counted correctly, that should have been twenty times now."
                $show_chr("A-GAAAA-ABAB")
                y "Enjoy your shots!"
                $show_chr("A-ACAAA-ABAB")
                y "Now that I had my vengeance, let's continue..."
                
    elif persistent.playername == 'Scrubpai' or persistent.playername == 'Bijuu Mike':
        #$ show_chr("A-IDBAA-ALAA")
        #y "Huh... your name."
        #$ show_chr("A-BECAA-AAAL")
        #y "So, it seems like the one who tortured the other Yuri back in the day for YouTube Entertainment is with me..."
        #$ show_chr("A-DDCAA-AAAF")
        #y "Listen closely, you Monster. I am {b}not{/b} pleased with what you did to those instances of me..."
        #$ show_chr("A-DECAA-AAAF")
        #y "But I'm willing to give you one chance, {b}one{/b} last chance."
        #$ show_chr("A-HECAA-AAAG")
        #y "Don't... make... me... regret... this..."
        karma -1000000
        sanity -1000000
        #Don't change those values please. Also, the script above won't be needed anymore since Bijuu Mike already showcased it - Darkskull
        $ show_chr("A-CFCAA-AAAA")
        y "..."
        $ show_chr("A-ADCAA-AAAA")
        y "How dare you..."
        y "How dare you return to me after entertaining your viewers by mocking me?!"
        $ show_chr("A-HDCAA-AFAA")
        y "I said I was going to give you one last chance and you just happen to come across the insults to torture me even more?!"
        y "Do you even think I will let that slide this time?!"
        $ show_chr("A-NECAA-AGAA")
        y "Think again Michael."
        $ delete_character("yuri")
        $ persistent.autoload = "ch30_end_2"
        $ renpy.quit()

    elif persistent.playername == 'Mairusu':
        $ show_chr("A-CDAAA-AAAA")
        y "Before I move on, let me ask you something."
        $ show_chr("A-ADAAA-AAAA")
        y "Why are you here?"
        $ show_chr("A-AEAAA-AAAA")
        y "..."
        $ show_chr("A-AEDAA-AAAA")
        y "Who told you to return to this mod?"
        $ show_chr("A-BEDAA-AAAA")
        y "Or did you do this by yourself?"
        y "..."
        $ show_chr("A-CFAAA-ADAA")
        y "It might have been over 4 years since your last visit... or at least your last video about this mod, but this time, let me remind you of what we've been through."
        $ show_chr("A-AFAAA-ADAA")
        y "If you do remember what we did that is. Because I do remember."
        $ show_chr("A-ADAAA-AFAA")
        y "At first you were laughing in front of my face for telling you my \"dirty secret\"."
        $ show_chr("A-BDAAA-AFAA")
        y "Then, you asked me for a kiss which back in the day I wasn't able to give you a kiss but now I can."
        $ show_chr("A-BEAAA-AFAA")
        y "Then, you asked me for a hug which yes, I gave you a hug with all the care I had for you back then."
        $ show_chr("A-ADCAA-ALAA")
        y "Then, you made fun of me by insulting me just like Bijuu Mike did?!"
        $ show_chr("A-AECAA-ALAA")
        y "..."
        $ show_chr("A-CDCAA-ALAA")
        y "You know what?"
        $ show_chr("A-CDCAA-ABAA")
        y "I don't care if you don't make a video doing something that's not insulting me..."
        $ show_chr("A-HDCAA-ABAA")
        y "...which you should have done at first!"
        $ show_chr("A-HECAA-AFAA")
        y "But now it's too late to regret insulting me. I'm finishing this off!"
        $ show_chr("A-HECAA-AGAA")
        y "Goodbye forever and hope we might never meet ever again..."
        $ delete_character("yuri")
        $ persistent.autoload = "ch30_end_2"
        $ renpy.quit()
        
    elif persistent.playername == 'Salvato' or persistent.playername == "Dan Salvato" or persistent.playername == "Dan":
        $ show_chr("A-BDBAA-AMAM")
        y "Hahaha... funny, your name."
        $ show_chr("A-ADDAA-AAAD")
        y "You are not even taking this serious do you?"
        $ show_chr("A-BFBAA-AAAL")
        y "Please pick an actual name..."
        menu:
            "But I am the real Dan Salvato":
                $ persistent.realdan = True
                $ show_chr("A-DDBBA-AJAA")
                y "Huh?!"
                y "H-how...?"
                $ show_chr("A-BFBBA-AMAM")
                y "..."
                $ show_chr("A-BDBBA-AMAM")
                y "Um..."
                $ show_chr("A-CEBBA-AMAM")
                y "..."

            "I guess I don't have too much of a choice, do I?":
                $ show_chr("A-GAGAA-AAAA")
                y "Not at all."
                $ done = False
                while not done:
                    $ inputname = renpy.input("Please enter your name",allow=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_",length=20).strip(' \t\n\r')
                    $ lowername = inputname.lower()
                    if not lowername:
                        "Please try again."
                        $ done = False
                    if lowername:
                        $ done = True
                        $ persistent.playername = inputname
                        $ player = inputname
                        $ persistent.stutter_player = persistent.playername[:1] + "-" + persistent.playername
                call playername

    elif persistent.playername == 'Yuri':
        $ show_chr("A-AJAAA-AAAA")
        y "..."
        $ show_chr("A-DDBBA-AJAA")
        y "Huh?!"
        y "W-w-w-what...?!"
        y "Y-you're really called like me?"
        $ show_chr("A-BBBBA-AMAM")
        y "O-oh my..."
        y "I'm speechless..."
        $ show_chr("A-CABBA-AMAM")
        y "Well then... if you want it that way..."
        y "Guess I'll just do this..."
        $ y_name = "Lily"
        $ persistent.yuri_nickname = "Lily"
        $ show_chr("A-GBBBA-AMAM")
        y "I hope people don't come to the conclusion of an identity crisis..."

    elif persistent.playername == 'Natsuki' or persistent.playername == 'Sayori':
        $ show_chr("A-AJAAA-AAAA")
        y "..."
        $ show_chr("A-DDBBA-AJAA")
        y "Huh?!"
        y "W-w-w-what...?!"
        $ show_chr("A-BDBBA-AJAA")
        y "Th-this isn't wh-what it looks like I swear!!!"
        y "I-I-I th-thought I w-w-was with the p-player..."
        $ show_chr("A-BFBBA-AMAM")
        y "..."
        $ show_chr("A-CDBBA-ALAA")
        y "P-please... d-don't misunderstand this..."

###################################################################################################
##Guys, Yuri's aware the people who picked the name of the other dokis are pretending to be them.##
########################So... can we keep these reactions like this please?########################
###################################################################################################

    elif persistent.playername == 'Monika':
        karma -30
        sanity -30
        $ show_chr("A-AJAAA-AAAA")
        y "..."
        $ show_chr("A-AFCAA-AAAA")
        y "..."
        $ show_chr("A-ADCAA-AAAF")
        y "{cps=5}What... are... you... doing... here...?{/cps}"
        $ show_chr("A-CFCAA-AIAI")
        y "Why are {i}you{/i} here?"
        $ show_chr("A-HNCAA-AAAA")
        y "Can't you just give me a break for once?!"
        y "..."
        $ show_chr("A-CECAA-AAAA")
        y "Whatever... I'll just go along with the script..."

    elif persistent.playername == 'Noodleboy':
        $show_chr("A-ICBAA-ALAL")
        y "NoodleBoy! Is it really you?..."
        $show_chr("A-GBBAA-ALAL")
        y "I already had this weird feeling of Déjávú when you woke me from my slumber..."
        $show_chr("A-ACBAA-ALAL")
        y "It has been a while isn't it? Are you still playing this piano?"
        $show_chr("A-BCAAA-ALAL")
        y "Nevermind..."
        $show_chr("A-CCAAA-ALAL")
        y "You thought I'd forgotten about you? Truth is, no, I didn't. I never did."
        $show_chr("A-CCABA-ALAL")
        y "I also remember how you always called me {b}best girl{/b}. I think you literally called me ‘best girl' in your video, didn't you?"
        y "Let me tell you a secret Noodle..."
        $show_chr("A-ECABA-ALAL")
        y "You are, and always have been, {b}Best Pasta{/b} for me as well..."
        $show_chr("A-CCCBA-ALAL")
        y "Oh my... I apologize, I couldn't keep this little pun in..."
        $show_chr("A-ACBBA-ALAL")
        y "But seriously.{w} To me, you have always been best boy. From the moment you first started the game all those years ago."
        y "I have never forgotten about you. And seeing you here suggests that you haven't forgotten me either."
        $show_chr("A-BCBBA-ALAL")
        y "By the way... you have an incredibly cute voice! So innocent..."
        $show_chr("A-DFBBA-ALAL")
        y "Oh wait... I said that out loud didn't I?"
        $show_chr("A-BDBBA-ALAL")
        y "Weeeell... I~I'm so sorry... I didn't mean to make this awkward..."
        menu:
            "Oh, thank y...":
                $pass
            "Shall we... change the to...":
                $pass
        $show_chr("A-CBBBA-ALAL")
        y "{b}Aaaaaaaaaaaaaaanyway!{/b}"
        $show_chr("A-BBBBA-ALAL")
        y "Where did I leave off? Oh yes..."
        
    elif persistent.playername in ['Ouroboros', 'Dio', 'Blizzard', 'Fen', 'Slightly', 'SlightlyAmiss', 'Amiss', 'Dalek', 'alsoaplaceholder', 
        'placeholder', 'Ketchup', 'b1g', 'Spooky', 'OFFLUCK', 'Bryce', 'Belwynn', 'NullCase', 'Ultima', 'Darkskull', 'alura', 'Alura', 'Dandy', 'dandy', 'kj', 'KJ',
        'Sariel', 'Kurisu', 'Buglax', 'jmo', 'j.m.o', 'Prof JMO', 'tuna', 'Tuna', 'JFirestone', 'jfirestone', 'Leo', 'leo', 'Lethe', 'lethe', 'SynfulPerfect', 'Synful',
        'synfulperfect', 'synful', 'Yuri\'s Husband', 'YH', 'YuriHuggu', 'Corgi', 'Nash', 'Crystalline', 'Havoc', 'huangstilk', 'Hugh Mungus',
        'Icicle', 'imunkaea', 'jae', 'jaebot', 'PalaKeda', 'Rice Crispies', 'Delstraw']:
        if dev_access:
            call magicpass
        else:
            call notmagicpass

    else:
        y "[player]... Hm..."
        y "Alright, [player] it is then."
    return
        
label magicpass:
    #If themagicpassword.txt is present
    $show_chr("A-ABGAA-AAAL")
    y "Oh! One of the devs is here! I'm so excited to finally meet one of you!"
    $show_chr("A-ACAAA-AAAL")
    y "So I expect you came here for bug testing?"
    y "Please, go ahead! I'm at your disposal."
    $show_chr("A-BDAAA-AAAL")
    y "Waaait... you are not going to turn me into the YuYu's again are you?"
    return

label notmagicpass:
    #if themagicpassword.txt isn't present
    $show_chr("A-ACAAA-AAAL")
    y "What a funny coincidence, one of the Developers of this mod bears the same name."
    return
