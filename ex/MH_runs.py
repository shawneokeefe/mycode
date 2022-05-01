#!/usr/bin/env python3
'''This module is a text-based RPG. Made by Shawn O'Keefe'''

# ======================================== IMPORTS ==============================================================================
import os             # ENABLES FUNCTIONS: os.system("clear")
import sys            # ENABLES FUNCTIONS: system.exit()

# ======================================== DICTIONARIES / LISTS ============================================== * Actions can have any number of assigned functions, but the code indexes/assigns them in groups of 4. Use '' as necessary.
                 #   ___________required for all actions_____________                                                                             _________________________ function_1 _____________________    ____________________ function_2 ________________________  >>>>>
                 #  [0           1           2            3         ]   4               5                6                  7                   [8               9              10              11        ]   [12             13             14             15         ]  >>>>>
                 #                                                                                                                               transfer        ele(act/item)  source_dict    dest_dict      ...
                 #   ACT ------- ACT_CALL -- ACT _DESC -- ACT_REMOVE -- REQ_ITEM_INV -- REQ_ITEM_ROOM -- REQ_ITEM_NO_INV -- REQ_ITEM__NO_ROOM -- ACT_FUNCTION -- PARAMETER 1 -- PARAMETER 2 -- PARAMETER 3 -- ACT_FUNCTION -- PARAMETER 1 -- PARAMETER 2 -- PARAMETER 3   >>>>>
