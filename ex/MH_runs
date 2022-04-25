#!/usr/bin/env python3
'''This module is a text-based RPG. Made by Shawn O'Keefe'''

# ======================================== IMPORTS
import os             #ENABLES FUNCTIONS: os.system("clear")
import sys            #ENABLES FUNCTIONS: system.exit()

# ======================================== DICTIONARIES / LISTS
rooms = {
  'porch'        :{
                    'desc'       : 'MONTY HALL PORCH:\n  Your driver pulls up to the curb and you get out. Drizzling rain hastens you up the steps to Monty Hall.\n  Renovated in the last three months, the old estate is awash with lights and pouring with music.\n  Costumed up for the bootleg era, you are eager to join your co-workers in the interactive mystery murder theater.',
                    'go'         : ['move', 'reception', 'GO to the reception'],
                    'return'     : ['move', 'curb', 'RETURN to the curb'],
                    'check'      : ['act', 'CHECK your invitation', 'Hmmm. Surely it was here? Did I leave it on the seat?'],
                  },
  'curb'         :{
                    'desc'       : 'CURBSIDE:\n  Your ride already left. Nothing at the curb except deep puddles, lamps, and trees swaying in the wind.',
                    'return'     : ['move', 'lobby', 'RETURN to Monty Hall'],
                    'call'       : ['act', 'CALL an uber and go home', 'Then again, maybe not. You came here to enjoy yourself. Might as well do it.', 'keep', 'requirement','cell phone'],
                    'jump'       : ['act', 'JUMP in the puddles', 'Splash, splash, splash!'],
                    'wet paper'  : ['item', 'wet paper', 'Dripping, but readable:\n\n Hi. Join me for Monty Hall\'s opening night for its dinner/mystery theater on 4 May. I bet you already heard about\n  the place, but do not forget to dress the part. We will be swinging the old-timesy fashion at 7pm.\n \n Your seat is paid, so if you are late ...\n I will kill you. LOL!\n \n  - Suse'],
                  },
  'reception'    :{
                    'desc'       : 'RECEPTION:\n  You take off your fedora and clack into the polished halls of an impressive foyer overlooked by a deep gallery\n  and steeped in jazz.  The lone receptionist perks up from behind a reception counter and gestures to you.\n "All parties are meeting in the lounge on your left. Lockout starts soon."',
                    'turn'       : ['move', 'lounge', 'TURN left into the lounge'],
                    'wander'     : ['move', 'gallery', 'WANDER right into the gallery'],
                    'suse'       : ['act', '"I am with SUSE. She arrive?"','"So, you\'re her partner. It\'s a fun role. Join her in the lounge before you get replaced. " the receptionist answered.'],
                    'return'     : ['act', 'RETURN to the curb', 'Alas! You can see your ride already disappearing down the driveway.'],
                    'call'       : ['act', 'CALL your friends', 'Better luck shouting ... or just go into the lounge.', 'keep', 'requirement','cell phone'],
                    'check'      : ['act', 'CHECK your invitation', 'Hmm, where is it? Oh well, better just get moving.'],                 
                  },
  'gallery'      :{
                    'desc'       : 'GALLERY:\n  Taking your own time, you opt to explore the gallery. The walls are littered with insets of period art,\n  memorabilia, and summaries of historical significance. As you scroll the displays, the lights fall, all goes silent.',
                    'fumble'     : ['move', 'lobby', 'Carefully FUMBLE your your way back to the lobby'],
                    'wait'       : ['act', 'WAIT a moment', 'No time restores the lights.'],
                    'call'       : ['act', 'CALL out to the staff', 'No response. Perhaps the staff are in the lounge or backrooms.'],

                  },
  'lounge'       :{
                    'desc'       : 'LOUNGE:\n  You entered the lounge, perhaps just barely soon enough. Guests were already filtering out and into the ballroom beyond.\n  Bright lights, art deco, and a glass gallery for a bar. Nothing stood out so much as the period ash tray with the sign,\n  "No Smoking."  Anachronisms aside, you spot Suse instantly, centered on the bar balancing a cocktail in her hand, a\n  giant plumed red hat on her head, and serpent around the shoulders.\n\n  She spots you and calls out, "Glad you could make it, and we got matching hats. How sweet of you." She rang a little\n  bell on the counter and beckoned you over. Mirri handed off her snake to the staff.\n\n  "Don\'t mind Mr. Rossum, I don\'t even know why I brought him tonight. You however have a purpose. Follow me."',
                    'follow'     : ['move', 'balcony', 'FOLLOW Suse', 'remove'], #NEED TO REMOVE IF YOU CHOOSE TO STAY
                    'exit'       : ['move', 'lobby', 'EXIT to the lobby'],
                    'refuse'     : ['act', 'REFUSE and stay behind','"How disappointing," you say, "I came to do some sleuthing, and I will do just that."\n \n  "You\'ll regret this, but must bid you farewell to do my part. Enjoy the snakes, ... I mean snacks," Suse snapped.\n \n  Suse exitted out a side door. Nothing but you and a room full of alcohol.'],
                    'friend'     : ['act', '"So, your FRIEND there."', '"Darling, ... it\'s called acting the part.," Suse teased, "Rossum is tame, even so python\'s are not venomous."', 'remove'],
                    'late'       : ['act', '"Sorry I am LATE,"', 'Not late. You were supposed to show up later than the rest of us." Suse replied.', 'remove'],
                    'purpose'    : ['act', '"PURPOSE?"', 'Suse grinned. "Because you get to be the mysterious Monty Hall!, and I am your lovely partner in crime.\n Were are going to reenact history tonight."', 'remove'],
                    'enter'      : ['act', 'ENTER the ballroom', 'Locked.  What might be going on in there?', 'remove'],
                    'next'       : ['act', '"What happens NEXT."', '"Ask later, come on." Suse beckoned.', 'remove'],
                    'cocktail'   : ['item', 'cocktail', 'At least you had time to snag a drink. After all, none of this would be here without alcohol.'],
                    'snacks'     : ['item', 'snacks', 'A doggy bag is okay, right?']
                  },
  'balcony'      :{
                    'desc'       : 'BALLROOM BALCONY:\n  The pathway leads upstairs ending at a wide balcony far above the ballroom. You can hear a\n  cacophony of murmering and laughter down below.\n\n  "This is where the action happens," explains Suse, "This isn\'t just a mystery theater, it is an escape room."\n  The staff will play out recordings\n  to manipulate our partiers while we choose how the house deals out its cards\n  from behind the scenes. Watch and I will guide you through it.',
                    'observe'    : ['act', 'OBSERVE the scene below', 'That\'s all folks. Tune in again for Part 2'],
                    'close'      : ['act', 'CLOSE your eyes', 'You can\'t help but peek'],
                  },                 
  'lobby'        :{
                    'desc'       : 'LOBBY:\n  What happened to the lights and music? The entrance is lit only a by sputtering candle. The darkness closes in.',
                    'delve'      : ['move', 'darkness','DELVE into the darkness'],
                    'go'         : ['move', 'outside', 'GO outside'],
                    'close'      : ['act', 'CLOSE the door', 'A gust from the entrance blows out the candle. You are plunged into total darkness'],
                    'lit candle' : ['item', 'lit candle', 'Mmmm! Mint and cinnamon.'],
                    #'burn'       : ['use', 'invitation', 'BURN your invitation', 'The paper curls, chars, and crumbles to dust.'],
                  },
  'outside'      :{
                    'desc'       : 'OUTSIDE:\n The rain isn\'t letting up and your suit isn\'t getting any drier. Nothing to see but the long private drive shimmering\n with the reflection of a row of lamps.',
                    'return'     : ['move', 'darkness', 'RETURN to Monty Hall'],
                    'call'       : ['act', 'CALL an uber', 'No reception. Monty Hall is just too far from civilization. Guess that helped the establishment and patrons avoid the law in the 1920s.', 'keep', 'requirement','cell phone'],
                    'walk'       : ['act', 'WALK home', 'Then again, maybe not. It was a 30-minute drive.'],
                  },                
  'darkness'     :{
                    'desc'       : 'DARKNESS:\n  So dark ... All is the void.',
                    'delve'      : ['move', 'backrooms', 'DELVE deeper. Maybe you will find a door.'],
                    'wait'       : ['act', 'WAIT and listen', 'Did you hear that? Did it hear you?'],
                  },
  'backrooms'    :{
                    'desc'       : 'BACKROOMS:\n  Fumbling into the backrooms and up a flight of stairs, you bump into something in the darkness. Something feathery,\n  overdressed, and with a bony elbow. "Ouch. Who bumped me?" It whispered.\n \n  Recognizing the voice you question, "Suse?"\n \n  "Glad you decided to show, but you and I need to hurry to the balcony. I will fill you in as we go along."',
                    'follow'     : ['move', 'balcony', 'FOLLOW Suse'],
                    'turn'       : ['act', 'TURN around', 'Suse pulls your arm, "Nope. You are going this way."'],
                  },
                  }
