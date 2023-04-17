from enum import Enum
from typing import Optional


class Opcodes(Enum):
    CMD = 0x01  # Execute a command via cli
    SELFDESTRUCT = 0x02  # Self destruct the agent (delete self and shut down)
    SYSINFO = 0x03  # Get system information
    SLEEP = 0x04  # Sleep for a given amount of time
    UPDATE_CONFIG = 0x05  # Update the implant's maleable config
    DOWNLOAD = 0x06  # Download a file from the implant to the server
    UPLOAD = 0x07  # Upload a file from the server to the implant
    INJECT = 0x08  # Inject a DLL into a process

    def __str__(self):
        return self.name

    @staticmethod
    def get_by_name(name: str) -> Optional[int]:
        for opcode in Opcodes:
            if opcode.name == name or opcode.name.lower() == name.lower():
                return opcode.value
        return None

    @staticmethod
    def get_by_value(value: int) -> Optional[str]:
        for opcode in Opcodes:
            if opcode.value == value:
                return opcode.name
        return None
