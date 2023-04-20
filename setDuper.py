import os
import requests

username = input("Username: ")
password = input("Password: ")

try:
    os.system("clear")
except:
    os.system("cls")

login = requests.post("https://id.blooket.com/api/users/login", json={"name": username, "password": password}).cookies

for cookie in login:
    cookies = {"bsid": cookie.value}

setId = input("Set id: ")

setData = requests.get(f"https://dashboard.blooket.com/api/games?gameId={setId}", cookies=cookies).json()

id = requests.post("https://dashboard.blooket.com/api/games",
                   json={"title": setData["title"], "author": username, "desc": setData["desc"], "coverImage": {},
                         "private": False}, cookies=cookies).json()["_id"]

for question in setData["questions"]:
    # print(question)
    try:
        image = {"url": question["image"]["url"], "id": "u"}
    except:
        image = {}
    data = {
        "answerImages": [{}, {}, {}, {}],
        "answerTypes": [],
        "answers": question["answers"],
        "correctAnswers": question["answers"],
        "gameId": id,
        "image": image,
        "qType": "mc",
        "question": question["question"],
        "random": True,
        "timeLimit": question["timeLimit"]
    }

    print(requests.put("https://dashboard.blooket.com/api/games/addquestion", cookies=cookies, json=data).status_code)
