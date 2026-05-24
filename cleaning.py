import json



def cleandata(data):
    data["users"]=[i for i in data["users"] if i["name"].strip()]
    data["users"]=[i for i in data["users"] if i["friends"] or i["liked_pages"]]
    for i in data["users"]:
        i["friends"]=list(set(i["friends"]))
    return data

    


    


    
data= json.load(open("data.json"))
data=cleandata(data)
json.dump(data,open("data1.json","w"))