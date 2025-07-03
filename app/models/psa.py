from app.models.base import info, zblocks_list
from app.utils import read_memory
from struct import Struct
from collections import namedtuple

zblocks_list.append('PSA')

psa_pattern = Struct(
    ">"
    "4s"  # FLCRNPSW
    "4s"  # 
    "8s"  # FLCROPSW
    "4s"  # FLCCVT
    "4s"  # 
    "8s"  # FLCEOPSW
    "8s"  # FLCSOPSW
    "8s"  # FLCPOPSW
    "8s"  # FLCMOPSW
    "8s"  # FLCIOPSW
    "8s"  # 
    "8s"  # FLCCVT64(0)
    "4s"  # 
    "4s"  # FLCCVT2
    "4s"  # 
    "4s"  # 
    "4s"  # FLCENPSW
    "4s"  # 
    "4s"  # FLCSNPSW
    "4s"  # 
    "4s"  # FLCPNPSW
    "4s"  # 
    "4s"  # FLCMNPSW
    "4s"  # 
    "4s"  # FLCINPSW
    "4s"  # 
    "4s"  # PSAEPARM
    "4s"  # PSAEEPSW(0)
    "2s"  # PSASPAD
    "2s"  # FLCEICOD
    "4s"  # PSAESPSW(0)
    "1s"  # 
    "1s"  # FLCSVILC
    "2s"  # FLCSVCN
    "8s"  # PSAEPPSW(0)
    "1s"  # 
    "1s"  # FLCPIILC
    "2s"  # FLCPICOD(0)
    "1s"  # PSAEECOD
    "1s"  # PSAPICOD
    "4s"  # FLCTEA(0)
    "3s"  # 
    "1s"  # FLCDXC(0)
    "1s"  # FLCTEAB3
    "1s"  # 
    "1s"  # FLCMCNUM
    "1s"  # FLCPERCD
    "1s"  # FLCATMID
    "4s"  # FLCPER
    "1s"  # 
    "3s"  # FLCMTRCD
    "1s"  # FLCTEARN
    "1s"  # FLCPERRN
    "1s"  # 
    "1s"  # FLCARCH
    "4s"  # PSAMPL
    "344s"  # (0)
    "16s"  # 
    "8s"  # FLCIOCDP(0)
    "4s"  # FLCSID
    "4s"  # FLCIOFP
    "8s"  # 
    "16s"  # FLCFACL(0)
    "1s"  # FLCFACL0
    "1s"  # FLCFACL1
    "1s"  # FLCFACL2
    "1s"  # FLCFACL3
    "1s"  # FLCFACL4
    "1s"  # FLCFACL5
    "1s"  # FLCFACL6
    "1s"  # FLCFACL7
    "1s"  # FLCFACL8
    "1s"  # FLCFACL9
    "6s"  # 
    "16s"  # FLCFACLE
    "8s"  # FLCMCIC
    "8s"  # 
    "4s"  # FLCFSA
    "4s"  # 
    "16s"  # FLCFLA
    "16s"  # FLCRV110
    "4s"  # FLCARSAV(16)
    "32s"  # FLCFPSAV
    "4s"  # FLCGRSAV(16)
    "4s"  # FLCCRSAV(16)
    "8s"  # FLCHDEND(0)
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
    "4s"  # PSASUPER(0)
    "1s"  # PSASUP1
    "1s"  # PSASUP2
    "1s"  # PSASUP3
    "1s"  # PSASUP4
    "9s"  # PSARV22C
    "2s"  # PSA_WORKUNIT_CBF_ATDISP
    "1s"  # PSARV237
    "2s"  # PSAPROCCLASS
    "2s"  # PSA_BYLPAR_PROCCLASS
    "1s"  # PSAPROCCLASS_BYTE0
    "1s"  # PSAPROCCLASS_BYTE1
    "1s"  # PSA_BYLPAR_PROCCLASS_BYTE0
    "1s"  # PSA_BYLPAR_PROCCLASS_BYTE1
    "1s"  # PSAPTYPE
    "1s"  # PSAILS
    "2s"  # PSALSVCI
    "1s"  # PSAFLAGS
    "10s"  # PSARV241
    "1s"  # PSASCAFF
    "4s"  # PSALKCRF
    "8s"  # (0)
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
    "116s"  # PSACLHT(0)
    "80s"  # PSACLHT1(0)
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
    "16s"  # PSACLHT2(0)
    "4s"  # PSARSML
    "4s"  # PSATRCEL
    "4s"  # PSAIOSL
    "4s"  # PSARVLK4
    "8s"  # PSACLHT3(0)
    "4s"  # PSACPUL
    "4s"  # PSARVLK5
    "12s"  # PSACLHT4(0)
    "4s"  # PSACMSL
    "4s"  # PSALOCAL
    "4s"  # PSARVLK6
    "4s"  # PSALCPUA
    "4s"  # PSAHLHI(0)
    "4s"  # PSACLHS(0)
    "1s"  # PSACLHS1
    "1s"  # PSACLHS2
    "1s"  # PSACLHS3
    "1s"  # PSACLHS4
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
    "2s"  # PSAVAL(0)
    "1s"  # PSAVAL_MACHINE
    "1s"  # 
    "64s"  # PSARSVT(0)
    "64s"  # PSARSVTE(0)
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
    "8s"  # (0)
    "8s"  # PSALWPSW
    "8s"  # PSARV3C8
    "4s"  # PSATSTK
    "4s"  # PSATSAV
    "4s"  # PSAASTK
    "4s"  # PSAASAV
    "8s"  # (0)
    "8s"  # PSARTPSW
    "8s"  # PSAPCR0E
    "4s"  # (0)
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
    "8s"  # (0)
    "4s"  # PSASCPSW
    "4s"  # 
    "8s"  # (0)
    "4s"  # PSASMPSW
    "4s"  # 
    "8s"  # (0)
    "16s"  # PSAPCPSW
    "8s"  # PSARV438
    "8s"  # (0)
    "16s"  # PSAMCX16
    "16s"  # PSARSP16
    "16s"  # PSAPSWSV16
    "8s"  # 
    "8s"  # PSAPSWSV
    "8s"  # (0)
    "8s"  # PSACPUT
    "4s"  # PSAPCFUN(0)
    "1s"  # PSAPCFB1
    "1s"  # PSAPCFB2
    "1s"  # PSAPCFB3
    "1s"  # PSAPCFB4
    "2s"  # PSAPCPS2
    "2s"  # PSARV47E
    "24s"  # PSAPCWKA
    "2s"  # PSAPCPS3
    "2s"  # PSAPCPS4
    "4s"  # PSAMODEW(0)
    "1s"  # 
    "1s"  # PSAMFLGS
    "1s"  # PSAMODEH
    "1s"  # PSAMODE
    "3s"  # 
    "1s"  # PSASTNSM
    "4s"  # PSALKJW
    "8s"  # PSADZERO(0)
    "4s"  # PSAFZERO
    "4s"  # 
    "4s"  # PSALKJW2
    "4s"  # PSALKPT
    "4s"  # PSALAA
    "4s"  # PSALIT2
    "4s"  # PSAECLTP
    "4s"  # PSACLHSE(0)
    "1s"  # PSALHEB0
    "1s"  # PSALHEB1
    "1s"  # PSALHEB2
    "1s"  # PSALHEB3
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
    "8s"  # PSASTKE(0)
    "2s"  # PSATKN
    "2s"  # PSAASD
    "4s"  # PSASEL
    "8s"  # (0)
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
    "8s"  # PSA_CR0ESAVEAREA(0)
    "4s"  # PSA_CR0ESAVEAREA_HW
    "4s"  # PSA_CR0ESAVEAREA_LW
    "16s"  # PSA_WINDOWWORKAREA
    "8s"  # PSA_WINDOWTODDELTA
    "4s"  # PSA_WINDOWTODDELTA_HW
    "4s"  # PSA_WINDOWTODDELTA_LW
    "8s"  # PSA_WINDOWLASTOPENTOD
    "8s"  # PSA_WINDOWCURRENTTOD
    "80s"  # PSARV600
    "8s"  # PSA_TIME_ON_CP
    "8s"  # PSATIME
    "4s"  # PSASRSAV
    "12s"  # PSAESC8
    "8s"  # PSADEXMW
    "64s"  # PSADSARS
    "8s"  # PSADTSAV
    "1s"  # PSAFF6C0(0)
    "8s"  # (0)
    "16s"  # PSADEXMS(0)
    "8s"  # PSADCR3(0)
    "4s"  # PSADSINS
    "4s"  # PSADPKSA(0)
    "2s"  # PSADPKM
    "2s"  # PSADSAS
    "8s"  # PSADCR4(0)
    "4s"  # PSADPINS
    "4s"  # PSADAXPA(0)
    "2s"  # PSADAX
    "2s"  # PSADPAS
    "8s"  # PSAUSEND(0)
    "192s"  # PSARV6E0
    "8s"  # PSAECVT
    "8s"  # PSAXCVT
    "8s"  # (0)
    "1s"  # PSADATLK(48)
    "4s"  # PSADATOF
    "4s"  # PSADATLN
    "4s"  # PSATBVTV
    "1s"  # PSATRACE
    "3s"  # PSARV7ED
    "8s"  # PSATBVTR
    "4s"  # PSATRVT
    "4s"  # PSATOT
    "8s"  # PSAUS2ST(0)
    "16s"  # PSACDSAV(0)
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
    "64s"  # PSATRSAV(0)
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
    "8s"  # (0)
    "64s"  # PSAGSAV
    "1s"  # PSAFF8A8(0)
    "4s"  # PSASCRG1
    "4s"  # PSASCRG2
    "4s"  # PSAGPREG(3)
    "4s"  # PSARSREG
    "4s"  # PSAPCGR8
    "4s"  # PSAPCGR9
    "8s"  # PSAPCGAB(0)
    "4s"  # PSAPCGRA
    "4s"  # PSAPCGRB
    "8s"  # (0)
    "64s"  # PSALKSA(0)
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
    "8s"  # (0)
    "72s"  # PSASLSA
    "1s"  # PSAFF950(0)
    "64s"  # PSAJSTSA
    "1s"  # PSAFF998(0)
    "8s"  # PSAUS2ND(0)
    "8s"  # (0)
    "64s"  # PSASLKSA(0)
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
    "8s"  # PSAFAFRR(0)
    "4s"  # PSAFFRR
    "4s"  # PSAFFRRS
    "36s"  # PSARVB5C
    "8s"  # (0)
    "1s"  # PSARVB80(88)
    "1s"  # PSASTAK(88)
    "1s"  # PSARVFD8(40)
    "8s"  # PSAEND(0)
)
psa_field_names = (
    "FLCRNPSW",
    "",
    "FLCROPSW",
    "FLCCVT",
    "",
    "FLCEOPSW",
    "FLCSOPSW",
    "FLCPOPSW",
    "FLCMOPSW",
    "FLCIOPSW",
    "",
    "FLCCVT64(0)",
    "",
    "FLCCVT2",
    "",
    "",
    "FLCENPSW",
    "",
    "FLCSNPSW",
    "",
    "FLCPNPSW",
    "",
    "FLCMNPSW",
    "",
    "FLCINPSW",
    "",
    "PSAEPARM",
    "PSAEEPSW(0)",
    "PSASPAD",
    "FLCEICOD",
    "PSAESPSW(0)",
    "",
    "FLCSVILC",
    "FLCSVCN",
    "PSAEPPSW(0)",
    "",
    "FLCPIILC",
    "FLCPICOD(0)",
    "PSAEECOD",
    "PSAPICOD",
    "FLCTEA(0)",
    "",
    "FLCDXC(0)",
    "FLCTEAB3",
    "",
    "FLCMCNUM",
    "FLCPERCD",
    "FLCATMID",
    "FLCPER",
    "",
    "FLCMTRCD",
    "FLCTEARN",
    "FLCPERRN",
    "",
    "FLCARCH",
    "PSAMPL",
    "(0)",
    "",
    "FLCIOCDP(0)",
    "FLCSID",
    "FLCIOFP",
    "",
    "FLCFACL(0)",
    "FLCFACL0",
    "FLCFACL1",
    "FLCFACL2",
    "FLCFACL3",
    "FLCFACL4",
    "FLCFACL5",
    "FLCFACL6",
    "FLCFACL7",
    "FLCFACL8",
    "FLCFACL9",
    "",
    "FLCFACLE",
    "FLCMCIC",
    "",
    "FLCFSA",
    "",
    "FLCFLA",
    "FLCRV110",
    "FLCARSAV(16)",
    "FLCFPSAV",
    "FLCGRSAV(16)",
    "FLCCRSAV(16)",
    "FLCHDEND(0)",
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
    "PSASUPER(0)",
    "PSASUP1",
    "PSASUP2",
    "PSASUP3",
    "PSASUP4",
    "PSARV22C",
    "PSA_WORKUNIT_CBF_ATDISP",
    "PSARV237",
    "PSAPROCCLASS",
    "PSA_BYLPAR_PROCCLASS",
    "PSAPROCCLASS_BYTE0",
    "PSAPROCCLASS_BYTE1",
    "PSA_BYLPAR_PROCCLASS_BYTE0",
    "PSA_BYLPAR_PROCCLASS_BYTE1",
    "PSAPTYPE",
    "PSAILS",
    "PSALSVCI",
    "PSAFLAGS",
    "PSARV241",
    "PSASCAFF",
    "PSALKCRF",
    "(0)",
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
    "PSACLHT(0)",
    "PSACLHT1(0)",
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
    "PSACLHT2(0)",
    "PSARSML",
    "PSATRCEL",
    "PSAIOSL",
    "PSARVLK4",
    "PSACLHT3(0)",
    "PSACPUL",
    "PSARVLK5",
    "PSACLHT4(0)",
    "PSACMSL",
    "PSALOCAL",
    "PSARVLK6",
    "PSALCPUA",
    "PSAHLHI(0)",
    "PSACLHS(0)",
    "PSACLHS1",
    "PSACLHS2",
    "PSACLHS3",
    "PSACLHS4",
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
    "PSAVAL(0)",
    "PSAVAL_MACHINE",
    "",
    "PSARSVT(0)",
    "PSARSVTE(0)",
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
    "(0)",
    "PSALWPSW",
    "PSARV3C8",
    "PSATSTK",
    "PSATSAV",
    "PSAASTK",
    "PSAASAV",
    "(0)",
    "PSARTPSW",
    "PSAPCR0E",
    "(0)",
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
    "(0)",
    "PSASCPSW",
    "",
    "(0)",
    "PSASMPSW",
    "",
    "(0)",
    "PSAPCPSW",
    "PSARV438",
    "(0)",
    "PSAMCX16",
    "PSARSP16",
    "PSAPSWSV16",
    "",
    "PSAPSWSV",
    "(0)",
    "PSACPUT",
    "PSAPCFUN(0)",
    "PSAPCFB1",
    "PSAPCFB2",
    "PSAPCFB3",
    "PSAPCFB4",
    "PSAPCPS2",
    "PSARV47E",
    "PSAPCWKA",
    "PSAPCPS3",
    "PSAPCPS4",
    "PSAMODEW(0)",
    "",
    "PSAMFLGS",
    "PSAMODEH",
    "PSAMODE",
    "",
    "PSASTNSM",
    "PSALKJW",
    "PSADZERO(0)",
    "PSAFZERO",
    "",
    "PSALKJW2",
    "PSALKPT",
    "PSALAA",
    "PSALIT2",
    "PSAECLTP",
    "PSACLHSE(0)",
    "PSALHEB0",
    "PSALHEB1",
    "PSALHEB2",
    "PSALHEB3",
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
    "PSASTKE(0)",
    "PSATKN",
    "PSAASD",
    "PSASEL",
    "(0)",
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
    "PSA_CR0ESAVEAREA(0)",
    "PSA_CR0ESAVEAREA_HW",
    "PSA_CR0ESAVEAREA_LW",
    "PSA_WINDOWWORKAREA",
    "PSA_WINDOWTODDELTA",
    "PSA_WINDOWTODDELTA_HW",
    "PSA_WINDOWTODDELTA_LW",
    "PSA_WINDOWLASTOPENTOD",
    "PSA_WINDOWCURRENTTOD",
    "PSARV600",
    "PSA_TIME_ON_CP",
    "PSATIME",
    "PSASRSAV",
    "PSAESC8",
    "PSADEXMW",
    "PSADSARS",
    "PSADTSAV",
    "PSAFF6C0(0)",
    "(0)",
    "PSADEXMS(0)",
    "PSADCR3(0)",
    "PSADSINS",
    "PSADPKSA(0)",
    "PSADPKM",
    "PSADSAS",
    "PSADCR4(0)",
    "PSADPINS",
    "PSADAXPA(0)",
    "PSADAX",
    "PSADPAS",
    "PSAUSEND(0)",
    "PSARV6E0",
    "PSAECVT",
    "PSAXCVT",
    "(0)",
    "PSADATLK(48)",
    "PSADATOF",
    "PSADATLN",
    "PSATBVTV",
    "PSATRACE",
    "PSARV7ED",
    "PSATBVTR",
    "PSATRVT",
    "PSATOT",
    "PSAUS2ST(0)",
    "PSACDSAV(0)",
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
    "PSATRSAV(0)",
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
    "(0)",
    "PSAGSAV",
    "PSAFF8A8(0)",
    "PSASCRG1",
    "PSASCRG2",
    "PSAGPREG(3)",
    "PSARSREG",
    "PSAPCGR8",
    "PSAPCGR9",
    "PSAPCGAB(0)",
    "PSAPCGRA",
    "PSAPCGRB",
    "(0)",
    "PSALKSA(0)",
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
    "(0)",
    "PSASLSA",
    "PSAFF950(0)",
    "PSAJSTSA",
    "PSAFF998(0)",
    "PSAUS2ND(0)",
    "(0)",
    "PSASLKSA(0)",
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
    "PSAFAFRR(0)",
    "PSAFFRR",
    "PSAFFRRS",
    "PSARVB5C",
    "(0)",
    "PSARVB80(88)",
    "PSASTAK(88)",
    "PSARVFD8(40)",
    "PSAEND(0)",
)
psa_offset_length = (
    info(0,4),  # FLCRNPSW
    info(4,4),  #
    info(8,8),  # FLCROPSW
    info(16,4),  # FLCCVT
    info(20,4),  #
    info(24,8),  # FLCEOPSW
    info(32,8),  # FLCSOPSW
    info(40,8),  # FLCPOPSW
    info(48,8),  # FLCMOPSW
    info(56,8),  # FLCIOPSW
    info(64,8),  #
    info(72,8),  # FLCCVT64(0)
    info(72,4),  #
    info(76,4),  # FLCCVT2
    info(80,4),  #
    info(84,4),  #
    info(88,4),  # FLCENPSW
    info(92,4),  #
    info(96,4),  # FLCSNPSW
    info(100,4),  #
    info(104,4),  # FLCPNPSW
    info(108,4),  #
    info(112,4),  # FLCMNPSW
    info(116,4),  #
    info(120,4),  # FLCINPSW
    info(124,4),  #
    info(128,4),  # PSAEPARM
    info(132,4),  # PSAEEPSW(0)
    info(132,2),  # PSASPAD
    info(134,2),  # FLCEICOD
    info(136,4),  # PSAESPSW(0)
    info(136,1),  #
    info(137,1),  # FLCSVILC
    info(138,2),  # FLCSVCN
    info(140,8),  # PSAEPPSW(0)
    info(140,1),  #
    info(141,1),  # FLCPIILC
    info(142,2),  # FLCPICOD(0)
    info(142,1),  # PSAEECOD
    info(143,1),  # PSAPICOD
    info(144,4),  # FLCTEA(0)
    info(144,3),  #
    info(147,1),  # FLCDXC(0)
    info(147,1),  # FLCTEAB3
    info(148,1),  #
    info(149,1),  # FLCMCNUM
    info(150,1),  # FLCPERCD
    info(151,1),  # FLCATMID
    info(152,4),  # FLCPER
    info(156,1),  #
    info(157,3),  # FLCMTRCD
    info(160,1),  # FLCTEARN
    info(161,1),  # FLCPERRN
    info(162,1),  #
    info(163,1),  # FLCARCH
    info(164,4),  # PSAMPL
    info(168,344),  # (0)
    info(168,16),  #
    info(184,8),  # FLCIOCDP(0)
    info(184,4),  # FLCSID
    info(188,4),  # FLCIOFP
    info(192,8),  #
    info(200,16),  # FLCFACL(0)
    info(200,1),  # FLCFACL0
    info(201,1),  # FLCFACL1
    info(202,1),  # FLCFACL2
    info(203,1),  # FLCFACL3
    info(204,1),  # FLCFACL4
    info(205,1),  # FLCFACL5
    info(206,1),  # FLCFACL6
    info(207,1),  # FLCFACL7
    info(208,1),  # FLCFACL8
    info(209,1),  # FLCFACL9
    info(210,6),  #
    info(216,16),  # FLCFACLE
    info(232,8),  # FLCMCIC
    info(240,8),  #
    info(248,4),  # FLCFSA
    info(252,4),  #
    info(256,16),  # FLCFLA
    info(272,16),  # FLCRV110
    info(288,4),  # FLCARSAV(16)
    info(352,32),  # FLCFPSAV
    info(384,4),  # FLCGRSAV(16)
    info(448,4),  # FLCCRSAV(16)
    info(512,8),  # FLCHDEND(0)
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
    info(552,4),  # PSASUPER(0)
    info(552,1),  # PSASUP1
    info(553,1),  # PSASUP2
    info(554,1),  # PSASUP3
    info(555,1),  # PSASUP4
    info(556,9),  # PSARV22C
    info(565,2),  # PSA_WORKUNIT_CBF_ATDISP
    info(567,1),  # PSARV237
    info(570,2),  # PSAPROCCLASS
    info(570,2),  # PSA_BYLPAR_PROCCLASS
    info(570,1),  # PSAPROCCLASS_BYTE0
    info(571,1),  # PSAPROCCLASS_BYTE1
    info(570,1),  # PSA_BYLPAR_PROCCLASS_BYTE0
    info(571,1),  # PSA_BYLPAR_PROCCLASS_BYTE1
    info(572,1),  # PSAPTYPE
    info(573,1),  # PSAILS
    info(574,2),  # PSALSVCI
    info(576,1),  # PSAFLAGS
    info(577,10),  # PSARV241
    info(587,1),  # PSASCAFF
    info(588,4),  # PSALKCRF
    info(592,8),  # (0)
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
    info(640,116),  # PSACLHT(0)
    info(640,80),  # PSACLHT1(0)
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
    info(720,16),  # PSACLHT2(0)
    info(720,4),  # PSARSML
    info(724,4),  # PSATRCEL
    info(728,4),  # PSAIOSL
    info(732,4),  # PSARVLK4
    info(736,8),  # PSACLHT3(0)
    info(736,4),  # PSACPUL
    info(740,4),  # PSARVLK5
    info(744,12),  # PSACLHT4(0)
    info(744,4),  # PSACMSL
    info(748,4),  # PSALOCAL
    info(752,4),  # PSARVLK6
    info(756,4),  # PSALCPUA
    info(760,4),  # PSAHLHI(0)
    info(760,4),  # PSACLHS(0)
    info(760,1),  # PSACLHS1
    info(761,1),  # PSACLHS2
    info(762,1),  # PSACLHS3
    info(763,1),  # PSACLHS4
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
    info(894,2),  # PSAVAL(0)
    info(894,1),  # PSAVAL_MACHINE
    info(895,1),  #
    info(896,64),  # PSARSVT(0)
    info(896,64),  # PSARSVTE(0)
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
    info(960,8),  # (0)
    info(960,8),  # PSALWPSW
    info(968,8),  # PSARV3C8
    info(976,4),  # PSATSTK
    info(980,4),  # PSATSAV
    info(984,4),  # PSAASTK
    info(988,4),  # PSAASAV
    info(992,8),  # (0)
    info(992,8),  # PSARTPSW
    info(1000,8),  # PSAPCR0E
    info(1008,4),  # (0)
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
    info(1048,8),  # (0)
    info(1048,4),  # PSASCPSW
    info(1052,4),  #
    info(1056,8),  # (0)
    info(1056,4),  # PSASMPSW
    info(1060,4),  #
    info(1064,8),  # (0)
    info(1064,16),  # PSAPCPSW
    info(1080,8),  # PSARV438
    info(1088,8),  # (0)
    info(1088,16),  # PSAMCX16
    info(1104,16),  # PSARSP16
    info(1120,16),  # PSAPSWSV16
    info(1120,8),  #
    info(1128,8),  # PSAPSWSV
    info(1136,8),  # (0)
    info(1136,8),  # PSACPUT
    info(1144,4),  # PSAPCFUN(0)
    info(1144,1),  # PSAPCFB1
    info(1145,1),  # PSAPCFB2
    info(1146,1),  # PSAPCFB3
    info(1147,1),  # PSAPCFB4
    info(1148,2),  # PSAPCPS2
    info(1150,2),  # PSARV47E
    info(1152,24),  # PSAPCWKA
    info(1176,2),  # PSAPCPS3
    info(1178,2),  # PSAPCPS4
    info(1180,4),  # PSAMODEW(0)
    info(1180,1),  #
    info(1181,1),  # PSAMFLGS
    info(1182,1),  # PSAMODEH
    info(1183,1),  # PSAMODE
    info(1184,3),  #
    info(1187,1),  # PSASTNSM
    info(1188,4),  # PSALKJW
    info(1192,8),  # PSADZERO(0)
    info(1192,4),  # PSAFZERO
    info(1196,4),  #
    info(1200,4),  # PSALKJW2
    info(1204,4),  # PSALKPT
    info(1208,4),  # PSALAA
    info(1212,4),  # PSALIT2
    info(1216,4),  # PSAECLTP
    info(1220,4),  # PSACLHSE(0)
    info(1220,1),  # PSALHEB0
    info(1221,1),  # PSALHEB1
    info(1222,1),  # PSALHEB2
    info(1223,1),  # PSALHEB3
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
    info(1432,8),  # PSASTKE(0)
    info(1432,2),  # PSATKN
    info(1434,2),  # PSAASD
    info(1436,4),  # PSASEL
    info(1440,8),  # (0)
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
    info(1496,8),  # PSA_CR0ESAVEAREA(0)
    info(1496,4),  # PSA_CR0ESAVEAREA_HW
    info(1500,4),  # PSA_CR0ESAVEAREA_LW
    info(1504,16),  # PSA_WINDOWWORKAREA
    info(1504,8),  # PSA_WINDOWTODDELTA
    info(1504,4),  # PSA_WINDOWTODDELTA_HW
    info(1508,4),  # PSA_WINDOWTODDELTA_LW
    info(1520,8),  # PSA_WINDOWLASTOPENTOD
    info(1528,8),  # PSA_WINDOWCURRENTTOD
    info(1536,80),  # PSARV600
    info(1616,8),  # PSA_TIME_ON_CP
    info(1624,8),  # PSATIME
    info(1632,4),  # PSASRSAV
    info(1636,12),  # PSAESC8
    info(1648,8),  # PSADEXMW
    info(1656,64),  # PSADSARS
    info(1728,8),  # PSADTSAV
    info(1728,1),  # PSAFF6C0(0)
    info(1736,8),  # (0)
    info(1736,16),  # PSADEXMS(0)
    info(1736,8),  # PSADCR3(0)
    info(1736,4),  # PSADSINS
    info(1740,4),  # PSADPKSA(0)
    info(1740,2),  # PSADPKM
    info(1742,2),  # PSADSAS
    info(1744,8),  # PSADCR4(0)
    info(1744,4),  # PSADPINS
    info(1748,4),  # PSADAXPA(0)
    info(1748,2),  # PSADAX
    info(1750,2),  # PSADPAS
    info(1760,8),  # PSAUSEND(0)
    info(1760,192),  # PSARV6E0
    info(1952,8),  # PSAECVT
    info(1960,8),  # PSAXCVT
    info(1968,8),  # (0)
    info(1968,1),  # PSADATLK(48)
    info(2016,4),  # PSADATOF
    info(2020,4),  # PSADATLN
    info(2024,4),  # PSATBVTV
    info(2028,1),  # PSATRACE
    info(2029,3),  # PSARV7ED
    info(2032,8),  # PSATBVTR
    info(2040,4),  # PSATRVT
    info(2044,4),  # PSATOT
    info(2048,8),  # PSAUS2ST(0)
    info(2048,16),  # PSACDSAV(0)
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
    info(2088,64),  # PSATRSAV(0)
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
    info(2216,8),  # (0)
    info(2216,64),  # PSAGSAV
    info(2216,1),  # PSAFF8A8(0)
    info(2280,4),  # PSASCRG1
    info(2284,4),  # PSASCRG2
    info(2288,4),  # PSAGPREG(3)
    info(2300,4),  # PSARSREG
    info(2304,4),  # PSAPCGR8
    info(2308,4),  # PSAPCGR9
    info(2312,8),  # PSAPCGAB(0)
    info(2312,4),  # PSAPCGRA
    info(2316,4),  # PSAPCGRB
    info(2320,8),  # (0)
    info(2320,64),  # PSALKSA(0)
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
    info(2384,8),  # (0)
    info(2384,72),  # PSASLSA
    info(2384,1),  # PSAFF950(0)
    info(2456,64),  # PSAJSTSA
    info(2456,1),  # PSAFF998(0)
    info(2520,8),  # PSAUS2ND(0)
    info(2520,8),  # (0)
    info(2520,64),  # PSASLKSA(0)
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
    info(2900,8),  # PSAFAFRR(0)
    info(2900,4),  # PSAFFRR
    info(2904,4),  # PSAFFRRS
    info(2908,36),  # PSARVB5C
    info(2944,8),  # (0)
    info(2944,1),  # PSARVB80(88)
    info(2944,1),  # PSASTAK(88)
    info(4056,1),  # PSARVFD8(40)
    info(4096,8),  # PSAEND(0)
)


psa_fields = namedtuple("cvt", psa_field_names)
cvt_info = psa_fields._make(psa_offset_length)

def get_psa() -> bytearray:
    cvt_buffer = bytearray(psa_pattern.size)
    read_memory(cvt_buffer, len(cvt_buffer), 0)
    return cvt_buffer

class PSA:
    def __init__(self):
        self.name = "PSA"
        self.long_name = "Prefix Save Area"
        self.fields = psa_field_names
        self.info = cvt_info._asdict()
        content = psa_fields._make(psa_pattern.unpack(get_psa()))
        self.content = content._asdict()
