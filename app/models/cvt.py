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
    "4s"  # CVTPRLTV
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
    "4s"  # CVTQTE00
    "4s"  # CVTQTD00
    "4s"  # CVTSTB
    "1s"  # CVTDCB
    "3s"  # CVTDCBA
    "4s"  # CVTSV76M
    "4s"  # CVTIXAVL
    "4s"  # CVTNUCB
    "4s"  # CVTFBOSV
    "4s"  # CVT0DS
    "4s"  # CVTECVT
    "4s"  # CVTDAIRX
    "4s"  # CVTMSER
    "4s"  # CVT0PT01
    "4s"  # CVTTVT
    "4s"  # CVT040ID
    "4s"  # CVTMZ00
    "4s"  # CVT1EF00
    "4s"  # CVTQOCR
    "4s"  # CVTQMWR
    "2s"  # CVTSNCTR
    "1s"  # CVTOPTA
    "1s"  # CVTOPTB
    "4s"  # CVTQCDSR
    "4s"  # CVTQLPAQ
    "4s"  # CVTENFCT
    "4s"  # CVTSMCA
    "4s"  # CVTABEND
    "4s"  # CVTUSER
    "4s"  # CVTMDLDS
    "2s"  # CVTQABST
    "2s"  # CVTLNKSC
    "4s"  # CVTTSCE
    "4s"  # CVTPATCH
    "4s"  # CVTRMS
    "4s"  # CVTSPDME
    "4s"  # CVT0SCR1
    "4s"  # CVTGTF
    "4s"  # CVTAQAVT
    "1s"  # CVTFLAG5
    "1s"  # CVTFLAG6
    "1s"  # CVTFLAG7
    "1s"  # CVTFLAG8
    "4s"  # CVTSAF
    "4s"  # CVTEXT1
    "4s"  # CVTCBSP
    "4s"  # CVTPURG
    "4s"  # CVTAMFF
    "4s"  # CVTQMSG
    "4s"  # CVTDMSR
    "4s"  # CVTSFR
    "4s"  # CVTGXL
    "4s"  # CVTREAL
    "4s"  # CVTPTRV
    "4s"  # CVTIHVP
    "4s"  # CVTJESCT
    "4s"  # CVTRS12C
    "4s"  # CVTTZ
    "4s"  # CVTMCHPR
    "4s"  # CVTEORM
    "4s"  # CVTPTRV3
    "4s"  # CVTLKRM
    "4s"  # CVTAPF
    "4s"  # CVTEXT2
    "4s"  # CVTHJES
    "4s"  # CVTRSTW2
    "8s"  # CVTSNAME
    "4s"  # CVTGETL
    "4s"  # CVTLPDSR
    "4s"  # CVTPVTP
    "4s"  # CVTLPDIA
    "4s"  # CVTRBCB
    "4s"  # CVTRS170
    "4s"  # CVTSLIDA
    "4s"  # CVTFLAGS
    "4s"  # CVTRT03
    "8s"  # CVTRS180
    "4s"  # CVTEXSNR
    "1s"  # CVTEXSNL
    "1s"  # CVTSPVLK
    "1s"  # CVTCTLFG
    "1s"  # CVTAPG
    "4s"  # CVTRSCN
    "4s"  # CVTTAS
    "4s"  # CVTTRCRM
    "4s"  # CVTSHRVM
    "4s"  # CVT0VL01
    "4s"  # CVTPPGMX
    "1s"  # CVTGRSST
    "1s"  # CVTFLAG9
    "2s"  # CVTBSM0F
    "4s"  # CVTGVT
    "4s"  # CVTASCRF
    "4s"  # CVTASCRL
    "4s"  # CVTPUTL
    "4s"  # CVTSRBRT
    "4s"  # CVTOLT0A
    "4s"  # CVTSMFEX
    "4s"  # CVTCSPIE
    "4s"  # CVTPTGT
    "1s"  # CVTSIGPT
    "1s"  # CVTSPDMC
    "1s"  # CVTDSSAC
    "1s"  # CVTRS1D7
    "4s"  # CVTSTCK
    "2s"  # CVTMAXMP
    "2s"  # CVTBSM2
    "4s"  # CVTSCAN
    "4s"  # CVTAUTHL
    "4s"  # CVTBLDCP
    "4s"  # CVTGETCL
    "4s"  # CVTFRECL
    "4s"  # CVTDELCP
    "4s"  # CVTCRMN
    "4s"  # CVTCRAS
    "4s"  # CVTQSAS
    "4s"  # CVTFRAS
    "4s"  # CVTS1EE
    "4s"  # CVTPARS
    "4s"  # CVTQUIS
    "4s"  # CVTSTXU
    "4s"  # CVTOPTE
    "4s"  # CVTSDRM
    "4s"  # CVTCSRT
    "4s"  # CVTAQTOP
    "4s"  # CVTVVMDI
    "4s"  # CVTASVT
    "4s"  # CVTGDA
    "4s"  # CVTASCBH
    "4s"  # CVTASCBL
    "4s"  # CVTRTMCT
    "4s"  # CVTSV60
    "4s"  # CVTSDMP
    "4s"  # CVTSCBP
    "4s"  # CVTSDBF
    "4s"  # CVTRTMS
    "4s"  # CVTTPIOS
    "4s"  # CVTSIC
    "4s"  # CVTOPCTP
    "4s"  # CVTEXPRO
    "4s"  # CVTGSMQ
    "4s"  # CVTLSMQ
    "4s"  # CVTRS26C
    "4s"  # CVTVWAIT
    "4s"  # CVTPARRL
    "4s"  # CVTAPFT
    "4s"  # CVTQCS01
    "4s"  # CVTFQCB
    "4s"  # CVTLQCB
    "4s"  # CVTRENQ
    "4s"  # CVTRSPIE
    "4s"  # CVTLKRMA
    "4s"  # CVTCSD
    "4s"  # CVTDQIQE
    "4s"  # CVTRPOST
    "4s"  # CVT062R1
    "4s"  # CVTVEAC0
    "4s"  # CVTGLMN
    "4s"  # CVTSPSA
    "4s"  # CVTWSAL
    "4s"  # CVTWSAG
    "4s"  # CVTWSAC
    "4s"  # CVTRECRQ
    "4s"  # CVTASMVT
    "4s"  # CVTIOBP
    "4s"  # CVTSPOST
    "4s"  # CVTRSTWD
    "4s"  # CVTFETCH
    "4s"  # CVT044R2
    "4s"  # CVTPERFM
    "4s"  # CVTDAIR
    "4s"  # CVTEHDEF
    "4s"  # CVTEHCIR
    "4s"  # CVTSSAP
    "4s"  # CVTAIDVT
    "4s"  # CVTIPCDS
    "4s"  # CVTIPCRI
    "4s"  # CVTIPCRP
    "4s"  # CVTPCCAT
    "4s"  # CVTLCCAT
    "4s"  # CVTXSFT
    "4s"  # CVTXSTKS
    "4s"  # CVTXSTKN
    "4s"  # CVTXUNSS
    "4s"  # CVTPWI
    "4s"  # CVTPVBP
    "4s"  # CVTMFCTL
    "4s"  # CVTMFRTR
    "4s"  # CVTVPSIB
    "4s"  # CVTVSI
    "4s"  # CVTEXCL
    "4s"  # CVTXUNSN
    "4s"  # CVTISNBR
    "4s"  # CVTXEXTR
    "4s"  # CVTMSFRM
    "4s"  # CVTSCPIN
    "4s"  # CVTWSMA
    "4s"  # CVTRMBR
    "4s"  # CVTLFRM
    "4s"  # CVTGMBR
    "4s"  # CVT0TC0A
    "4s"  # CVTRLSTG
    "4s"  # CVTSPFRR
    "4s"  # CVTRS360
    "4s"  # CVTSVT
    "4s"  # CVTIRECM
    "4s"  # CVTDARCM
    "4s"  # CVT0PT02
    "4s"  # CVTRS374
    "4s"  # CVTWTCB
    "4s"  # CVTVACR
    "4s"  # CVTRECON
    "4s"  # CVTGTFR8
    "4s"  # CVTVSTOP
    "4s"  # CVTVPSA
    "4s"  # CVTRMPTT
    "4s"  # CVTRMPMT
    "4s"  # CVTEXP1
    "4s"  # CVTCSDRL
    "4s"  # CVTSSRB
    "4s"  # CVTRS3A4
    "4s"  # CVTQV1
    "4s"  # CVTQV2
    "4s"  # CVTQV3
    "4s"  # CVTGSDA
    "4s"  # CVTADV
    "4s"  # CVTTPIO
    "4s"  # CVTRS3C0
    "4s"  # CVTEVENT
    "4s"  # CVTSSCR
    "4s"  # CVTCBBR
    "4s"  # CVTEFF02
    "4s"  # CVTLSCH
    "4s"  # CVTCDEQ
    "4s"  # CVTHSM
    "4s"  # CVTRAC
    "4s"  # CVTCGK
    "4s"  # CVTSRM
    "4s"  # CVT0PT0E
    "4s"  # CVT0PT03
    "4s"  # CVTTCASP
    "4s"  # CVTCTTVT
    "4s"  # CVTJTERM
    "4s"  # CVTRSUME
    "4s"  # CVTTCTL
    "4s"  # CVTRMT
    "4s"  # CVTT6SVC
    "4s"  # CVTSUSP
    "4s"  # CVTIHASU
    "4s"  # CVTSFV
    "4s"  # CVTIDEVN
    "4s"  # CVTSMF83
    "4s"  # CVTSMFSP
    "4s"  # CVTMSFCB
    "4s"  # CVTHID
    "4s"  # CVTPSXM
    "4s"  # CVTUCBSC
    "4s"  # CVTTPUR
    "4s"  # CVTDPUR
    "4s"  # CVTTRPOS
    "4s"  # CVTRS444
    "2s"  # CVTXCPCT
    "2s"  # CVTCALL
    "4s"  # CVTVFIND
    "4s"  # CVTVFGET
    "4s"  # CVTVFMEM
    "4s"  # CVTVFCB
    "4s"  # CVTPGSER
    "4s"  # CVTTSKI
    "4s"  # CVTCPGUB
    "4s"  # CVTCPGUP
    "4s"  # CVTCPGTC
    "4s"  # CVTCPFRE
    "4s"  # CVTSLIST
    "4s"  # CVTSREGN
    "4s"  # CVTSLOC
    "4s"  # CVTCPBDB
    "4s"  # CVTCPDLB
    "4s"  # CVTDOFFS
    "4s"  # CVTDOFFE
    "4s"  # CVTRCEP
    "4s"  # CVTCPGUS
    "4s"  # CVTGRRGN
    "4s"  # CVTGVRGN
    "1s"  # CVTIONLV
    "3s"  # CVTRS4A1
    "2x"  
    "2s"  # CVTRS4A2
    "4s"  # CVTFUNC
    "4s"  # CVTSMEXT
    "4s"  # CVTNUCMP
    "1s"  # CVTXAFL
    "3s"  # CVTRS4B5
    "4s"  # CVTVTAM
    "4s"  # CVTSPIP
    "4s"  # CVTDFA
    "4s"  # CVTNVT0
    "4s"  # CVTCSOMF
    "4s"  # CVTCSOAL
    "4s"  # CVTICHPT
    "4s"  # CVTCSOCR
    "4s"  # CVTCSOCS
    "4s"  # CVTLLTA
    "4s"  # CVTDCQA
    "4s"  # CVTUCBA
    "4s"  # CVTVESTU
    "4s"  # CVTNUCLU
    "16s"  # CVTOSLVL
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
    "CVTPRLTV",
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
    "CVTQTE00",
    "CVTQTD00",
    "CVTSTB",
    "CVTDCB",
    "CVTDCBA",
    "CVTSV76M",
    "CVTIXAVL",
    "CVTNUCB",
    "CVTFBOSV",
    "CVT0DS",
    "CVTECVT",
    "CVTDAIRX",
    "CVTMSER",
    "CVT0PT01",
    "CVTTVT",
    "CVT040ID",
    "CVTMZ00",
    "CVT1EF00",
    "CVTQOCR",
    "CVTQMWR",
    "CVTSNCTR",
    "CVTOPTA",
    "CVTOPTB",
    "CVTQCDSR",
    "CVTQLPAQ",
    "CVTENFCT",
    "CVTSMCA",
    "CVTABEND",
    "CVTUSER",
    "CVTMDLDS",
    "CVTQABST",
    "CVTLNKSC",
    "CVTTSCE",
    "CVTPATCH",
    "CVTRMS",
    "CVTSPDME",
    "CVT0SCR1",
    "CVTGTF",
    "CVTAQAVT",
    "CVTFLAG5",
    "CVTFLAG6",
    "CVTFLAG7",
    "CVTFLAG8",
    "CVTSAF",
    "CVTEXT1",
    "CVTCBSP",
    "CVTPURG",
    "CVTAMFF",
    "CVTQMSG",
    "CVTDMSR",
    "CVTSFR",
    "CVTGXL",
    "CVTREAL",
    "CVTPTRV",
    "CVTIHVP",
    "CVTJESCT",
    "CVTRS12C",
    "CVTTZ",
    "CVTMCHPR",
    "CVTEORM",
    "CVTPTRV3",
    "CVTLKRM",
    "CVTAPF",
    "CVTEXT2",
    "CVTHJES",
    "CVTRSTW2",
    "CVTSNAME",
    "CVTGETL",
    "CVTLPDSR",
    "CVTPVTP",
    "CVTLPDIA",
    "CVTRBCB",
    "CVTRS170",
    "CVTSLIDA",
    "CVTFLAGS",
    "CVTRT03",
    "CVTRS180",
    "CVTEXSNR",
    "CVTEXSNL",
    "CVTSPVLK",
    "CVTCTLFG",
    "CVTAPG",
    "CVTRSCN",
    "CVTTAS",
    "CVTTRCRM",
    "CVTSHRVM",
    "CVT0VL01",
    "CVTPPGMX",
    "CVTGRSST",
    "CVTFLAG9",
    "CVTBSM0F",
    "CVTGVT",
    "CVTASCRF",
    "CVTASCRL",
    "CVTPUTL",
    "CVTSRBRT",
    "CVTOLT0A",
    "CVTSMFEX",
    "CVTCSPIE",
    "CVTPTGT",
    "CVTSIGPT",
    "CVTSPDMC",
    "CVTDSSAC",
    "CVTRS1D7",
    "CVTSTCK",
    "CVTMAXMP",
    "CVTBSM2",
    "CVTSCAN",
    "CVTAUTHL",
    "CVTBLDCP",
    "CVTGETCL",
    "CVTFRECL",
    "CVTDELCP",
    "CVTCRMN",
    "CVTCRAS",
    "CVTQSAS",
    "CVTFRAS",
    "CVTS1EE",
    "CVTPARS",
    "CVTQUIS",
    "CVTSTXU",
    "CVTOPTE",
    "CVTSDRM",
    "CVTCSRT",
    "CVTAQTOP",
    "CVTVVMDI",
    "CVTASVT",
    "CVTGDA",
    "CVTASCBH",
    "CVTASCBL",
    "CVTRTMCT",
    "CVTSV60",
    "CVTSDMP",
    "CVTSCBP",
    "CVTSDBF",
    "CVTRTMS",
    "CVTTPIOS",
    "CVTSIC",
    "CVTOPCTP",
    "CVTEXPRO",
    "CVTGSMQ",
    "CVTLSMQ",
    "CVTRS26C",
    "CVTVWAIT",
    "CVTPARRL",
    "CVTAPFT",
    "CVTQCS01",
    "CVTFQCB",
    "CVTLQCB",
    "CVTRENQ",
    "CVTRSPIE",
    "CVTLKRMA",
    "CVTCSD",
    "CVTDQIQE",
    "CVTRPOST",
    "CVT062R1",
    "CVTVEAC0",
    "CVTGLMN",
    "CVTSPSA",
    "CVTWSAL",
    "CVTWSAG",
    "CVTWSAC",
    "CVTRECRQ",
    "CVTASMVT",
    "CVTIOBP",
    "CVTSPOST",
    "CVTRSTWD",
    "CVTFETCH",
    "CVT044R2",
    "CVTPERFM",
    "CVTDAIR",
    "CVTEHDEF",
    "CVTEHCIR",
    "CVTSSAP",
    "CVTAIDVT",
    "CVTIPCDS",
    "CVTIPCRI",
    "CVTIPCRP",
    "CVTPCCAT",
    "CVTLCCAT",
    "CVTXSFT",
    "CVTXSTKS",
    "CVTXSTKN",
    "CVTXUNSS",
    "CVTPWI",
    "CVTPVBP",
    "CVTMFCTL",
    "CVTMFRTR",
    "CVTVPSIB",
    "CVTVSI",
    "CVTEXCL",
    "CVTXUNSN",
    "CVTISNBR",
    "CVTXEXTR",
    "CVTMSFRM",
    "CVTSCPIN",
    "CVTWSMA",
    "CVTRMBR",
    "CVTLFRM",
    "CVTGMBR",
    "CVT0TC0A",
    "CVTRLSTG",
    "CVTSPFRR",
    "CVTRS360",
    "CVTSVT",
    "CVTIRECM",
    "CVTDARCM",
    "CVT0PT02",
    "CVTRS374",
    "CVTWTCB",
    "CVTVACR",
    "CVTRECON",
    "CVTGTFR8",
    "CVTVSTOP",
    "CVTVPSA",
    "CVTRMPTT",
    "CVTRMPMT",
    "CVTEXP1",
    "CVTCSDRL",
    "CVTSSRB",
    "CVTRS3A4",
    "CVTQV1",
    "CVTQV2",
    "CVTQV3",
    "CVTGSDA",
    "CVTADV",
    "CVTTPIO",
    "CVTRS3C0",
    "CVTEVENT",
    "CVTSSCR",
    "CVTCBBR",
    "CVTEFF02",
    "CVTLSCH",
    "CVTCDEQ",
    "CVTHSM",
    "CVTRAC",
    "CVTCGK",
    "CVTSRM",
    "CVT0PT0E",
    "CVT0PT03",
    "CVTTCASP",
    "CVTCTTVT",
    "CVTJTERM",
    "CVTRSUME",
    "CVTTCTL",
    "CVTRMT",
    "CVTT6SVC",
    "CVTSUSP",
    "CVTIHASU",
    "CVTSFV",
    "CVTIDEVN",
    "CVTSMF83",
    "CVTSMFSP",
    "CVTMSFCB",
    "CVTHID",
    "CVTPSXM",
    "CVTUCBSC",
    "CVTTPUR",
    "CVTDPUR",
    "CVTTRPOS",
    "CVTRS444",
    "CVTXCPCT",
    "CVTCALL",
    "CVTVFIND",
    "CVTVFGET",
    "CVTVFMEM",
    "CVTVFCB",
    "CVTPGSER",
    "CVTTSKI",
    "CVTCPGUB",
    "CVTCPGUP",
    "CVTCPGTC",
    "CVTCPFRE",
    "CVTSLIST",
    "CVTSREGN",
    "CVTSLOC",
    "CVTCPBDB",
    "CVTCPDLB",
    "CVTDOFFS",
    "CVTDOFFE",
    "CVTRCEP",
    "CVTCPGUS",
    "CVTGRRGN",
    "CVTGVRGN",
    "CVTIONLV",
    "CVTRS4A1",
    "CVTRS4A2",
    "CVTFUNC",
    "CVTSMEXT",
    "CVTNUCMP",
    "CVTXAFL",
    "CVTRS4B5",
    "CVTVTAM",
    "CVTSPIP",
    "CVTDFA",
    "CVTNVT0",
    "CVTCSOMF",
    "CVTCSOAL",
    "CVTICHPT",
    "CVTCSOCR",
    "CVTCSOCS",
    "CVTLLTA",
    "CVTDCQA",
    "CVTUCBA",
    "CVTVESTU",
    "CVTNUCLU",
    "CVTOSLVL",
)
cvt_offset_length = (
    info(0,4),  # CVTTCBP
    info(4,4),  # CVT0EF00
    info(8,4),  # CVTLINK
    info(12,4),  # CVTAUSCB
    info(16,4),  # CVTBUF
    info(20,4),  # CVTXAPG
    info(24,4),  # CVT0VL00
    info(28,4),  # CVTPCNVT
    info(32,4),  # CVTPRLTV
    info(36,4),  # CVTLLCB
    info(40,4),  # CVTLLTRM
    info(44,4),  # CVTXTLER
    info(48,4),  # CVTSYSAD
    info(52,4),  # CVTBTERM
    info(56,4),  # CVTDATE
    info(60,4),  # CVTMSLT
    info(64,4),  # CVTZDTAB
    info(68,4),  # CVTXITP
    info(72,4),  # CVT0EF01
    info(76,4),  # CVTVPRM
    info(80,2),  # CVTEXIT
    info(82,2),  # CVTBRET
    info(84,4),  # CVTSVDCB
    info(88,4),  # CVTTPC
    info(92,4),  # CVTFLGCS
    info(96,4),  # CVTCVT
    info(100,4),  # CVTCUCB
    info(104,4),  # CVTQTE00
    info(108,4),  # CVTQTD00
    info(112,4),  # CVTSTB
    info(116,1),  # CVTDCB
    info(117,3),  # CVTDCBA
    info(120,4),  # CVTSV76M
    info(124,4),  # CVTIXAVL
    info(128,4),  # CVTNUCB
    info(132,4),  # CVTFBOSV
    info(136,4),  # CVT0DS
    info(140,4),  # CVTECVT
    info(144,4),  # CVTDAIRX
    info(148,4),  # CVTMSER
    info(152,4),  # CVT0PT01
    info(156,4),  # CVTTVT
    info(160,4),  # CVT040ID
    info(164,4),  # CVTMZ00
    info(168,4),  # CVT1EF00
    info(172,4),  # CVTQOCR
    info(176,4),  # CVTQMWR
    info(180,2),  # CVTSNCTR
    info(182,1),  # CVTOPTA
    info(183,1),  # CVTOPTB
    info(184,4),  # CVTQCDSR
    info(188,4),  # CVTQLPAQ
    info(192,4),  # CVTENFCT
    info(196,4),  # CVTSMCA
    info(200,4),  # CVTABEND
    info(204,4),  # CVTUSER
    info(208,4),  # CVTMDLDS
    info(212,2),  # CVTQABST
    info(214,2),  # CVTLNKSC
    info(216,4),  # CVTTSCE
    info(220,4),  # CVTPATCH
    info(224,4),  # CVTRMS
    info(228,4),  # CVTSPDME
    info(232,4),  # CVT0SCR1
    info(236,4),  # CVTGTF
    info(240,4),  # CVTAQAVT
    info(244,1),  # CVTFLAG5
    info(245,1),  # CVTFLAG6
    info(246,1),  # CVTFLAG7
    info(247,1),  # CVTFLAG8
    info(248,4),  # CVTSAF
    info(252,4),  # CVTEXT1
    info(256,4),  # CVTCBSP
    info(260,4),  # CVTPURG
    info(264,4),  # CVTAMFF
    info(268,4),  # CVTQMSG
    info(272,4),  # CVTDMSR
    info(276,4),  # CVTSFR
    info(280,4),  # CVTGXL
    info(284,4),  # CVTREAL
    info(288,4),  # CVTPTRV
    info(292,4),  # CVTIHVP
    info(296,4),  # CVTJESCT
    info(300,4),  # CVTRS12C
    info(304,4),  # CVTTZ
    info(308,4),  # CVTMCHPR
    info(312,4),  # CVTEORM
    info(316,4),  # CVTPTRV3
    info(320,4),  # CVTLKRM
    info(324,4),  # CVTAPF
    info(328,4),  # CVTEXT2
    info(332,4),  # CVTHJES
    info(336,4),  # CVTRSTW2
    info(340,8),  # CVTSNAME
    info(348,4),  # CVTGETL
    info(352,4),  # CVTLPDSR
    info(356,4),  # CVTPVTP
    info(360,4),  # CVTLPDIA
    info(364,4),  # CVTRBCB
    info(368,4),  # CVTRS170
    info(372,4),  # CVTSLIDA
    info(376,4),  # CVTFLAGS
    info(380,4),  # CVTRT03
    info(384,8),  # CVTRS180
    info(392,4),  # CVTEXSNR
    info(396,1),  # CVTEXSNL
    info(397,1),  # CVTSPVLK
    info(398,1),  # CVTCTLFG
    info(399,1),  # CVTAPG
    info(404,4),  # CVTRSCN
    info(408,4),  # CVTTAS
    info(412,4),  # CVTTRCRM
    info(416,4),  # CVTSHRVM
    info(420,4),  # CVT0VL01
    info(424,4),  # CVTPPGMX
    info(428,1),  # CVTGRSST
    info(429,1),  # CVTFLAG9
    info(430,2),  # CVTBSM0F
    info(432,4),  # CVTGVT
    info(436,4),  # CVTASCRF
    info(440,4),  # CVTASCRL
    info(444,4),  # CVTPUTL
    info(448,4),  # CVTSRBRT
    info(452,4),  # CVTOLT0A
    info(456,4),  # CVTSMFEX
    info(460,4),  # CVTCSPIE
    info(464,4),  # CVTPTGT
    info(468,1),  # CVTSIGPT
    info(469,1),  # CVTSPDMC
    info(470,1),  # CVTDSSAC
    info(471,1),  # CVTRS1D7
    info(472,4),  # CVTSTCK
    info(476,2),  # CVTMAXMP
    info(478,2),  # CVTBSM2
    info(480,4),  # CVTSCAN
    info(484,4),  # CVTAUTHL
    info(488,4),  # CVTBLDCP
    info(492,4),  # CVTGETCL
    info(496,4),  # CVTFRECL
    info(500,4),  # CVTDELCP
    info(504,4),  # CVTCRMN
    info(508,4),  # CVTCRAS
    info(512,4),  # CVTQSAS
    info(516,4),  # CVTFRAS
    info(520,4),  # CVTS1EE
    info(524,4),  # CVTPARS
    info(528,4),  # CVTQUIS
    info(532,4),  # CVTSTXU
    info(536,4),  # CVTOPTE
    info(540,4),  # CVTSDRM
    info(544,4),  # CVTCSRT
    info(548,4),  # CVTAQTOP
    info(552,4),  # CVTVVMDI
    info(556,4),  # CVTASVT
    info(560,4),  # CVTGDA
    info(564,4),  # CVTASCBH
    info(568,4),  # CVTASCBL
    info(572,4),  # CVTRTMCT
    info(576,4),  # CVTSV60
    info(580,4),  # CVTSDMP
    info(584,4),  # CVTSCBP
    info(588,4),  # CVTSDBF
    info(592,4),  # CVTRTMS
    info(596,4),  # CVTTPIOS
    info(600,4),  # CVTSIC
    info(604,4),  # CVTOPCTP
    info(608,4),  # CVTEXPRO
    info(612,4),  # CVTGSMQ
    info(616,4),  # CVTLSMQ
    info(620,4),  # CVTRS26C
    info(624,4),  # CVTVWAIT
    info(628,4),  # CVTPARRL
    info(632,4),  # CVTAPFT
    info(636,4),  # CVTQCS01
    info(640,4),  # CVTFQCB
    info(644,4),  # CVTLQCB
    info(648,4),  # CVTRENQ
    info(652,4),  # CVTRSPIE
    info(656,4),  # CVTLKRMA
    info(660,4),  # CVTCSD
    info(664,4),  # CVTDQIQE
    info(668,4),  # CVTRPOST
    info(672,4),  # CVT062R1
    info(676,4),  # CVTVEAC0
    info(680,4),  # CVTGLMN
    info(684,4),  # CVTSPSA
    info(688,4),  # CVTWSAL
    info(692,4),  # CVTWSAG
    info(696,4),  # CVTWSAC
    info(700,4),  # CVTRECRQ
    info(704,4),  # CVTASMVT
    info(708,4),  # CVTIOBP
    info(712,4),  # CVTSPOST
    info(716,4),  # CVTRSTWD
    info(720,4),  # CVTFETCH
    info(724,4),  # CVT044R2
    info(728,4),  # CVTPERFM
    info(732,4),  # CVTDAIR
    info(736,4),  # CVTEHDEF
    info(740,4),  # CVTEHCIR
    info(744,4),  # CVTSSAP
    info(748,4),  # CVTAIDVT
    info(752,4),  # CVTIPCDS
    info(756,4),  # CVTIPCRI
    info(760,4),  # CVTIPCRP
    info(764,4),  # CVTPCCAT
    info(768,4),  # CVTLCCAT
    info(772,4),  # CVTXSFT
    info(776,4),  # CVTXSTKS
    info(780,4),  # CVTXSTKN
    info(784,4),  # CVTXUNSS
    info(788,4),  # CVTPWI
    info(792,4),  # CVTPVBP
    info(796,4),  # CVTMFCTL
    info(800,4),  # CVTMFRTR
    info(804,4),  # CVTVPSIB
    info(808,4),  # CVTVSI
    info(812,4),  # CVTEXCL
    info(816,4),  # CVTXUNSN
    info(820,4),  # CVTISNBR
    info(824,4),  # CVTXEXTR
    info(828,4),  # CVTMSFRM
    info(832,4),  # CVTSCPIN
    info(836,4),  # CVTWSMA
    info(840,4),  # CVTRMBR
    info(844,4),  # CVTLFRM
    info(848,4),  # CVTGMBR
    info(852,4),  # CVT0TC0A
    info(856,4),  # CVTRLSTG
    info(860,4),  # CVTSPFRR
    info(864,4),  # CVTRS360
    info(868,4),  # CVTSVT
    info(872,4),  # CVTIRECM
    info(876,4),  # CVTDARCM
    info(880,4),  # CVT0PT02
    info(884,4),  # CVTRS374
    info(888,4),  # CVTWTCB
    info(892,4),  # CVTVACR
    info(896,4),  # CVTRECON
    info(900,4),  # CVTGTFR8
    info(904,4),  # CVTVSTOP
    info(908,4),  # CVTVPSA
    info(912,4),  # CVTRMPTT
    info(916,4),  # CVTRMPMT
    info(920,4),  # CVTEXP1
    info(924,4),  # CVTCSDRL
    info(928,4),  # CVTSSRB
    info(932,4),  # CVTRS3A4
    info(936,4),  # CVTQV1
    info(940,4),  # CVTQV2
    info(944,4),  # CVTQV3
    info(948,4),  # CVTGSDA
    info(952,4),  # CVTADV
    info(956,4),  # CVTTPIO
    info(960,4),  # CVTRS3C0
    info(964,4),  # CVTEVENT
    info(968,4),  # CVTSSCR
    info(972,4),  # CVTCBBR
    info(976,4),  # CVTEFF02
    info(980,4),  # CVTLSCH
    info(984,4),  # CVTCDEQ
    info(988,4),  # CVTHSM
    info(992,4),  # CVTRAC
    info(996,4),  # CVTCGK
    info(1000,4),  # CVTSRM
    info(1004,4),  # CVT0PT0E
    info(1008,4),  # CVT0PT03
    info(1012,4),  # CVTTCASP
    info(1016,4),  # CVTCTTVT
    info(1020,4),  # CVTJTERM
    info(1024,4),  # CVTRSUME
    info(1028,4),  # CVTTCTL
    info(1032,4),  # CVTRMT
    info(1036,4),  # CVTT6SVC
    info(1040,4),  # CVTSUSP
    info(1044,4),  # CVTIHASU
    info(1048,4),  # CVTSFV
    info(1052,4),  # CVTIDEVN
    info(1056,4),  # CVTSMF83
    info(1060,4),  # CVTSMFSP
    info(1064,4),  # CVTMSFCB
    info(1068,4),  # CVTHID
    info(1072,4),  # CVTPSXM
    info(1076,4),  # CVTUCBSC
    info(1080,4),  # CVTTPUR
    info(1084,4),  # CVTDPUR
    info(1088,4),  # CVTTRPOS
    info(1092,4),  # CVTRS444
    info(1096,2),  # CVTXCPCT
    info(1098,2),  # CVTCALL
    info(1100,4),  # CVTVFIND
    info(1104,4),  # CVTVFGET
    info(1108,4),  # CVTVFMEM
    info(1112,4),  # CVTVFCB
    info(1116,4),  # CVTPGSER
    info(1120,4),  # CVTTSKI
    info(1124,4),  # CVTCPGUB
    info(1128,4),  # CVTCPGUP
    info(1132,4),  # CVTCPGTC
    info(1136,4),  # CVTCPFRE
    info(1140,4),  # CVTSLIST
    info(1144,4),  # CVTSREGN
    info(1148,4),  # CVTSLOC
    info(1152,4),  # CVTCPBDB
    info(1156,4),  # CVTCPDLB
    info(1160,4),  # CVTDOFFS
    info(1164,4),  # CVTDOFFE
    info(1168,4),  # CVTRCEP
    info(1172,4),  # CVTCPGUS
    info(1176,4),  # CVTGRRGN
    info(1180,4),  # CVTGVRGN
    info(1184,1),  # CVTIONLV
    info(1185,3),  # CVTRS4A1
    info(1190,2),  # CVTRS4A2
    info(1192,4),  # CVTFUNC
    info(1196,4),  # CVTSMEXT
    info(1200,4),  # CVTNUCMP
    info(1204,1),  # CVTXAFL
    info(1205,3),  # CVTRS4B5
    info(1208,4),  # CVTVTAM
    info(1212,4),  # CVTSPIP
    info(1216,4),  # CVTDFA
    info(1220,4),  # CVTNVT0
    info(1224,4),  # CVTCSOMF
    info(1228,4),  # CVTCSOAL
    info(1232,4),  # CVTICHPT
    info(1236,4),  # CVTCSOCR
    info(1240,4),  # CVTCSOCS
    info(1244,4),  # CVTLLTA
    info(1248,4),  # CVTDCQA
    info(1252,4),  # CVTUCBA
    info(1256,4),  # CVTVESTU
    info(1260,4),  # CVTNUCLU
    info(1264,16),  # CVTOSLVL
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
