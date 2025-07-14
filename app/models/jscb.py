xxxx_pattern = Struct(
    ">"
    "4s"  # JSCRSV01
    "4s"  # JSCHPCE(0)
    "1s"  # JSCRSV32
    "3s"  # JSCHPCEA
    "4s"  # JSCBSHR
    "4s"  # JSCBTCP
    "4s"  # JSCBPCC
    "4s"  # JSCBTCBP
    "4s"  # JSCBIJSC
    "4s"  # JSCBDBTB
    "4s"  # JSCBID
    "4s"  # JSCBDCB(0)
    "1s"  # JSCRSV02
    "3s"  # JSCBDCBA
    "1s"  # JSCBSTEP
    "3s"  # JSCRSV03
    "4s"  # JSCBSECB
    "1s"  # JSCBOPTS
    "6s"  # JSCBCRB6
    "1s"  # JSCBSWT1
    "4s"  # JSCBQMPI
    "4s"  # JSCBJESW
    "4s"  # JSCBWTP(0)
    "1s"  # JSCBWTFG
    "1s"  # JSCBWTSP
    "2s"  # JSCBPMG
    "4s"  # JSCBCSCB
    "4s"  # JSCBJCT(0)
    "1s"  # JSCRSV24
    "3s"  # JSCJCTP(0)
    "3s"  # JSCBJCTA
    "4s"  # JSCBPSCB
    "2s"  # JSCBASID(0)
    "2s"  # JSCBTJID
    "1s"  # JSCBFBYT
    "1s"  # JSCBRV08
    "4s"  # JSCBIECB
    "8s"  # JSCBJRBA
    "4s"  # JSCBALOC
    "4s"  # JSCBJNL(0)
    "1s"  # JSCBJJSB
    "3s"  # JSCBJNLA
    "4s"  # JSCBJNLR
    "4s"  # JSCBSMLR
    "4s"  # JSCBSUB(0)
    "1s"  # JSCRSV31
    "3s"  # JSCBSUBA
    "2s"  # JSCBSONO
    "2s"  # JSCBCRB2
    "8s"  # JSCBFRBA
    "4s"  # JSCBSSIB
    "4s"  # JSCDSABQ
    "4s"  # JSCGDDNO
    "4s"  # JSCSCT(0)
    "1s"  # JSCRSV55
    "3s"  # JSCSCTP
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
    "8s"  # JSCBPGMN(0)
    "4s"  # JSCBECB1
    "4s"  # JSCBECB2
    "4s"  # JSCDSNQP
    "4s"  # JSCBCSCX
    "4s"  # JSCAMCPL
)
xxxx_field_names = (
    "JSCRSV01",
    "JSCHPCE(0)",
    "JSCRSV32",
    "JSCHPCEA",
    "JSCBSHR",
    "JSCBTCP",
    "JSCBPCC",
    "JSCBTCBP",
    "JSCBIJSC",
    "JSCBDBTB",
    "JSCBID",
    "JSCBDCB(0)",
    "JSCRSV02",
    "JSCBDCBA",
    "JSCBSTEP",
    "JSCRSV03",
    "JSCBSECB",
    "JSCBOPTS",
    "JSCBCRB6",
    "JSCBSWT1",
    "JSCBQMPI",
    "JSCBJESW",
    "JSCBWTP(0)",
    "JSCBWTFG",
    "JSCBWTSP",
    "JSCBPMG",
    "JSCBCSCB",
    "JSCBJCT(0)",
    "JSCRSV24",
    "JSCJCTP(0)",
    "JSCBJCTA",
    "JSCBPSCB",
    "JSCBASID(0)",
    "JSCBTJID",
    "JSCBFBYT",
    "JSCBRV08",
    "JSCBIECB",
    "JSCBJRBA",
    "JSCBALOC",
    "JSCBJNL(0)",
    "JSCBJJSB",
    "JSCBJNLA",
    "JSCBJNLR",
    "JSCBSMLR",
    "JSCBSUB(0)",
    "JSCRSV31",
    "JSCBSUBA",
    "JSCBSONO",
    "JSCBCRB2",
    "JSCBFRBA",
    "JSCBSSIB",
    "JSCDSABQ",
    "JSCGDDNO",
    "JSCSCT(0)",
    "JSCRSV55",
    "JSCSCTP",
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
    "JSCBPGMN(0)",
    "JSCBECB1",
    "JSCBECB2",
    "JSCDSNQP",
    "JSCBCSCX",
    "JSCAMCPL",
)
xxxx_offset_length = (
    info(188,4),  # JSCRSV01
    info(192,4),  # JSCHPCE(0)
    info(192,1),  # JSCRSV32
    info(193,3),  # JSCHPCEA
    info(196,4),  # JSCBSHR
    info(200,4),  # JSCBTCP
    info(204,4),  # JSCBPCC
    info(208,4),  # JSCBTCBP
    info(212,4),  # JSCBIJSC
    info(216,4),  # JSCBDBTB
    info(220,4),  # JSCBID
    info(224,4),  # JSCBDCB(0)
    info(224,1),  # JSCRSV02
    info(225,3),  # JSCBDCBA
    info(228,1),  # JSCBSTEP
    info(229,3),  # JSCRSV03
    info(232,4),  # JSCBSECB
    info(236,1),  # JSCBOPTS
    info(237,6),  # JSCBCRB6
    info(243,1),  # JSCBSWT1
    info(244,4),  # JSCBQMPI
    info(248,4),  # JSCBJESW
    info(252,4),  # JSCBWTP(0)
    info(252,1),  # JSCBWTFG
    info(253,1),  # JSCBWTSP
    info(254,2),  # JSCBPMG
    info(256,4),  # JSCBCSCB
    info(260,4),  # JSCBJCT(0)
    info(260,1),  # JSCRSV24
    info(261,3),  # JSCJCTP(0)
    info(261,3),  # JSCBJCTA
    info(264,4),  # JSCBPSCB
    info(268,2),  # JSCBASID(0)
    info(268,2),  # JSCBTJID
    info(270,1),  # JSCBFBYT
    info(271,1),  # JSCBRV08
    info(272,4),  # JSCBIECB
    info(276,8),  # JSCBJRBA
    info(284,4),  # JSCBALOC
    info(288,4),  # JSCBJNL(0)
    info(288,1),  # JSCBJJSB
    info(289,3),  # JSCBJNLA
    info(292,4),  # JSCBJNLR
    info(296,4),  # JSCBSMLR
    info(300,4),  # JSCBSUB(0)
    info(300,1),  # JSCRSV31
    info(301,3),  # JSCBSUBA
    info(304,2),  # JSCBSONO
    info(306,2),  # JSCBCRB2
    info(308,8),  # JSCBFRBA
    info(316,4),  # JSCBSSIB
    info(320,4),  # JSCDSABQ
    info(324,4),  # JSCGDDNO
    info(328,4),  # JSCSCT(0)
    info(328,1),  # JSCRSV55
    info(329,3),  # JSCSCTP
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
    info(360,8),  # JSCBPGMN(0)
    info(360,4),  # JSCBECB1
    info(364,4),  # JSCBECB2
    info(368,4),  # JSCDSNQP
    info(372,4),  # JSCBCSCX
    info(376,4),  # JSCAMCPL
)