rooms = {        

  'porch'        :{
                    'desc'       : 'MONTY HALL PORCH:\n  Your driver pulls up to the curb and you get out. Drizzling rain hastens you up the steps to Monty Hall.\n  Renovated in the last three months, the old estate is awash with lights and pouring with music.\n  Costumed up for the bootleg era, you are eager to join your co-workers in the interactive mystery murder theater.',
                    'go'         : ['move', 'reception', 'GO to the reception'],
                    'return'     : ['move', 'curb', 'RETURN to the curb'],
                    'check'      : ['act', 'CHECK your invitation', 'Hmmm. Surely it was here? Did I leave it on the seat?', 'remove'],
                  },
  'curb'         :{
                    'desc'       : 'CURBSIDE:\n  Your ride already left. Nothing at the curb except deep puddles, lamps, and trees swaying in the wind.',
                    'return'     : ['move', 'lobby', 'RETURN to Monty Hall'],
                    'call'       : ['act', 'CALL an uber and go home', 'Then again, maybe not. You came here to enjoy yourself. Might as well do it.', 'remove', 'cell phone', ''],
                    'jump'       : ['act', 'JUMP in the puddles', 'Splash, splash, splash!', ''],
                    'invitation' : ['item', 'invitation', 'Dripping, but readable:\n\n  Hi. Join me for Monty Hall\'s opening night for its dinner/mystery theater on 4 May. I bet you already heard about\n  the place, but do not forget to dress the part. We will be swinging the old-timesy fashion at 7pm.\n \n Your seat is paid, so if you are late ...\n I will kill you. LOL!\n \n  - Suse'],
                  },
  'reception'    :{
                    'desc'       : 'RECEPTION:\n  You take off your fedora and clack into the polished halls of an impressive foyer overlooked by a deep gallery\n  and steeped in jazz.  The lone receptionist perks up from behind a reception counter and gestures to you.\n  "All parties are meeting in the lounge on your left. Lockout starts soon."',
                    'turn'       : ['move', 'lounge', 'TURN left into the lounge'],
                    'wander'     : ['move', 'gallery', 'WANDER right into the gallery'],
                    'suse'       : ['act', '"I\'m with SUSE. She arrive?"','"So, you\'re her partner. It\'s a fun role. Join her in the lounge before you get replaced. " the receptionist answered.', 'remove'],
                    'return'     : ['act', 'RETURN to the curb', 'Alas! You can see the lights of your ride already disappearing down the driveway.', 'remove'],
                    'call'       : ['act', 'CALL your friends', 'Better luck shouting ... or just go into the lounge.', '', 'cell phone',''],
                    'check'      : ['act', 'CHECK your invitation', 'Hmm, where is it? Oh well, better just get moving.', 'remove'],                 
                  },
  'gallery'      :{
                    'desc'       : 'GALLERY:\n  Taking your own time, you opt to explore the gallery. The walls are littered with insets of period art,\n  memorabilia, and summaries of historical significance. As you scroll the displays, the lights fall, all goes silent.',
                    'fumble'     : ['move', 'lobby', 'Carefully FUMBLE your your way back to the lobby'],
                    'wait'       : ['act', 'WAIT a moment', 'No time restores the lights.', ''],
                    'call'       : ['act', 'CALL out to the staff', 'No response. Perhaps the staff are in the lounge or backrooms.', 'remove'],
                  },
  'lounge'       :{
                    'desc'       : 'LOUNGE:\n  You entered the lounge, perhaps just barely soon enough. Guests were already filtering out and into the ballroom beyond.\n  Bright lights, art deco, and a glass gallery for a bar. Nothing stood out so much as the period ash tray with the sign,\n  "No Smoking."  Anachronisms aside, you spot Suse instantly, centered on the bar balancing a cocktail in her hand, a\n  giant plumed red hat on her head, and serpent around the shoulders.\n\n  She spots you and calls out, "Glad you could make it, and we got matching hats. How sweet of you." She rang a little\n  bell on the counter and beckoned you over. Mirri handed off her snake to the staff.\n\n  "Don\'t mind Mr. Rossum, I don\'t even know why I brought him tonight. You however have a purpose. Follow me."',
                    'follow'     : ['move', 'balcony', 'FOLLOW Suse',],
                    'exit'       : ['move', 'lobby', 'EXIT to the lobby'],
                    'refuse'     : ['act', 'REFUSE and stay behind','"How disappointing," you say, "I came to do some sleuthing, and I will do just that."\n \n  "You\'ll regret this, but must bid you farewell to do my part. Enjoy the snakes, ... I mean snacks," Suse snapped.\n \n  Suse exitted out a side door. Nothing but you and a room full of alcohol.', 'remove', '', '', '', '', 'transfer', 'follow', 'rooms', 'bank', 'transfer', 'purpose', 'rooms', 'bank', 'transfer', 'friend', 'rooms', 'bank'],
                    'friend'     : ['act', '"So, your FRIEND there."', '"Darling, ... it\'s called acting the part.," Suse teased, "Rossum is tame, even so pythons are not venomous."', 'remove'],
                    'purpose'    : ['act', '"PURPOSE?"', 'Suse grinned. "Because you get to be the mysterious Monty Hall!... and I am your lovely partner in crime.\n We\'re are going to reenact history tonight."', 'remove'],
                    'enter'      : ['act', 'ENTER the ballroom', 'Locked.  What might be going on in there?', 'remove'],
                    'enjoy'      : ['act', 'ENJOY a drink', 'Maybe you should have savored that one a bit more', 'remove', 'cocktail', '', 'transfer', 'cocktail', 'inventory', 'bank'],
                    'try'        : ['act', 'TRY the fingerfood', 'Whoops. That baguette took a trip to the floor.', 'remove', 'baguette', '', '', '', 'transfer', 'baguette', 'inventory', 'bank', 'transfer', 'happy accident', 'bank', 'rooms'],
                    'cocktail'   : ['item', 'cocktail', 'At least you had time to snag a drink. After all, none of this would be here without alcohol.'],
                    'baguette'   : ['item', 'baguette', 'Slippery, slathered in cream cheese. Can I get a doggy bag?'],
                  },
  'balcony'      :{
                    'desc'       : 'BALLROOM BALCONY:\n  The pathway leads upstairs ending at a wide balcony far above the ballroom. You can hear a\n  cacophony of murmuring and laughter down below.\n\n  "This is where the action happens," explains Suse, "This isn\'t just a mystery theater, it is an escape room."\n  The staff will play out recordings to manipulate our partiers while we choose how the house deals out its cards\n  from behind the scenes. Watch and I will guide you through it.',
                    'observe'    : ['act', 'OBSERVE the scene below', 'That\'s all folks. Tune in again for Part 2.', ''],
                    'close'      : ['act', 'CLOSE your eyes', 'You can\'t help but peek.', 'remove'],
                  },                 
  'lobby'        :{
                    'desc'       : 'LOBBY:\n  What happened to the lights and music? The entrance is lit only a by sputtering candle. The darkness closes in.',
                    'delve'      : ['move', 'darkness','DELVE into the darkness'],
                    'go'         : ['move', 'outside', 'GO outside'],
                    'open'       : ['act', 'OPEN the window', 'A wave of sleet spatters you as you briefly open the window. You quickly shut it, but too late to save your only light.\n  You are plunged into total darkness', 'remove', '', '', '', '',      'transfer', 'lit candle', 'inventory', 'bank',      'transfer', 'lit candle', 'rooms', 'bank',      'transfer', 'candle', 'bank', 'rooms',      'transfer', 'burn', 'rooms', 'bank'],
                    'lit candle' : ['item', 'lit candle', 'Mmmm! Mint and cinnamon.'],
                    'burn'       : ['act', 'BURN your invitation', 'The paper curls, chars, and crumbles to dust.', 'remove', 'invitation', 'lit candle', '', '',      'transfer',  'invitation', 'inventory', 'bank'],
                  },
  'outside'      :{
                    'desc'       : 'OUTSIDE:\n The rain isn\'t letting up and your suit isn\'t getting any drier. Nothing to see but the long private drive shimmering\n with the reflection of a row of lamps.',
                    'return'     : ['move', 'darkness', 'RETURN to Monty Hall'],
                    'call'       : ['act', 'CALL an uber', 'No reception. Monty Hall is just too far from civilization. Guess that helped the establishment and patrons avoid the law in the 1920s.', 'remove', 'cell phone', ''],
                    'walk'       : ['act', 'WALK home', 'Then again, maybe not. It was a 30-minute drive.', 'remove'],
                  },                
  'darkness'     :{
                    'desc'       : 'DARKNESS:\n  So dark ... All is the void.',
                    'delve'      : ['move', 'backrooms', 'DELVE deeper. Maybe you will find a door.'],
                    'wait'       : ['act', 'WAIT and listen', 'Did you hear that? Did it hear you?', ''],
                  },
  'backrooms'    :{
                    'desc'       : 'BACKROOMS:\n  Fumbling into the backrooms and up a flight of stairs, you bump into something in the darkness. Something feathery,\n  overdressed, and with a bony elbow. "Ouch. Who bumped me?" It whispered.\n \n  Recognizing the voice you question, "Suse?"\n \n  "Glad you decided to show, but you and I need to hurry to the balcony. I will fill you in as we go along."',
                    'follow'     : ['move', 'balcony', 'FOLLOW Suse'],
                    'turn'       : ['act', 'TURN around', 'Suse pulls your arm, "Nope. You are going this way."', 'remove'],
                  },
  'test room'    :{
                    'desc'       : 'TEST ROOM:\n  Welcome to the test room."',
                    'create'     : ['act', 'CREATE (5) test items to test action iterations.', 'Iteration test complete."', 'remove', '', '', '', '', 'transfer', 'test item 1', 'bank', 'inventory', 'transfer', 'test item 2', 'bank', 'inventory', 'transfer', 'test item 3', 'bank', 'inventory', 'transfer', 'test item 4', 'bank', 'inventory', 'transfer', 'test item 5', 'bank', 'inventory'],
                    'list'       : ['act', 'LIST additional actions available in this room', 'Actions added', 'remove', '', '', '', '', 'transfer', 'juggle', 'bank', 'rooms'],
                  },                  
                  }
