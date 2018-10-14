import requests
import time

##################################################
nickname = "" # enter the nickname whose steamid u wanna find.

##################################################





class NicknameDoesntExist(Exception):
    def __init__(self):
        return
		
def getUserCode(nickname):
    getNicknameUrl = "https://pubg.op.gg/api/find/users?nickname[]=" + nickname
    rNicknameCode = requests.get(getNicknameUrl)
    jNicknameCode = rNicknameCode.json()
    nicknameDict = jNicknameCode[nickname]
    nicknameCode = ""
    # print(nicknameCode)
    try:
        nicknameCode = nicknameDict["_id"]
        if nicknameCode == None:
            raise NicknameDoesntExist("Nickname doesnt exist.")
    except Exception as e:
        print("Nickname doesnt exist.")
    return nicknameCode

print("Please wait.........")
nicknameCode = getUserCode(nickname)

userUrl = "https://pubg.op.gg/api/users/" + nicknameCode
rUserUrl = requests.get(userUrl)
jUserUrl = rUserUrl.json()

listJoinSeason = jUserUrl["seasons"]
seasonsList = []
for i in listJoinSeason:
    seasonsList.append(i["season"])
# print(seasonsList)
summaryPlayedWith = "https://pubg.op.gg/api/users/" + nicknameCode + "/matches/summary-played-with?season="
flag = False
for i in seasonsList:
    if flag == True:
        break
    someoneWithUser = summaryPlayedWith + i
    rSummaryPlayerWith = requests.get(someoneWithUser)
    jSummaryPlayerWith = rSummaryPlayerWith.json()
    users = jSummaryPlayerWith["users"]
    if users != []:
        if flag == True:
            break
        time.sleep(3)
        findOneNickname = users[0]["user"]["nickname"]
        findOneCode = getUserCode(findOneNickname)
        summaryPlayedWithThis = "https://pubg.op.gg/api/users/" + findOneCode + "/matches/summary-played-with?season=" + i
        rSummaryPlayedWithThis = requests.get(summaryPlayedWithThis)
        jSummaryPlayedWithThis = rSummaryPlayedWithThis.json()
        listUser = jSummaryPlayedWithThis["users"]
        if len(listUser) != 0:
            for j in listUser:
                name = j["user"]["nickname"]
                if name == nickname:
                    print(j["user"]["identity_id"])
                    flag = True
















