inventory =       {  
                    'cell phone' : ['item', 'cell phone', 'Powered, but only one bar here. Maybe I should climb a tree.'],
                    'lint'       : ['item', 'lint', 'Fluff. Always to be found when you need it.'],
                    'wallet'     : ['item', 'wallet', '- Cards ... check.\n- Cash ... check.\n- Breath mints ... darn.'],
                  } 
remove_acts =     {
                    'invite'      : 'invite',
                  }
destroy_items =   {
                    'wet paper'   : 'wet paper',
                    'candle'      : 'candle',
                  }

# ======================================== INITIAL STATE
current_room = 'porch'
game_over = 0
grue = 0

# ======================================== STATUS SCREEN
def status():
    '''This function refreshes the screen and prints the current status of the RPG scenario.'''
    os.system("clear")
    print('''
=======================================================================================================================
                                     ╔╦╗╔═╗╔╗╔╔╦╗╦ ╦  ╦ ╦╔═╗╦  ╦    ╔╦╗╦ ╦╦═╗╔╦╗╔═╗╦═╗
                                     ║║║║ ║║║║ ║ ╚╦╝  ╠═╣╠═╣║  ║    ║║║║ ║╠╦╝ ║║║╣ ╠╦╝
                                     ╩ ╩╚═╝╝╚╝ ╩  ╩   ╩ ╩╩ ╩╩═╝╩═╝  ╩ ╩╚═╝╩╚══╩╝╚═╝╩╚═
=======================================================================================================================''')
    print()
    print(f"{rooms[current_room]['desc']} \n")
    print('=======================================================================================================================')

    print(f"INVENTORY:  ", end="")
    for inv_elements in inventory.keys():
        print(f"{inv_elements.upper()}, ", end="")

    print("\nACTIONS:")
    for act_elements in rooms[current_room]:
        if rooms[current_room][act_elements][0] == "act":
            print(f" - {rooms[current_room][act_elements][1]}")
        if rooms[current_room][act_elements][0] == "move":
            print(f" - {rooms[current_room][act_elements][2]}")

    print(f"ITEMS IN ROOM:  ", end="")
    for elements in rooms[current_room]:
        if rooms[current_room][elements][0] == 'item':
            print(f"{rooms[current_room][elements][1].upper()},  ", end="")
    print()

    print('======================================================================================================================')
    print('======================================   Type a KEYWORD to make your actions.   ======================================', '\n')