inventory =       {  
                    'cell phone' : ['item', 'cell phone', 'Powered, but only one bar here. Maybe I should climb a tree.'],
                    'lint'       : ['item', 'lint', 'Fluff. Always to be found when you need it.'],
                    'wallet'     : ['item', 'wallet', '- Cards .......... check.\n- Cash ........... check.\n- Breath mints ... darn.'],
                  }

bank = {
  'lounge'       :{
                    'late'       : ['act', '"Sorry I am LATE,"', 'Not late. You were supposed to show up later than the rest of us." Suse replied.', 'remove'],
                    'next'       : ['act', '"What happens NEXT."', '"Ask later, come on." Suse beckoned.', 'remove'],
                    'happy accident' : ['item', 'happy accident', 'We don\'t make mistakes, only happy accidents. Surely the baguette was meant to be free.'],  
                  },
  'lobby'        :{                    
                    'candle'      : ['item', 'candle', 'Snuffed out, but it still smells good'],
                  },
  'test room'    :{
                    'juggle'      : ['act', 'JUGGLE your test items.', 'What a feat!', '', 'test item 1', '', 'wallet', 'cell phone'],
                    'test item 1' : ['item', 'test item 1', 'flavor text - blueberry'],
                    'test item 2' : ['item', 'test item 2', 'flavor text - strawberry'],
                    'test item 3' : ['item', 'test item 3', 'flavor text - apple'],
                    'test item 4' : ['item', 'test item 4', 'flavor text - grape'],
                    'test item 5' : ['item', 'test item 5', 'flavor text - watermelon'],
                  },
                  }

