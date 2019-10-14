# The script of the game goes in this file.

# Character definitions
define y =Character("You")
define d =Character("Demon", who_font="fonts/JFS.ttf", what_font="fonts/JFS.ttf")

# The game starts here.
label start:
    #choice variables for tracking what players have seen
    $ tinder = True
    $ texts = True
    $ email = True

    scene background1

    "You sit on your couch, legs propped up on your coffee table."
    "Through your window, the sky burns orange as the sun tucks itself behind the treeline."
    "You chew absentmindedly on your bottom lip as you reach for your phone."

    scene background2
    with dissolve

    "Your phone screen shines bright."


    label phone:
    scene background3
    with dissolve

    "You have no new notifications."
    menu:
        "Open Tinder" if tinder:
            $tinder = False
            jump tinder
        "Open Messages" if texts:
            $texts = False
            jump messages
        "Open Email" if email:
            $email = False
            jump email


    label tinder:
    "The application takes several, irritating seconds to open."


    label jackson:
    "Jackson \n{i}Compassionate and caring. Loves theater, music, and dancing. Bartender. ENFP if you care about that sort of thing.{/i}"
    menu:
        "Swipe left":
            jump ash
        "Swipe right":
            jump ash


    label ash:
    "Ash \n{i}Sometimes I garden, sometimes I protest ICE. Trying to meet someone else who has seen Space Ghost Coast to Coast.{/i}"
    menu:
        "Swipe left":
            jump newt
        "Swipe right":
            jump newt


    label newt:
    "Newt \n{i}just looking for the \"u\" to my \"wu\"{/i}"
    menu:
        "Swipe left":
            "You realize that fifteen minutes have passed and sigh."
            jump phone
        "Swipe right":
            "You realize that fifteen minutes have passed and sigh."
            jump phone


    label messages:
        "You have a text from your mother left on 'read.'"
        menu:
            "show message":
                "Hi sweetie, it’s your Mom. I saw your status on Facebook and I wanted to ask you… are you okay?"
                jump phone


    label email:
        "Are you having trouble in the bedroom?
        \n8 Timeless Skills to Learn Now
        \nMake the Most of Your Money."
        "Our Top 20 List of Tops. Number 5 will surprise you.
        \nTD Bank - Your online Bank Statement Is Available"
        "Fares from $79 one-way? Let’s shake on it.
        \nsteps to summon demons for fiery pleasure.
        \nCapital One - Your payment is due."
        "WAIT!..."
        "...pleasure..."
        "with demons?!"
        menu:
            "Open \"steps to summon demons for fiery pleasure\"":
                "After reading the instructions, you scrounge around your apartment and collect several materials."

                #searching montage
                scene background5
                with dissolve
                $renpy.pause(2.0)

                scene background6
                with dissolve
                $renpy.pause(2.0)

                scene background7
                with dissolve
                $renpy.pause(2.0)

                scene background8
                with dissolve
                $renpy.pause(2.0)

                jump ritual


    label ritual:
        scene background4
        with dissolve

        "You begin by sweeping the floor of your living room. You can't believe how much dust has accumulated since the last time you swept."
        "Depression sucks."
        "You sprinkle a large circle of salt around the room."

        scene background9
        with dissolve

        "It's not perfect, but you tried you gave it your best effort."
        "You turn your attention to the items you scavenged from around your home to use to call the corners."


    label easternGate:
        "What will you use to call the Eastern Gates, the Winds of Imagination?"
        menu:
            "A goose feather taken from your pillow":
                image feather = im.FactorScale("feather.png", .5)
                show feather
                with dissolve
                $renpy.pause(2.0)
                hide feather
                jump southernGate
            "A plastic recorder you won as an arcade prize":
                show recorder
                with dissolve
                $renpy.pause(2.0)
                hide recorder
                jump southernGate
            "A pinwheel you got at Pride":
                show pinwheel
                with dissolve
                $renpy.pause(2.0)
                hide pinwheel
                jump southernGate
            "A USB fan you unplugged from your laptop":
                show fan
                with dissolve
                $renpy.pause(2.0)
                hide fan
                jump southernGate
            #need item to appear


    label southernGate:
        "What will you use to call the Southern Gates, the Fires of Passion?"
        menu:
            "A candle from your bathroom":
                show candle
                with dissolve
                $renpy.pause(2.0)
                hide candle
                jump westernGate
            "A bottle of Sriracha... It's probably still fresh...":
                show sriracha
                with dissolve
                $renpy.pause(2.0)
                hide sriracha
                jump westernGate
            "Your most recent mixtape that you named “Fire on the Dance Floor”":
                image tape = "mixTape.png"
                show tape
                with dissolve
                $renpy.pause(2.0)
                hide tape
                jump westernGate
            "A comfort lighter you dug up from your kitchen drawer":
                image lighter = "comfortLighter.png"
                show lighter
                with dissolve
                $renpy.pause(2.0)
                hide lighter
                jump westernGate
            #need item to appear


    label westernGate:
        "What will you use to call the Western Gates, the Waters of Intuition?"
        menu:
            "A snorkle":
                show snorkle
                with dissolve
                $renpy.pause(2.0)
                hide snorkle
                jump northernGate
            "A nautalus shell from your visit to the cape":
                show conch
                with dissolve
                $renpy.pause(2.0)
                hide conch
                jump northernGate
            "A bowl of water with “Sparky” written on the side":
                image bowl = "dogBowl.png"
                show bowl
                with dissolve
                $renpy.pause(2.0)
                hide bowl
                jump northernGate
            "Your neti pot":
                image neti = "netiPot.png"
                show neti
                with dissolve
                $renpy.pause(2.0)
                hide neti
                jump northernGate
            #need item to appear


    label northernGate:
        "What will you use to call the Northern gates, the Grounds of Work?"
        menu:
            "A ring your good friend, Sonya gave to you, she says it’s real onyx":
                show ring
                with dissolve
                $renpy.pause(2.0)
                hide ring
                jump summon
            "A succulent plant potted in soil":
                show succulent
                with dissolve
                $renpy.pause(2.0)
                hide succulent
                jump summon
            "Coffee grounds from your morning brew":
                show coffee
                with dissolve
                $renpy.pause(2.0)
                hide coffee
                jump summon
            "A rock, what? You thought it looked cool.":
                show rock
                with dissolve
                $renpy.pause(2.0)
                hide rock
                jump summon
            #need item to appear

    #IMPORTANT NOTE: With the font and size, for PC, only print up to three lines at a time. For the demon only print 4. Otherwise it gets cut off.
    label summon:
        "Having finished the setup, you step into the circle, bow, and begin your incantation."
        stop music fadeout 2.0
        y "... Heed my call and arise from the depths of the fiery pit."
        "You finish...."
        play music "sounds/demonmusic.ogg"

        scene background10
        with dissolve

        "The smell of sulfur suffocates you, and you see thick, black smoke filling your circle."
        #demon appears
        #image smoke = im.FactorScale("demoncloud.png")
        show demoncloud
        with dissolve
        "A shadowy figure ascends, shrouded in the black clouds."

        d "Greedy mortal, thou has disrupted \nmy time in the infernal depths. \nTell me, what is it thine purpose, \nto summon me into thine realm?..."
        d "A djinn am not I. \nFor wishes I do not grant."
        d "So speaketh thine intent, \nAnd I shall perhaps consent."

        menu:
            "So... Uh... There's this email that I got.":
                jump prose1
            "Do you… Come here often?":
                jump prose1
            "Have sex with me.":
                jump prose1


    label prose1:
        y "Unfurl your spine \nEyes, curtains closed \nTendons stretched"
        y "Across the sheets \nCome to tuck me in"
        "Your brows furrow. This wasn’t exactly how you wanted to communicate your message..."
        d "To thee, I am but a thing, \nA conduit for your pleasure, \nRest assured, I see you asking \nYet I’ll take measures."
        menu:
            "I'm ready.":
                jump prose2
            "I want you.":
                jump prose2
            "Fuck me!":
                jump prose2


    label prose2:
        y "Pleading, clenched fist \nTeased hair"
        y "Turned away \nIrises to Earth"
        d "You demand such a task \nto be turned nose to ground \nYet you understand not who you ask \nTo turn you around."
        menu:
            "It will be great.":
                jump prose3
            "I want you tonight.":
                jump prose3
            "You will enjoy it.":
                jump prose3


    label prose3:
        y "Taste honey \nSugar-coated lip \nAnd toffee tongue"
        y "Slinking closer \nDown flights of stairs"
        d "Thou art being pig-like in thine request. \nYour soul in this circle the cost \nYet my patience you test. \nAnd I would rather count my loss."
        menu:
            "C'mon, it's just sex.":
                jump prose4
            "But I really want to.":
                jump prose4
            "I'll show you a good time.":
                jump prose4


    label prose4:
        y "Fingertips on cloth \nCloth on skin \nGranite cheekbones and"
        y "Baking soda breath \nBreathe on me"
        d "A circle drawn, \nAnd harkened my ascent, \nAnd yet forgone, \nAsking my consent."
        menu:
            "I... Summoned you to have sex with me.":
                jump gross
            "Oh my god, you're right. I'm sorry.":
                jump apology


    label gross:
        y "The summoner is law \nLegislation serves me"
        y "Obey these desires \nBefore freedom"
        d "Though I come from the under realm \nMy body is my own \nThine words I quell, \nThine ignorance hath shown."
        y "..."
        stop music fadeout 2.0
        d "Okay, I've kept up this prose bullshit for this long, and you still don't get the message. I don't want to have sex with you. Fuck off. Keep your soul, we don't need gross assholes like you in hell."
        play music "sounds/grossmusic.ogg" fadein 1.0
        "The demon recedes into the circle, quickly followed by the smoke."
        hide demoncloud
        with dissolve
        "You stand motionless as the smoke dissipates into the air."
        "You chide your fingers, and take a deep gulp."
        #new salt pile bg?
        "You pick up your broom and begin to sweep the salt into several manageable piles as you process the exchange."

        scene background11
        with dissolve

        "You reach for your phone. The battery is dead."

        scene backgroundblack
        with dissolve

        "You are alone in a dark room."
        return


    label apology:
        y "Soft words spoken \nWith velvet intentions"
        y "Fast lips \nDo not lovers make"
        d "Thou disturbs my sensibilities. \nContinue thine apology, mortal maggot."
        y "Apologies are brittle \nLike bones"
        y "But mine are steel \nMy promises gold-plated"
        d "Words are cheap, actions louder. \nShow thine sincerity."
        y "Boiled water and tea bags \nConservations clothed \nIn curiosity."
        stop music fadeout 2.0
        y "Start again \nWith me."
        play music "sounds/apologymusic.ogg"
        d "I do enjoy a nice cup of Chamomile. "
        "The small crystals tickle your foot as you create an opening in your salt circle."

        scene background12
        with dissolve

        "You pull out a chair from the kitchen table and invite the demon to sit if he wishes."
        return
