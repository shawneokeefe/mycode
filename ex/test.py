#!/usr/bin/env python3

def T2(item1, item2):
        print(f"Replaced function line 1 {item1}")
        print(f"Replaced function line 2 {item2}")   
        print(f"{inv}")
# =========================================
def TT():
        input("TEST TEXT")
def T2(item1, item2):
        print(f"Original item {item1}")
        print(f"New item {item2}")
# =========================================
rooms =       { 'porch'      : {'act'     : ['act_call', 'act_name', T2("lint", "tin"), 'lint', 'tin'],
                                'muffin'  : ['item', 'muffin', 'Yum.']                                       }  }

inv   =       { 'lint'       : ['item', 'lint', 'Fluff.'],
                'muffin'     : ['item', 'muffin', 'Yum.']                                                       }

trans =       { 'tin'        : ['item', 'tin', 'Fluff.'],
                'muffin top' : ['item', 'nut', 'hard.']                                                         }
# =========================================
current_room = rooms['porch']
# =========================================

current_room['act'][2]