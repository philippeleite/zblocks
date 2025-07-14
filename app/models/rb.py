from app.models.base import info
from app.utils import read_memory
from struct import Struct
from collections import namedtuple

rb_pattern = Struct(
    ">"
    "8s"  # RBEXRTNM
    "2s"  # RBSYSDP1
    "2s"  # RBSTAB
    "4s"  # RBSYSDP2
    "8s"  # RBOPSW
    "4s"  # RBSYSDP3
    "4s"  # RBLINK
    "4s"  # RBGRS0
    "4s"  # RBGRS1
    "4s"  # RBGRS2
    "4s"  # RBGRS3
    "4s"  # RBGRS4
    "4s"  # RBGRS5
    "4s"  # RBGRS6
    "4s"  # RBGRS7
    "4s"  # RBGRS8
    "4s"  # RBGRS9
    "4s"  # RBGRS10
    "4s"  # RBGRS11
    "4s"  # RBGRS12
    "4s"  # RBGRS13
    "4s"  # RBGRS14
    "4s"  # RBGRS15
    "80s"  # RBEXSAVE
)

rb_field_names = (
    "RBEXRTNM",
    "RBSYSDP1",
    "RBSTAB",
    "RBSYSDP2",
    "RBOPSW",
    "RBSYSDP3",
    "RBLINK",
    "RBGRS0",
    "RBGRS1",
    "RBGRS2",
    "RBGRS3",
    "RBGRS4",
    "RBGRS5",
    "RBGRS6",
    "RBGRS7",
    "RBGRS8",
    "RBGRS9",
    "RBGRS10",
    "RBGRS11",
    "RBGRS12",
    "RBGRS13",
    "RBGRS14",
    "RBGRS15",
    "RBEXSAVE",
)

rb_offset_length = (
    info(0,8),  # RBEXRTNM
    info(8,2),  # RBSYSDP1
    info(10,2),  # RBSTAB
    info(12,4),  # RBSYSDP2
    info(16,8),  # RBOPSW
    info(24,4),  # RBSYSDP3
    info(28,4),  # RBLINK
    info(32,4),  # RBGRS0
    info(36,4),  # RBGRS1
    info(40,4),  # RBGRS2
    info(44,4),  # RBGRS3
    info(48,4),  # RBGRS4
    info(52,4),  # RBGRS5
    info(56,4),  # RBGRS6
    info(60,4),  # RBGRS7
    info(64,4),  # RBGRS8
    info(68,4),  # RBGRS9
    info(72,4),  # RBGRS10
    info(76,4),  # RBGRS11
    info(80,4),  # RBGRS12
    info(84,4),  # RBGRS13
    info(88,4),  # RBGRS14
    info(92,4),  # RBGRS15
    info(96,80),  # RBEXSAVE
)

rb_fields = namedtuple("rb", rb_field_names)
rb_info = rb_fields._make(rb_offset_length)


def get_rb(address: int) -> bytearray:
    buffer = bytearray(rb_pattern.size)
    read_memory(buffer, len(buffer), address)
    return buffer


class RB:
    name = "RB"
    long_name = "Request Block"
    fields = rb_field_names
    info = rb_info
    def __init__(self, address):
        content = rb_fields._make(rb_pattern.unpack(get_rb(address)))
        self.content = content