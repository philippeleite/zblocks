from app.models.base import info, zblocks_list
from app.utils import read_memory
from struct import Struct
from collections import namedtuple

zblocks_list.append('PSA')

psa_pattern = Struct(
    ">"
    "4s"  # FLCRNPSW
    "4s"  # FLCRNPSW2
    "8s"  # FLCROPSW
    "4s"  # FLCCVT
    "4s"  # FLCRESV1
    "8s"  # FLCEOPSW
    "8s"  # FLCSOPSW
    "8s"  # FLCPOPSW
    "8s"  # FLCMOPSW
    "8s"  # FLCIOPSW
    "8s"  # FLCRESV2
    "8s"  # FLCCVT64
    "4s"  # FLCRESV3
    "4s"  # FLCTRACE
    "4s"  # FLCENPSW
    "4s"  # FLCENPSW2
    "4s"  # FLCSNPSW
    "4s"  # FLCSNPSW2
    "4s"  # FLCPNPSW
    "4s"  # FLCPNPSW2
    "4s"  # FLCMNPSW
    "4s"  # FLCMNPSW2
    "4s"  # FLCINPSW
    "4s"  # FLCINPSW2
    "4s"  # PSAEPARM
    "4s"  # PSAEEPSW
    "4s"  # PSAESPSW
    "8s"  # PSAEPPSW
    "1s"  # FLCRESV4
    "1s"  # FLCMCNUM
    "1s"  # FLCPERCD
    "1s"  # FLCATMID
    "4s"  # FLCPER
    "1s"  # FLCRESV5
    "3s"  # FLCMTRCD
    "1s"  # FLCTEARN
    "1s"  # FLCPERRN
    "1s"  # FLCRESV6
    "1s"  # FLCARCH
    "4s"  # PSAMPL
    "16s" # FLCRESV7 
    "8s"  # FLCIOCDP
    "8s"  # FLCRESV8
    "16s"  # FLCFACL
    "16s"  # FLCFACLE
    "8s"  # FLCMCIC
    "8s"  # FLCRESV9
    "4s"  # FLCFSA
    "4s"  # FLCRESVA
    "16s"  # FLCFLA
    "16s"  # FLCRV110
    "64s"  # FLCARSAV
    "32s"  # FLCFPSAV
    "64s"  # FLCGRSAV
    "64s"  # FLCCRSAV
    "4s"  # PSAPSA
    "2s"  # PSACPUPA
    "2s"  # PSACPULA
    "4s"  # PSAPCCAV
    "4s"  # PSAPCCAR
    "4s"  # PSALCCAV
    "4s"  # PSALCCAR
    "4s"  # PSATNEW
    "4s"  # PSATOLD
    "4s"  # PSAANEW
    "4s"  # PSAAOLD
    "4s"  # PSASUPER
    "9s"  # PSARV22C
    "2s"  # PSA_WORKUNIT_CBF_ATDISP
    "1s"  # PSARV237
    "2s"  # PSA_WORKUNIT_PROCCLASSATDISP
    "2s"  # PSAPROCCLASS
    "1s"  # PSAPTYPE
    "1s"  # PSAILS
    "2s"  # PSALSVCI
    "1s"  # PSAFLAGS
    "10s"  # PSARV241
    "1s"  # PSASCAFF
    "4s"  # PSALKCRF
    "8s"  # PSAMPSW
    "8s"  # PSAICNT
    "1s"  # PSAXAD
    "1s"  # PSAINTSM
    "14s"  # PSARV262
    "4s"  # PSASTOSM
    "4s"  # PSAHLHIS
    "1s"  # PSARECUR
    "1s"  # PSARSSM
    "1s"  # PSASNSM2
    "1s"  # PSARTM1S
    "4s"  # PSALWTSA
    "4s"  # PSADISPL
    "4s"  # PSAASML
    "4s"  # PSASALCL
    "4s"  # PSAIOSSL
    "4s"  # PSARSMDL
    "4s"  # PSAIOSUL
    "4s"  # PSARSMQL
    "4s"  # PSARV29C
    "4s"  # PSARV2A0
    "4s"  # PSATPACL
    "4s"  # PSAOPTL
    "4s"  # PSARSMGL
    "4s"  # PSAVFIXL
    "4s"  # PSAASMGL
    "4s"  # PSARSMSL
    "4s"  # PSARSMXL
    "4s"  # PSARSMAL
    "4s"  # PSAVPAGL
    "4s"  # PSARSMCL
    "4s"  # PSARVLK2
    "4s"  # PSARSML
    "4s"  # PSATRCEL
    "4s"  # PSAIOSL
    "4s"  # PSARVLK4
    "4s"  # PSACPUL
    "4s"  # PSARVLK5
    "4s"  # PSACMSL
    "4s"  # PSALOCAL
    "4s"  # PSARVLK6
    "4s"  # PSALCPUA
    "4s"  # PSACLHS
    "4s"  # PSALITA
    "8s"  # PSASTOR8
    "4s"  # PSACR0
    "1s"  # PSAMCHFL
    "1s"  # PSASYMSK
    "1s"  # PSAACTCD
    "1s"  # PSAMCHIC
    "4s"  # PSAWKRAP
    "4s"  # PSAWKVAP
    "2s"  # PSAVSTAP
    "2s"  # PSACPUSA
    "4s"  # PSASTOR
    "90s"  # PSAIDAWK
    "2s"  # PSARET
    "2s"  # PSARETCD
    "2s"  # PSAVAL
    "4s"  # PSACSTK
    "4s"  # PSANSTK
    "4s"  # PSASSTK
    "4s"  # PSASSAV
    "4s"  # PSAMSTK
    "4s"  # PSAMSAV
    "4s"  # PSAPSTK
    "4s"  # PSAPSAV
    "4s"  # PSAESTK1
    "4s"  # PSAESAV1
    "4s"  # PSAESTK2
    "4s"  # PSAESAV2
    "4s"  # PSAESTK3
    "4s"  # PSAESAV3
    "4s"  # PSARSTK
    "4s"  # PSARSAV
    "8s"  # PSALWPSW
    "8s"  # PSARV3C8
    "4s"  # PSATSTK
    "4s"  # PSATSAV
    "4s"  # PSAASTK
    "4s"  # PSAASAV
    "8s"  # PSARTPSW
    "8s"  # PSAPCR0E
    "4s"  # PSASFACC
    "4s"  # PSALSFCC
    "2s"  # PSASVC13
    "1s"  # PSAFPFL
    "1s"  # PSAINTE
    "12s"  # PSARV3FC
    "4s"  # PSAATCVT
    "4s"  # PSAWTCOD
    "4s"  # PSASCWA
    "4s"  # PSARSMSA
    "4s"  # PSASCPSW
    "4s"  # PSASCPSW2
    "4s"  # PSASMPSW
    "4s"  # PSASMPSW2
    "16s"  # PSAPCPSW
    "8s"  # PSARV438
    "16s"  # PSAMCX16
    "16s"  # PSARSP16
    "16s"  # PSAPSWSV16
    "8s"  # PSACPUT
    "4s"  # PSAPCFUN
    "2s"  # PSAPCPS2
    "2s"  # PSARV47E
    "24s"  # PSAPCWKA
    "2s"  # PSAPCPS3
    "2s"  # PSAPCPS4
    "4s"  # PSAMODEW
    "3s"  # FLCRESVB
    "1s"  # PSASTNSM
    "4s"  # PSALKJW
    "8s"  # PSADZERO
    "4s"  # PSALKJW2
    "4s"  # PSALKPT
    "4s"  # PSALAA
    "4s"  # PSALIT2
    "4s"  # PSAECLTP
    "4s"  # PSACLHSE
    "8s"  # PSARV4C8
    "144s"  # PSARV4D0
    "36s"  # PSADIAG560
    "4s"  # PSARV584
    "1s"  # PSAHWFB
    "1s"  # PSACR0CB
    "2s"  # PSARV58A
    "4s"  # PSACR0SV
    "4s"  # PSAPCCR0
    "4s"  # PSARCR0
    "8s"  # PSASTKE
    "4s"  # PSASKPSW
    "4s"  # PSASKPS2
    "4s"  # PSACPCLS
    "4s"  # PSARV5AC
    "4s"  # PSASCFS
    "4s"  # PSAPAWA
    "1s"  # PSASCFB
    "3s"  # PSARV5B9
    "4s"  # PSACR0M1
    "4s"  # PSACR0M2
    "4s"  # PSARV5C4
    "8s"  # PSA_CR0EMASKOFFEXTINT
    "8s"  # PSA_CR0EMASKONEXTINT
    "8s"  # PSA_CR0ESAVEAREA
    "16s"  # PSA_WINDOWWORKAREA
    "8s"  # PSA_WINDOWLASTOPENTOD
    "8s"  # PSA_WINDOWCURRENTTOD
    "80s"  # PSARV600
    "8s"  # PSA_TIME_ON_CP
    "8s"  # PSATIME
    "4s"  # PSASRSAV
    "12s"  # PSAESC8
    "8s"  # PSADEXMW
    "64s"  # PSADSARS
    "8s"  # PSA_PCFLIH_TRACE_INTERRUPT_CPUT
    "8s"  # PSADTSAV
    "16s"  # PSADEXMS
    "8s"  # PSA_TIME_ON_ZCBP_NORMALIZED
    "192s"  # PSARV6E0
    "8s"  # PSAECVT
    "8s"  # PSAXCVT
    "48s"  # PSADATLK
    "4s"  # PSADATOF
    "4s"  # PSADATLN
    "4s"  # PSATBVTV
    "1s"  # PSATRACE
    "3s"  # PSARV7ED
    "8s"  # PSATBVTR
    "4s"  # PSATRVT
    "4s"  # PSATOT
    "4s"  # PSACDSAE
    "4s"  # PSACDSAF
    "4s"  # PSACDSA0
    "4s"  # PSACDSA1
    "4s"  # PSAGSPSW
    "4s"  # PSAGSRGS
    "4s"  # PSA_MASTERASTEREALADDR
    "4s"  # PSASV01R
    "4s"  # PSASV14R
    "4s"  # PSAEMS2R
    "4s"  # PSATRGR0
    "4s"  # PSATRGR1
    "4s"  # PSATRGR2
    "4s"  # PSATRGR3
    "4s"  # PSATRGR4
    "4s"  # PSATRGR5
    "4s"  # PSATRGR6
    "4s"  # PSATRGR7
    "4s"  # PSATRGR8
    "4s"  # PSATRGR9
    "4s"  # PSATRGRA
    "4s"  # PSATRGRB
    "4s"  # PSATRGRC
    "4s"  # PSATRGRD
    "4s"  # PSATRGRE
    "4s"  # PSATRGRF
    "4s"  # PSATRSV1
    "4s"  # PSATRSVS
    "8s"  # PSATRSV2
    "40s"  # PSARV878
    "8s"  # PSAGSAVH
    "64s"  # PSAGSAV
    "4s"  # PSASCRG1
    "4s"  # PSASCRG2
    "12s"  # PSAGPREG
    "4s"  # PSARSREG
    "4s"  # PSAPCGR8
    "4s"  # PSAPCGR9
    "4s"  # PSAPCGRA
    "4s"  # PSAPCGRB
    "4s"  # PSALKR0
    "4s"  # PSALKR1
    "4s"  # PSALKR2
    "4s"  # PSALKR3
    "4s"  # PSALKR4
    "4s"  # PSALKR5
    "4s"  # PSALKR6
    "4s"  # PSALKR7
    "4s"  # PSALKR8
    "4s"  # PSALKR9
    "4s"  # PSALKR10
    "4s"  # PSALKR11
    "4s"  # PSALKR12
    "4s"  # PSALKR13
    "4s"  # PSALKR14
    "4s"  # PSALKR15
    "72s"  # PSASLSA
    "64s"  # PSAJSTSA
    "4s"  # PSASLKR0
    "4s"  # PSASLKR1
    "4s"  # PSASLKR2
    "4s"  # PSASLKR3
    "4s"  # PSASLKR4
    "4s"  # PSASLKR5
    "4s"  # PSASLKR6
    "4s"  # PSASLKR7
    "4s"  # PSASLKR8
    "4s"  # PSASLKR9
    "4s"  # PSASLKRA
    "4s"  # PSASLKRB
    "4s"  # PSASLKRC
    "4s"  # PSASLKRD
    "4s"  # PSASLKRE
    "4s"  # PSASLKRF
    "8s"  # PSA_SETLOCKI_SAVEAREA
    "4s"  # PSA_LASTLOGCPUHELDLOCK
    "24s"  # PSARVA24
    "64s"  # PSASCSAV
    "1s"  # PSASFLGS
    "1s"  # PSAMISCF
    "2s"  # PSARVA7E
    "188s"  # PSARVA80
    "4s"  # PSAGSCH7
    "4s"  # PSAGSCH8
    "4s"  # PSALSCH1
    "4s"  # PSALSCH2
    "4s"  # PSASVT
    "4s"  # PSASVTX
    "4s"  # PSAFFRR
    "4s"  # PSAFFRRS
    "36s" # PSARVB5C
    "1112s" # PSARVB80(88)
    "40s"  # PSARVFD8(40)
)
psa_field_names = (
    "FLCRNPSW",
    "FLCRNPSW2",
    "FLCROPSW",
    "FLCCVT",
    "FLCRESV1",
    "FLCEOPSW",
    "FLCSOPSW",
    "FLCPOPSW",
    "FLCMOPSW",
    "FLCIOPSW",
    "FLCRESV2",
    "FLCCVT64",
    "FLCRESV3",
    "FLCTRACE",
    "FLCENPSW",
    "FLCENPSW2",
    "FLCSNPSW",
    "FLCSNPSW2",
    "FLCPNPSW",
    "FLCPNPSW2",
    "FLCMNPSW",
    "FLCMNPSW2",
    "FLCINPSW",
    "FLCINPSW2",
    "PSAEPARM",
    "PSAEEPSW",
    "PSAESPSW",
    "PSAEPPSW",
    "FLCRESV4",
    "FLCMCNUM",
    "FLCPERCD",
    "FLCATMID",
    "FLCPER",
    "FLCRESV5",
    "FLCMTRCD",
    "FLCTEARN",
    "FLCPERRN",
    "FLCRESV6",
    "FLCARCH",
    "PSAMPL",
    "FLCRESV7",
    "FLCIOCDP",
    "FLCRESV8",
    "FLCFACL",
    "FLCFACLE",
    "FLCMCIC",
    "FLCRESV9",
    "FLCFSA",
    "FLCRESVA",
    "FLCFLA",
    "FLCRV110",
    "FLCARSAV",
    "FLCFPSAV",
    "FLCGRSAV",
    "FLCCRSAV",
    "PSAPSA",
    "PSACPUPA",
    "PSACPULA",
    "PSAPCCAV",
    "PSAPCCAR",
    "PSALCCAV",
    "PSALCCAR",
    "PSATNEW",
    "PSATOLD",
    "PSAANEW",
    "PSAAOLD",
    "PSASUPER",
    "PSARV22C",
    "PSA_WORKUNIT_CBF_ATDISP",
    "PSARV237",
    "PSA_WORKUNIT_PROCCLASSATDISP",
    "PSAPROCCLASS",
    "PSAPTYPE",
    "PSAILS",
    "PSALSVCI",
    "PSAFLAGS",
    "PSARV241",
    "PSASCAFF",
    "PSALKCRF",
    "PSAMPSW",
    "PSAICNT",
    "PSAXAD",
    "PSAINTSM",
    "PSARV262",
    "PSASTOSM",
    "PSAHLHIS",
    "PSARECUR",
    "PSARSSM",
    "PSASNSM2",
    "PSARTM1S",
    "PSALWTSA",
    "PSADISPL",
    "PSAASML",
    "PSASALCL",
    "PSAIOSSL",
    "PSARSMDL",
    "PSAIOSUL",
    "PSARSMQL",
    "PSARV29C",
    "PSARV2A0",
    "PSATPACL",
    "PSAOPTL",
    "PSARSMGL",
    "PSAVFIXL",
    "PSAASMGL",
    "PSARSMSL",
    "PSARSMXL",
    "PSARSMAL",
    "PSAVPAGL",
    "PSARSMCL",
    "PSARVLK2",
    "PSARSML",
    "PSATRCEL",
    "PSAIOSL",
    "PSARVLK4",
    "PSACPUL",
    "PSARVLK5",
    "PSACMSL",
    "PSALOCAL",
    "PSARVLK6",
    "PSALCPUA",
    "PSACLHS",
    "PSALITA",
    "PSASTOR8",
    "PSACR0",
    "PSAMCHFL",
    "PSASYMSK",
    "PSAACTCD",
    "PSAMCHIC",
    "PSAWKRAP",
    "PSAWKVAP",
    "PSAVSTAP",
    "PSACPUSA",
    "PSASTOR",
    "PSAIDAWK",
    "PSARET",
    "PSARETCD",
    "PSAVAL",
    "PSACSTK",
    "PSANSTK",
    "PSASSTK",
    "PSASSAV",
    "PSAMSTK",
    "PSAMSAV",
    "PSAPSTK",
    "PSAPSAV",
    "PSAESTK1",
    "PSAESAV1",
    "PSAESTK2",
    "PSAESAV2",
    "PSAESTK3",
    "PSAESAV3",
    "PSARSTK",
    "PSARSAV",
    "PSALWPSW",
    "PSARV3C8",
    "PSATSTK",
    "PSATSAV",
    "PSAASTK",
    "PSAASAV",
    "PSARTPSW",
    "PSAPCR0E",
    "PSASFACC",
    "PSALSFCC",
    "PSASVC13",
    "PSAFPFL",
    "PSAINTE",
    "PSARV3FC",
    "PSAATCVT",
    "PSAWTCOD",
    "PSASCWA",
    "PSARSMSA",
    "PSASCPSW",
    "PSASCPSW2",
    "PSASMPSW",
    "PSASMPSW2",
    "PSAPCPSW",
    "PSARV438",
    "PSAMCX16",
    "PSARSP16",
    "PSAPSWSV16",
    "PSACPUT",
    "PSAPCFUN",
    "PSAPCPS2",
    "PSARV47E",
    "PSAPCWKA",
    "PSAPCPS3",
    "PSAPCPS4",
    "PSAMODEW",
    "FLCRESVB",
    "PSASTNSM",
    "PSALKJW",
    "PSADZERO",
    "PSALKJW2",
    "PSALKPT",
    "PSALAA",
    "PSALIT2",
    "PSAECLTP",
    "PSACLHSE",
    "PSARV4C8",
    "PSARV4D0",
    "PSADIAG560",
    "PSARV584",
    "PSAHWFB",
    "PSACR0CB",
    "PSARV58A",
    "PSACR0SV",
    "PSAPCCR0",
    "PSARCR0",
    "PSASTKE",
    "PSASKPSW",
    "PSASKPS2",
    "PSACPCLS",
    "PSARV5AC",
    "PSASCFS",
    "PSAPAWA",
    "PSASCFB",
    "PSARV5B9",
    "PSACR0M1",
    "PSACR0M2",
    "PSARV5C4",
    "PSA_CR0EMASKOFFEXTINT",
    "PSA_CR0EMASKONEXTINT",
    "PSA_CR0ESAVEAREA",
    "PSA_WINDOWWORKAREA",
    "PSA_WINDOWLASTOPENTOD",
    "PSA_WINDOWCURRENTTOD",
    "PSARV600",
    "PSA_TIME_ON_CP",
    "PSATIME",
    "PSASRSAV",
    "PSAESC8",
    "PSADEXMW",
    "PSADSARS",
    "PSA_PCFLIH_TRACE_INTERRUPT_CPUT",
    "PSADTSAV",
    "PSADEXMS",
    "PSA_TIME_ON_ZCBP_NORMALIZED",
    "PSARV6E0",
    "PSAECVT",
    "PSAXCVT",
    "PSADATLK",
    "PSADATOF",
    "PSADATLN",
    "PSATBVTV",
    "PSATRACE",
    "PSARV7ED",
    "PSATBVTR",
    "PSATRVT",
    "PSATOT",
    "PSACDSAE",
    "PSACDSAF",
    "PSACDSA0",
    "PSACDSA1",
    "PSAGSPSW",
    "PSAGSRGS",
    "PSA_MASTERASTEREALADDR",
    "PSASV01R",
    "PSASV14R",
    "PSAEMS2R",
    "PSATRGR0",
    "PSATRGR1",
    "PSATRGR2",
    "PSATRGR3",
    "PSATRGR4",
    "PSATRGR5",
    "PSATRGR6",
    "PSATRGR7",
    "PSATRGR8",
    "PSATRGR9",
    "PSATRGRA",
    "PSATRGRB",
    "PSATRGRC",
    "PSATRGRD",
    "PSATRGRE",
    "PSATRGRF",
    "PSATRSV1",
    "PSATRSVS",
    "PSATRSV2",
    "PSARV878",
    "PSAGSAVH",
    "PSAGSAV",
    "PSASCRG1",
    "PSASCRG2",
    "PSAGPREG",
    "PSARSREG",
    "PSAPCGR8",
    "PSAPCGR9",
    "PSAPCGRA",
    "PSAPCGRB",
    "PSALKR0",
    "PSALKR1",
    "PSALKR2",
    "PSALKR3",
    "PSALKR4",
    "PSALKR5",
    "PSALKR6",
    "PSALKR7",
    "PSALKR8",
    "PSALKR9",
    "PSALKR10",
    "PSALKR11",
    "PSALKR12",
    "PSALKR13",
    "PSALKR14",
    "PSALKR15",
    "PSASLSA",
    "PSAJSTSA",
    "PSASLKR0",
    "PSASLKR1",
    "PSASLKR2",
    "PSASLKR3",
    "PSASLKR4",
    "PSASLKR5",
    "PSASLKR6",
    "PSASLKR7",
    "PSASLKR8",
    "PSASLKR9",
    "PSASLKRA",
    "PSASLKRB",
    "PSASLKRC",
    "PSASLKRD",
    "PSASLKRE",
    "PSASLKRF",
    "PSA_SETLOCKI_SAVEAREA",
    "PSA_LASTLOGCPUHELDLOCK",
    "PSARVA24",
    "PSASCSAV",
    "PSASFLGS",
    "PSAMISCF",
    "PSARVA7E",
    "PSARVA80",
    "PSAGSCH7",
    "PSAGSCH8",
    "PSALSCH1",
    "PSALSCH2",
    "PSASVT",
    "PSASVTX",
    "PSAFFRR",
    "PSAFFRRS",
    "PSARVB5C",
    "PSARVB80",
    "PSARVFD8",
)
psa_offset_length = (
    info(0,4),  # FLCRNPSW
    info(4,4),  # FLCRNPSW2
    info(8,8),  # FLCROPSW
    info(16,4),  # FLCCVT
    info(20,4),  # FLCRESV1
    info(24,8),  # FLCEOPSW
    info(32,8),  # FLCSOPSW
    info(40,8),  # FLCPOPSW
    info(48,8),  # FLCMOPSW
    info(56,8),  # FLCIOPSW
    info(64,8),  # FLCRESV2
    info(72,8),  # FLCCVT64
    info(80,4),  # FLCRESV3
    info(84,4),  # FLCTRACE
    info(88,4),  # FLCENPSW
    info(92,4),  # FLCENPSW2
    info(96,4),  # FLCSNPSW
    info(100,4),  # FLCSNPSW2
    info(104,4),  # FLCPNPSW
    info(108,4),  # FLCPNPSW2
    info(112,4),  # FLCMNPSW
    info(116,4),  # FLCMNPSW2
    info(120,4),  # FLCINPSW
    info(124,4),  # FLCINPSW2
    info(128,4),  # PSAEPARM
    info(132,4),  # PSAEEPSW
    info(136,4),  # PSAESPSW
    info(140,8),  # PSAEPPSW
    info(148,1),  # FLCRESV4
    info(149,1),  # FLCMCNUM
    info(150,1),  # FLCPERCD
    info(151,1),  # FLCATMID
    info(152,4),  # FLCPER
    info(156,1),  # FLCRESV5
    info(157,3),  # FLCMTRCD
    info(160,1),  # FLCTEARN
    info(161,1),  # FLCPERRN
    info(162,1),  # FLCRESV6
    info(163,1),  # FLCARCH
    info(164,4),  # PSAMPL
    info(168,16), # FLCRESV7
    info(184,8),  # FLCIOCDP
    info(192,8),  # FLCRESV8
    info(200,16),  # FLCFACL
    info(216,16),  # FLCFACLE
    info(232,8),  # FLCMCIC
    info(240,8),  # FLCRESV9
    info(248,4),  # FLCFSA
    info(252,4),  # FLCRESVA
    info(256,16),  # FLCFLA
    info(272,16),  # FLCRV110
    info(288,64),  # FLCARSAV
    info(352,32),  # FLCFPSAV
    info(384,64),  # FLCGRSAV
    info(448,64),  # FLCCRSAV
    info(512,4),  # PSAPSA
    info(516,2),  # PSACPUPA
    info(518,2),  # PSACPULA
    info(520,4),  # PSAPCCAV
    info(524,4),  # PSAPCCAR
    info(528,4),  # PSALCCAV
    info(532,4),  # PSALCCAR
    info(536,4),  # PSATNEW
    info(540,4),  # PSATOLD
    info(544,4),  # PSAANEW
    info(548,4),  # PSAAOLD
    info(552,4),  # PSASUPER
    info(556,9),  # PSARV22C
    info(565,2),  # PSA_WORKUNIT_CBF_ATDISP
    info(567,1),  # PSARV237
    info(568,2),  # PSA_WORKUNIT_PROCCLASSATDISP
    info(570,2),  # PSAPROCCLASS
    info(572,1),  # PSAPTYPE
    info(573,1),  # PSAILS
    info(574,2),  # PSALSVCI
    info(576,1),  # PSAFLAGS
    info(577,10),  # PSARV241
    info(587,1),  # PSASCAFF
    info(588,4),  # PSALKCRF
    info(592,8),  # PSAMPSW
    info(600,8),  # PSAICNT
    info(608,1),  # PSAXAD
    info(609,1),  # PSAINTSM
    info(610,14),  # PSARV262
    info(624,4),  # PSASTOSM
    info(628,4),  # PSAHLHIS
    info(632,1),  # PSARECUR
    info(633,1),  # PSARSSM
    info(634,1),  # PSASNSM2
    info(635,1),  # PSARTM1S
    info(636,4),  # PSALWTSA
    info(640,4),  # PSADISPL
    info(644,4),  # PSAASML
    info(648,4),  # PSASALCL
    info(652,4),  # PSAIOSSL
    info(656,4),  # PSARSMDL
    info(660,4),  # PSAIOSUL
    info(664,4),  # PSARSMQL
    info(668,4),  # PSARV29C
    info(672,4),  # PSARV2A0
    info(676,4),  # PSATPACL
    info(680,4),  # PSAOPTL
    info(684,4),  # PSARSMGL
    info(688,4),  # PSAVFIXL
    info(692,4),  # PSAASMGL
    info(696,4),  # PSARSMSL
    info(700,4),  # PSARSMXL
    info(704,4),  # PSARSMAL
    info(708,4),  # PSAVPAGL
    info(712,4),  # PSARSMCL
    info(716,4),  # PSARVLK2
    info(720,4),  # PSARSML
    info(724,4),  # PSATRCEL
    info(728,4),  # PSAIOSL
    info(732,4),  # PSARVLK4
    info(736,4),  # PSACPUL
    info(740,4),  # PSARVLK5
    info(744,4),  # PSACMSL
    info(748,4),  # PSALOCAL
    info(752,4),  # PSARVLK6
    info(756,4),  # PSALCPUA
    info(760,4),  # PSACLHS
    info(764,4),  # PSALITA
    info(768,8),  # PSASTOR8
    info(776,4),  # PSACR0
    info(780,1),  # PSAMCHFL
    info(781,1),  # PSASYMSK
    info(782,1),  # PSAACTCD
    info(783,1),  # PSAMCHIC
    info(784,4),  # PSAWKRAP
    info(788,4),  # PSAWKVAP
    info(792,2),  # PSAVSTAP
    info(794,2),  # PSACPUSA
    info(796,4),  # PSASTOR
    info(800,90),  # PSAIDAWK
    info(890,2),  # PSARET
    info(892,2),  # PSARETCD
    info(894,2),  # PSAVAL
    info(896,4),  # PSACSTK
    info(900,4),  # PSANSTK
    info(904,4),  # PSASSTK
    info(908,4),  # PSASSAV
    info(912,4),  # PSAMSTK
    info(916,4),  # PSAMSAV
    info(920,4),  # PSAPSTK
    info(924,4),  # PSAPSAV
    info(928,4),  # PSAESTK1
    info(932,4),  # PSAESAV1
    info(936,4),  # PSAESTK2
    info(940,4),  # PSAESAV2
    info(944,4),  # PSAESTK3
    info(948,4),  # PSAESAV3
    info(952,4),  # PSARSTK
    info(956,4),  # PSARSAV
    info(960,8),  # PSALWPSW
    info(968,8),  # PSARV3C8
    info(976,4),  # PSATSTK
    info(980,4),  # PSATSAV
    info(984,4),  # PSAASTK
    info(988,4),  # PSAASAV
    info(992,8),  # PSARTPSW
    info(1000,8),  # PSAPCR0E
    info(1008,4),  # PSASFACC
    info(1012,4),  # PSALSFCC
    info(1016,2),  # PSASVC13
    info(1018,1),  # PSAFPFL
    info(1019,1),  # PSAINTE
    info(1020,12),  # PSARV3FC
    info(1032,4),  # PSAATCVT
    info(1036,4),  # PSAWTCOD
    info(1040,4),  # PSASCWA
    info(1044,4),  # PSARSMSA
    info(1048,4),  # PSASCPSW
    info(1052,4),  # PSASCPSW2
    info(1056,4),  # PSASMPSW
    info(1060,4),  # PSASMPSW2
    info(1064,16),  # PSAPCPSW
    info(1080,8),  # PSARV438
    info(1088,16),  # PSAMCX16
    info(1104,16),  # PSARSP16
    info(1120,16),  # PSAPSWSV16
    info(1136,8),  # PSACPUT
    info(1144,4),  # PSAPCFUN
    info(1148,2),  # PSAPCPS2
    info(1150,2),  # PSARV47E
    info(1152,24),  # PSAPCWKA
    info(1176,2),  # PSAPCPS3
    info(1178,2),  # PSAPCPS4
    info(1180,4),  # PSAMODEW
    info(1184,3),  # FLCRESVB
    info(1187,1),  # PSASTNSM
    info(1188,4),  # PSALKJW
    info(1192,8),  # PSADZERO
    info(1200,4),  # PSALKJW2
    info(1204,4),  # PSALKPT
    info(1208,4),  # PSALAA
    info(1212,4),  # PSALIT2
    info(1216,4),  # PSAECLTP
    info(1220,4),  # PSACLHSE
    info(1224,8),  # PSARV4C8
    info(1232,144),  # PSARV4D0
    info(1376,36),  # PSADIAG560
    info(1412,4),  # PSARV584
    info(1416,1),  # PSAHWFB
    info(1417,1),  # PSACR0CB
    info(1418,2),  # PSARV58A
    info(1420,4),  # PSACR0SV
    info(1424,4),  # PSAPCCR0
    info(1428,4),  # PSARCR0
    info(1432,8),  # PSASTKE
    info(1440,4),  # PSASKPSW
    info(1444,4),  # PSASKPS2
    info(1448,4),  # PSACPCLS
    info(1452,4),  # PSARV5AC
    info(1456,4),  # PSASCFS
    info(1460,4),  # PSAPAWA
    info(1464,1),  # PSASCFB
    info(1465,3),  # PSARV5B9
    info(1468,4),  # PSACR0M1
    info(1472,4),  # PSACR0M2
    info(1476,4),  # PSARV5C4
    info(1480,8),  # PSA_CR0EMASKOFFEXTINT
    info(1488,8),  # PSA_CR0EMASKONEXTINT
    info(1496,8),  # PSA_CR0ESAVEAREA
    info(1504,16),  # PSA_WINDOWWORKAREA
    info(1520,8),  # PSA_WINDOWLASTOPENTOD
    info(1528,8),  # PSA_WINDOWCURRENTTOD
    info(1536,80),  # PSARV600
    info(1616,8),  # PSA_TIME_ON_CP
    info(1624,8),  # PSATIME
    info(1632,4),  # PSASRSAV
    info(1636,12),  # PSAESC8
    info(1648,8),  # PSADEXMW
    info(1656,64),  # PSADSARS
    info(1720,8),  # PSA_PCFLIH_TRACE_INTERRUPT_CPUT
    info(1728,8),  # PSADTSAV
    info(1736,16),  # PSADEXMS
    info(1752,8),  # PSA_TIME_ON_ZCBP_NORMALIZED
    info(1760,192),  # PSARV6E0
    info(1952,8),  # PSAECVT
    info(1960,8),  # PSAXCVT
    info(1968,48),  # PSADATLK
    info(2016,4),  # PSADATOF
    info(2020,4),  # PSADATLN
    info(2024,4),  # PSATBVTV
    info(2028,1),  # PSATRACE
    info(2029,3),  # PSARV7ED
    info(2032,8),  # PSATBVTR
    info(2040,4),  # PSATRVT
    info(2044,4),  # PSATOT
    info(2048,4),  # PSACDSAE
    info(2052,4),  # PSACDSAF
    info(2056,4),  # PSACDSA0
    info(2060,4),  # PSACDSA1
    info(2064,4),  # PSAGSPSW
    info(2068,4),  # PSAGSRGS
    info(2072,4),  # PSA_MASTERASTEREALADDR
    info(2076,4),  # PSASV01R
    info(2080,4),  # PSASV14R
    info(2084,4),  # PSAEMS2R
    info(2088,4),  # PSATRGR0
    info(2092,4),  # PSATRGR1
    info(2096,4),  # PSATRGR2
    info(2100,4),  # PSATRGR3
    info(2104,4),  # PSATRGR4
    info(2108,4),  # PSATRGR5
    info(2112,4),  # PSATRGR6
    info(2116,4),  # PSATRGR7
    info(2120,4),  # PSATRGR8
    info(2124,4),  # PSATRGR9
    info(2128,4),  # PSATRGRA
    info(2132,4),  # PSATRGRB
    info(2136,4),  # PSATRGRC
    info(2140,4),  # PSATRGRD
    info(2144,4),  # PSATRGRE
    info(2148,4),  # PSATRGRF
    info(2152,4),  # PSATRSV1
    info(2156,4),  # PSATRSVS
    info(2160,8),  # PSATRSV2
    info(2168,40),  # PSARV878
    info(2208,8),  # PSAGSAVH
    info(2216,64),  # PSAGSAV
    info(2280,4),  # PSASCRG1
    info(2284,4),  # PSASCRG2
    info(2288,12),  # PSAGPREG
    info(2300,4),  # PSARSREG
    info(2304,4),  # PSAPCGR8
    info(2308,4),  # PSAPCGR9
    info(2312,4),  # PSAPCGRA
    info(2316,4),  # PSAPCGRB
    info(2320,4),  # PSALKR0
    info(2324,4),  # PSALKR1
    info(2328,4),  # PSALKR2
    info(2332,4),  # PSALKR3
    info(2336,4),  # PSALKR4
    info(2340,4),  # PSALKR5
    info(2344,4),  # PSALKR6
    info(2348,4),  # PSALKR7
    info(2352,4),  # PSALKR8
    info(2356,4),  # PSALKR9
    info(2360,4),  # PSALKR10
    info(2364,4),  # PSALKR11
    info(2368,4),  # PSALKR12
    info(2372,4),  # PSALKR13
    info(2376,4),  # PSALKR14
    info(2380,4),  # PSALKR15
    info(2384,72),  # PSASLSA
    info(2456,64),  # PSAJSTSA
    info(2520,4),  # PSASLKR0
    info(2524,4),  # PSASLKR1
    info(2528,4),  # PSASLKR2
    info(2532,4),  # PSASLKR3
    info(2536,4),  # PSASLKR4
    info(2540,4),  # PSASLKR5
    info(2544,4),  # PSASLKR6
    info(2548,4),  # PSASLKR7
    info(2552,4),  # PSASLKR8
    info(2556,4),  # PSASLKR9
    info(2560,4),  # PSASLKRA
    info(2564,4),  # PSASLKRB
    info(2568,4),  # PSASLKRC
    info(2572,4),  # PSASLKRD
    info(2576,4),  # PSASLKRE
    info(2580,4),  # PSASLKRF
    info(2584,8),  # PSA_SETLOCKI_SAVEAREA
    info(2592,4),  # PSA_LASTLOGCPUHELDLOCK
    info(2596,24),  # PSARVA24
    info(2620,64),  # PSASCSAV
    info(2684,1),  # PSASFLGS
    info(2685,1),  # PSAMISCF
    info(2686,2),  # PSARVA7E
    info(2688,188),  # PSARVA80
    info(2876,4),  # PSAGSCH7
    info(2880,4),  # PSAGSCH8
    info(2884,4),  # PSALSCH1
    info(2888,4),  # PSALSCH2
    info(2892,4),  # PSASVT
    info(2896,4),  # PSASVTX
    info(2900,4),  # PSAFFRR
    info(2904,4),  # PSAFFRRS
    info(2908,36),  # PSARVB5C
    info(2944,1112),  # PSARVB80
    info(4056,40),  # PSARVFD8
)


psa_fields = namedtuple("cvt", psa_field_names)
cvt_info = psa_fields._make(psa_offset_length)

def get_psa() -> bytearray:
    cvt_buffer = bytearray(psa_pattern.size)
    read_memory(cvt_buffer, len(cvt_buffer), 0)
    return cvt_buffer

class PSA:
    def __init__(self):
        name = "PSA"
        long_name = "Prefix Save Area"
        fields = psa_field_names
        info = cvt_info
        content = psa_fields._make(psa_pattern.unpack(get_psa()))
        self.content = content
