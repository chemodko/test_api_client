from src.utils.randoms import random_number


dlcs = [
    {
        "description": "New awesome sport cars",
        "dlcName": "Cars dlc",
        "isDlcFree": True,
        "price": 0,
        "rating": 10,
        "similarDlc": {
            "dlcNameFromAnotherGame": "DLC from GTA 5",
            "isFree": True
        }
    }
]


games = [
    {
        "company": "RockStar Games",
        "description": "An action-adventure computer game with an open world.",
        "dlcs": [],
        "gameId": random_number(),
        "genre": "action-adventure",
        "isFree": False,
        "price": 2999,
        "publish_date": "2023-12-05T09:16:22.745Z",
        "rating": 9,
        "requiredAge": True,
        "requirements": {
            "hardDrive": 100,
            "osName": "Windows 10, Windows 11",
            "ramGb": 4,
            "videoCard": "ANY"
        },
        "tags": [
            "Awesome", "Cool", "Blood"
        ],
        "title": "GTA 6"
    },
    {
        "company": "RockStar Games",
        "description": "An action-adventure computer game with an open world.",
        "dlcs": dlcs,
        "gameId": random_number(),
        "genre": "action-adventure",
        "isFree": False,
        "price": 2999,
        "publish_date": "2023-12-05T09:16:22.745Z",
        "rating": 9,
        "requiredAge": True,
        "requirements": {
            "hardDrive": 100,
            "osName": "Windows 10, Windows 11",
            "ramGb": 4,
            "videoCard": "ANY"
        },
        "tags": [
            "Awesome", "Cool", "Blood"
        ],
        "title": "GTA 6"
    }
]

