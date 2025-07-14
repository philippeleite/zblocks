from app.models.base import info
from app.utils import read_memory
from struct import Struct
from collections import namedtuple

tcb_pattern = Struct(
    ">"
    "4s"  # TCBRBP
    "4s"  # TCBPIE
    "4s"  # TCBDEB
    "4s"  # TCBTIO
    "4s"  # TCBCMP
    "4s"  # TCBTRN
    "4s"  # TCBMSS
    "1s"  # TCBPKF
    "5s"  # TCBFLGS
    "1s"  # TCBLMP
    "1s"  # TCBDSP
    "4s"  # TCBLLS
    "4s"  # TCBJLB
    "4s"  # TCBJPQ
    "4s"  # TCBGRS0
    "4s"  # TCBGRS1
    "4s"  # TCBGRS2
    "4s"  # TCBGRS3
    "4s"  # TCBGRS4
    "4s"  # TCBGRS5
    "4s"  # TCBGRS6
    "4s"  # TCBGRS7
    "4s"  # TCBGRS8
    "4s"  # TCBGRS9
    "4s"  # TCBGRS10
    "4s"  # TCBGRS11
    "4s"  # TCBGRS12
    "4s"  # TCBGRS13
    "4s"  # TCBGRS14
    "4s"  # TCBGRS15
    "4s"  # TCBFSA
    "4s"  # TCBTCB
    "4s"  # TCBTME
    "4s"  # TCBJSTCB
    "4s"  # TCBNTC
    "4s"  # TCBOTC
    "4s"  # TCBLTC
    "4s"  # TCBIQE
    "4s"  # TCBECB
    "1s"  # TCBTSFLG
    "1s"  # TCBSTPCT
    "1s"  # TCBTSLP
    "1s"  # TCBTSDP
    "4s"  # TCBRD
    "4s"  # TCBAE
    "4s"  # TCBSTAB
    "4s"  # TCBTCT
    "4s"  # TCBUSER
    "4s"  # TCBSCNDY
    "4s"  # TCBMDIDS
    "4s"  # TCBJSCB
    "4s"  # TCBSSAT
    "4s"  # TCBIOBRC
    "4s"  # TCBEXCPD
    "4s"  # TCBEXT1
    "4s"  # TCBBITS
    "1s"  # TCBDAR
    "1s"  # TCBRSV37
    "1s"  # TCBSYSCT
    "1s"  # TCBSTMCT
    "4s"  # TCBEXT2
    "4s"  # TCBR0D4
    "4s"  # TCBXSB
    "4s"  # TCBBACK
    "4s"  # TCBRTWA
    "4s"  # TCBNSSP
    "4s"  # TCBXLAS
    "1s"  # TCBABCUR
    "1s"  # TCBFJMCT
    "1s"  # TCBTID
    "1s"  # TCBFLGS8
    "4s"  # TCBXSCT
    "4s"  # TCBFOE
    "4s"  # TCBSWA
    "4s"  # TCBSTAWA
    "4s"  # TCBTCBID
    "4s"  # TCBRTM12
    "4s"  # TCBESTAE
    "4s"  # TCBUKYSP
    "2s"  # TCBPROPF
    "2s"  # TCBAFFN
    "1s"  # TCBFBYT1
    "1s"  # TCBFBYT2
    "1s"  # TCBFBYT3
    "1s"  # TCBFBYT4
    "4s"  # TCBRPT
    "4s"  # TCBVAT
    "4s"  # TCBSWASA
    "4s"  # TCBSVCA2
    "4s"  # TCBERD
    "4s"  # TCBEAE
    "4s"  # TCBARC
    "4s"  # TCBGRES
    "4s"  # TCBSTCB
    "8s"  # TCBTTIME
    "4s"  # TCBCELAP
    "2s"  # TCBR148
    "1s"  # TCBRBYT1
    "1s"  # TCBLEVEL
    "4s"  # TCBBDT
    "4s"  # TCBNDAXP
    "4s"  # TCBSENV
)

