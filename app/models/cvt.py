from app.models.base import Field
from app.utils import read_memory
from struct import unpack, Struct

cvt_pattern = Struct(
    ">"
    "4s"     # CVTTCBP
    "4s"     # CVT0EF00
    "4s"     # CVTLINK
    "4s"     # CVTAUSCB
    "4s"     # CVTBUF
    "4s"     # CVTXAPG
    "4s"     # CVT0VL00
    "4s"     # CVTPCNVT
    "4s"     # CVTPRLVT
    "4s"     # CVTLLCB
    "4s"     # CVTLLTRM
    "4s"     # CVTXTLER
    "4s"     # CVTSYSAD
    "4s"     # CVTBTERM
    "4s"     # CVTDATE
    "4s"     # CVTMSLT
    "4s"     # CVTZDTAB
    "4s"     # CVTXITP
    "4s"     # CVT0EF01
    "2s"     # CVTVSS
    "2s"     # CVTVPSM
    "2s"     # CVTEXIT
    "2s"     # CVTBRET
    "4s"     # CVTSVDCB
    "4s"     # CVTTPC
    "s"      # CVTFLGC0
    "s"      # CVTFLGC1
    "2s"     # CVTICPID
    "4s"     # CVTCVT
    "4s"     # CVTCUCB
)

class CVT:
    def __init__(self):
        cvt_address_buffer = bytearray(4)
        read_memory(cvt_address_buffer, len(cvt_address_buffer), int("10", 16))
        cvt_address = int.from_bytes(cvt_address_buffer, byteorder='big')
        cvt_buffer = bytearray(1280)
        read_memory(cvt_buffer, len(cvt_buffer), cvt_address)

        self.fields: list[Field] = []
        cvt = cvt_pattern.unpack(cvt_buffer)