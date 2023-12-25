from enum import Enum

class StatusType(str, Enum):
    DONE = "done"
    PENDING = "pending"