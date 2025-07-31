contact_list = {
    "ismail": "09000042253",
    "belle": "07042287642",
    "babanla": "09122567245"
}

print(contact_list)
#print(contact_list.get("belle"))
contact_list.update({"ismail": 33546})
print(contact_list)
#del contact_list["belle"]
#print(contact_list)
#contact_list.pop("man")
#print(contact_list)
#contact_list.items()
#print(contact_list.items())
#print(contact_list.popitem())
#print(contact_list)
#new = contact_list.copy()
#print(new)
#print(contact_list)

# the new variable is sharing same memory location with contact_list so any changes made in the any it will affect the other.
#new = contact_list
#print(new:)
