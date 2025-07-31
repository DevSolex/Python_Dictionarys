#we are creating a data for blockfuse labs
Blockfuse_labs = {
    "web2": {
"sunday": 25,
"monday": 15,
"friday": 17
 },
    "web3": {
"solex": 25,
"unex": 13,
"scholer": 23
 }
}

print(Blockfuse_labs["web2"]["monday"])
#Blockfuse_labs["web2"] = Blockfuse_labs.update({{"web2""sunday": 10}})
Blockfuse_labs["web2"]["monday"] += 100
print(Blockfuse_labs["web2"]["monday"])
