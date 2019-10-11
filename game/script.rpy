# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y =Character("You")
define d = Character("Demon")





# The game starts here.

label start:
    #choice variables for tracking
    $ tinder = True
    $ texts = True
    $ email = True

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

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
        "Are you having trouble in the bedroom? \n8 Timeless Skills to Learn Now \nMake the Most of Your Money."
        "Our Top 20 List of Tops. Number 5 will surprise you. \nsteps to summon demons for fiery pleasure. \nFares from $79 one-way? Let’s shake on it."
        "TD Bank - Your online Bank Statement Is Available. \nCapital One - Your payment is due."
        "WAIT!..."
        "...pleasure..."
        "with demons?!"
        menu:
            "Open \"steps to summon demons for fiery pleasure\"":
                "After reading the instructions, you scrounge around your apartment and collect several materials."
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
                jump southernGate
            "A plastic recorder you won as an arcade prize":
                jump southernGate
            "A pinwheel you got at Pride":
                jump southernGate
            "A punctured milar balloon that reads “It’s a Boy”":
                jump southernGate
    label southernGate:
        "What will you use to call the Southern Gates, the Fires of Passion?"
        menu:
            "A candle from your bathroom":
                jump westernGate
            "A bottle of Sriracha... It's probably still fresh...":
                jump westernGate
            "Your most recent mixtape that you named “Fire on the Dance Floor”":
                jump westernGate
            "A comfort lighter you dug up from your kitchen drawer":
                jump westernGate
    label westernGate:
        "What will you use to call the Western Gates, the Waters of Intuition?"
        menu:
            "A snorkle":
                jump northernGate
            "A nautalus shell from your visit to the cape":
                jump northernGate
            "A bowl of water with “Sparky” written on the side":
                jump northernGate
            "Your neti pot":
                jump northernGate
    label northernGate:
        "What will you use to call the Northern gates, the Grounds of Work?"
        menu:
            "A ring your good friend, Sonya gave to you, she says it’s real onyx":
                jump summon
            "A succulent plant potted in soil":
                jump summon
            "Coffee grounds from your morning brew":
                jump summon
            "A rock, what? You thought it looked cool.":
                jump summon
    label summon:
    "Having finished the setup, you step into the circle, bow, and begin your incantation."
    "... Heed my call and arise from the depths of the fiery pit,” You finish...."
    "The smell of sulfur suffocates you, and you see thick, black smoke filling your circle."
    "A shadowy figure ascends, shrowded in the black clouds."

    d "Greedy mortal, thou has disrupted
    my time in the infernal depths.
    Tell me, what is it thine purpose,
    to summon me into thine realm?..."
    "A djinn am not I.
    For wishes I do not grant."
    "So speaketh thine intent,
    And I shall perhaps consent."







    return
