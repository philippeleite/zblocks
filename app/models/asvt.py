from app.models.base import info, zblocks_list
from app.utils import read_memory
from struct import Struct
from collections import namedtuple

zblocks_list.append('ASVT')

asvt_pattern = Struct(
    ">"
    "464s"  # ASVTPRFX
    "4s"  # ASVTHWMASID
    "4s"  # ASVTCURHIGHASID
    "4s"  # ASVTREUA
    "4s"  # ASVTRAVL
    "4s"  # ASVTAAV
    "4s"  # ASVTAST
    "4s"  # ASVTANR
    "4s"  # ASVTSTRT
    "4s"  # ASVTNONR
    "4s"  # ASVTMAXI
    "8s"  # ASVTRSHD
    "4s"  # ASVTASVT
    "4s"  # ASVTMAXU
    "4s"  # ASVTMDSC
    "4s"  # ASVTFRST
    "4s"  # ASVTENTY
)
asvt_field_names = (
    "ASVTPRFX",
    "ASVTHWMASID",
    "ASVTCURHIGHASID",
    "ASVTREUA",
    "ASVTRAVL",
    "ASVTAAV",
    "ASVTAST",
    "ASVTANR",
    "ASVTSTRT",
    "ASVTNONR",
    "ASVTMAXI",
    "ASVTRSHD",
    "ASVTASVT",
    "ASVTMAXU",
    "ASVTMDSC",
    "ASVTFRST",
    "ASVTENTY",
)
asvt_offset_length = (
    info(0,464),  # ASVTPRFX
    info(464,4),  # ASVTHWMASID
    info(468,4),  # ASVTCURHIGHASID
    info(472,4),  # ASVTREUA
    info(476,4),  # ASVTRAVL
    info(480,4),  # ASVTAAV
    info(484,4),  # ASVTAST
    info(488,4),  # ASVTANR
    info(492,4),  # ASVTSTRT
    info(496,4),  # ASVTNONR
    info(500,4),  # ASVTMAXI
    info(504,8),  # ASVTRSHD
    info(512,4),  # ASVTASVT
    info(516,4),  # ASVTMAXU
    info(520,4),  # ASVTMDSC
    info(524,4),  # ASVTFRST
    info(528,4),  # ASVTENTY
)

asvt_fields = namedtuple("asvt", asvt_field_names)
asvt_info = asvt_fields._make(asvt_offset_length)


def get_asvt_address() -> int:
    address_buffer = bytearray(4)
    read_memory(address_buffer, len(address_buffer), 16)
    address_cvt = int.from_bytes(address_buffer, byteorder='big')
    read_memory(address_buffer, len(address_buffer), address_cvt + 556)
    address = int.from_bytes(address_buffer, byteorder='big')
    return address


def get_asvt() -> bytearray:
    buffer = bytearray(asvt_pattern.size)
    address = get_asvt_address()
    read_memory(buffer, len(buffer), address)
    return buffer

def get_asvt_number_of_entries() -> int:
    buffer = get_asvt()
    return int.from_bytes(buffer[516:520], byteorder='big')

def get_asvt_entries() -> list:
    number_of_entries = get_asvt_number_of_entries()
    buffer = bytearray(number_of_entries * 4)
    read_memory(buffer, len(buffer), get_asvt_address() + 528)
    entries = []
    for i in range(0, len(buffer), 4):
        entries.append(buffer[i:i+4])
    return entries

class ASVT:
    name = "ASVT"
    long_name = "Address Space Vector Table"
    fields = asvt_field_names
    info = asvt_info
    def __init__(self):
        content = asvt_fields._make(asvt_pattern.unpack(get_asvt()))
        self.content = content
        self.entries = get_asvt_entries()