# ======================================== INITIAL STATE ========================================================================
current_room = 'porch'
game_over = 0
grue = 0

# ======================================== TEST FUNCTIONS======================================================================
def TP(test_print):
    input(f"TEST PRINT: {type(test_print)} -- {str('test_print')} -- {test_print}")
def WW(wait):
    input(f"WAITING: {wait}")
    
 # ======================================== ACTION FUNCTIONS======================================================================

def transfer(element, source, dest):                                                                               # ELEMENT (act, item),       SOURCE/DEST (rooms, inventory, bank)
    WW('TRANSFER')
    
    if element in inventory and source == 'inventory':
        if dest == 'bank':
            bank[current_room][element] = inventory[element]
        if dest == 'rooms':
            rooms[current_room][element] = inventory[element]
        inventory.pop(element)
    
    if element in rooms[current_room] and source == 'rooms':
        if dest == 'inventory':
            inventory[element] = rooms[current_room][element]
        if dest == 'bank':
            bank[current_room][element] = rooms[current_room][element]
        rooms[current_room].pop(element)
 
    if element in bank[current_room] and source == 'bank':
        if dest == 'inventory':
            inventory[element] = bank[current_room][element]
        if dest == 'rooms':
            rooms[current_room][element] = bank[current_room][element]
        bank[current_room].pop(element)       
            
