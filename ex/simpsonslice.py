#!/usr/bin/env python3
"""Morning Slicing Challenge!"""
SURVEYLIST = [1, 2, 3, 4]
if SURVEYLIST -- [1, 2, 3, 4]
    print(1)
if 6 not in SURVEYLIST:
    print(2)


#challenge= ["science","turbo", ["goggles", "eyes"],"nothing"]
#challenge= ["science",
            "turbo", ["goggles", "eyes"],
            "nothing"]
print(challenge[3])
nothing = print(challenge[2][
print(nothing)


#trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
#trial= ["science",
        "turbo",
            {
                "eyes": "goggles",
                "goggles": "eyes"},
        "nothing"]


eyes= trial[2]["goggles"]
goggles= trial[2]["eyes"]
nothing= trial[3]

# order of key values does not matter in a dictionary, therefore, you must use "name"
# list always slice by index []
# dictionary always slide by name {}
# a dictionary within a list is sliced out by index




















#nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]
#nightmare= [{
            "slappy":
                "a",
            "text":  "b",
                    "kumquat":
                        "goggles",
                        "user":{
                            "awesome":
                                "c",
                                "name": {
                                    "first":
                                        "eyes",
                                        "last": "toes"}},
            "banana":
                15,
                "d": "nothing"}]

#print(f"My {challenge["turbo"][1]}! The {challenge["turbo"][0]} do {challenge["nothing"]}!")
print(challenge["turbo"]["goggles"])
print(challenge["turbo"][0])
print(challenge["nothing"])
def main():
    """write your code in this function to solve the challenge"""

    # write one print function for each list above
    # get the strings "eyes," "goggles," and "nothing from each
    # final output for each print should look like this:
    """My eyes! The goggles do nothing!"""

    print(f"My {challenge[turbo][1]}! The {challenge[turbo][0]} do {challenge[nothing]}!")
    # print(f"My {}! The {} do {}!")
    # print(f"My {}! The {} do {}!")

    # if __name__ == "__main__": # <-- what is this??? we will review later :)
    main()
