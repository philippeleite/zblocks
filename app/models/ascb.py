from app.models.base import info, zblocks_list
from app.utils import read_memory
from struct import Struct
from collections import namedtuple

zblocks_list.append('ASCB')

ascb_pattern = Struct(
    ">"
    "4s"  # ASCBASCB
    "4s"  # ASCBFWDP
    "4s"  # ASCBBWDP
    "4s"  # ASCBLTCS
    "4s"  # ASCBSVRB_PREZOS12
    "4s"  # ASCBSYNC_PREZOS12
    "4s"  # ASCBIOSP
    "4s"  # ASCBWQLK
    "4s"  # ASCBSAWQ_PREZOS11
    "2s"  # ASCBASID
    "1s"  # ASCBDIAG026
    "1s"  # ASCBSRMFLAGS
    "1s"  # ASCBLL5
    "1s"  # ASCBHLHI
    "2s"  # ASCBDPH
    "4s"  # ASCBTCBE
    "4s"  # ASCBLDA
    "1s"  # ASCBRSMF
    "1s"  # ASCBFLG3
    "2s"  # ASCBHASI_PREZOS11
    "4s"  # ASCBCSCB
    "4s"  # ASCBTSB
    "8s"  # ASCBEJST
    "8s"  # ASCBEWST
    "4s"  # ASCBJSTL
    "4s"  # ASCBECB
    "4s"  # ASCBUBET
    "4s"  # ASCBTLCH
    "4s"  # ASCBDUMP
    "4s"  # ASCBFW1
    "4s"  # ASCBTMCH
    "4s"  # ASCBASXB
    "4s"  # ASCBFW2
    "4s"  # ASCBSCNT
    "4s"  # ASCBLLWQ
    "4s"  # ASCBRCTP
    "4s"  # ASCBLOCK
    "4s"  # ASCBLSWQ
    "4s"  # ASCBQECB
    "4s"  # ASCBMECB
    "4s"  # ASCBOUCB
    "4s"  # ASCBOUXB
    "4s"  # ASCBFW2A
    "4s"  # ASCBEJST_DISPS
    "4s"  # ASCBIQEA
    "4s"  # ASCBRTMC
    "4s"  # ASCBMCC
    "4s"  # ASCBJBNI
    "4s"  # ASCBJBNS
    "4s"  # ASCBSRQ
    "4s"  # ASCBVGTT
    "4s"  # ASCBPCTT
    "2s"  # ASCBSSRB
    "1s"  # ASCBSMCT
    "1s"  # ASCBSRBM
    "4s"  # ASCBSWTL
    "8s"  # ASCBSRBT
    "4s"  # ASCBLTCB
    "4s"  # ASCBLTCN
    "4s"  # ASCBTCBS
    "4s"  # ASCBLSQT
    "4s"  # ASCBWPRB
    "4s"  # ASCBSRDP
    "4s"  # ASCBLOCI
    "4s"  # ASCBCMLW
    "4s"  # ASCBSRBT_DISPS
    "4s"  # ASCBSSOM
    "4s"  # ASCBASTE
    "4s"  # ASCBLTOV
    "4s"  # ASCBATOV
    "2s"  # ASCBETC
    "2s"  # ASCBETCN
    "2s"  # ASCBLXR
    "2s"  # ASCBAXR
    "4s"  # ASCBSTKH
    "4s"  # ASCBCSWD
    "4s"  # ASCBR114
    "4s"  # ASCBJAFBADDR
    "4s"  # ASCBXTCB
    "4s"  # ASCBFW3
    "4s"  # ASCBGXL
    "8s"  # ASCBEATT
    "8s"  # ASCBINTS
    "4s"  # ASCBFW4
    "4s"  # ASCBRCMS
    "4s"  # ASCBIOSC
    "2s"  # ASCBPKML
    "2s"  # ASCBXCNT
    "4s"  # ASCBNSQA
    "4s"  # ASCBASM
    "4s"  # ASCBASSB
    "4s"  # ASCBTCME
    "4s"  # ASCBGQIR
    "4s"  # ASCBLSQE
    "8s"  # ASCBIOSX
    "2s"  # ASCBR168
    "2s"  # ASCBSVCN
    "4s"  # ASCBRSME
    "4s"  # ASCBAVM
    "4s"  # ASCBARC
    "4s"  # ASCBRSM
    "4s"  # ASCBDCTI
)
ascb_field_names = (
    "ASCBASCB",
    "ASCBFWDP",
    "ASCBBWDP",
    "ASCBLTCS",
    "ASCBSVRB_PREZOS12",
    "ASCBSYNC_PREZOS12",
    "ASCBIOSP",
    "ASCBWQLK",
    "ASCBSAWQ_PREZOS11",
    "ASCBASID",
    "ASCBDIAG026",
    "ASCBSRMFLAGS",
    "ASCBLL5",
    "ASCBHLHI",
    "ASCBDPH",
    "ASCBTCBE",
    "ASCBLDA",
    "ASCBRSMF",
    "ASCBFLG3",
    "ASCBHASI_PREZOS11",
    "ASCBCSCB",
    "ASCBTSB",
    "ASCBEJST",
    "ASCBEWST",
    "ASCBJSTL",
    "ASCBECB",
    "ASCBUBET",
    "ASCBTLCH",
    "ASCBDUMP",
    "ASCBFW1",
    "ASCBTMCH",
    "ASCBASXB",
    "ASCBFW2",
    "ASCBSCNT",
    "ASCBLLWQ",
    "ASCBRCTP",
    "ASCBLOCK",
    "ASCBLSWQ",
    "ASCBQECB",
    "ASCBMECB",
    "ASCBOUCB",
    "ASCBOUXB",
    "ASCBFW2A",
    "ASCBEJST_DISPS",
    "ASCBIQEA",
    "ASCBRTMC",
    "ASCBMCC",
    "ASCBJBNI",
    "ASCBJBNS",
    "ASCBSRQ",
    "ASCBVGTT",
    "ASCBPCTT",
    "ASCBSSRB",
    "ASCBSMCT",
    "ASCBSRBM",
    "ASCBSWTL",
    "ASCBSRBT",
    "ASCBLTCB",
    "ASCBLTCN",
    "ASCBTCBS",
    "ASCBLSQT",
    "ASCBWPRB",
    "ASCBSRDP",
    "ASCBLOCI",
    "ASCBCMLW",
    "ASCBSRBT_DISPS",
    "ASCBSSOM",
    "ASCBASTE",
    "ASCBLTOV",
    "ASCBATOV",
    "ASCBETC",
    "ASCBETCN",
    "ASCBLXR",
    "ASCBAXR",
    "ASCBSTKH",
    "ASCBCSWD",
    "ASCBR114",
    "ASCBJAFBADDR",
    "ASCBXTCB",
    "ASCBFW3",
    "ASCBGXL",
    "ASCBEATT",
    "ASCBINTS",
    "ASCBFW4",
    "ASCBRCMS",
    "ASCBIOSC",
    "ASCBPKML",
    "ASCBXCNT",
    "ASCBNSQA",
    "ASCBASM",
    "ASCBASSB",
    "ASCBTCME",
    "ASCBGQIR",
    "ASCBLSQE",
    "ASCBIOSX",
    "ASCBR168",
    "ASCBSVCN",
    "ASCBRSME",
    "ASCBAVM",
    "ASCBARC",
    "ASCBRSM",
    "ASCBDCTI",
)
ascb_offset_length = (
    info(0,4),  # ASCBASCB
    info(4,4),  # ASCBFWDP
    info(8,4),  # ASCBBWDP
    info(12,4),  # ASCBLTCS
    info(16,4),  # ASCBSVRB_PREZOS12
    info(20,4),  # ASCBSYNC_PREZOS12
    info(24,4),  # ASCBIOSP
    info(28,4),  # ASCBWQLK
    info(32,4),  # ASCBSAWQ_PREZOS11
    info(36,2),  # ASCBASID
    info(38,1),  # ASCBDIAG026
    info(39,1),  # ASCBSRMFLAGS
    info(40,1),  # ASCBLL5
    info(41,1),  # ASCBHLHI
    info(42,2),  # ASCBDPH
    info(44,4),  # ASCBTCBE
    info(48,4),  # ASCBLDA
    info(52,1),  # ASCBRSMF
    info(53,1),  # ASCBFLG3
    info(54,2),  # ASCBHASI_PREZOS11
    info(56,4),  # ASCBCSCB
    info(60,4),  # ASCBTSB
    info(64,8),  # ASCBEJST
    info(72,8),  # ASCBEWST
    info(80,4),  # ASCBJSTL
    info(84,4),  # ASCBECB
    info(88,4),  # ASCBUBET
    info(92,4),  # ASCBTLCH
    info(96,4),  # ASCBDUMP
    info(100,4),  # ASCBFW1
    info(104,4),  # ASCBTMCH
    info(108,4),  # ASCBASXB
    info(112,4),  # ASCBFW2
    info(116,4),  # ASCBSCNT
    info(120,4),  # ASCBLLWQ
    info(124,4),  # ASCBRCTP
    info(128,4),  # ASCBLOCK
    info(132,4),  # ASCBLSWQ
    info(136,4),  # ASCBQECB
    info(140,4),  # ASCBMECB
    info(144,4),  # ASCBOUCB
    info(148,4),  # ASCBOUXB
    info(152,4),  # ASCBFW2A
    info(156,4),  # ASCBEJST_DISPS
    info(160,4),  # ASCBIQEA
    info(164,4),  # ASCBRTMC
    info(168,4),  # ASCBMCC
    info(172,4),  # ASCBJBNI
    info(176,4),  # ASCBJBNS
    info(180,4),  # ASCBSRQ
    info(184,4),  # ASCBVGTT
    info(188,4),  # ASCBPCTT
    info(192,2),  # ASCBSSRB
    info(194,1),  # ASCBSMCT
    info(195,1),  # ASCBSRBM
    info(196,4),  # ASCBSWTL
    info(200,8),  # ASCBSRBT
    info(208,4),  # ASCBLTCB
    info(212,4),  # ASCBLTCN
    info(216,4),  # ASCBTCBS
    info(220,4),  # ASCBLSQT
    info(224,4),  # ASCBWPRB
    info(228,4),  # ASCBSRDP
    info(232,4),  # ASCBLOCI
    info(236,4),  # ASCBCMLW
    info(240,4),  # ASCBSRBT_DISPS
    info(244,4),  # ASCBSSOM
    info(248,4),  # ASCBASTE
    info(252,4),  # ASCBLTOV
    info(256,4),  # ASCBATOV
    info(260,2),  # ASCBETC
    info(262,2),  # ASCBETCN
    info(264,2),  # ASCBLXR
    info(266,2),  # ASCBAXR
    info(268,4),  # ASCBSTKH
    info(272,4),  # ASCBCSWD
    info(276,4),  # ASCBR114
    info(280,4),  # ASCBJAFBADDR
    info(284,4),  # ASCBXTCB
    info(288,4),  # ASCBFW3
    info(292,4),  # ASCBGXL
    info(296,8),  # ASCBEATT
    info(304,8),  # ASCBINTS
    info(312,4),  # ASCBFW4
    info(316,4),  # ASCBRCMS
    info(320,4),  # ASCBIOSC
    info(324,2),  # ASCBPKML
    info(326,2),  # ASCBXCNT
    info(328,4),  # ASCBNSQA
    info(332,4),  # ASCBASM
    info(336,4),  # ASCBASSB
    info(340,4),  # ASCBTCME
    info(344,4),  # ASCBGQIR
    info(348,4),  # ASCBLSQE
    info(352,8),  # ASCBIOSX
    info(360,2),  # ASCBR168
    info(362,2),  # ASCBSVCN
    info(364,4),  # ASCBRSME
    info(368,4),  # ASCBAVM
    info(372,4),  # ASCBARC
    info(376,4),  # ASCBRSM
    info(380,4),  # ASCBDCTI
)

ascb_fields = namedtuple("cvt", ascb_field_names)
ascb_info = ascb_fields._make(ascb_offset_length)


def get_ascb_address() -> int:
    address_buffer = bytearray(4)
    read_memory(address_buffer, len(address_buffer), 548)
    address = int.from_bytes(address_buffer, byteorder='big')
    return address


def get_ascb(address: int | None) -> bytearray:
    buffer = bytearray(ascb_pattern.size)
    # address = address or get_ascb_address()
    read_memory(buffer, len(buffer), address or get_ascb_address())
    return buffer


class ASCB:
    name = "ASCB"
    long_name = "Address Space Control Block"
    fields = ascb_field_names
    info = ascb_info
    def __init__(self, address):
        content = ascb_fields._make(ascb_pattern.unpack(get_ascb(address)))
        self.content = content