tcb_field_names = (
    "TCBRBP",
    "TCBPIE",
    "TCBDEB",
    "TCBTIO",
    "TCBCMP",
    "TCBTRN",
    "TCBMSS",
    "TCBPKF",
    "TCBFLGS",
    "TCBLMP",
    "TCBDSP",
    "TCBLLS",
    "TCBJLB",
    "TCBJPQ",
    "TCBGRS0",
    "TCBGRS1",
    "TCBGRS2",
    "TCBGRS3",
    "TCBGRS4",
    "TCBGRS5",
    "TCBGRS6",
    "TCBGRS7",
    "TCBGRS8",
    "TCBGRS9",
    "TCBGRS10",
    "TCBGRS11",
    "TCBGRS12",
    "TCBGRS13",
    "TCBGRS14",
    "TCBGRS15",
    "TCBFSA",
    "TCBTCB",
    "TCBTME",
    "TCBJSTCB",
    "TCBNTC",
    "TCBOTC",
    "TCBLTC",
    "TCBIQE",
    "TCBECB",
    "TCBTSFLG",
    "TCBSTPCT",
    "TCBTSLP",
    "TCBTSDP",
    "TCBRD",
    "TCBAE",
    "TCBSTAB",
    "TCBTCT",
    "TCBUSER",
    "TCBSCNDY",
    "TCBMDIDS",
    "TCBJSCB",
    "TCBSSAT",
    "TCBIOBRC",
    "TCBEXCPD",
    "TCBEXT1",
    "TCBBITS",
    "TCBDAR",
    "TCBRSV37",
    "TCBSYSCT",
    "TCBSTMCT",
    "TCBEXT2",
    "TCBR0D4",
    "TCBXSB",
    "TCBBACK",
    "TCBRTWA",
    "TCBNSSP",
    "TCBXLAS",
    "TCBABCUR",
    "TCBFJMCT",
    "TCBTID",
    "TCBFLGS8",
    "TCBXSCT",
    "TCBFOE",
    "TCBSWA",
    "TCBSTAWA",
    "TCBTCBID",
    "TCBRTM12",
    "TCBESTAE",
    "TCBUKYSP",
    "TCBPROPF",
    "TCBAFFN",
    "TCBFBYT1",
    "TCBFBYT2",
    "TCBFBYT3",
    "TCBFBYT4",
    "TCBRPT",
    "TCBVAT",
    "TCBSWASA",
    "TCBSVCA2",
    "TCBERD",
    "TCBEAE",
    "TCBARC",
    "TCBGRES",
    "TCBSTCB",
    "TCBTTIME",
    "TCBCELAP",
    "TCBR148",
    "TCBRBYT1",
    "TCBLEVEL",
    "TCBBDT",
    "TCBNDAXP",
    "TCBSENV",
)

