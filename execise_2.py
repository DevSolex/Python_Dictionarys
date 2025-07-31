import pprint
oxford = {
    "apple": "a common friut",
    "ball": "a round object",
    "cat": "an animal",
    "dog": "nangwans dog meat",
    "egg": "a spherical cookable object",
    "fish": "a cold blooded vertebrete",
    "goat": "abdullahi",
    "house": "a building",
    "idiot": "wild animal",
    "jackal": "wild animal"
}


pprint.pprint(oxford)
#print("meaning of ball" + oxford["ball"])
oxford["kettle"] = "a vessel for boiling"
oxford["jackal"] = "a wild animal in the bush"
print(oxford.keys(),  type(oxford.keys()))
print(oxford.values(),  type(oxford.values()))


