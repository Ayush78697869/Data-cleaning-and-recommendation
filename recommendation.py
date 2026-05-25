import json

data=json.load(open("data1.json","r"))

def friends1(user_id,data):
    
    friends={}
    for i in data["users"]:
        friends[i["id"]]=list(set(i["friends"]))
    if user_id not in friends:
        return []    
    friends_of_user =friends[user_id]
    #return friends_of_user
    suggestions=[]
    if user_id not in friends:
            print("No such user")
    for i in friends_of_user:
        if i not in friends:
             continue
        suggestions.extend(list(set(friends[i])-set(friends_of_user)-{user_id}))

    return suggestions

        



print(friends1(2,data))