tcb_offset_length = (
    info(0,4),  # TCBRBP
    info(4,4),  # TCBPIE
    info(8,4),  # TCBDEB
    info(12,4),  # TCBTIO
    info(16,4),  # TCBCMP
    info(20,4),  # TCBTRN
    info(24,4),  # TCBMSS
    info(28,1),  # TCBPKF
    info(29,5),  # TCBFLGS
    info(34,1),  # TCBLMP
    info(35,1),  # TCBDSP
    info(36,4),  # TCBLLS
    info(40,4),  # TCBJLB
    info(44,4),  # TCBJPQ
    info(48,4),  # TCBGRS0
    info(52,4),  # TCBGRS1
    info(56,4),  # TCBGRS2
    info(60,4),  # TCBGRS3
    info(64,4),  # TCBGRS4
    info(68,4),  # TCBGRS5
    info(72,4),  # TCBGRS6
    info(76,4),  # TCBGRS7
    info(80,4),  # TCBGRS8
    info(84,4),  # TCBGRS9
    info(88,4),  # TCBGRS10
    info(92,4),  # TCBGRS11
    info(96,4),  # TCBGRS12
    info(100,4),  # TCBGRS13
    info(104,4),  # TCBGRS14
    info(108,4),  # TCBGRS15
    info(112,4),  # TCBFSA
    info(116,4),  # TCBTCB
    info(120,4),  # TCBTME
    info(124,4),  # TCBJSTCB
    info(128,4),  # TCBNTC
    info(132,4),  # TCBOTC
    info(136,4),  # TCBLTC
    info(140,4),  # TCBIQE
    info(144,4),  # TCBECB
    info(148,1),  # TCBTSFLG
    info(149,1),  # TCBSTPCT
    info(150,1),  # TCBTSLP
    info(151,1),  # TCBTSDP
    info(152,4),  # TCBRD
    info(156,4),  # TCBAE
    info(160,4),  # TCBSTAB
    info(164,4),  # TCBTCT
    info(168,4),  # TCBUSER
    info(172,4),  # TCBSCNDY
    info(176,4),  # TCBMDIDS
    info(180,4),  # TCBJSCB
    info(184,4),  # TCBSSAT
    info(188,4),  # TCBIOBRC
    info(192,4),  # TCBEXCPD
    info(196,4),  # TCBEXT1
    info(200,4),  # TCBBITS
    info(204,1),  # TCBDAR
    info(205,1),  # TCBRSV37
    info(206,1),  # TCBSYSCT
    info(207,1),  # TCBSTMCT
    info(208,4),  # TCBEXT2
    info(212,4),  # TCBR0D4
    info(216,4),  # TCBXSB
    info(220,4),  # TCBBACK
    info(224,4),  # TCBRTWA
    info(228,4),  # TCBNSSP
    info(232,4),  # TCBXLAS
    info(236,1),  # TCBABCUR
    info(237,1),  # TCBFJMCT
    info(238,1),  # TCBTID
    info(239,1),  # TCBFLGS8
    info(240,4),  # TCBXSCT
    info(244,4),  # TCBFOE
    info(248,4),  # TCBSWA
    info(252,4),  # TCBSTAWA
    info(256,4),  # TCBTCBID
    info(260,4),  # TCBRTM12
    info(264,4),  # TCBESTAE
    info(268,4),  # TCBUKYSP
    info(272,2),  # TCBPROPF
    info(274,2),  # TCBAFFN
    info(276,1),  # TCBFBYT1
    info(277,1),  # TCBFBYT2
    info(278,1),  # TCBFBYT3
    info(279,1),  # TCBFBYT4
    info(280,4),  # TCBRPT
    info(284,4),  # TCBVAT
    info(288,4),  # TCBSWASA
    info(292,4),  # TCBSVCA2
    info(296,4),  # TCBERD
    info(300,4),  # TCBEAE
    info(304,4),  # TCBARC
    info(308,4),  # TCBGRES
    info(312,4),  # TCBSTCB
    info(316,8),  # TCBTTIME
    info(324,4),  # TCBCELAP
    info(328,2),  # TCBR148
    info(330,1),  # TCBRBYT1
    info(331,1),  # TCBLEVEL
    info(332,4),  # TCBBDT
    info(336,4),  # TCBNDAXP
    info(340,4),  # TCBSENV
)

tcb_fields = namedtuple("tcb", tcb_field_names)
tcb_info = tcb_fields._make(tcb_offset_length)


def get_tcb(address: int) -> bytearray:
    buffer = bytearray(tcb_pattern.size)
    read_memory(buffer, len(buffer), address)
    return buffer


class TCB:
    name = "TCB"
    long_name = "Task Control Block"
    fields = tcb_field_names
    info = tcb_info
    def __init__(self, address):
        content = tcb_fields._make(tcb_pattern.unpack(get_tcb(address)))
        self.content = content