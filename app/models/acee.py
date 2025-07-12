from app.models.base import info, zblocks_list
from app.utils import read_memory
from struct import Struct
from collections import namedtuple

zblocks_list.append('ACEE')

acee_pattern = Struct(
    ">"
    "4s"  # ACEEACEE
    "4s"  # ACEECORE
    "1s"  # ACEEVRSN
    "3s"  # ACEESBVR
    "4s"  # ACEEIEP
    "4s"  # ACEEINST
    "1s"  # ACEEUSRL
    "8s"  # ACEEUSRI
    "1s"  # ACEEGRPL
    "8s"  # ACEEGRPN
    "1s"  # ACEEFLG1
    "1s"  # ACEEFLG2
    "1s"  # ACEEFLG3
    "3s"  # ACEEDATE
    "8s"  # ACEEPROC
    "4s"  # ACEETRMP
    "2s"  # ACEEFLG4
    "1s"  # ACEEAPLV
    "1s"  # ACEETRLV
    "4s"  # ACEETRDA
    "8s"  # ACEETRID
    "4s"  # ACEEAMP
    "4s"  # ACEECLTH
    "4s"  # ACEECLCP
    "4s"  # ACEEAPTR
    "8s"  # ACEEAPLN
    "4s"  # ACEEAPDA
    "4s"  # ACEEUNAM
    "4s"  # ACEEMDLS
    "4s"  # ACEECGRP
    "4s"  # ACEEGATA
    "4s"  # ACEEFCGP
    "4s"  # ACEEDSLP
    "4s"  # ACEEDAT4
    "4s"  # ACEEPADS
    "1s"  # ACEESLVL
    "1s"  # ACEEFLG5
    "1s"  # ACEEFLG6
    "1s"  # ACEERSV1
    "4s"  # ACEE3PTY
    "4s"  # ACEEPLCL
    "8s"  # ACEESUID
    "4s"  # ACEEOCOX
    "4s"  # ACEEPTDS
    "4s"  # ACEEX5PR
    "4s"  # ACEETOKP
    "4s"  # ACEESRVA
    "4s"  # ACEESRVP
    "4s"  # ACEENSTA
    "4s"  # ACEEICTX
    "4s"  # ACEEIDID
    "4s"  # ACEETIME
)

acee_field_names = (
    "ACEEACEE",
    "ACEECORE",
    "ACEEVRSN",
    "ACEESBVR",
    "ACEEIEP",
    "ACEEINST",
    "ACEEUSRL",
    "ACEEUSRI",
    "ACEEGRPL",
    "ACEEGRPN",
    "ACEEFLG1",
    "ACEEFLG2",
    "ACEEFLG3",
    "ACEEDATE",
    "ACEEPROC",
    "ACEETRMP",
    "ACEEFLG4",
    "ACEEAPLV",
    "ACEETRLV",
    "ACEETRDA",
    "ACEETRID",
    "ACEEAMP",
    "ACEECLTH",
    "ACEECLCP",
    "ACEEAPTR",
    "ACEEAPLN",
    "ACEEAPDA",
    "ACEEUNAM",
    "ACEEMDLS",
    "ACEECGRP",
    "ACEEGATA",
    "ACEEFCGP",
    "ACEEDSLP",
    "ACEEDAT4",
    "ACEEPADS",
    "ACEESLVL",
    "ACEEFLG5",
    "ACEEFLG6",
    "ACEERSV1",
    "ACEE3PTY",
    "ACEEPLCL",
    "ACEESUID",
    "ACEEOCOX",
    "ACEEPTDS",
    "ACEEX5PR",
    "ACEETOKP",
    "ACEESRVA",
    "ACEESRVP",
    "ACEENSTA",
    "ACEEICTX",
    "ACEEIDID",
    "ACEETIME",
)

acee_offset_length = (
    info(0,4),  # ACEEACEE
    info(4,4),  # ACEECORE
    info(8,1),  # ACEEVRSN
    info(9,3),  # ACEESBVR
    info(12,4),  # ACEEIEP
    info(16,4),  # ACEEINST
    info(20,1),  # ACEEUSRL
    info(21,8),  # ACEEUSRI
    info(29,1),  # ACEEGRPL
    info(30,8),  # ACEEGRPN
    info(38,1),  # ACEEFLG1
    info(39,1),  # ACEEFLG2
    info(40,1),  # ACEEFLG3
    info(41,3),  # ACEEDATE
    info(44,8),  # ACEEPROC
    info(52,4),  # ACEETRMP
    info(56,2),  # ACEEFLG4
    info(58,1),  # ACEEAPLV
    info(59,1),  # ACEETRLV
    info(60,4),  # ACEETRDA
    info(64,8),  # ACEETRID
    info(72,4),  # ACEEAMP
    info(76,4),  # ACEECLTH
    info(80,4),  # ACEECLCP
    info(84,4),  # ACEEAPTR
    info(88,8),  # ACEEAPLN
    info(96,4),  # ACEEAPDA
    info(100,4),  # ACEEUNAM
    info(104,4),  # ACEEMDLS
    info(108,4),  # ACEECGRP
    info(112,4),  # ACEEGATA
    info(116,4),  # ACEEFCGP
    info(120,4),  # ACEEDSLP
    info(124,4),  # ACEEDAT4
    info(128,4),  # ACEEPADS
    info(132,1),  # ACEESLVL
    info(133,1),  # ACEEFLG5
    info(134,1),  # ACEEFLG6
    info(135,1),  # ACEERSV1
    info(136,4),  # ACEE3PTY
    info(140,4),  # ACEEPLCL
    info(144,8),  # ACEESUID
    info(152,4),  # ACEEOCOX
    info(156,4),  # ACEEPTDS
    info(160,4),  # ACEEX5PR
    info(164,4),  # ACEETOKP
    info(168,4),  # ACEESRVA
    info(172,4),  # ACEESRVP
    info(176,4),  # ACEENSTA
    info(180,4),  # ACEEICTX
    info(184,4),  # ACEEIDID
    info(188,4),  # ACEETIME
)

acee_fields = namedtuple("acee", acee_field_names)
acee_info = acee_fields._make(acee_offset_length)


def get_acee_address() -> int:
    address_buffer = bytearray(4)
    read_memory(address_buffer, len(address_buffer), 548)
    address_ascb = int.from_bytes(address_buffer, byteorder='big')
    read_memory(address_buffer, len(address_buffer), address_ascb + 108)
    address_asxb = int.from_bytes(address_buffer, byteorder='big')
    read_memory(address_buffer, len(address_buffer), address_asxb + 200)
    address = int.from_bytes(address_buffer, byteorder='big')
    return address


def get_acee(address: int | None) -> bytearray:
    buffer = bytearray(acee_pattern.size)
    read_memory(buffer, len(buffer), address or get_acee_address())
    return buffer


class ACEE:
    name = "ACEE"
    long_name = "Accessor Environment Element"
    fields = acee_field_names
    info = acee_info
    def __init__(self, address):
        content = acee_fields._make(acee_pattern.unpack(get_acee(address)))
        self.content = content