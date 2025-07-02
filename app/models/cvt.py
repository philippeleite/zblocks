from app.models.base import info, zblocks_list
from app.utils import read_memory
from struct import Struct
from collections import namedtuple

zblocks_list.append('CVT')

cvt_pattern = Struct(
    ">"
    "4s"  # CVTTCBP
    "4s"  # CVT0EF00
    "4s"  # CVTLINK
    "4s"  # CVTAUSCB
    "4s"  # CVTBUF
    "4s"  # CVTXAPG
    "4s"  # CVT0VL00
    "4s"  # CVTPCNVT
    "4s"  # CVTPRLVT
    "4s"  # CVTLLCB
    "4s"  # CVTLLTRM
    "4s"  # CVTXTLER
    "4s"  # CVTSYSAD
    "4s"  # CVTBTERM
    "4s"  # CVTDATE
    "4s"  # CVTMSLT
    "4s"  # CVTZDTAB
    "4s"  # CVTXITP
    "4s"  # CVT0EF01
    "4s"  # CVTVPRM
    "2s"  # CVTEXIT
    "2s"  # CVTBRET
    "4s"  # CVTSVDCB
    "4s"  # CVTTPC
    "4s"  # CVTFLGCS
    "4s"  # CVTCVT
    "4s"  # CVTCUCB
)

cvt_field_names = (
    "CVTTCBP",
    "CVT0EF00",
    "CVTLINK",
    "CVTAUSCB",
    "CVTBUF",
    "CVTXAPG",
    "CVT0VL00",
    "CVTPCNVT",
    "CVTPRLVT",
    "CVTLLCB",
    "CVTLLTRM",
    "CVTXTLER",
    "CVTSYSAD",
    "CVTBTERM",
    "CVTDATE",
    "CVTMSLT",
    "CVTZDTAB",
    "CVTXITP",
    "CVT0EF01",
    "CVTVPRM",
    "CVTEXIT",
    "CVTBRET",
    "CVTSVDCB",
    "CVTTPC",
    "CVTFLGCS",
    "CVTCVT",
    "CVTCUCB",
)

cvt_offset_length = (
    info(0, 4),  # CVTTCBP
    info(4, 4),  # CVT0EF00
    info(8, 4),  # CVTLINK
    info(12, 4),  # CVTAUSCB
    info(16, 4),  # CVTBUF
    info(20, 4),  # CVTXAPG
    info(24, 4),  # CVT0VL00
    info(28, 4),  # CVTPCNVT
    info(32, 4),  # CVTPRLTV
    info(36, 4),  # CVTLLCB
    info(40, 4),  # CVTLLTRM
    info(44, 4),  # CVTXTLER
    info(48, 4),  # CVTSYSAD
    info(52, 4),  # CVTBTERM
    info(56, 4),  # CVTDATE
    info(60, 4),  # CVTMSLT
    info(64, 4),  # CVTZDTAB
    info(68, 4),  # CVTXITP
    info(72, 4),  # CVT0EF01
    info(76, 4),  # CVTVPRM
    info(80, 2),  # CVTEXIT
    info(82, 2),  # CVTBRET
    info(84, 4),  # CVTSVDCB
    info(88, 4),  # CVTTPC
    info(92, 4),  # CVTFLGCS
    info(96, 4),  # CVTCVT
    info(100, 4),  # CVTCUCB
)

cvt_fields = namedtuple("cvt", cvt_field_names)
cvt_info = cvt_fields._make(cvt_offset_length)


def get_cvt_address() -> int:
    cvt_address_buffer = bytearray(4)
    read_memory(cvt_address_buffer, len(cvt_address_buffer), int("10", 16))
    cvt_address = int.from_bytes(cvt_address_buffer, byteorder='big')
    return cvt_address


def get_cvt() -> bytearray:
    cvt_buffer = bytearray(cvt_pattern.size)
    cvt_address = get_cvt_address()
    read_memory(cvt_buffer, len(cvt_buffer), cvt_address)
    return cvt_buffer


class CVT:
    def __init__(self):
        self.name = "CVT"
        self.long_name = "Communications Vector Table"
        self.fields = cvt_field_names
        self.info = cvt_info._asdict()
        content = cvt_fields._make(cvt_pattern.unpack(get_cvt()))
        self.content = content._asdict()
