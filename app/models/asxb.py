from app.models.base import info, zblocks_list
from app.utils import read_memory
from struct import Struct
from collections import namedtuple

zblocks_list.append('ASXB')

asxb_pattern = Struct(
    ">"
    "4s"  # ASXBASXB
    "4s"  # ASXBFTCB
    "4s"  # ASXBLTCB
    "2s"  # ASXBTCBS
    "1s"  # ASXBFLG1
    "1s"  # ASXBSCHD
    "4s"  # ASXBMPST
    "4s"  # ASXBLWA
    "4s"  # ASXBVFVT
    "4s"  # ASXBSAF
    "4s"  # ASXBIHSA
    "72s"  # ASXBFLSA
    "4s"  # ASXBOMCB
    "4s"  # ASXBSPSA
    "4s"  # ASXBRSMD
    "4s"  # ASXBRCTD
    "4s"  # ASXBDECB
    "4s"  # ASXBOUSB
    "4s"  # ASXBCRWK
    "16s"  # ASXBPRG
    "8s"  # ASXBPSWD
    "4s"  # ASXBSIRB
    "4s"  # ASXBETSK
    "4s"  # ASXBFIQE
    "4s"  # ASXBLIQE
    "4s"  # ASXBFRQE
    "4s"  # ASXBLRQE
    "4s"  # ASXBFSRB
    "4s"  # ASXBLSRB
    "8s"  # ASXBUSR8
    "4s"  # ASXBSENV
    "4s"  # ASXBSFRS
    "4s"  # ASXBNSSA_PREZOS11
    "4s"  # ASXBNSCT_PREZOS11
    "4s"  # ASXBCASW
    "4s"  # ASXBPT0E
    "4s"  # ASXBCAPC
    "4s"  # ASXBJSVT
    "4s"  # ASXBDIVW
    "4s"  # ASXBCAPT
    "4s"  # ASXBLINF
    "4s"  # ASXBPIRL
    "4s"  # ASXBITCB
    "4s"  # ASXBRZVP
    "4s"  # ASXBGRSP
    "4s"  # ASXBVASB
    "8s"  # ASXBALEC
    "8s"  # ASXBR110
    "4s"  # ASXBEXTA
    "4s"  # ASXBAXRL
    "8s"  # ASXB_MAPREQ_ADDR
    "4s"  # ASXBLCPI
    "4s"  # ASXBTCBPMEPOOLID
    "8s"  # ASXBCMTM
    "4s"  # ASXBCNZCPID
    "4s"  # ASXB_NOABDUMP
    "16s"  # ASXBDIAG140
    "176s"  # ASXBR150
    "4s"  # ASXBNSSA
    "4s"  # ASXBNSCT
    "248s"  # ASXBR208
)

asxb_field_names = (
    "ASXBASXB",
    "ASXBFTCB",
    "ASXBLTCB",
    "ASXBTCBS",
    "ASXBFLG1",
    "ASXBSCHD",
    "ASXBMPST",
    "ASXBLWA",
    "ASXBVFVT",
    "ASXBSAF",
    "ASXBIHSA",
    "ASXBFLSA",
    "ASXBOMCB",
    "ASXBSPSA",
    "ASXBRSMD",
    "ASXBRCTD",
    "ASXBDECB",
    "ASXBOUSB",
    "ASXBCRWK",
    "ASXBPRG",
    "ASXBPSWD",
    "ASXBSIRB",
    "ASXBETSK",
    "ASXBFIQE",
    "ASXBLIQE",
    "ASXBFRQE",
    "ASXBLRQE",
    "ASXBFSRB",
    "ASXBLSRB",
    "ASXBUSR8",
    "ASXBSENV",
    "ASXBSFRS",
    "ASXBNSSA_PREZOS11",
    "ASXBNSCT_PREZOS11",
    "ASXBCASW",
    "ASXBPT0E",
    "ASXBCAPC",
    "ASXBJSVT",
    "ASXBDIVW",
    "ASXBCAPT",
    "ASXBLINF",
    "ASXBPIRL",
    "ASXBITCB",
    "ASXBRZVP",
    "ASXBGRSP",
    "ASXBVASB",
    "ASXBALEC",
    "ASXBR110",
    "ASXBEXTA",
    "ASXBAXRL",
    "ASXB_MAPREQ_ADDR",
    "ASXBLCPI",
    "ASXBTCBPMEPOOLID",
    "ASXBCMTM",
    "ASXBCNZCPID",
    "ASXB_NOABDUMP",
    "ASXBDIAG140",
    "ASXBR150",
    "ASXBNSSA",
    "ASXBNSCT",
    "ASXBR208",
)

