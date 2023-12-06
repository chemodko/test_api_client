from enum import Enum


class StatusMessage(Enum):
    success = "success"
    fail = "fail"


class UserMessage(Enum):
    user_created = "User created"
    login_exist = "Login already exist"
    miss = "Missing login or password"
    pass_changed = "User password successfully changed"
    empty_pass = "Body has no password parameter"
    user_deleted = "User successfully deleted"

    game_created = "Game created"
    game_not_exist = "Game with this id not exist"
    games_limit = "Limit of games, user can have only 20 games"
    game_deleted = "Game successfully deleted"
    dlc_changed = "DlC successfully changed"
    dlc_deleted = "Game DLC successfully deleted"
    empty_dlc_list = "List with DLC to delete cant be empty or null"
    field_updated = "New value edited successfully on field description"
    cant_find_field = "Cannot find field"
    incorrect_field_type = "Cannot set new value because field has incorrect type"

