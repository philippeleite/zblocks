from app.models.base import info, zblocks_list
from app.utils import read_memory
from struct import Struct
from collections import namedtuple

zblocks_list.append('JSAB')

jsab_pattern = Struct(
    ">"
    "4s"  # JSABID
    "4s"  # JSABNEXT
    "4s"  # JSABLEN
    "1s"  # JSABVERS
    "1s"  # JSABFLG1
    "1s"  # JSABFLG2
    "1s"  # JSABCLEV
    "4s"  # JSABSCID
    "8s"  # JSABJBID
    "8s"  # JSABJBNM
    "8s"  # JSABPREF
    "8s"  # JSABUSID
    "4s"  # JSABSSNM
    "16s"  # JSABRESC
    "8s"  # JSABESTK
    "8s"  # JSABXSTK
    "4s"  # JSABUSER
    "8s"  # JSABGPNM
    "1s"  # JSABJFL1
    "1s"  # JSABJFL2
    "1s"  # JSABJFL3
    "1s"  # JSABJFL4
    "1s"  # JSABJFL5
    "3s"  # JSABRSV1
    "20s"  # JSABRESV
    "64s"  # JSABCORR
)
jsab_field_names = (
    "JSABID",
    "JSABNEXT",
    "JSABLEN",
    "JSABVERS",
    "JSABFLG1",
    "JSABFLG2",
    "JSABCLEV",
    "JSABSCID",
    "JSABJBID",
    "JSABJBNM",
    "JSABPREF",
    "JSABUSID",
    "JSABSSNM",
    "JSABRESC",
    "JSABESTK",
    "JSABXSTK",
    "JSABUSER",
    "JSABGPNM",
    "JSABJFL1",
    "JSABJFL2",
    "JSABJFL3",
    "JSABJFL4",
    "JSABJFL5",
    "JSABRSV1",
    "JSABRESV",
    "JSABCORR",
)
jsab_offset_length = (
    info(0,4),  # JSABID
    info(4,4),  # JSABNEXT
    info(8,4),  # JSABLEN
    info(12,1),  # JSABVERS
    info(13,1),  # JSABFLG1
    info(14,1),  # JSABFLG2
    info(15,1),  # JSABCLEV
    info(16,4),  # JSABSCID
    info(20,8),  # JSABJBID
    info(28,8),  # JSABJBNM
    info(36,8),  # JSABPREF
    info(44,8),  # JSABUSID
    info(52,4),  # JSABSSNM
    info(56,16),  # JSABRESC
    info(72,8),  # JSABESTK
    info(80,8),  # JSABXSTK
    info(88,4),  # JSABUSER
    info(92,8),  # JSABGPNM
    info(100,1),  # JSABJFL1
    info(101,1),  # JSABJFL2
    info(102,1),  # JSABJFL3
    info(103,1),  # JSABJFL4
    info(104,1),  # JSABJFL5
    info(105,3),  # JSABRSV1
    info(108,20), # JSABRESV
    info(128,64),  # JSABCORR
)

jsab_fields = namedtuple("jsab", jsab_field_names)
jsab_info = jsab_fields._make(jsab_offset_length)


def get_jsab_address() -> int:
    address_buffer = bytearray(4)
    read_memory(address_buffer, len(address_buffer), 548)
    address_ascb = int.from_bytes(address_buffer, byteorder='big')
    read_memory(address_buffer, len(address_buffer), address_ascb + 336)
    address_assb = int.from_bytes(address_buffer, byteorder='big')
    read_memory(address_buffer, len(address_buffer), address_assb + 168)
    address = int.from_bytes(address_buffer, byteorder='big')
    return address


def get_jsab() -> bytearray:
    buffer = bytearray(jsab_pattern.size)
    address = get_jsab_address()
    read_memory(buffer, len(buffer), address)
    return buffer


class JSAB:
    name = "JSAB"
    long_name = "Job Scheduler Address Space Control Block"
    fields = jsab_field_names
    info = jsab_info
    def __init__(self):
        content = jsab_fields._make(jsab_pattern.unpack(get_jsab()))
        self.content = content