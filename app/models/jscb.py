from app.models.base import info
from app.utils import read_memory
from struct import Struct
from collections import namedtuple

jscb_pattern = Struct(
    ">"
    "188s" # JSCBRSV0
    "4s"  # JSCRSV01
    "4s"  # JSCHPCE
    "4s"  # JSCBSHR
    "4s"  # JSCBTCP
    "4s"  # JSCBPCC
    "4s"  # JSCBTCBP
    "4s"  # JSCBIJSC
    "4s"  # JSCBDBTB
    "4s"  # JSCBID
    "4s"  # JSCBDCB
    "1s"  # JSCBSTEP
    "3s"  # JSCRSV03
    "4s"  # JSCBSECB
    "1s"  # JSCBOPTS
    "6s"  # JSCBCRB6
    "1s"  # JSCBSWT1
    "4s"  # JSCBQMPI
    "4s"  # JSCBJESW
    "4s"  # JSCBWTP
    "4s"  # JSCBCSCB
    "4s"  # JSCBJCT
    "4s"  # JSCBPSCB
    "2s"  # JSCBTJID
    "1s"  # JSCBFBYT
    "1s"  # JSCBRV08
    "4s"  # JSCBIECB
    "8s"  # JSCBJRBA
    "4s"  # JSCBALOC
    "4s"  # JSCBJNL
    "4s"  # JSCBJNLR
    "4s"  # JSCBSMLR
    "4s"  # JSCBSUB
    "2s"  # JSCBSONO
    "2s"  # JSCBCRB2
    "8s"  # JSCBFRBA
    "4s"  # JSCBSSIB
    "4s"  # JSCDSABQ
    "4s"  # JSCGDDNO
    "4s"  # JSCSCT
    "4s"  # JSCTMCOR
    "4s"  # JSCBVATA
    "2s"  # JSCRSV08
    "2s"  # JSCBODNO
    "2s"  # JSCDDNUM
    "1s"  # JSCRSV33
    "1s"  # JSCBSWSP
    "4s"  # JSCBACT
    "4s"  # JSCRSV09
    "4s"  # JSCBEACB
    "8s"  # JSCBPGMN
    "4s"  # JSCDSNQP
    "4s"  # JSCBCSCX
    "4s"  # JSCAMCPL
)

jscb_field_names = (
    "JSCBRSV0",
    "JSCRSV01",
    "JSCHPCE",
    "JSCBSHR",
    "JSCBTCP",
    "JSCBPCC",
    "JSCBTCBP",
    "JSCBIJSC",
    "JSCBDBTB",
    "JSCBID",
    "JSCBDCB",
    "JSCBSTEP",
    "JSCRSV03",
    "JSCBSECB",
    "JSCBOPTS",
    "JSCBCRB6",
    "JSCBSWT1",
    "JSCBQMPI",
    "JSCBJESW",
    "JSCBWTP",
    "JSCBCSCB",
    "JSCBJCT",
    "JSCBPSCB",
    "JSCBTJID",
    "JSCBFBYT",
    "JSCBRV08",
    "JSCBIECB",
    "JSCBJRBA",
    "JSCBALOC",
    "JSCBJNL",
    "JSCBJNLR",
    "JSCBSMLR",
    "JSCBSUB",
    "JSCBSONO",
    "JSCBCRB2",
    "JSCBFRBA",
    "JSCBSSIB",
    "JSCDSABQ",
    "JSCGDDNO",
    "JSCSCT",
    "JSCTMCOR",
    "JSCBVATA",
    "JSCRSV08",
    "JSCBODNO",
    "JSCDDNUM",
    "JSCRSV33",
    "JSCBSWSP",
    "JSCBACT",
    "JSCRSV09",
    "JSCBEACB",
    "JSCBPGMN",
    "JSCDSNQP",
    "JSCBCSCX",
    "JSCAMCPL",
)

jscb_offset_length = (
    info(0,188),  # JSCBRSV0
    info(188,4),  # JSCRSV01
    info(192,4),  # JSCHPCE
    info(196,4),  # JSCBSHR
    info(200,4),  # JSCBTCP
    info(204,4),  # JSCBPCC
    info(208,4),  # JSCBTCBP
    info(212,4),  # JSCBIJSC
    info(216,4),  # JSCBDBTB
    info(220,4),  # JSCBID
    info(224,4),  # JSCBDCB
    info(228,1),  # JSCBSTEP
    info(229,3),  # JSCRSV03
    info(232,4),  # JSCBSECB
    info(236,1),  # JSCBOPTS
    info(237,6),  # JSCBCRB6
    info(243,1),  # JSCBSWT1
    info(244,4),  # JSCBQMPI
    info(248,4),  # JSCBJESW
    info(252,4),  # JSCBWTP
    info(256,4),  # JSCBCSCB
    info(260,4),  # JSCBJCT
    info(264,4),  # JSCBPSCB
    info(268,2),  # JSCBTJID
    info(270,1),  # JSCBFBYT
    info(271,1),  # JSCBRV08
    info(272,4),  # JSCBIECB
    info(276,8),  # JSCBJRBA
    info(284,4),  # JSCBALOC
    info(288,4),  # JSCBJNL
    info(292,4),  # JSCBJNLR
    info(296,4),  # JSCBSMLR
    info(300,4),  # JSCBSUB
    info(304,2),  # JSCBSONO
    info(306,2),  # JSCBCRB2
    info(308,8),  # JSCBFRBA
    info(316,4),  # JSCBSSIB
    info(320,4),  # JSCDSABQ
    info(324,4),  # JSCGDDNO
    info(328,4),  # JSCSCT
    info(332,4),  # JSCTMCOR
    info(336,4),  # JSCBVATA
    info(340,2),  # JSCRSV08
    info(342,2),  # JSCBODNO
    info(344,2),  # JSCDDNUM
    info(346,1),  # JSCRSV33
    info(347,1),  # JSCBSWSP
    info(348,4),  # JSCBACT
    info(352,4),  # JSCRSV09
    info(356,4),  # JSCBEACB
    info(360,8),  # JSCBPGMN
    info(368,4),  # JSCDSNQP
    info(372,4),  # JSCBCSCX
    info(376,4),  # JSCAMCPL
)

jscb_fields = namedtuple("jscb", jscb_field_names)
jscb_info = jscb_fields._make(jscb_offset_length)


def get_jscb(address: int) -> bytearray:
    buffer = bytearray(jscb_pattern.size)
    read_memory(buffer, len(buffer), address)
    return buffer


class JSCB:
    name = "JSCB"
    long_name = "Job/Step Control Block"
    fields = jscb_field_names
    info = jscb_info
    def __init__(self, address):
        content = jscb_fields._make(jscb_pattern.unpack(get_jscb(address)))
        self.content = content