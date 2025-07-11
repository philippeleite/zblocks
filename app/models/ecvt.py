from app.models.base import info, zblocks_list
from app.utils import read_memory
from struct import Struct
from collections import namedtuple

zblocks_list.append('ECVT')

ecvt_pattern = Struct(
    ">"
    "4s"  # ECVTECVT
    "4s"  # ECVTCPLX
    "8s"  # ECVTSPLX
    "4s"  # ECVTSPLE
    "4s"  # ECVTSPLQ
    "4s"  # ECVTSTC1
    "4s"  # ECVTSTC2
    "4s"  # ECVTSTC3
    "4s"  # ECVTSTC4
    "4s"  # ECVTAPPC
    "4s"  # ECVTSCH
    "4s"  # ECVTIOSF
    "4s"  # ECVTOMDA
    "2s"  # ECVTCSVN
    "1s"  # ECVTCNZ
    "1s"  # ECVTALOC
    "4s"  # ECVTBPMS
    "4s"  # ECVTBPME
    "4s"  # ECVTAPMS
    "4s"  # ECVTAPME
    "4s"  # ECVTQUCB
    "4s"  # ECVTSSDF
    "4s"  # ECVTSSDS
    "4s"  # ECVT_CUSTOMER_AREA_ADDR
    "4s"  # ECVTSRBT
    "4s"  # ECVTDPQH
    "4s"  # ECVTTCRE
    "16s"  # ECVTXCFG
    "4s"  # ECVTR078
    "4s"  # ECVTR07C
    "4s"  # ECVTSCHA
    "4s"  # ECVTHFXS
    "4s"  # ECVTDLCB
    "4s"  # ECVTNTTP
    "4s"  # ECVTSRBJ
    "4s"  # ECVTSRBL
    "4s"  # ECVTMSCH
    "4s"  # ECVTCAL
    "8s"  # ECVTLOAD
    "8s"  # ECVTMLPR
    "4s"  # ECVTTCP
    "4s"  # ECVTHISNMT
    "4s"  # ECVTNVDM
    "4s"  # ECVTR0BC
    "4s"  # ECVTGRMP
    "4s"  # ECVTWLM
    "4s"  # ECVTCSM
    "4s"  # ECVTCTBL
    "4s"  # ECVTPMCS
    "4s"  # ECVTPMCR
    "4s"  # ECVTSTX1
    "4s"  # ECVTSTX2
    "4s"  # ECVTSLID
    "4s"  # ECVTCSVT
    "4s"  # ECVTASA
    "4s"  # ECVTEXPM
    "4s"  # ECVTOCVT
    "4s"  # ECVTOEXT
    "4s"  # ECVTCMPS
    "4s"  # ECVTNUCP
    "4s"  # ECVTXRAT
    "4s"  # ECVTPWVT
    "2s"  # ECVTCLON
    "1s"  # ECVTGMOD
    "1s"  # ECVTLPDELEN
    "4s"  # ECVTDUCU
    "4s"  # ECVTALCK
    "4s"  # ECVTSXMP
    "2s"  # ECVTR118
    "2s"  # ECVTPTIM
    "4s"  # ECVTJCCT
    "4s"  # ECVTLSAB
    "4s"  # ECVTETPE
    "4s"  # ECVTSYMT
    "4s"  # ECVTESYM
    "4s"  # ECVTFLGS
    "4s"  # ECVTESY1
    "4s"  # ECVTPETM
    "4s"  # ECVTETPT
    "4s"  # ECVTENVT
    "4s"  # ECVTVSER
    "4s"  # ECVTLSEN
    "4s"  # ECVTDGNB
    "8s"  # ECVTHDNM
    "8s"  # ECVTLPNM
    "8s"  # ECVTVMNM
    "4s"  # ECVTGRM
    "4s"  # ECVTSEIF
    "4s"  # ECVTAES
    "4s"  # ECVTRSMT
    "16s"  # ECVTMMEM
    "4s"  # ECVTIPA
    "16s"  # ECVTMMET
    "4s"  # ECVTMMEQ
    "4s"  # ECVTMMEA
    "4s"  # ECVTEAEX
    "4s"  # ECVTEAUX
    "4s"  # ECVTMMEC
    "4s"  # ECVTIPST
    "4s"  # ECVTRRSW
    "4s"  # ECVTRRTT
    "4s"  # ECVTRRMT
    "4s"  # ECVTPRED
    "16s"  # ECVTCEMT
    "4s"  # ECVTCEME
    "4s"  # ECVTCEMR
    "4s"  # ECVTPSEQ
    "16s"  # ECVTPOWN
    "16s"  # ECVTPNAM
    "2s"  # ECVTPVER
    "2s"  # ECVTPREL
    "2s"  # ECVTPMOD
    "1s"  # ECVTPDVL
    "1s"  # ECVTTTFL
    "4s"  # ECVTCURX
    "4s"  # ECVTCTXR
    "4s"  # ECVTCRGR
    "4s"  # ECVTCSRB
    "4s"  # ECVTREM1
    "4s"  # ECVTREM2
    "4s"  # ECVTXFR3
    "4s"  # ECVTCICB
    "4s"  # ECVTDLPF
    "4s"  # ECVTDLPL
    "4s"  # ECVTSRBR
    "4s"  # ECVTBCBA
    "8s"  # ECVTPIDN
    "4s"  # ECVTRMDP
    "4s"  # ECVTRMDS
    "4s"  # ECVTRSU1
    "4s"  # ECVTPEST
    "4s"  # ECVTCDYN
    "4s"  # ECVTFCDA
    "8s"  # ECVTEORM
    "4s"  # ECVTCBLS
    "4s"  # ECVTRINS
    "4s"  # ECVTTTCA
    "4s"  # ECVTLCXT
    "4s"  # ECVTOESI
    "4s"  # ECVTOXSB
    "4s"  # ECVTESTU
    "4s"  # ECVTRBUP
    "4s"  # ECVTOSAI
    "4s"  # ECVTPFA
    "4s"  # ECVTCRDT
    "4s"  # ECVTCTB2
    "4s"  # ECVTJAOF
    "4s"  # ECVTXPCB
    "16s"  # ECVTLPUB
    "8s"  # ECVTLPID
    "8s"  # ECVTLVID
    "4s"  # ECVTLKLN
    "4s"  # ECVTLKAD
    "2s"  # ECVTCACHELINESIZE
    "1s"  # ECVTCACHELINESTARTBDY
    "1s"  # ECVT_OSPROTECT
    "4s"  # ECVTRFPT
    "2s"  # ECVT_INSTALLED_CPU_HWM
    "2s"  # ECVT_INSTALLED_CPU_AT_IPL
    "4s"  # ECVTCRIT
    "8s"  # ECVTTEDVECTORTABLEADDR
    "8s"  # ECVTTEDSTORAGEBYTESALLOCATED
    "4s"  # ECVTTEDS
    "12s"  # ECVTMMIG
    "8s"  # ECVTOSARX
    "8s"  # ECVT_HCWA
    "4s"  # ECVTSLCA
    "4s"  # ECVTCPGUM
    "4s"  # ECVTCPFRM
    "4s"  # ECVTCPGCM
    "4s"  # ECVT4QV1
    "4s"  # ECVT4QV2
    "4s"  # ECVT4QV3
    "4s"  # ECVT4QV4
    "4s"  # ECVT4QV5
    "4s"  # ECVT4QV6
    "4s"  # ECVT4QV7
    "4s"  # ECVTTENC
    "4s"  # ECVTSCF
    "4s"  # ECVTTSTH
    "4s"  # ECVTSTC5
    "4s"  # ECVTSTC6
    "4s"  # ECVTCH1
    "4s"  # ECVTCH2
    "4s"  # ECVTCEAB
    "4s"  # ECVTAXRB
    "4s"  # ECVTECT
    "4s"  # ECVTFACL
    "2s"  # ECVTMAXCOREID
    "2s"  # ECVTNUMCPUIDSINCORE
    "4s"  # ECVTNTRM
    "4s"  # ECVTSDC
    "4s"  # ECVTHIAB
    "4s"  # ECVTHWIP
    "4s"  # ECVTSCPIN
    "8s"  # ECVTHP1
    "2s"  # ECVTMAXMPNUMBYTESINMASK
    "2s"  # ECVTPHYSICALTOLOGICALMASK
    "2s"  # ECVTLOGICALTOPHYSICALMASK
    "1s"  # ECVTAPPFLAGS
    "1s"  # ECVT_OSPROTECT_WHENSYSTEM
    "4s"  # ECVT_GETSRBIDTOKEN
    "4s"  # ECVTXTSW
    "4s"  # ECVT_SMF_CMS_LOCKINST_ADDR
    "4s"  # ECVT_ENQDEQ_CMS_LOCKINST_ADDR
    "4s"  # ECVT_LATCH_CMS_LOCKINST_ADDR
    "4s"  # ECVT_CMS_LOCKINST_ADDR
    "4s"  # ECVTHZRB
    "4s"  # ECVTGTZ
    "4s"  # ECVTCPGUC
    "4s"  # ECVTCPFRC
    "4s"  # ECVTCPGCC
    "2s"  # ECVT_INSTALLED_CORE_HWM
    "2s"  # ECVT_INSTALLED_CORE_AT_IPL
    "16s"  # ECVTLSO
    "16s"  # ECVTLDTO
    "4s"  # ECVTIZUGSP
    "4s"  # ECVTSVTX
    "8s"  # ECVTR3D8
    "1s"  # ECVT_BOOSTINFO_FLAGS0
    "1s"  # ECVT_BOOSTINFO_SYSPARM_FLAGS
    "1s"  # ECVT_BOOSTINFO_FLAGS1
    "1s"  # ECVT_BOOSTINFO_SD_FLAGS1
    "2s"  # ECVT_BOOSTINFO_TRANSIENTZIIPCORES
    "1s"  # ECVT_BOOSTINFO_FLAGS2
    "1s"  # ECVT_BOOSTLEVEL
    "16s" # ECVT_BOOSTINFO_EXPECTED_ENDETOD
    "4s"  # ECVT_RPBOOSTS_NUM
    "4s"  # ECVT_RPBOOSTS_NUM_IGNORED
    "8s"  # ECVT_RPB_DURATION
    "1s"  # ECVT_RPB_BOOSTINFO_FLAGS1
    "1s"  # ECVT_RPBOOSTS_REQUESTOR_ID
    "2s"  # ECVTR40A
    "4s"  # ECVT_RPBOOSTS_NUMBYREQUESTOR_ADDR
    "4s"  # ECVT_RPBOOSTS_NUM_WHILEDIS
    "4s"  # ECVTR414
    "8s"  # ECVT_RPB_DURATION_POTENTIAL
    "8s"  # ECVT_RPB_DURATION_POTENTIAL_E
    "8s"  # ECVT_RPB_EN_DIS_LOCAL_TIMESTAMP
    "8s"  # ECVTR430
)
ecvt_field_names = (
    "ECVTECVT",
    "ECVTCPLX",
    "ECVTSPLX",
    "ECVTSPLE",
    "ECVTSPLQ",
    "ECVTSTC1",
    "ECVTSTC2",
    "ECVTSTC3",
    "ECVTSTC4",
    "ECVTAPPC",
    "ECVTSCH",
    "ECVTIOSF",
    "ECVTOMDA",
    "ECVTCSVN",
    "ECVTCNZ",
    "ECVTALOC",
    "ECVTBPMS",
    "ECVTBPME",
    "ECVTAPMS",
    "ECVTAPME",
    "ECVTQUCB",
    "ECVTSSDF",
    "ECVTSSDS",
    "ECVT_CUSTOMER_AREA_ADDR",
    "ECVTSRBT",
    "ECVTDPQH",
    "ECVTTCRE",
    "ECVTXCFG",
    "ECVTR078",
    "ECVTR07C",
    "ECVTSCHA",
    "ECVTHFXS",
    "ECVTDLCB",
    "ECVTNTTP",
    "ECVTSRBJ",
    "ECVTSRBL",
    "ECVTMSCH",
    "ECVTCAL",
    "ECVTLOAD",
    "ECVTMLPR",
    "ECVTTCP",
    "ECVTHISNMT",
    "ECVTNVDM",
    "ECVTR0BC",
    "ECVTGRMP",
    "ECVTWLM",
    "ECVTCSM",
    "ECVTCTBL",
    "ECVTPMCS",
    "ECVTPMCR",
    "ECVTSTX1",
    "ECVTSTX2",
    "ECVTSLID",
    "ECVTCSVT",
    "ECVTASA",
    "ECVTEXPM",
    "ECVTOCVT",
    "ECVTOEXT",
    "ECVTCMPS",
    "ECVTNUCP",
    "ECVTXRAT",
    "ECVTPWVT",
    "ECVTCLON",
    "ECVTGMOD",
    "ECVTLPDELEN",
    "ECVTDUCU",
    "ECVTALCK",
    "ECVTSXMP",
    "ECVTR118",
    "ECVTPTIM",
    "ECVTJCCT",
    "ECVTLSAB",
    "ECVTETPE",
    "ECVTSYMT",
    "ECVTESYM",
    "ECVTFLGS",
    "ECVTESY1",
    "ECVTPETM",
    "ECVTETPT",
    "ECVTENVT",
    "ECVTVSER",
    "ECVTLSEN",
    "ECVTDGNB",
    "ECVTHDNM",
    "ECVTLPNM",
    "ECVTVMNM",
    "ECVTGRM",
    "ECVTSEIF",
    "ECVTAES",
    "ECVTRSMT",
    "ECVTMMEM",
    "ECVTIPA",
    "ECVTMMET",
    "ECVTMMEQ",
    "ECVTMMEA",
    "ECVTEAEX",
    "ECVTEAUX",
    "ECVTMMEC",
    "ECVTIPST",
    "ECVTRRSW",
    "ECVTRRTT",
    "ECVTRRMT",
    "ECVTPRED",
    "ECVTCEMT",
    "ECVTCEME",
    "ECVTCEMR",
    "ECVTPSEQ",
    "ECVTPOWN",
    "ECVTPNAM",
    "ECVTPVER",
    "ECVTPREL",
    "ECVTPMOD",
    "ECVTPDVL",
    "ECVTTTFL",
    "ECVTCURX",
    "ECVTCTXR",
    "ECVTCRGR",
    "ECVTCSRB",
    "ECVTREM1",
    "ECVTREM2",
    "ECVTXFR3",
    "ECVTCICB",
    "ECVTDLPF",
    "ECVTDLPL",
    "ECVTSRBR",
    "ECVTBCBA",
    "ECVTPIDN",
    "ECVTRMDP",
    "ECVTRMDS",
    "ECVTRSU1",
    "ECVTPEST",
    "ECVTCDYN",
    "ECVTFCDA",
    "ECVTEORM",
    "ECVTCBLS",
    "ECVTRINS",
    "ECVTTTCA",
    "ECVTLCXT",
    "ECVTOESI",
    "ECVTOXSB",
    "ECVTESTU",
    "ECVTRBUP",
    "ECVTOSAI",
    "ECVTPFA",
    "ECVTCRDT",
    "ECVTCTB2",
    "ECVTJAOF",
    "ECVTXPCB",
    "ECVTLPUB",
    "ECVTLPID",
    "ECVTLVID",
    "ECVTLKLN",
    "ECVTLKAD",
    "ECVTCACHELINESIZE",
    "ECVTCACHELINESTARTBDY",
    "ECVT_OSPROTECT",
    "ECVTRFPT",
    "ECVT_INSTALLED_CPU_HWM",
    "ECVT_INSTALLED_CPU_AT_IPL",
    "ECVTCRIT",
    "ECVTTEDVECTORTABLEADDR",
    "ECVTTEDSTORAGEBYTESALLOCATED",
    "ECVTTEDS",
    "ECVTMMIG",
    "ECVTOSARX",
    "ECVT_HCWA",
    "ECVTSLCA",
    "ECVTCPGUM",
    "ECVTCPFRM",
    "ECVTCPGCM",
    "ECVT4QV1",
    "ECVT4QV2",
    "ECVT4QV3",
    "ECVT4QV4",
    "ECVT4QV5",
    "ECVT4QV6",
    "ECVT4QV7",
    "ECVTTENC",
    "ECVTSCF",
    "ECVTTSTH",
    "ECVTSTC5",
    "ECVTSTC6",
    "ECVTCH1",
    "ECVTCH2",
    "ECVTCEAB",
    "ECVTAXRB",
    "ECVTECT",
    "ECVTFACL",
    "ECVTMAXCOREID",
    "ECVTNUMCPUIDSINCORE",
    "ECVTNTRM",
    "ECVTSDC",
    "ECVTHIAB",
    "ECVTHWIP",
    "ECVTSCPIN",
    "ECVTHP1",
    "ECVTMAXMPNUMBYTESINMASK",
    "ECVTPHYSICALTOLOGICALMASK",
    "ECVTLOGICALTOPHYSICALMASK",
    "ECVTAPPFLAGS",
    "ECVT_OSPROTECT_WHENSYSTEM",
    "ECVT_GETSRBIDTOKEN",
    "ECVTXTSW",
    "ECVT_SMF_CMS_LOCKINST_ADDR",
    "ECVT_ENQDEQ_CMS_LOCKINST_ADDR",
    "ECVT_LATCH_CMS_LOCKINST_ADDR",
    "ECVT_CMS_LOCKINST_ADDR",
    "ECVTHZRB",
    "ECVTGTZ",
    "ECVTCPGUC",
    "ECVTCPFRC",
    "ECVTCPGCC",
    "ECVT_INSTALLED_CORE_HWM",
    "ECVT_INSTALLED_CORE_AT_IPL",
    "ECVTLSO",
    "ECVTLDTO",
    "ECVTIZUGSP",
    "ECVTSVTX",
    "ECVTR3D8",
    "ECVT_BOOSTINFO_FLAGS0",
    "ECVT_BOOSTINFO_SYSPARM_FLAGS",
    "ECVT_BOOSTINFO_FLAGS1",
    "ECVT_BOOSTINFO_SD_FLAGS1",
    "ECVT_BOOSTINFO_TRANSIENTZIIPCORES",
    "ECVT_BOOSTINFO_FLAGS2",
    "ECVT_BOOSTLEVEL",
    "ECVT_BOOSTINFO_EXPECTED_ENDETOD",
    "ECVT_RPBOOSTS_NUM",
    "ECVT_RPBOOSTS_NUM_IGNORED",
    "ECVT_RPB_DURATION",
    "ECVT_RPB_BOOSTINFO_FLAGS1",
    "ECVT_RPBOOSTS_REQUESTOR_ID",
    "ECVTR40A",
    "ECVT_RPBOOSTS_NUMBYREQUESTOR_ADDR",
    "ECVT_RPBOOSTS_NUM_WHILEDIS",
    "ECVTR414",
    "ECVT_RPB_DURATION_POTENTIAL",
    "ECVT_RPB_DURATION_POTENTIAL_E",
    "ECVT_RPB_EN_DIS_LOCAL_TIMESTAMP",
    "ECVTR430",
)
ecvt_offset_length = (
    info(0,4),  # ECVTECVT
    info(4,4),  # ECVTCPLX
    info(8,8),  # ECVTSPLX
    info(16,4),  # ECVTSPLE
    info(20,4),  # ECVTSPLQ
    info(24,4),  # ECVTSTC1
    info(28,4),  # ECVTSTC2
    info(32,4),  # ECVTSTC3
    info(36,4),  # ECVTSTC4
    info(40,4),  # ECVTAPPC
    info(44,4),  # ECVTSCH
    info(48,4),  # ECVTIOSF
    info(52,4),  # ECVTOMDA
    info(56,2),  # ECVTCSVN
    info(58,1),  # ECVTCNZ
    info(59,1),  # ECVTALOC
    info(60,4),  # ECVTBPMS
    info(64,4),  # ECVTBPME
    info(68,4),  # ECVTAPMS
    info(72,4),  # ECVTAPME
    info(76,4),  # ECVTQUCB
    info(80,4),  # ECVTSSDF
    info(84,4),  # ECVTSSDS
    info(88,4),  # ECVT_CUSTOMER_AREA_ADDR
    info(92,4),  # ECVTSRBT
    info(96,4),  # ECVTDPQH
    info(100,4),  # ECVTTCRE
    info(104,16),  # ECVTXCFG
    info(120,4),  # ECVTR078
    info(124,4),  # ECVTR07C
    info(128,4),  # ECVTSCHA
    info(132,4),  # ECVTHFXS
    info(136,4),  # ECVTDLCB
    info(140,4),  # ECVTNTTP
    info(144,4),  # ECVTSRBJ
    info(148,4),  # ECVTSRBL
    info(152,4),  # ECVTMSCH
    info(156,4),  # ECVTCAL
    info(160,8),  # ECVTLOAD
    info(168,8),  # ECVTMLPR
    info(176,4),  # ECVTTCP
    info(180,4),  # ECVTHISNMT
    info(184,4),  # ECVTNVDM
    info(188,4),  # ECVTR0BC
    info(192,4),  # ECVTGRMP
    info(196,4),  # ECVTWLM
    info(200,4),  # ECVTCSM
    info(204,4),  # ECVTCTBL
    info(208,4),  # ECVTPMCS
    info(212,4),  # ECVTPMCR
    info(216,4),  # ECVTSTX1
    info(220,4),  # ECVTSTX2
    info(224,4),  # ECVTSLID
    info(228,4),  # ECVTCSVT
    info(232,4),  # ECVTASA
    info(236,4),  # ECVTEXPM
    info(240,4),  # ECVTOCVT
    info(244,4),  # ECVTOEXT
    info(248,4),  # ECVTCMPS
    info(252,4),  # ECVTNUCP
    info(256,4),  # ECVTXRAT
    info(260,4),  # ECVTPWVT
    info(264,2),  # ECVTCLON
    info(266,1),  # ECVTGMOD
    info(267,1),  # ECVTLPDELEN
    info(268,4),  # ECVTDUCU
    info(272,4),  # ECVTALCK
    info(276,4),  # ECVTSXMP
    info(280,2),  # ECVTR118
    info(282,2),  # ECVTPTIM
    info(284,4),  # ECVTJCCT
    info(288,4),  # ECVTLSAB
    info(292,4),  # ECVTETPE
    info(296,4),  # ECVTSYMT
    info(300,4),  # ECVTESYM
    info(304,4),  # ECVTFLGS
    info(308,4),  # ECVTESY1
    info(312,4),  # ECVTPETM
    info(316,4),  # ECVTETPT
    info(320,4),  # ECVTENVT
    info(324,4),  # ECVTVSER
    info(328,4),  # ECVTLSEN
    info(332,4),  # ECVTDGNB
    info(336,8),  # ECVTHDNM
    info(344,8),  # ECVTLPNM
    info(352,8),  # ECVTVMNM
    info(360,4),  # ECVTGRM
    info(364,4),  # ECVTSEIF
    info(368,4),  # ECVTAES
    info(372,4),  # ECVTRSMT
    info(376,16),  # ECVTMMEM
    info(392,4),  # ECVTIPA
    info(396,16),  # ECVTMMET
    info(412,4),  # ECVTMMEQ
    info(416,4),  # ECVTMMEA
    info(420,4),  # ECVTEAEX
    info(424,4),  # ECVTEAUX
    info(428,4),  # ECVTMMEC
    info(432,4),  # ECVTIPST
    info(436,4),  # ECVTRRSW
    info(440,4),  # ECVTRRTT
    info(444,4),  # ECVTRRMT
    info(448,4),  # ECVTPRED
    info(452,16),  # ECVTCEMT
    info(468,4),  # ECVTCEME
    info(472,4),  # ECVTCEMR
    info(476,4),  # ECVTPSEQ
    info(480,16),  # ECVTPOWN
    info(496,16),  # ECVTPNAM
    info(512,2),  # ECVTPVER
    info(514,2),  # ECVTPREL
    info(516,2),  # ECVTPMOD
    info(518,1),  # ECVTPDVL
    info(519,1),  # ECVTTTFL
    info(520,4),  # ECVTCURX
    info(524,4),  # ECVTCTXR
    info(528,4),  # ECVTCRGR
    info(532,4),  # ECVTCSRB
    info(536,4),  # ECVTREM1
    info(540,4),  # ECVTREM2
    info(544,4),  # ECVTXFR3
    info(548,4),  # ECVTCICB
    info(552,4),  # ECVTDLPF
    info(556,4),  # ECVTDLPL
    info(560,4),  # ECVTSRBR
    info(564,4),  # ECVTBCBA
    info(568,8),  # ECVTPIDN
    info(576,4),  # ECVTRMDP
    info(580,4),  # ECVTRMDS
    info(584,4),  # ECVTRSU1
    info(588,4),  # ECVTPEST
    info(592,4),  # ECVTCDYN
    info(596,4),  # ECVTFCDA
    info(600,8),  # ECVTEORM
    info(608,4),  # ECVTCBLS
    info(612,4),  # ECVTRINS
    info(616,4),  # ECVTTTCA
    info(620,4),  # ECVTLCXT
    info(624,4),  # ECVTOESI
    info(628,4),  # ECVTOXSB
    info(632,4),  # ECVTESTU
    info(636,4),  # ECVTRBUP
    info(640,4),  # ECVTOSAI
    info(644,4),  # ECVTPFA
    info(648,4),  # ECVTCRDT
    info(652,4),  # ECVTCTB2
    info(656,4),  # ECVTJAOF
    info(660,4),  # ECVTXPCB
    info(664,16),  # ECVTLPUB
    info(680,8),  # ECVTLPID
    info(688,8),  # ECVTLVID
    info(696,4),  # ECVTLKLN
    info(700,4),  # ECVTLKAD
    info(704,2),  # ECVTCACHELINESIZE
    info(706,1),  # ECVTCACHELINESTARTBDY
    info(707,1),  # ECVT_OSPROTECT
    info(708,4),  # ECVTRFPT
    info(712,2),  # ECVT_INSTALLED_CPU_HWM
    info(714,2),  # ECVT_INSTALLED_CPU_AT_IPL
    info(716,4),  # ECVTCRIT
    info(720,8),  # ECVTTEDVECTORTABLEADDR
    info(728,8),  # ECVTTEDSTORAGEBYTESALLOCATED
    info(736,4),  # ECVTTEDS
    info(740,12),  # ECVTMMIG
    info(752,8),  # ECVTOSARX
    info(760,8),  # ECVT_HCWA
    info(768,4),  # ECVTSLCA
    info(772,4),  # ECVTCPGUM
    info(776,4),  # ECVTCPFRM
    info(780,4),  # ECVTCPGCM
    info(784,4),  # ECVT4QV1
    info(788,4),  # ECVT4QV2
    info(792,4),  # ECVT4QV3
    info(796,4),  # ECVT4QV4
    info(800,4),  # ECVT4QV5
    info(804,4),  # ECVT4QV6
    info(808,4),  # ECVT4QV7
    info(812,4),  # ECVTTENC
    info(816,4),  # ECVTSCF
    info(820,4),  # ECVTTSTH
    info(824,4),  # ECVTSTC5
    info(828,4),  # ECVTSTC6
    info(832,4),  # ECVTCH1
    info(836,4),  # ECVTCH2
    info(840,4),  # ECVTCEAB
    info(844,4),  # ECVTAXRB
    info(848,4),  # ECVTECT
    info(852,4),  # ECVTFACL
    info(856,2),  # ECVTMAXCOREID
    info(858,2),  # ECVTNUMCPUIDSINCORE
    info(860,4),  # ECVTNTRM
    info(864,4),  # ECVTSDC
    info(868,4),  # ECVTHIAB
    info(872,4),  # ECVTHWIP
    info(876,4),  # ECVTSCPIN
    info(880,8),  # ECVTHP1
    info(888,2),  # ECVTMAXMPNUMBYTESINMASK
    info(890,2),  # ECVTPHYSICALTOLOGICALMASK
    info(892,2),  # ECVTLOGICALTOPHYSICALMASK
    info(894,1),  # ECVTAPPFLAGS
    info(895,1),  # ECVT_OSPROTECT_WHENSYSTEM
    info(896,4),  # ECVT_GETSRBIDTOKEN
    info(900,4),  # ECVTXTSW
    info(904,4),  # ECVT_SMF_CMS_LOCKINST_ADDR
    info(908,4),  # ECVT_ENQDEQ_CMS_LOCKINST_ADDR
    info(912,4),  # ECVT_LATCH_CMS_LOCKINST_ADDR
    info(916,4),  # ECVT_CMS_LOCKINST_ADDR
    info(920,4),  # ECVTHZRB
    info(924,4),  # ECVTGTZ
    info(928,4),  # ECVTCPGUC
    info(932,4),  # ECVTCPFRC
    info(936,4),  # ECVTCPGCC
    info(940,2),  # ECVT_INSTALLED_CORE_HWM
    info(942,2),  # ECVT_INSTALLED_CORE_AT_IPL
    info(944,16),  # ECVTLSO
    info(960,16),  # ECVTLDTO
    info(976,4),  # ECVTIZUGSP
    info(980,4),  # ECVTSVTX
    info(984,8),  # ECVTR3D8
    info(992,1),  # ECVT_BOOSTINFO_FLAGS0
    info(993,1),  # ECVT_BOOSTINFO_SYSPARM_FLAGS
    info(994,1),  # ECVT_BOOSTINFO_FLAGS1
    info(995,1),  # ECVT_BOOSTINFO_SD_FLAGS1
    info(996,2),  # ECVT_BOOSTINFO_TRANSIENTZIIPCORES
    info(998,1),  # ECVT_BOOSTINFO_FLAGS2
    info(999,1),  # ECVT_BOOSTLEVEL
    info(1000,16), # ECVT_BOOSTINFO_EXPECTED_ENDETOD
    info(1016,4),  # ECVT_RPBOOSTS_NUM
    info(1020,4),  # ECVT_RPBOOSTS_NUM_IGNORED
    info(1024,8),  # ECVT_RPB_DURATION
    info(1032,1),  # ECVT_RPB_BOOSTINFO_FLAGS1
    info(1033,1),  # ECVT_RPBOOSTS_REQUESTOR_ID
    info(1034,2),  # ECVTR40A
    info(1036,4),  # ECVT_RPBOOSTS_NUMBYREQUESTOR_ADDR
    info(1040,4),  # ECVT_RPBOOSTS_NUM_WHILEDIS
    info(1044,4),  # ECVTR414
    info(1048,8),  # ECVT_RPB_DURATION_POTENTIAL
    info(1056,8),  # ECVT_RPB_DURATION_POTENTIAL_E
    info(1064,8),  # ECVT_RPB_EN_DIS_LOCAL_TIMESTAMP
    info(1072,8),  # ECVTR430
)

ecvt_fields = namedtuple("ecvt", ecvt_field_names)
ecvt_info = ecvt_fields._make(ecvt_offset_length)


def get_ecvt_address() -> int:
    address_buffer = bytearray(4)
    read_memory(address_buffer, len(address_buffer), 16)
    address_cvt = int.from_bytes(address_buffer, byteorder='big')
    read_memory(address_buffer, len(address_buffer), address_cvt + 140)
    address = int.from_bytes(address_buffer, byteorder='big')
    return address


def get_ecvt() -> bytearray:
    buffer = bytearray(ecvt_pattern.size)
    address = get_ecvt_address()
    read_memory(buffer, len(buffer), address)
    return buffer


class ECVT:
    name = "ECVT"
    long_name = "Extended Communications Vector Table"
    fields = ecvt_field_names
    info = ecvt_info
    def __init__(self):
        content = ecvt_fields._make(ecvt_pattern.unpack(get_ecvt()))
        self.content = content