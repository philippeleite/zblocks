from app.models.base import info, zblocks_list
from app.utils import read_memory
from struct import Struct
from collections import namedtuple

zblocks_list.append('ASSB')

assb_pattern = Struct(
    ">"
    "4s"  # ASSBASSB
    "4s"  # ASSBSMFL
    "4s"  # ASSBUBAV
    "4s"  # ASSBUBAD
    "4s"  # ASSBUPAV
    "4s"  # ASSBR014
    "1s"  # ASSBXMF1
    "1s"  # ASSBXMF2
    "2s"  # ASSBXMCC
    "4s"  # ASSBCBTP
    "4s"  # ASSBVSC
    "4s"  # ASSBNVSC
    "4s"  # ASSBASRR
    "4s"  # ASSBDEXP
    "4s"  # ASSBSTW1
    "4s"  # ASSBISQN
    "4s"  # ASSBBPSA
    "4s"  # ASSBCSCT
    "4s"  # ASSBBALV
    "4s"  # ASSBBALD
    "4s"  # ASSBXMSE
    "4s"  # ASSBTSQN
    "4s"  # ASSBVCNT
    "4s"  # ASSBPALV
    "4s"  # ASSBASEI
    "4s"  # ASSBRMA
    "8s"  # ASSBHST
    "8s"  # ASSBIIPT
    "4s"  # ASSBANEC
    "4s"  # ASSBSDOV
    "4s"  # ASSBMCSO
    "4s"  # ASSBDFAS
    "4s"  # ASSBFLGS
    "4s"  # ASSBASCB
    "4s"  # ASSBASRF
    "4s"  # ASSBASRB
    "4s"  # ASSBSSD
    "4s"  # ASSBMQMA
    "8s"  # ASSBLASB
    "4s"  # ASSBSCH
    "4s"  # ASSBFSC
    "4s"  # ASSBJSAB
    "4s"  # ASSBRCTW
    "4s"  # ASSBLDXH
    "4s"  # ASSBLDXL
    "4s"  # ASSBTLMI
    "4s"  # ASSBSDAS
    "4s"  # ASSBTPIN
    "4s"  # ASSBSPIN
    "4s"  # ASSBECT1
    "4s"  # ASSBECT2
    "4s"  # ASSBMT#
    "4s"  # ASSBDFP
    "2s"  # ASSBSASI
    "2s"  # ASSBSNEW
    "4s"  # ASSBNTTP
    "4s"  # ASSBOECB
    "4s"  # ASSBOASB
    "4s"  # ASSBXSBA
    "4s"  # ASSBDLCB
    "4s"  # ASSBVAB
    "4s"  # ASSBLMAB
    "4s"  # ASSBIOCT
    "4s"  # ASSBCTT
    "4s"  # ASSBXRCT
    "4s"  # ASSB_NONENCT_PSRB_CP_DISPS
    "4s"  # ASSBTASB
    "4s"  # ASSBTPMA
    "4s"  # ASSBROSU
    "4s"  # ASSBTPMT
    "4s"  # ASSBSSDT
    "4s"  # ASSBTAWQ
    "4s"  # ASSBWCML
    "4s"  # ASSBWS3S
    "4s"  # ASSBWSSS
    "4s"  # ASSBCAPQ
    "4s"  # ASSBPTAR
    "4s"  # ASSBWTCT
    "4s"  # ASSBSBCT
    "4s"  # ASSBARBP
    "4s"  # ASSBRCTR
    "4s"  # ASSBSCAH
    "1s"  # ASSBTTFL
    "1s"  # ASSBWMF1
    "2s"  # ASSBPSWC
    "4s"  # ASSBIXGA
    "8s"  # ASSBJBNI
    "8s"  # ASSBJBNS
    "8s"  # ASSBASST
    "8s"  # ASSBPHTM
    "4s"  # ASSBCRWQ
    "4s"  # ASSBSCWQ
    "4s"  # ASSBLCNT
    "4s"  # ASSBACNT
    "4s"  # ASSBLCPD
    "4s"  # ASSBSLSC
    "4s"  # ASSBPVTC
    "4s"  # ASSBCTX
    "16s"  # ASSBHALE
    "4s"  # ASSB_TIME_ON_ZAAP_DISPS
    "4s"  # ASSBSRSN
    "4s"  # ASSBWLMS
    "4s"  # ASSBBCBA
    "4s"  # ASSBCSM
    "4s"  # ASSBPECT
    "4s"  # ASSBRRSA
    "2s"  # ASSBOFLG
    "2s"  # ASSBSCAF
    "4s"  # ASSBCTXC
    "4s"  # ASSBRMCT
    "4s"  # ASSBLRBA
    "4s"  # ASSBSLFA
    "1s"  # ASSBPFIDASSIGNCNT
    "1s"  # ASSBFABRICPRIORITY
    "2s"  # ASSBIOMS
    "2s"  # ASSBPROMOTIONCOUNT
    "1s"  # ASSBTIOP
    "1s"  # ASSBCSDP
    "8s"  # ASSB_TIME_IFA_ON_CP
    "8s"  # ASSB_TIME_ON_IFA
    "8s"  # ASSB_TIME_ON_CP
    "5s"  # ASSBMTCI
    "1s"  # ASSBFLG4
    "1s"  # ASSBQIOP
    "1s"  # ASSBCRYP
    "8s"  # ASSBPHTM_BASE
    "4s"  # ASSBEARLYMEMTERMRM
    "4s"  # ASSB_LAA_CPID
    "8s"  # ASSB_IFA_PHTM
    "4s"  # ASSB_TIME_ON_ZIIP_DISPS
    "4s"  # ASSB_ZIIP_ENCT_DISPS
    "4s"  # ASSB_NONENCT_PSRB_ZAAP_DISPS
    "4s"  # ASSB_NONENCT_PSRB_ZIIP_DISPS
    "8s"  # ASSB_BASE_PHTM
    "8s"  # ASSB_IFA_BASE_PHTM
    "8s"  # ASSB_BASE_ENCT
    "8s"  # ASSB_IFA_BASE_ENCT
    "4s"  # ASSB_CP_AFFINITY_NODE
    "4s"  # ASSB_IFA_AFFINITY_NODE
    "4s"  # ASSB_SUP_AFFINITY_NODE
    "4s"  # ASSBSRBCPOOLPMECOUNT
    "8s"  # ASSB_TIME_ON_SUP
    "8s"  # ASSB_TIME_SUP_ON_CP
    "8s"  # ASSB_SUP_PHTM
    "8s"  # ASSB_SRB_TIME_ON_CP
    "8s"  # ASSB_SUP_ENCT
    "8s"  # ASSB_IFA_ON_CP_ENCT
    "4s"  # ASSBSOWN
    "4s"  # ASSBSOWT
    "8s"  # ASSB_IFA_ON_CP_BASE_ENCT
    "8s"  # ASSB_TIME_AT_PDP
    "8s"  # ASSB_SRBT_BASE
    "4s"  # ASSBCASC
    "4s"  # ASSBNUMBERUNAUTHPETS
    "8s"  # ASSB_ASST_TIME_ON_CP
    "8s"  # ASSB_SWITCH_TO_ZAAPZIIP_COUNT
    "8s"  # ASSBASAB
    "8s"  # ASSB_SUP_BASE_ENCT
    "8s"  # ASSB_SUP_ON_CP_ENCT
    "8s"  # ASSB_SUP_ON_CP_BASE_ENCT
    "4s"  # ASSBRMIN
    "4s"  # ASSBRTMA
    "8s"  # ASSB_HDLOCKPROMOTION_TIME_AT_PDP
    "4s"  # ASSB_SMFCMS_LOCKINST_ADDR
    "4s"  # ASSB_ENQDEQ_CMS_LOCKINST_ADDR
    "4s"  # ASSB_LATCH_CMS_LOCKINST_ADDR
    "4s"  # ASSB_CMS_LOCKINST_ADDR
    "4s"  # ASSB_LOCAL_LOCKINST_ADDR
    "4s"  # ASSB_HDLOCKPROMOTE_DISPS
    "4s"  # ASSBSAWQ
    "252s"  # ASSBR304
    "4s"  # ASSBHREQ
    "2s"  # ASSBHASI
    "250s"  # ASSBR406
    "8s"  # ASSB_ENCT
    "4s"  # ASSB_ENCT_DISPS
    "4s"  # ASSB_ENCT_HDLOCKPROMOTE_DISPS
    "8s"  # ASSB_ENCT_HDLOCKPROMOTE_TIME
    "232s"  # ASSBR518
    "8s"  # ASSB_IFA_ENCT
    "4s"  # ASSB_ZAAP_ENCT_DISPS
    "4s"  # ASSBBROKENUP_SEQNUM
    "160s"  # ASSBDIAG610
    "8s"  # ASSB_CCB_REALADDR
    "8s"  # ASSB_AICB_REALADDR
    "16s"  # ASSBR6C0
    "8s"  # ASSB_AICB_VIRTADDR
    "8s"  # ASSB_CRYPCTRS_VIRTADDR
    "8s"  # ASSB_NNPICTRS_VIRTADDR
    "8s"  # ASSB_SRB_TIME_ON_ZCBP
    "8s"  # ASSB_ASST_TIME_ON_ZCBP
    "4s"  # ASSB_SRB_TIME_ON_ZCBP_DISPS
    "4s"  # ASSB_ASST_TIME_ON_ZCBP_DISPS
    "4s"  # ASSBETSC
    "252s"  # ASSBR704
    "4s"  # ASSBCMLC
    "4s"  # ASSBR804
    "4s"  # ASSBSVRB
    "4s"  # ASSBSYNC
    "240s"  # ASSBR810
    "8s"  # ASSB_VARTIME_AT_PDP
    "8s"  # ASSB_VARWEIGHTED_TIME_AT_PDP
    "8s"  # ASSB_HCWA
    "8s"  # ASSB_SCMBC
    "8s"  # ASSB_ZIIP_PHTM_BASE
    "4s"  # ASSB_MAJORS_PREEMPTED
    "4s"  # ASSB_MINORS_PREEMPTED
    "8s"  # ASSBINITIATORJOBID
    "4s"  # ASSBINITIATORSEQNUM
    "4s"  # ASSBR93C
    "112s"  # ASSBDIAG940
    "8s"  # ASSB_TIME_JAVA_ON_ZIIP
    "8s"  # ASSB_TIME_JAVA_ON_CP
)
assb_field_names = (
    "ASSBASSB",
    "ASSBSMFL",
    "ASSBUBAV",
    "ASSBUBAD",
    "ASSBUPAV",
    "ASSBR014",
    "ASSBXMF1",
    "ASSBXMF2",
    "ASSBXMCC",
    "ASSBCBTP",
    "ASSBVSC",
    "ASSBNVSC",
    "ASSBASRR",
    "ASSBDEXP",
    "ASSBSTW1",
    "ASSBISQN",
    "ASSBBPSA",
    "ASSBCSCT",
    "ASSBBALV",
    "ASSBBALD",
    "ASSBXMSE",
    "ASSBTSQN",
    "ASSBVCNT",
    "ASSBPALV",
    "ASSBASEI",
    "ASSBRMA",
    "ASSBHST",
    "ASSBIIPT",
    "ASSBANEC",
    "ASSBSDOV",
    "ASSBMCSO",
    "ASSBDFAS",
    "ASSBFLGS",
    "ASSBASCB",
    "ASSBASRF",
    "ASSBASRB",
    "ASSBSSD",
    "ASSBMQMA",
    "ASSBLASB",
    "ASSBSCH",
    "ASSBFSC",
    "ASSBJSAB",
    "ASSBRCTW",
    "ASSBLDXH",
    "ASSBLDXL",
    "ASSBTLMI",
    "ASSBSDAS",
    "ASSBTPIN",
    "ASSBSPIN",
    "ASSBECT1",
    "ASSBECT2",
    "ASSBMT#",
    "ASSBDFP",
    "ASSBSASI",
    "ASSBSNEW",
    "ASSBNTTP",
    "ASSBOECB",
    "ASSBOASB",
    "ASSBXSBA",
    "ASSBDLCB",
    "ASSBVAB",
    "ASSBLMAB",
    "ASSBIOCT",
    "ASSBCTT",
    "ASSBXRCT",
    "ASSB_NONENCT_PSRB_CP_DISPS",
    "ASSBTASB",
    "ASSBTPMA",
    "ASSBROSU",
    "ASSBTPMT",
    "ASSBSSDT",
    "ASSBTAWQ",
    "ASSBWCML",
    "ASSBWS3S",
    "ASSBWSSS",
    "ASSBCAPQ",
    "ASSBPTAR",
    "ASSBWTCT",
    "ASSBSBCT",
    "ASSBARBP",
    "ASSBRCTR",
    "ASSBSCAH",
    "ASSBTTFL",
    "ASSBWMF1",
    "ASSBPSWC",
    "ASSBIXGA",
    "ASSBJBNI",
    "ASSBJBNS",
    "ASSBASST",
    "ASSBPHTM",
    "ASSBCRWQ",
    "ASSBSCWQ",
    "ASSBLCNT",
    "ASSBACNT",
    "ASSBLCPD",
    "ASSBSLSC",
    "ASSBPVTC",
    "ASSBCTX",
    "ASSBHALE",
    "ASSB_TIME_ON_ZAAP_DISPS",
    "ASSBSRSN",
    "ASSBWLMS",
    "ASSBBCBA",
    "ASSBCSM",
    "ASSBPECT",
    "ASSBRRSA",
    "ASSBOFLG",
    "ASSBSCAF",
    "ASSBCTXC",
    "ASSBRMCT",
    "ASSBLRBA",
    "ASSBSLFA",
    "ASSBPFIDASSIGNCNT",
    "ASSBFABRICPRIORITY",
    "ASSBIOMS",
    "ASSBPROMOTIONCOUNT",
    "ASSBTIOP",
    "ASSBCSDP",
    "ASSB_TIME_IFA_ON_CP",
    "ASSB_TIME_ON_IFA",
    "ASSB_TIME_ON_CP",
    "ASSBMTCI",
    "ASSBFLG4",
    "ASSBQIOP",
    "ASSBCRYP",
    "ASSBPHTM_BASE",
    "ASSBEARLYMEMTERMRM",
    "ASSB_LAA_CPID",
    "ASSB_IFA_PHTM",
    "ASSB_TIME_ON_ZIIP_DISPS",
    "ASSB_ZIIP_ENCT_DISPS",
    "ASSB_NONENCT_PSRB_ZAAP_DISPS",
    "ASSB_NONENCT_PSRB_ZIIP_DISPS",
    "ASSB_BASE_PHTM",
    "ASSB_IFA_BASE_PHTM",
    "ASSB_BASE_ENCT",
    "ASSB_IFA_BASE_ENCT",
    "ASSB_CP_AFFINITY_NODE",
    "ASSB_IFA_AFFINITY_NODE",
    "ASSB_SUP_AFFINITY_NODE",
    "ASSBSRBCPOOLPMECOUNT",
    "ASSB_TIME_ON_SUP",
    "ASSB_TIME_SUP_ON_CP",
    "ASSB_SUP_PHTM",
    "ASSB_SRB_TIME_ON_CP",
    "ASSB_SUP_ENCT",
    "ASSB_IFA_ON_CP_ENCT",
    "ASSBSOWN",
    "ASSBSOWT",
    "ASSB_IFA_ON_CP_BASE_ENCT",
    "ASSB_TIME_AT_PDP",
    "ASSB_SRBT_BASE",
    "ASSBCASC",
    "ASSBNUMBERUNAUTHPETS",
    "ASSB_ASST_TIME_ON_CP",
    "ASSB_SWITCH_TO_ZAAPZIIP_COUNT",
    "ASSBASAB",
    "ASSB_SUP_BASE_ENCT",
    "ASSB_SUP_ON_CP_ENCT",
    "ASSB_SUP_ON_CP_BASE_ENCT",
    "ASSBRMIN",
    "ASSBRTMA",
    "ASSB_HDLOCKPROMOTION_TIME_AT_PDP",
    "ASSB_SMFCMS_LOCKINST_ADDR",
    "ASSB_ENQDEQ_CMS_LOCKINST_ADDR",
    "ASSB_LATCH_CMS_LOCKINST_ADDR",
    "ASSB_CMS_LOCKINST_ADDR",
    "ASSB_LOCAL_LOCKINST_ADDR",
    "ASSB_HDLOCKPROMOTE_DISPS",
    "ASSBSAWQ",
    "ASSBR304",
    "ASSBHREQ",
    "ASSBHASI",
    "ASSBR406",
    "ASSB_ENCT",
    "ASSB_ENCT_DISPS",
    "ASSB_ENCT_HDLOCKPROMOTE_DISPS",
    "ASSB_ENCT_HDLOCKPROMOTE_TIME",
    "ASSBR518",
    "ASSB_IFA_ENCT",
    "ASSB_ZAAP_ENCT_DISPS",
    "ASSBBROKENUP_SEQNUM",
    "ASSBDIAG610",
    "ASSB_CCB_REALADDR",
    "ASSB_AICB_REALADDR",
    "ASSBR6C0",
    "ASSB_AICB_VIRTADDR",
    "ASSB_CRYPCTRS_VIRTADDR",
    "ASSB_NNPICTRS_VIRTADDR",
    "ASSB_SRB_TIME_ON_ZCBP",
    "ASSB_ASST_TIME_ON_ZCBP",
    "ASSB_SRB_TIME_ON_ZCBP_DISPS",
    "ASSB_ASST_TIME_ON_ZCBP_DISPS",
    "ASSBETSC",
    "ASSBR704",
    "ASSBCMLC",
    "ASSBR804",
    "ASSBSVRB",
    "ASSBSYNC",
    "ASSBR810",
    "ASSB_VARTIME_AT_PDP",
    "ASSB_VARWEIGHTED_TIME_AT_PDP",
    "ASSB_HCWA",
    "ASSB_SCMBC",
    "ASSB_ZIIP_PHTM_BASE",
    "ASSB_MAJORS_PREEMPTED",
    "ASSB_MINORS_PREEMPTED",
    "ASSBINITIATORJOBID",
    "ASSBINITIATORSEQNUM",
    "ASSBR93C",
    "ASSBDIAG940",
    "ASSB_TIME_JAVA_ON_ZIIP",
    "ASSB_TIME_JAVA_ON_CP",
)
assb_offset_length = (
    info(0,4),  # ASSBASSB
    info(4,4),  # ASSBSMFL
    info(8,4),  # ASSBUBAV
    info(12,4),  # ASSBUBAD
    info(16,4),  # ASSBUPAV
    info(20,4),  # ASSBR014
    info(24,1),  # ASSBXMF1
    info(25,1),  # ASSBXMF2
    info(26,2),  # ASSBXMCC
    info(28,4),  # ASSBCBTP
    info(32,4),  # ASSBVSC
    info(36,4),  # ASSBNVSC
    info(40,4),  # ASSBASRR
    info(44,4),  # ASSBDEXP
    info(48,4),  # ASSBSTW1
    info(52,4),  # ASSBISQN
    info(56,4),  # ASSBBPSA
    info(60,4),  # ASSBCSCT
    info(64,4),  # ASSBBALV
    info(68,4),  # ASSBBALD
    info(72,4),  # ASSBXMSE
    info(76,4),  # ASSBTSQN
    info(80,4),  # ASSBVCNT
    info(84,4),  # ASSBPALV
    info(88,4),  # ASSBASEI
    info(92,4),  # ASSBRMA
    info(96,8),  # ASSBHST
    info(104,8),  # ASSBIIPT
    info(112,4),  # ASSBANEC
    info(116,4),  # ASSBSDOV
    info(120,4),  # ASSBMCSO
    info(124,4),  # ASSBDFAS
    info(128,4),  # ASSBFLGS
    info(132,4),  # ASSBASCB
    info(136,4),  # ASSBASRF
    info(140,4),  # ASSBASRB
    info(144,4),  # ASSBSSD
    info(148,4),  # ASSBMQMA
    info(152,8),  # ASSBLASB
    info(160,4),  # ASSBSCH
    info(164,4),  # ASSBFSC
    info(168,4),  # ASSBJSAB
    info(172,4),  # ASSBRCTW
    info(176,4),  # ASSBLDXH
    info(180,4),  # ASSBLDXL
    info(184,4),  # ASSBTLMI
    info(188,4),  # ASSBSDAS
    info(192,4),  # ASSBTPIN
    info(196,4),  # ASSBSPIN
    info(200,4),  # ASSBECT1
    info(204,4),  # ASSBECT2
    info(208,4),  # ASSBMT#
    info(212,4),  # ASSBDFP
    info(216,2),  # ASSBSASI
    info(218,2),  # ASSBSNEW
    info(220,4),  # ASSBNTTP
    info(224,4),  # ASSBOECB
    info(228,4),  # ASSBOASB
    info(232,4),  # ASSBXSBA
    info(236,4),  # ASSBDLCB
    info(240,4),  # ASSBVAB
    info(244,4),  # ASSBLMAB
    info(248,4),  # ASSBIOCT
    info(252,4),  # ASSBCTT
    info(256,4),  # ASSBXRCT
    info(260,4),  # ASSB_NONENCT_PSRB_CP_DISPS
    info(264,4),  # ASSBTASB
    info(268,4),  # ASSBTPMA
    info(272,4),  # ASSBROSU
    info(276,4),  # ASSBTPMT
    info(280,4),  # ASSBSSDT
    info(284,4),  # ASSBTAWQ
    info(288,4),  # ASSBWCML
    info(292,4),  # ASSBWS3S
    info(296,4),  # ASSBWSSS
    info(300,4),  # ASSBCAPQ
    info(304,4),  # ASSBPTAR
    info(308,4),  # ASSBWTCT
    info(312,4),  # ASSBSBCT
    info(316,4),  # ASSBARBP
    info(320,4),  # ASSBRCTR
    info(324,4),  # ASSBSCAH
    info(328,1),  # ASSBTTFL
    info(329,1),  # ASSBWMF1
    info(330,2),  # ASSBPSWC
    info(332,4),  # ASSBIXGA
    info(336,8),  # ASSBJBNI
    info(344,8),  # ASSBJBNS
    info(352,8),  # ASSBASST
    info(360,8),  # ASSBPHTM
    info(368,4),  # ASSBCRWQ
    info(372,4),  # ASSBSCWQ
    info(376,4),  # ASSBLCNT
    info(380,4),  # ASSBACNT
    info(384,4),  # ASSBLCPD
    info(388,4),  # ASSBSLSC
    info(392,4),  # ASSBPVTC
    info(396,4),  # ASSBCTX
    info(400,16),  # ASSBHALE
    info(416,4),  # ASSB_TIME_ON_ZAAP_DISPS
    info(420,4),  # ASSBSRSN
    info(424,4),  # ASSBWLMS
    info(428,4),  # ASSBBCBA
    info(432,4),  # ASSBCSM
    info(436,4),  # ASSBPECT
    info(440,4),  # ASSBRRSA
    info(444,2),  # ASSBOFLG
    info(446,2),  # ASSBSCAF
    info(448,4),  # ASSBCTXC
    info(452,4),  # ASSBRMCT
    info(456,4),  # ASSBLRBA
    info(460,4),  # ASSBSLFA
    info(464,1),  # ASSBPFIDASSIGNCNT
    info(465,1),  # ASSBFABRICPRIORITY
    info(466,2),  # ASSBIOMS
    info(468,2),  # ASSBPROMOTIONCOUNT
    info(470,1),  # ASSBTIOP
    info(471,1),  # ASSBCSDP
    info(472,8),  # ASSB_TIME_IFA_ON_CP
    info(480,8),  # ASSB_TIME_ON_IFA
    info(488,8),  # ASSB_TIME_ON_CP
    info(496,5),  # ASSBMTCI
    info(501,1),  # ASSBFLG4
    info(502,1),  # ASSBQIOP
    info(503,1),  # ASSBCRYP
    info(504,8),  # ASSBPHTM_BASE
    info(512,4),  # ASSBEARLYMEMTERMRM
    info(516,4),  # ASSB_LAA_CPID
    info(520,8),  # ASSB_IFA_PHTM
    info(528,4),  # ASSB_TIME_ON_ZIIP_DISPS
    info(532,4),  # ASSB_ZIIP_ENCT_DISPS
    info(536,4),  # ASSB_NONENCT_PSRB_ZAAP_DISPS
    info(540,4),  # ASSB_NONENCT_PSRB_ZIIP_DISPS
    info(544,8),  # ASSB_BASE_PHTM
    info(552,8),  # ASSB_IFA_BASE_PHTM
    info(560,8),  # ASSB_BASE_ENCT
    info(568,8),  # ASSB_IFA_BASE_ENCT
    info(576,4),  # ASSB_CP_AFFINITY_NODE
    info(580,4),  # ASSB_IFA_AFFINITY_NODE
    info(584,4),  # ASSB_SUP_AFFINITY_NODE
    info(588,4),  # ASSBSRBCPOOLPMECOUNT
    info(592,8),  # ASSB_TIME_ON_SUP
    info(600,8),  # ASSB_TIME_SUP_ON_CP
    info(608,8),  # ASSB_SUP_PHTM
    info(616,8),  # ASSB_SRB_TIME_ON_CP
    info(624,8),  # ASSB_SUP_ENCT
    info(632,8),  # ASSB_IFA_ON_CP_ENCT
    info(640,4),  # ASSBSOWN
    info(644,4),  # ASSBSOWT
    info(648,8),  # ASSB_IFA_ON_CP_BASE_ENCT
    info(656,8),  # ASSB_TIME_AT_PDP
    info(664,8),  # ASSB_SRBT_BASE
    info(672,4),  # ASSBCASC
    info(676,4),  # ASSBNUMBERUNAUTHPETS
    info(680,8),  # ASSB_ASST_TIME_ON_CP
    info(688,8),  # ASSB_SWITCH_TO_ZAAPZIIP_COUNT
    info(696,8),  # ASSBASAB
    info(704,8),  # ASSB_SUP_BASE_ENCT
    info(712,8),  # ASSB_SUP_ON_CP_ENCT
    info(720,8),  # ASSB_SUP_ON_CP_BASE_ENCT
    info(728,4),  # ASSBRMIN
    info(732,4),  # ASSBRTMA
    info(736,8),  # ASSB_HDLOCKPROMOTION_TIME_AT_PDP
    info(744,4),  # ASSB_SMFCMS_LOCKINST_ADDR
    info(748,4),  # ASSB_ENQDEQ_CMS_LOCKINST_ADDR
    info(752,4),  # ASSB_LATCH_CMS_LOCKINST_ADDR
    info(756,4),  # ASSB_CMS_LOCKINST_ADDR
    info(760,4),  # ASSB_LOCAL_LOCKINST_ADDR
    info(764,4),  # ASSB_HDLOCKPROMOTE_DISPS
    info(768,4),  # ASSBSAWQ
    info(772,252),  # ASSBR304
    info(1024,4),  # ASSBHREQ
    info(1028,2),  # ASSBHASI
    info(1030,250),  # ASSBR406
    info(1280,8),  # ASSB_ENCT
    info(1288,4),  # ASSB_ENCT_DISPS
    info(1292,4),  # ASSB_ENCT_HDLOCKPROMOTE_DISPS
    info(1296,8),  # ASSB_ENCT_HDLOCKPROMOTE_TIME
    info(1304,232),  # ASSBR518
    info(1536,8),  # ASSB_IFA_ENCT
    info(1544,4),  # ASSB_ZAAP_ENCT_DISPS
    info(1548,4),  # ASSBBROKENUP_SEQNUM
    info(1552,160),  # ASSBDIAG610
    info(1712,8),  # ASSB_CCB_REALADDR
    info(1720,8),  # ASSB_AICB_REALADDR
    info(1728,16),  # ASSBR6C0
    info(1744,8),  # ASSB_AICB_VIRTADDR
    info(1752,8),  # ASSB_CRYPCTRS_VIRTADDR
    info(1760,8),  # ASSB_NNPICTRS_VIRTADDR
    info(1768,8),  # ASSB_SRB_TIME_ON_ZCBP
    info(1776,8),  # ASSB_ASST_TIME_ON_ZCBP
    info(1784,4),  # ASSB_SRB_TIME_ON_ZCBP_DISPS
    info(1788,4),  # ASSB_ASST_TIME_ON_ZCBP_DISPS
    info(1792,4),  # ASSBETSC
    info(1796,252),  # ASSBR704
    info(2048,4),  # ASSBCMLC
    info(2052,4),  # ASSBR804
    info(2056,4),  # ASSBSVRB
    info(2060,4),  # ASSBSYNC
    info(2064,240),  # ASSBR810
    info(2304,8),  # ASSB_VARTIME_AT_PDP
    info(2312,8),  # ASSB_VARWEIGHTED_TIME_AT_PDP
    info(2320,8),  # ASSB_HCWA
    info(2328,8),  # ASSB_SCMBC
    info(2336,8),  # ASSB_ZIIP_PHTM_BASE
    info(2344,4),  # ASSB_MAJORS_PREEMPTED
    info(2348,4),  # ASSB_MINORS_PREEMPTED
    info(2352,8),  # ASSBINITIATORJOBID
    info(2360,4),  # ASSBINITIATORSEQNUM
    info(2364,4),  # ASSBR93C
    info(2368,112),  # ASSBDIAG940
    info(2480,8),  # ASSB_TIME_JAVA_ON_ZIIP
    info(2488,8),  # ASSB_TIME_JAVA_ON_CP
)

assb_fields = namedtuple("cvt", assb_field_names)
assb_info = assb_fields._make(assb_offset_length)


def get_assb_address() -> int:
    address_buffer = bytearray(4)
    read_memory(address_buffer, len(address_buffer), 548)
    address_ascb = int.from_bytes(address_buffer, byteorder='big')
    read_memory(address_buffer, len(address_buffer), address_ascb + 336)
    address = int.from_bytes(address_buffer, byteorder='big')
    return address


def get_assb(address: int | None) -> bytearray:
    buffer = bytearray(assb_pattern.size)
    read_memory(buffer, len(buffer), address or get_assb_address())
    return buffer


class ASSB:
    name = "ASSB"
    long_name = "Address Space Secondary Block"
    fields = assb_field_names
    info = assb_info
    def __init__(self, address):
        content = assb_fields._make(assb_pattern.unpack(get_assb(address)))
        self.content = content
