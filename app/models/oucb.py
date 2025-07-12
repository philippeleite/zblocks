from app.models.base import info, zblocks_list
from app.utils import read_memory
from struct import Struct
from collections import namedtuple

zblocks_list.append('OUCB')

oucb_pattern = Struct(
    ">"
    "4s"  # OUCBNAME
    "4s"  # OUCBFWD
    "4s"  # OUCBBCK
    "4s"  # OUCBTMA
    "1s"  # OUCBQFL
    "1s"  # OUCBSFL
    "1s"  # OUCBYFL
    "1s"  # OUCBAFL
    "1s"  # OUCBTFL
    "1s"  # OUCBEFL
    "1s"  # OUCBASSTATUS
    "1s"  # OUCBUFL
    "1s"  # OUCBLFL
    "1s"  # OUCBRFL
    "1s"  # OUCBNDP
    "1s"  # OUCBTNDP
    "1s"  # OUCBMFL
    "1s"  # OUCBIAC
    "1s"  # OUCBRSV1
    "1s"  # OUCBPGP
    "2s"  # OUCBWSCI
    "2s"  # OUCBWRCI
    "1s"  # OUCBMFL2
    "1s"  # OUCBMFL3
    "2s"  # OUCBDMO
    "1s"  # OUCBDMN
    "1s"  # OUCBSRC
    "2s"  # OUCBSWC
    "4s"  # OUCBASCB
    "4s"  # OUCBPAGP
    "4s"  # OUCBTMW
    "4s"  # OUCBWMS
    "4s"  # OUCBCPU
    "4s"  # OUCBIOC
    "4s"  # OUCBMSO
    "4s"  # OUCBTMS
    "4s"  # OUCBTMO
    "4s"  # OUCBDRFR
    "4s"  # OUCBACT
    "2s"  # OUCBACN
    "1s"  # OUCBCFL
    "1s"  # OUCBCSBT
    "4s"  # OUCBCMRV
    "4s"  # OUCBWMRL
    "2s"  # OUCBVAL
    "1s"  # OUCBPFL
    "1s"  # OUCBACTL
    "8s"  # OUCBIOCL
    "1s"  # OUCBDSPC
    "1s"  # OUCBDSPN
    "2s"  # OUCBNTSP
    "8s"  # OUCBPSS
    "4s"  # OUCBPST
    "4s"  # OUCBRCT
    "4s"  # OUCBIIT
    "2s"  # OUCBNDS
    "1s"  # OUCBNTSG
    "1s"  # OUCBRSV2
    "4s"  # OUCBTME
    "4s"  # OUCBTML
    "4s"  # OUCBDWMS
    "4s"  # OUCBSRB
    "4s"  # OUCBTWSS
    "4s"  # OUCBTMP
    "4s"  # OUCBDLYT
    "4s"  # OUCBHST
    "4s"  # OUCBCFS
    "4s"  # OUCBSUBN
    "2s"  # OUCBRPG
    "2s"  # OUCBSPG
    "2s"  # OUCBNPG
    "2s"  # OUCBSRPG
    "2s"  # OUCBNRPG
    "2s"  # OUCBURPG
    "2s"  # OUCBCRPG
    "2s"  # OUCBARPG
    "4s"  # OUCBDRFP
    "8s"  # OUCBTRXN
    "8s"  # OUCBUSRD
    "8s"  # OUCBCLS
    "4s"  # OUCBTRS
    "4s"  # OUCBTRR
    "4s"  # OUCBACTP
    "4s"  # OUCBSWSS
    "4s"  # OUCBPSUM
    "2s"  # OUCBFIXB
    "1s"  # OUCBAPLV
    "1s"  # OUCBESAP
    "8s"  # OUCBRST
)

oucb_field_names = (
    "OUCBNAME",
    "OUCBFWD",
    "OUCBBCK",
    "OUCBTMA",
    "OUCBQFL",
    "OUCBSFL",
    "OUCBYFL",
    "OUCBAFL",
    "OUCBTFL",
    "OUCBEFL",
    "OUCBASSTATUS",
    "OUCBUFL",
    "OUCBLFL",
    "OUCBRFL",
    "OUCBNDP",
    "OUCBTNDP",
    "OUCBMFL",
    "OUCBIAC",
    "OUCBRSV1",
    "OUCBPGP",
    "OUCBWSCI",
    "OUCBWRCI",
    "OUCBMFL2",
    "OUCBMFL3",
    "OUCBDMO",
    "OUCBDMN",
    "OUCBSRC",
    "OUCBSWC",
    "OUCBASCB",
    "OUCBPAGP",
    "OUCBTMW",
    "OUCBWMS",
    "OUCBCPU",
    "OUCBIOC",
    "OUCBMSO",
    "OUCBTMS",
    "OUCBTMO",
    "OUCBDRFR",
    "OUCBACT",
    "OUCBACN",
    "OUCBCFL",
    "OUCBCSBT",
    "OUCBCMRV",
    "OUCBWMRL",
    "OUCBVAL",
    "OUCBPFL",
    "OUCBACTL",
    "OUCBIOCL",
    "OUCBDSPC",
    "OUCBDSPN",
    "OUCBNTSP",
    "OUCBPSS",
    "OUCBPST",
    "OUCBRCT",
    "OUCBIIT",
    "OUCBNDS",
    "OUCBNTSG",
    "OUCBRSV2",
    "OUCBTME",
    "OUCBTML",
    "OUCBDWMS",
    "OUCBSRB",
    "OUCBTWSS",
    "OUCBTMP",
    "OUCBDLYT",
    "OUCBHST",
    "OUCBCFS",
    "OUCBSUBN",
    "OUCBRPG",
    "OUCBSPG",
    "OUCBNPG",
    "OUCBSRPG",
    "OUCBNRPG",
    "OUCBURPG",
    "OUCBCRPG",
    "OUCBARPG",
    "OUCBDRFP",
    "OUCBTRXN",
    "OUCBUSRD",
    "OUCBCLS",
    "OUCBTRS",
    "OUCBTRR",
    "OUCBACTP",
    "OUCBSWSS",
    "OUCBPSUM",
    "OUCBFIXB",
    "OUCBAPLV",
    "OUCBESAP",
    "OUCBRST",
)