# ======================================== STATUS SCREEN ========================================================================
def status():  
    '''This function refreshes the screen and prints the current status of the RPG scenario.'''
    global current_room

    try:
        os.system("clear")
    except:
        os.system("cls")
        
    print('''
=======================================================================================================================                                    
                            ╔╦╗ ╔═╗ ╔╗╔ ╔╦╗ ╦ ╦    ╦ ╦ ╔═╗ ╦  ╦      ╔╦╗ ╦ ╦ ╦═╗ ╔╦╗ ╔═╗ ╦═╗
                            ║║║ ║ ║ ║║║  ║  ╚╦╝    ╠═╣ ╠═╣ ║  ║      ║║║ ║ ║ ╠╦╝  ║║ ║╣  ╠╦╝
                            ╩ ╩ ╚═╝ ╝╚╝  ╩   ╩     ╩ ╩ ╩ ╩ ╩═╝╩═╝    ╩ ╩ ╚═╝ ╩╚═ ═╩╝ ╚═╝ ╩╚═
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

# ====================================== GAME LOOP ==============================================================================
def main():
    '''This function processes the player's commands and calls for status screen updates.'''
    global game_over, grue, current_room

    while True:
        status()

        if game_over == 1:                                                                                         # EXIT AFTER GAME OVER
            if grue >= 3:
                print("You were eaten by a grue! - GAME OVER")
            input("Press ENTER to exit.")
            sys.exit()

        while game_over == 0:                                                                                      # GAME OVER CONDITIONS
            choice = input('> ',)
            choice = choice.lower()

            if rooms[current_room] == "darkness" or "gallery" and choice == "wait":                                # GAME OVER - EATEN BY GRUE
                if "lit candle" not in rooms[current_room] and "lit candle" not in inventory:
                    grue += 1
                    if grue >= 3:
                        game_over = 1
                        break

            if choice == 'refresh':                                                                                # REFRESHES THE STATUS SCREEN
                status()
                continue
            
            if choice == 'teleport':                                                                               # TELEPORT
                print("AVAILABLE ROOMS:")
                for room_names in rooms.keys():
                    print(f"{room_names}  ", end="")
                q_teleport = input("\n\n Teleport to which room? \n> ")
                q_teleport = q_teleport.lower()
                if q_teleport in rooms.keys():
                    current_room = q_teleport
                    break
                else: continue        

            elif choice in rooms[current_room] and rooms[current_room][choice][0] == "item":                       # ADD TO INVENTORY, REMOVE FROM ROOM
                item_get = rooms[current_room][choice]                                                          
                inventory[choice] = [item_get[0], item_get[1], item_get[2]]           
                rooms[current_room].pop(choice)
                input(f"Added {choice.upper()} to inventory. Press enter to continue. \n")
                break

            elif choice in inventory:                                                                              # CHECK ITEM DESCRIPTION, DROP INTO ROOM
                item_drop = inventory[choice]
                print(f"{inventory[choice][2]}  \n")
                q_drop = input(f"Drop {choice.upper()}? (Y/N) \n> ")
                if q_drop == "Y" or q_drop == "y":
                    rooms[current_room][choice] = [item_drop[0], item_drop[1], item_drop[2]]         
                    inventory.pop(choice)
                    input(f"Dropped {choice.upper()}. Press enter to continue. \n")
                    break
                else: continue

            elif choice in rooms[current_room] and rooms[current_room][choice][0] == "move":                       # CHANGE ROOMS
                current_room = rooms[current_room][choice][1]
                break

            elif choice in rooms[current_room] and rooms[current_room][choice][0] == "act":                        # PERFORM ACTIONS
#                WW('ACT VARIABLES')
                act_full = rooms[current_room][choice]
                act_text = rooms[current_room][choice][2]
                act_remove = rooms[current_room][choice][3]                      
                act_length = len(act_full)

#                WW('CHECK REQ ITEM')                                                                               # CHECKS FOR REQUIRED ITEMS - INV / ROOM                
                if act_length > 4:
                    act_item_req_inv = rooms[current_room][choice][4]
                    act_item_req_room = rooms[current_room][choice][5]  
                    if act_item_req_inv not in inventory and act_item_req_inv != '':
                        print(f"I need to get {act_item_req_inv.upper()} first.")
                        continue
                    if act_item_req_room not in rooms[current_room] and act_item_req_room != '':
                        print(f"{act_item_req_room.upper()} needs to be in the room first.")
                        continue

#                WW('CHECK REQ ABSENCE OF ITEM')                                                                    # ACT WILL NOT EXECUTE WITH ITEM IN - INV / ROOM                      
                if act_length > 6:         
                    act_item_req_no_inv = rooms[current_room][choice][6] 
                    act_item_req_no_room = rooms[current_room][choice][7] 
                    if act_item_req_no_inv in inventory and act_item_req_inv != '':
                        print(f"Cannot do that while {act_item_req_no_inv.upper()} is on hand.")
                        continue
                    if act_item_req_no_room in rooms[current_room] and act_item_req_no_room != '':
                        print(f"Cannot do that while {act_item_req_no_room.upper()} is nearby.")
                        continue                    

#                WW('DETERMINE QTY OF ACTION FUNCTIONS')                                                           # DETERMINES HOW MANY FUNCTIONS ARE IN AN ACT LIST
                act_func_count = (act_length-8)/4                                                                  # EVERY ACT FUNCTION ADDS 4 ELEMENTS TO THE ACT LIST
                act_iteration = 0
#                input(f"This action will iterate for {str(act_func_count)} action_functions.")

#                WW('START ACTION WHILE LOOP')
                while act_iteration <= act_func_count and act_length > 8:
                    act_iteration += 1
                
                    index_act_func = 4+(4*act_iteration)                                                           # DETERMINES ACTION LIST INDEX VALUES FOR EACH ACTION ITERATION
                    index_act_func_p1 = 5+(4*act_iteration)
                    index_act_func_p2 = 6+(4*act_iteration)
                    index_act_func_p3 = 7+(4*act_iteration)
                   
                    act_func = act_full[index_act_func]                                                            # ASSIGNS INDEX VALUES TO THE PARAMETERS OF THE ACTION FUNCTION
                    act_func_p1 = act_full[index_act_func_p1]
                    act_func_p2 = act_full[index_act_func_p2]
                    act_func_p3 = act_full[index_act_func_p3]
                    
#                    WW('CHECK ACT FUNCTIONS')                                                                     # CALLS THE ACTION FUNCTIONS
                    if act_func != '':

                        if act_func == 'transfer':
#                            WW('CALLING TRANSFER')
                            transfer(act_func_p1, act_func_p2, act_func_p3)
                        
#                        input(f" Completed iteration {str(act_iteration)}.")
                        
                        if act_iteration < act_func_count:
                            continue
                        break
                                                                                                      
#                WW('ACTS - CLEANUP & REFRESH')                                                                     # CLEANUP & REFRESH
                print(f"{act_text}")                                                                        
                if "remove" in act_remove or act_func_count > 0:
                    rooms[current_room].pop(choice)
                    input("Press enter to continue.\n")
                    break    
                continue
                
            else:    
                print("Action not available.")
                continue

        else:
            continue

# ====================================== CALL MAIN ==============================================================================

if __name__ == "__main__":
    main()