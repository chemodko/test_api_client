from enum import Enum


class StatusMessage(Enum):
    success = "success"
    fail = "fail"


class UserMessage(Enum):
    user_created = "User created"
    exist = "Login already exist"
    miss = "Missing login or password"
    changed = "User password successfully changed"
    empty_pass = "Body has no password parameter"
    user_deleted = "User successfully deleted"

    game_created = "Game created"
    game_not_exist = "Game with this id not exist"
    games_limit = "Limit of games, user can have only 20 games"
    game_deleted = "Game successfully deleted"