asxb_offset_length = (
    info(0,4),  # ASXBASXB
    info(4,4),  # ASXBFTCB
    info(8,4),  # ASXBLTCB
    info(12,2),  # ASXBTCBS
    info(14,1),  # ASXBFLG1
    info(15,1),  # ASXBSCHD
    info(16,4),  # ASXBMPST
    info(20,4),  # ASXBLWA
    info(24,4),  # ASXBVFVT
    info(28,4),  # ASXBSAF
    info(32,4),  # ASXBIHSA
    info(36,72),  # ASXBFLSA
    info(108,4),  # ASXBOMCB
    info(112,4),  # ASXBSPSA
    info(116,4),  # ASXBRSMD
    info(120,4),  # ASXBRCTD
    info(124,4),  # ASXBDECB
    info(128,4),  # ASXBOUSB
    info(132,4),  # ASXBCRWK
    info(136,16),  # ASXBPRG
    info(152,8),  # ASXBPSWD
    info(160,4),  # ASXBSIRB
    info(164,4),  # ASXBETSK
    info(168,4),  # ASXBFIQE
    info(172,4),  # ASXBLIQE
    info(176,4),  # ASXBFRQE
    info(180,4),  # ASXBLRQE
    info(184,4),  # ASXBFSRB
    info(188,4),  # ASXBLSRB
    info(192,8),  # ASXBUSR8
    info(200,4),  # ASXBSENV
    info(204,4),  # ASXBSFRS
    info(208,4),  # ASXBNSSA_PREZOS11
    info(212,4),  # ASXBNSCT_PREZOS11
    info(216,4),  # ASXBCASW
    info(220,4),  # ASXBPT0E
    info(224,4),  # ASXBCAPC
    info(228,4),  # ASXBJSVT
    info(232,4),  # ASXBDIVW
    info(236,4),  # ASXBCAPT
    info(240,4),  # ASXBLINF
    info(244,4),  # ASXBPIRL
    info(248,4),  # ASXBITCB
    info(252,4),  # ASXBRZVP
    info(256,4),  # ASXBGRSP
    info(260,4),  # ASXBVASB
    info(264,8),  # ASXBALEC
    info(272,8),  # ASXBR110
    info(280,4),  # ASXBEXTA
    info(284,4),  # ASXBAXRL
    info(288,8),  # ASXB_MAPREQ_ADDR
    info(296,4),  # ASXBLCPI
    info(300,4),  # ASXBTCBPMEPOOLID
    info(304,8),  # ASXBCMTM
    info(312,4),  # ASXBCNZCPID
    info(316,4),  # ASXB_NOABDUMP
    info(320,16),  # ASXBDIAG140
    info(336,176),  # ASXBR150
    info(512,4),  # ASXBNSSA
    info(516,4),  # ASXBNSCT
    info(520,248),  # ASXBR208
)

asxb_fields = namedtuple("assb", asxb_field_names)
asxb_info = asxb_fields._make(asxb_offset_length)


def get_asxb_address() -> int:
    address_buffer = bytearray(4)
    read_memory(address_buffer, len(address_buffer), 548)
    address_ascb = int.from_bytes(address_buffer, byteorder='big')
    read_memory(address_buffer, len(address_buffer), address_ascb + 108)
    address = int.from_bytes(address_buffer, byteorder='big')
    return address


def get_asxb(address: int | None) -> bytearray:
    buffer = bytearray(asxb_pattern.size)
    read_memory(buffer, len(buffer), address or get_asxb_address())
    return buffer


class ASXB:
    name = "ASXB"
    long_name = "Address Space Extension Block"
    fields = asxb_field_names
    info = asxb_info
    def __init__(self, address):
        content = asxb_fields._make(asxb_pattern.unpack(get_asxb(address)))
        self.content = content