oucb_offset_length = (
    info(0,4),  # OUCBNAME
    info(4,4),  # OUCBFWD
    info(8,4),  # OUCBBCK
    info(12,4),  # OUCBTMA
    info(16,1),  # OUCBQFL
    info(17,1),  # OUCBSFL
    info(18,1),  # OUCBYFL
    info(19,1),  # OUCBAFL
    info(20,1),  # OUCBTFL
    info(21,1),  # OUCBEFL
    info(22,1),  # OUCBASSTATUS
    info(23,1),  # OUCBUFL
    info(24,1),  # OUCBLFL
    info(25,1),  # OUCBRFL
    info(26,1),  # OUCBNDP
    info(27,1),  # OUCBTNDP
    info(28,1),  # OUCBMFL
    info(29,1),  # OUCBIAC
    info(30,1),  # OUCBRSV1
    info(31,1),  # OUCBPGP
    info(32,2),  # OUCBWSCI
    info(34,2),  # OUCBWRCI
    info(36,1),  # OUCBMFL2
    info(37,1),  # OUCBMFL3
    info(38,2),  # OUCBDMO
    info(40,1),  # OUCBDMN
    info(41,1),  # OUCBSRC
    info(42,2),  # OUCBSWC
    info(44,4),  # OUCBASCB
    info(48,4),  # OUCBPAGP
    info(52,4),  # OUCBTMW
    info(56,4),  # OUCBWMS
    info(60,4),  # OUCBCPU
    info(64,4),  # OUCBIOC
    info(68,4),  # OUCBMSO
    info(72,4),  # OUCBTMS
    info(76,4),  # OUCBTMO
    info(80,4),  # OUCBDRFR
    info(84,4),  # OUCBACT
    info(88,2),  # OUCBACN
    info(90,1),  # OUCBCFL
    info(91,1),  # OUCBCSBT
    info(92,4),  # OUCBCMRV
    info(96,4),  # OUCBWMRL
    info(100,2),  # OUCBVAL
    info(102,1),  # OUCBPFL
    info(103,1),  # OUCBACTL
    info(104,8),  # OUCBIOCL
    info(112,1),  # OUCBDSPC
    info(113,1),  # OUCBDSPN
    info(114,2),  # OUCBNTSP
    info(116,8),  # OUCBPSS
    info(124,4),  # OUCBPST
    info(128,4),  # OUCBRCT
    info(132,4),  # OUCBIIT
    info(136,2),  # OUCBNDS
    info(138,1),  # OUCBNTSG
    info(139,1),  # OUCBRSV2
    info(140,4),  # OUCBTME
    info(144,4),  # OUCBTML
    info(148,4),  # OUCBDWMS
    info(152,4),  # OUCBSRB
    info(156,4),  # OUCBTWSS
    info(160,4),  # OUCBTMP
    info(164,4),  # OUCBDLYT
    info(168,4),  # OUCBHST
    info(172,4),  # OUCBCFS
    info(176,4),  # OUCBSUBN
    info(180,2),  # OUCBRPG
    info(182,2),  # OUCBSPG
    info(184,2),  # OUCBNPG
    info(186,2),  # OUCBSRPG
    info(188,2),  # OUCBNRPG
    info(190,2),  # OUCBURPG
    info(192,2),  # OUCBCRPG
    info(194,2),  # OUCBARPG
    info(196,4),  # OUCBDRFP
    info(200,8),  # OUCBTRXN
    info(208,8),  # OUCBUSRD
    info(216,8),  # OUCBCLS
    info(224,4),  # OUCBTRS
    info(228,4),  # OUCBTRR
    info(232,4),  # OUCBACTP
    info(236,4),  # OUCBSWSS
    info(240,4),  # OUCBPSUM
    info(244,2),  # OUCBFIXB
    info(246,1),  # OUCBAPLV
    info(247,1),  # OUCBESAP
    info(248,8),  # OUCBRST
)

oucb_fields = namedtuple("oucb", oucb_field_names)
oucb_info = oucb_fields._make(oucb_offset_length)


def get_oucb_address() -> int:
    address_buffer = bytearray(4)
    read_memory(address_buffer, len(address_buffer), 548)
    address_ascb = int.from_bytes(address_buffer, byteorder='big')
    read_memory(address_buffer, len(address_buffer), address_ascb + 144)
    address = int.from_bytes(address_buffer, byteorder='big')
    return address


def get_oucb(address: int | None) -> bytearray:
    buffer = bytearray(oucb_pattern.size)
    read_memory(buffer, len(buffer), address or get_oucb_address())
    return buffer


class OUCB:
    name = "OUCB"
    long_name = "Resources Manager User Control Block"
    fields = oucb_field_names
    info = oucb_info
    def __init__(self, address):
        content = oucb_fields._make(oucb_pattern.unpack(get_oucb(address)))
        self.content = content