from enum import Enum


class StatusMessage(Enum):
    success = "success"
    fail = "fail"


class UserMessage(Enum):
    created = "User created"
    exist = "Login already exist"
    miss = "Missing login or password"
    changed = "User password successfully changed"
    empty_pass = "Body has no password parameter"
    deleted = "User successfully deleted"

