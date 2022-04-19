#!/usr/bin/env python3

pokedex={"Bulbasaur":"Grass/Poison",
         "Squirtle":"Water",
         "Charmander":"Fire"}
pokedex["Pikachu"] = "Electric"

choice= input("Name a Generation 1 starter Pokemon:\n>")
print(pokedex.get(choice, "Sorry, we don't have any record of that Pokemon!"))


if choice not in pokedex
    print("Make a new selection")
else : print("Great choice!")


pokelist=", ".join(pokedex.keys())
print(pokelist)

print(pokedex.keys())
print(pokedex.values())