# ========== GAME LOOP ===============
#def main():
#    '''This function process the player's commands and calls for status screen updates.'''
while True:
    status()

    if game_over == 1:                                                                                      # EXIT AFTER GAME OVER
        if grue >= 3:
            print("You were eaten by a grue! - GAME OVER")
        input("Press ENTER to exit.")
        sys.exit()

    while game_over == 0:
        choice = input('> ',)
        choice = choice.lower()

        if choice == 'teleport':                                                                            # TELEPORT
            print("AVAILABLE ROOMS:")
            for room_names in rooms.keys():
                print(f"{room_names}  ", end="")
            q_teleport = input("\n\n, Teleport to which room? \n> ")
            if q_teleport in rooms.keys():
                current_room = q_teleport
                break
            else: continue         

        elif choice in rooms[current_room] and rooms[current_room][choice][0] == "item":                    # ADD TO INVENTORY, REMOVE FROM ROOM
            inventory[choice] = ['item', rooms[current_room][choice][1], rooms[current_room][choice][2]]
            del rooms[current_room][choice]
            input(f"Added {choice.upper()} to inventory. Press enter to continue. \n")
            break

        elif choice in inventory:                                                                           # CHECK ITEM DESCRIPTION, DROP INTO ROOM
            print(f"{inventory[choice][2]}  \n")
            q_drop = input(f"Drop {choice.upper()}? (Y/N) \n> ")
            if q_drop == "Y" or q_drop == "y":
                rooms[current_room][choice] = inventory[choice]          
                inventory.pop(choice)
                input(f"Dropped {choice.upper()}. Press enter to continue. \n")
                break
            else: continue

        elif choice in rooms[current_room] and rooms[current_room][choice][0] == "move":                    # CHANGE ROOMS
            current_room = rooms[current_room][choice][1]
            break

        elif choice in rooms[current_room] and rooms[current_room][choice][0] == "act":                     # PERFORM ACTIONS

            if current_room == "darkness" or "gallery" and choice == "wait" and "lit candle" not in current_room:    # EATEN BY GRUE
                grue += 1
                if grue >= 3:
                    game_over = 1
                    break
            try:
                if rooms[current_room][choice][4] == "requirement" and rooms[current_room][choice][5] not in inventory:
                    print(f"Cannot do that without {rooms[current_room][choice][5].upper()}.")
                    continue
                elif rooms[current_room][choice][3] == "remove":
                    print(f"{rooms[current_room][choice][2]} \n")
                    rooms[current_room].pop(choice)
                    input("Press enter to continue.\n")
                    break
            except:
                print(f"{rooms[current_room][choice][2]} \n")
                continue
            finally:
                if choice == "close" and current_room == "lobby" and "lit candle" not in inventory:              # CONVERT LIT CANDLE >>> CANDLE
                    del rooms[current_room]["lit candle"]
                    rooms[current_room] = ['item', 'candle', 'No longer lit, but at least it still smells good.']
                    #print(f"{rooms[current_room][choice][2]} \n")
                    input("Press enter to continue.\n")
                    break

            print(f"{rooms[current_room][choice][2]} \n")
        
        else:    
            print("Action not available.")
            continue
    else: continue

#if __name__ == "__main__":
#    main()