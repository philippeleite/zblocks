from app.models.base import info, zblocks_list
from app.utils import read_memory
from struct import Struct
from collections import namedtuple

zblocks_list.append('LCCA')

lcca_pattern = Struct(
    ">"
    "4s"  # LCCALCCA
    "2s"  # LCCACPUA
    "2s"  # LCCACAFM
    "64s"  # LCCAPGR1
    "64s"  # LCCAPGR2
    "8s"  # LCCAPPSW
    "4s"  # LCCAPINT
    "4s"  # LCCAPVAD
    "1s"  # LCCAPICC
    "1s"  # LCCADSF3
    "2s"  # LCCAWUQDEGRRAN
    "4s"  # LCCACR0
    "64s"  # LCCAPGR3
    "4s"  # LCCAP2A0
    "4s"  # LCCAP2A1
    "4s"  # LCCAP2A2
    "4s"  # LCCAP2A3
    "4s"  # LCCAP2A4
    "4s"  # LCCAP2A5
    "4s"  # LCCAP2A6
    "4s"  # LCCAP2A7
    "4s"  # LCCAP2A8
    "4s"  # LCCAP2A9
    "4s"  # LCCAP2AA
    "4s"  # LCCAP2AB
    "4s"  # LCCAP2AC
    "4s"  # LCCAP2AD
    "4s"  # LCCAP2AE
    "4s"  # LCCAP2AF
    "8s"  # LCCAP3C0
    "8s"  # LCCAP3C1
    "8s"  # LCCAP3C2
    "16s"  # LCCAP3XM
    "8s"  # LCCAP3C5
    "8s"  # LCCAP3C6
    "8s"  # LCCAP3C7
    "8s"  # LCCAP3C8
    "8s"  # LCCAP3C9
    "8s"  # LCCAP3CA
    "8s"  # LCCAP3CB
    "8s"  # LCCAP3CC
    "8s"  # LCCAP3CD
    "8s"  # LCCAP3CE
    "8s"  # LCCAP3CF
    "4s"  # LCCADSA2
    "4s"  # LCCASHRL
    "8s"  # LCCA_PARTIALCPUMASK
    "4s"  # LCCARSMAD_LWA
    "4s"  # LCCARSMXM_LWA
    "4s"  # LCCARSMST_LWA
    "4s"  # LCCARSMCM_LWA
    "4s"  # LCCADNU2_LWA
    "20s"  # LCCAR1D4
    "8s"  # LCCAPSW3
    "32s"  # LCCAINGR
    "2s"  # LCCABBCT
    "2s"  # LCCAWFCT
    "4s"  # LCCAMCR0
    "4s"  # LCCAIHRC
    "4s"  # LCCASPIN
    "4s"  # LCCATODH
    "4s"  # LCCATODL
    "4s"  # LCCACPUS
    "1s"  # LCCADSF1
    "1s"  # LCCADSF2
    "1s"  # LCCAPSMK
    "1s"  # LCCASCFL
    "4s"  # LCCAPWEB
    "4s"  # LCCADBCT
    "4s"  # LCCADSV1
    "4s"  # LCCADSV2
    "4s"  # LCCADSV3
    "4s"  # LCCADSV4
    "4s"  # LCCADSV5
    "4s"  # LCCADSV6
    "4s"  # LCCAEE1R
    "4s"  # LCCAEE2R
    "4s"  # LCCAEE3R
    "1s"  # LCCAPTR1
    "1s"  # LCCAPTR2
    "1s"  # LCCAPTR3
    "1s"  # LCCAPPR2
    "4s"  # LCCA_THREADMASK
    "4s"  # LCCAWTD
    "4s"  # LCCAWSD
    "4s"  # LCCAWSU
    "4s"  # LCCAWS
    "1s"  # LCCASTCT
    "1s"  # LCCAFLCS
    "2s"  # LCCABBCC
    "8s"  # LCCAWTIM
    "16s"  # LCCASXMR
    "2s"  # LCCA_PARTIALCPUMASKOFFSET
    "1s"  # LCCADSF4
    "1s"  # LCCAPCFL
    "4s"  # LCCAESC5SRBADDR
    "4s"  # LCCA_NHTM_AT_CPTM_UPDATE
    "4s"  # LCCALCCX
    "4s"  # LCCAFPWR
    "4s"  # LCCAESAV
    "4s"  # LCCAAOLD
    "4s"  # LCCATOLD
    "4s"  # LCCASRBJ
    "4s"  # LCCADCPU
    "4s"  # LCCARCPU
    "4s"  # LCCACRLC
    "4s"  # LCCAR2B0
    "1s"  # LCCACRFL
    "1s"  # LCCACREX
    "1s"  # LCCALKFG
    "1s"  # LCCASTFL
    "4s"  # LCCASLEB
    "4s"  # LCCASLIP
    "8s"  # LCCALWTM
    "4s"  # LCCASSA2
    "4s"  # LCCASSA5
    "8s"  # LCCASRBF
    "4s"  # LCCAORMT
    "4s"  # LCCANHTM
    "4s"  # LCCAIOWA
    "4s"  # LCCAIOR1
    "4s"  # LCCAIOR2
    "4s"  # LCCAIOR3
    "1s"  # LCCAR2F2
    "1s"  # LCCAWFL2
    "64s"  # LCCARSGR
    "16s"  # LCCAWDT
    "4s"  # LCCACWEB
    "4s"  # LCCANWEB
    "1s"  # LCCACWEBFLAGS
    "1s"  # LCCAR34D
    "2s"  # LCCAWUQR
    "4s"  # LCCAWUQM
    "8s"  # LCCAFWP
    "4s"  # LCCASRSA
    "4s"  # LCCASMQJ
    "4s"  # LCCASPLJ
    "4s"  # LCCAETP
    "4s"  # LCCAETPB
    "2s"  # LCCAALTP
    "2s"  # LCCAWUQI
    "2s"  # LCCAALTI
    "1s"  # LCCADISPATCHMIXFLAGS
    "1s"  # LCCAFLGS
    "2s"  # LCCAR378
    "2s"  # LCCAPALP
    "4s"  # LCCARWQL
    "64s"  # LCCASGPR
    "1s"  # LCCADS0F
    "1s"  # LCCAFPFL
    "2s"  # LCCAPERC
    "4s"  # LCCAPERA
    "4s"  # LCCASDUV
    "4s"  # LCCAR3CC
    "4s"  # LCCAIDUV
    "4s"  # LCCAR3D4
    "4s"  # LCCASCW1
    "4s"  # LCCASCW2
    "4s"  # LCCASCW3
    "4s"  # LCCASCW4
    "8s"  # LCCA_WUQA_EQPRIRQMDP_TOD
    "8s"  # LCCA_CR0ESAVEAREA
    "8s"  # LCCA_TIMERCR0ESAVEAREA
    "40s"  # LCCAR400
    "8s"  # LCCADIAG428
    "8s"  # LCCASDR8
    "8s"  # LCCAIDR8
    "2s"  # LCCAR440
    "2s"  # LCCADIAG442
    "4s"  # LCCA_SRBPARM
    "8s"  # LCCABEA1
    "8s"  # LCCABEA2
    "8s"  # LCCABEA3
    "8s"  # LCCABEA4
    "8s"  # LCCABEA5
    "8s"  # LCCAELKP
    "72s" # LCCASTG1
    "20s" # LCCASCSA
    "52s" # LCCASREG
    "1s"  # LCCASMSK
    "1s"  # LCCARSMK
    "1s"  # LCCAPGMM
    "1s"  # LCCATCFB
    "28s" # LCCARES1
    "12s" # LCCARES2
    "4s"  # LCCASPSW
    "4s"  # LCCASRGS
    "4s"  # LCCAPRMW
    "4s"  # LCCAPTCB
    "4s"  # LCCAPRTN
    "8s"  # LCCACDXM
    "4s"  # LCCATCBC
    "4s"  # LCCASRBC
    "4s"  # LCCACR8W
    "4s"  # LCCAIOSS
    "4s"  # LCCAIOC3
    "4s"  # LCCAIOC4
    "4s"  # LCCABBRC
    "4s"  # LCCACDS0
    "4s"  # LCCACDS1
    "4s"  # LCCACDS2
    "4s"  # LCCACDS3
    "4s"  # LCCACDS4
    "4s"  # LCCACDS5
    "4s"  # LCCACDS6
    "4s"  # LCCACDS7
    "4s"  # LCCACDS8
    "4s"  # LCCACDS9
    "4s"  # LCCACDSA
    "4s"  # LCCACDSB
    "4s"  # LCCACDSC
    "4s"  # LCCACDSD
    "4s"  # LCCACDSE
    "4s"  # LCCACDSF
    "64s" # LCCASLSA
    "4s"  # LCCARWEB
    "40s" # LCCAPOST
    "4s"  # LCCAALOV
    "4s"  # LCCAPSB2
    "4s"  # LCCALSSD
    "4s"  # LCCALSDP
    "8s"  # LCCAXTIM
    "4s"  # LCCAP3A0
    "4s"  # LCCAP3A1
    "4s"  # LCCAP3A2
    "4s"  # LCCAP3A3
    "4s"  # LCCAP3A4
    "4s"  # LCCAP3A5
    "4s"  # LCCAP3A6
    "4s"  # LCCAP3A7
    "4s"  # LCCAP3A8
    "4s"  # LCCAP3A9
    "4s"  # LCCAP3AA
    "4s"  # LCCAP3AB
    "4s"  # LCCAP3AC
    "4s"  # LCCAP3AD
    "4s"  # LCCAP3AE
    "4s"  # LCCAP3AF
    "64s" # LCCAEMS0
    "8s"  # LCCAPPS1
    "4s"  # LCCAPIC1
    "4s"  # LCCAPTE1
    "64s" # LCCAPGR4
    "72s" # LCCAPSLI
    "4s"  # LCCALSHD
    "4s"  # LCCALSHP
    "8s"  # LCCAPPS3
    "4s"  # LCCAPIC3
    "4s"  # LCCAPTE3
    "4s"  # LCCAP1A0
    "4s"  # LCCAP1A1
    "4s"  # LCCAP1A2
    "4s"  # LCCAP1A3
    "4s"  # LCCAP1A4
    "4s"  # LCCAP1A5
    "4s"  # LCCAP1A6
    "4s"  # LCCAP1A7
    "4s"  # LCCAP1A8
    "4s"  # LCCAP1A9
    "4s"  # LCCAP1AA
    "4s"  # LCCAP1AB
    "4s"  # LCCAP1AC
    "4s"  # LCCAP1AD
    "4s"  # LCCAP1AE
    "4s"  # LCCAP1AF
    "4s"  # LCCAP4A0
    "4s"  # LCCAP4A1
    "4s"  # LCCAP4A2
    "4s"  # LCCAP4A3
    "4s"  # LCCAP4A4
    "4s"  # LCCAP4A5
    "4s"  # LCCAP4A6
    "4s"  # LCCAP4A7
    "4s"  # LCCAP4A8
    "4s"  # LCCAP4A9
    "4s"  # LCCAP4AA
    "4s"  # LCCAP4AB
    "4s"  # LCCAP4AC
    "4s"  # LCCAP4AD
    "4s"  # LCCAP4AE
    "4s"  # LCCAP4AF
    "4s"  # LCCARAR0
    "4s"  # LCCARAR1
    "4s"  # LCCARAR2
    "4s"  # LCCARAR3
    "4s"  # LCCARAR4
    "4s"  # LCCARAR5
    "4s"  # LCCARAR6
    "4s"  # LCCARAR7
    "4s"  # LCCARAR8
    "4s"  # LCCARAR9
    "4s"  # LCCARARA
    "4s"  # LCCARARB
    "4s"  # LCCARARC
    "4s"  # LCCARARD
    "4s"  # LCCARARE
    "4s"  # LCCARARF
    "8s"  # LCCAP1C0
    "8s"  # LCCAP1C1
    "8s"  # LCCAP1C2
    "8s"  # LCCAP1C3
    "8s"  # LCCAP1C4
    "8s"  # LCCAP1C5
    "8s"  # LCCAP1C6
    "8s"  # LCCAP1C7
    "8s"  # LCCAP1C8
    "8s"  # LCCAP1C9
    "8s"  # LCCAP1CA
    "8s"  # LCCAP1CB
    "8s"  # LCCAP1CC
    "8s"  # LCCAP1CD
    "8s"  # LCCAP1CE
    "8s"  # LCCAP1CF
    "8s"  # LCCAP2C0
    "8s"  # LCCAP2C1
    "8s"  # LCCAP2C2
    "8s"  # LCCAP2C3
    "8s"  # LCCAP2C4
    "8s"  # LCCAP2C5
    "8s"  # LCCAP2C6
    "8s"  # LCCAP2C7
    "8s"  # LCCAP2C8
    "8s"  # LCCAP2C9
    "8s"  # LCCAP2CA
    "8s"  # LCCAP2CB
    "8s"  # LCCAP2CC
    "8s"  # LCCAP2CD
    "8s"  # LCCAP2CE
    "8s"  # LCCAP2CF
    "1s"  # LCCAPWAIT
    "1s"  # LCCADACT
    "2s"  # LCCAOILC
    "4s"  # LCCAPSB5
    "4s"  # LCCAP5A0
    "4s"  # LCCAP5A1
    "4s"  # LCCAP5A2
    "4s"  # LCCAP5A3
    "4s"  # LCCAP5A4
    "4s"  # LCCAP5A5
    "4s"  # LCCAP5A6
    "4s"  # LCCAP5A7
    "4s"  # LCCAP5A8
    "4s"  # LCCAP5A9
    "4s"  # LCCAP5AA
    "4s"  # LCCAP5AB
    "4s"  # LCCAP5AC
    "4s"  # LCCAP5AD
    "4s"  # LCCAP5AE
    "4s"  # LCCAP5AF
    "1s"  # LCCAPTR5
    "1s"  # LCCAPMFV
    "2s"  # LCCADIEP
    "64s" # LCCAPGR5
    "4s"  # LCCADSA5
    "8s"  # LCCAPPS5
    "4s"  # LCCAPIC5
    "4s"  # LCCAPTE5
    "8s"  # LCCATTSC
    "8s"  # LCCAWTSC
    "4s"  # LCCATP
    "4s"  # LCCATPU
    "4s"  # LCCAWP
    "4s"  # LCCAWPU
    "4s"  # LCCATPB
    "4s"  # LCCATPUB
    "4s"  # LCCAWPB
    "4s"  # LCCAWPUB
    "2s"  # LCCAOID
    "1s"  # LCCAMTSC
    "1s"  # LCCACTSC
    "4s"  # LCCAPPRI
    "4s"  # LCCACPTM
    "4s"  # LCCACLSD
    "68s" # LCCAWUQA
    "4s"  # LCCAHPWUQ
    "8s"  # LCCASPECHELPREQTOD
    "8s"  # LCCADIAGA50
    "4s"  # LCCAALTCWEB
    "4s"  # LCCAALTPWEB
    "8s"  # LCCARA60
)
lcca_field_names = (
    "LCCALCCA",
    "LCCACPUA",
    "LCCACAFM",
    "LCCAPGR1",
    "LCCAPGR2",
    "LCCAPPSW",
    "LCCAPINT",
    "LCCAPVAD",
    "LCCAPICC",
    "LCCADSF3",
    "LCCAWUQDEGRRAN",
    "LCCACR0",
    "LCCAPGR3",
    "LCCAP2A0",
    "LCCAP2A1",
    "LCCAP2A2",
    "LCCAP2A3",
    "LCCAP2A4",
    "LCCAP2A5",
    "LCCAP2A6",
    "LCCAP2A7",
    "LCCAP2A8",
    "LCCAP2A9",
    "LCCAP2AA",
    "LCCAP2AB",
    "LCCAP2AC",
    "LCCAP2AD",
    "LCCAP2AE",
    "LCCAP2AF",
    "LCCAP3C0",
    "LCCAP3C1",
    "LCCAP3C2",
    "LCCAP3XM",
    "LCCAP3C5",
    "LCCAP3C6",
    "LCCAP3C7",
    "LCCAP3C8",
    "LCCAP3C9",
    "LCCAP3CA",
    "LCCAP3CB",
    "LCCAP3CC",
    "LCCAP3CD",
    "LCCAP3CE",
    "LCCAP3CF",
    "LCCADSA2",
    "LCCASHRL",
    "LCCA_PARTIALCPUMASK",
    "LCCARSMAD_LWA",
    "LCCARSMXM_LWA",
    "LCCARSMST_LWA",
    "LCCARSMCM_LWA",
    "LCCADNU2_LWA",
    "LCCAR1D4",
    "LCCAPSW3",
    "LCCAINGR",
    "LCCABBCT",
    "LCCAWFCT",
    "LCCAMCR0",
    "LCCAIHRC",
    "LCCASPIN",
    "LCCATODH",
    "LCCATODL",
    "LCCACPUS",
    "LCCADSF1",
    "LCCADSF2",
    "LCCAPSMK",
    "LCCASCFL",
    "LCCAPWEB",
    "LCCADBCT",
    "LCCADSV1",
    "LCCADSV2",
    "LCCADSV3",
    "LCCADSV4",
    "LCCADSV5",
    "LCCADSV6",
    "LCCAEE1R",
    "LCCAEE2R",
    "LCCAEE3R",
    "LCCAPTR1",
    "LCCAPTR2",
    "LCCAPTR3",
    "LCCAPPR2",
    "LCCA_THREADMASK",
    "LCCAWTD",
    "LCCAWSD",
    "LCCAWSU",
    "LCCAWS",
    "LCCASTCT",
    "LCCAFLCS",
    "LCCABBCC",
    "LCCAWTIM",
    "LCCASXMR",
    "LCCA_PARTIALCPUMASKOFFSET",
    "LCCADSF4",
    "LCCAPCFL",
    "LCCAESC5SRBADDR",
    "LCCA_NHTM_AT_CPTM_UPDATE",
    "LCCALCCX",
    "LCCAFPWR",
    "LCCAESAV",
    "LCCAAOLD",
    "LCCATOLD",
    "LCCASRBJ",
    "LCCADCPU",
    "LCCARCPU",
    "LCCACRLC",
    "LCCAR2B0",
    "LCCACRFL",
    "LCCACREX",
    "LCCALKFG",
    "LCCASTFL",
    "LCCASLEB",
    "LCCASLIP",
    "LCCALWTM",
    "LCCASSA2",
    "LCCASSA5",
    "LCCASRBF",
    "LCCAORMT",
    "LCCANHTM",
    "LCCAIOWA",
    "LCCAIOR1",
    "LCCAIOR2",
    "LCCAIOR3",
    "LCCAR2F2",
    "LCCAWFL2",
    "LCCARSGR",
    "LCCAWDT",
    "LCCACWEB",
    "LCCANWEB",
    "LCCACWEBFLAGS",
    "LCCAR34D",
    "LCCAWUQR",
    "LCCAWUQM",
    "LCCAFWP",
    "LCCASRSA",
    "LCCASMQJ",
    "LCCASPLJ",
    "LCCAETP",
    "LCCAETPB",
    "LCCAALTP",
    "LCCAWUQI",
    "LCCAALTI",
    "LCCADISPATCHMIXFLAGS",
    "LCCAFLGS",
    "LCCAR378",
    "LCCAPALP",
    "LCCARWQL",
    "LCCASGPR",
    "LCCADS0F",
    "LCCAFPFL",
    "LCCAPERC",
    "LCCAPERA",
    "LCCASDUV",
    "LCCAR3CC",
    "LCCAIDUV",
    "LCCAR3D4",
    "LCCASCW1",
    "LCCASCW2",
    "LCCASCW3",
    "LCCASCW4",
    "LCCA_WUQA_EQPRIRQMDP_TOD",
    "LCCA_CR0ESAVEAREA",
    "LCCA_TIMERCR0ESAVEAREA",
    "LCCAR400",
    "LCCADIAG428",
    "LCCASDR8",
    "LCCAIDR8",
    "LCCAR440",
    "LCCADIAG442",
    "LCCA_SRBPARM",
    "LCCABEA1",
    "LCCABEA2",
    "LCCABEA3",
    "LCCABEA4",
    "LCCABEA5",
    "LCCAELKP",
    "LCCASTG1",
    "LCCASCSA",
    "LCCASREG",
    "LCCASMSK",
    "LCCARSMK",
    "LCCAPGMM",
    "LCCATCFB",
    "LCCARES1",
    "LCCARES2",
    "LCCASPSW",
    "LCCASRGS",
    "LCCAPRMW",
    "LCCAPTCB",
    "LCCAPRTN",
    "LCCACDXM",
    "LCCATCBC",
    "LCCASRBC",
    "LCCACR8W",
    "LCCAIOSS",
    "LCCAIOC3",
    "LCCAIOC4",
    "LCCABBRC",
    "LCCACDS0",
    "LCCACDS1",
    "LCCACDS2",
    "LCCACDS3",
    "LCCACDS4",
    "LCCACDS5",
    "LCCACDS6",
    "LCCACDS7",
    "LCCACDS8",
    "LCCACDS9",
    "LCCACDSA",
    "LCCACDSB",
    "LCCACDSC",
    "LCCACDSD",
    "LCCACDSE",
    "LCCACDSF",
    "LCCASLSA",
    "LCCARWEB",
    "LCCAPOST",
    "LCCAALOV",
    "LCCAPSB2",
    "LCCALSSD",
    "LCCALSDP",
    "LCCAXTIM",
    "LCCAP3A0",
    "LCCAP3A1",
    "LCCAP3A2",
    "LCCAP3A3",
    "LCCAP3A4",
    "LCCAP3A5",
    "LCCAP3A6",
    "LCCAP3A7",
    "LCCAP3A8",
    "LCCAP3A9",
    "LCCAP3AA",
    "LCCAP3AB",
    "LCCAP3AC",
    "LCCAP3AD",
    "LCCAP3AE",
    "LCCAP3AF",
    "LCCAEMS0",
    "LCCAPPS1",
    "LCCAPIC1",
    "LCCAPTE1",
    "LCCAPGR4",
    "LCCAPSLI",
    "LCCALSHD",
    "LCCALSHP",
    "LCCAPPS3",
    "LCCAPIC3",
    "LCCAPTE3",
    "LCCAP1A0",
    "LCCAP1A1",
    "LCCAP1A2",
    "LCCAP1A3",
    "LCCAP1A4",
    "LCCAP1A5",
    "LCCAP1A6",
    "LCCAP1A7",
    "LCCAP1A8",
    "LCCAP1A9",
    "LCCAP1AA",
    "LCCAP1AB",
    "LCCAP1AC",
    "LCCAP1AD",
    "LCCAP1AE",
    "LCCAP1AF",
    "LCCAP4A0",
    "LCCAP4A1",
    "LCCAP4A2",
    "LCCAP4A3",
    "LCCAP4A4",
    "LCCAP4A5",
    "LCCAP4A6",
    "LCCAP4A7",
    "LCCAP4A8",
    "LCCAP4A9",
    "LCCAP4AA",
    "LCCAP4AB",
    "LCCAP4AC",
    "LCCAP4AD",
    "LCCAP4AE",
    "LCCAP4AF",
    "LCCARAR0",
    "LCCARAR1",
    "LCCARAR2",
    "LCCARAR3",
    "LCCARAR4",
    "LCCARAR5",
    "LCCARAR6",
    "LCCARAR7",
    "LCCARAR8",
    "LCCARAR9",
    "LCCARARA",
    "LCCARARB",
    "LCCARARC",
    "LCCARARD",
    "LCCARARE",
    "LCCARARF",
    "LCCAP1C0",
    "LCCAP1C1",
    "LCCAP1C2",
    "LCCAP1C3",
    "LCCAP1C4",
    "LCCAP1C5",
    "LCCAP1C6",
    "LCCAP1C7",
    "LCCAP1C8",
    "LCCAP1C9",
    "LCCAP1CA",
    "LCCAP1CB",
    "LCCAP1CC",
    "LCCAP1CD",
    "LCCAP1CE",
    "LCCAP1CF",
    "LCCAP2C0",
    "LCCAP2C1",
    "LCCAP2C2",
    "LCCAP2C3",
    "LCCAP2C4",
    "LCCAP2C5",
    "LCCAP2C6",
    "LCCAP2C7",
    "LCCAP2C8",
    "LCCAP2C9",
    "LCCAP2CA",
    "LCCAP2CB",
    "LCCAP2CC",
    "LCCAP2CD",
    "LCCAP2CE",
    "LCCAP2CF",
    "LCCAPWAIT",
    "LCCADACT",
    "LCCAOILC",
    "LCCAPSB5",
    "LCCAP5A0",
    "LCCAP5A1",
    "LCCAP5A2",
    "LCCAP5A3",
    "LCCAP5A4",
    "LCCAP5A5",
    "LCCAP5A6",
    "LCCAP5A7",
    "LCCAP5A8",
    "LCCAP5A9",
    "LCCAP5AA",
    "LCCAP5AB",
    "LCCAP5AC",
    "LCCAP5AD",
    "LCCAP5AE",
    "LCCAP5AF",
    "LCCAPTR5",
    "LCCAPMFV",
    "LCCADIEP",
    "LCCAPGR5",
    "LCCADSA5",
    "LCCAPPS5",
    "LCCAPIC5",
    "LCCAPTE5",
    "LCCATTSC",
    "LCCAWTSC",
    "LCCATP",
    "LCCATPU",
    "LCCAWP",
    "LCCAWPU",
    "LCCATPB",
    "LCCATPUB",
    "LCCAWPB",
    "LCCAWPUB",
    "LCCAOID",
    "LCCAMTSC",
    "LCCACTSC",
    "LCCAPPRI",
    "LCCACPTM",
    "LCCACLSD",
    "LCCAWUQA",
    "LCCAHPWUQ",
    "LCCASPECHELPREQTOD",
    "LCCADIAGA50",
    "LCCAALTCWEB",
    "LCCAALTPWEB",
    "LCCARA60",
)
lcca_offset_length = (
    info(0,4),  # LCCALCCA
    info(4,2),  # LCCACPUA
    info(6,2),  # LCCACAFM
    info(8,64),  # LCCAPGR1
    info(72,64),  # LCCAPGR2
    info(136,8),  # LCCAPPSW
    info(144,4),  # LCCAPINT
    info(148,4),  # LCCAPVAD
    info(152,1),  # LCCAPICC
    info(153,1),  # LCCADSF3
    info(154,2),  # LCCAWUQDEGRRAN
    info(156,4),  # LCCACR0
    info(160,64),  # LCCAPGR3
    info(224,4),  # LCCAP2A0
    info(228,4),  # LCCAP2A1
    info(232,4),  # LCCAP2A2
    info(236,4),  # LCCAP2A3
    info(240,4),  # LCCAP2A4
    info(244,4),  # LCCAP2A5
    info(248,4),  # LCCAP2A6
    info(252,4),  # LCCAP2A7
    info(256,4),  # LCCAP2A8
    info(260,4),  # LCCAP2A9
    info(264,4),  # LCCAP2AA
    info(268,4),  # LCCAP2AB
    info(272,4),  # LCCAP2AC
    info(276,4),  # LCCAP2AD
    info(280,4),  # LCCAP2AE
    info(284,4),  # LCCAP2AF
    info(288,8),  # LCCAP3C0
    info(296,8),  # LCCAP3C1
    info(304,8),  # LCCAP3C2
    info(312,16),  # LCCAP3XM
    info(328,8),  # LCCAP3C5
    info(336,8),  # LCCAP3C6
    info(344,8),  # LCCAP3C7
    info(352,8),  # LCCAP3C8
    info(360,8),  # LCCAP3C9
    info(368,8),  # LCCAP3CA
    info(376,8),  # LCCAP3CB
    info(384,8),  # LCCAP3CC
    info(392,8),  # LCCAP3CD
    info(400,8),  # LCCAP3CE
    info(408,8),  # LCCAP3CF
    info(416,4),  # LCCADSA2
    info(420,4),  # LCCASHRL
    info(424,8),  # LCCA_PARTIALCPUMASK
    info(432,4),  # LCCARSMAD_LWA
    info(436,4),  # LCCARSMXM_LWA
    info(440,4),  # LCCARSMST_LWA
    info(444,4),  # LCCARSMCM_LWA
    info(448,4),  # LCCADNU2_LWA
    info(452,20),  # LCCAR1D4
    info(472,8),  # LCCAPSW3
    info(480,32),  # LCCAINGR
    info(512,2),  # LCCABBCT
    info(514,2),  # LCCAWFCT
    info(516,4),  # LCCAMCR0
    info(520,4),  # LCCAIHRC
    info(524,4),  # LCCASPIN
    info(528,4),  # LCCATODH
    info(532,4),  # LCCATODL
    info(536,4),  # LCCACPUS
    info(540,1),  # LCCADSF1
    info(541,1),  # LCCADSF2
    info(542,1),  # LCCAPSMK
    info(543,1),  # LCCASCFL
    info(544,4),  # LCCAPWEB
    info(548,4),  # LCCADBCT
    info(552,4),  # LCCADSV1
    info(556,4),  # LCCADSV2
    info(560,4),  # LCCADSV3
    info(564,4),  # LCCADSV4
    info(568,4),  # LCCADSV5
    info(572,4),  # LCCADSV6
    info(576,4),  # LCCAEE1R
    info(580,4),  # LCCAEE2R
    info(584,4),  # LCCAEE3R
    info(588,1),  # LCCAPTR1
    info(589,1),  # LCCAPTR2
    info(590,1),  # LCCAPTR3
    info(591,1),  # LCCAPPR2
    info(592,4),  # LCCA_THREADMASK
    info(596,4),  # LCCAWTD
    info(600,4),  # LCCAWSD
    info(604,4),  # LCCAWSU
    info(608,4),  # LCCAWS
    info(612,1),  # LCCASTCT
    info(613,1),  # LCCAFLCS
    info(614,2),  # LCCABBCC
    info(616,8),  # LCCAWTIM
    info(624,16),  # LCCASXMR
    info(640,2),  # LCCA_PARTIALCPUMASKOFFSET
    info(642,1),  # LCCADSF4
    info(643,1),  # LCCAPCFL
    info(644,4),  # LCCAESC5SRBADDR
    info(648,4),  # LCCA_NHTM_AT_CPTM_UPDATE
    info(652,4),  # LCCALCCX
    info(656,4),  # LCCAFPWR
    info(660,4),  # LCCAESAV
    info(664,4),  # LCCAAOLD
    info(668,4),  # LCCATOLD
    info(672,4),  # LCCASRBJ
    info(676,4),  # LCCADCPU
    info(680,4),  # LCCARCPU
    info(684,4),  # LCCACRLC
    info(688,4),  # LCCAR2B0
    info(692,1),  # LCCACRFL
    info(693,1),  # LCCACREX
    info(694,1),  # LCCALKFG
    info(695,1),  # LCCASTFL
    info(696,4),  # LCCASLEB
    info(700,4),  # LCCASLIP
    info(704,8),  # LCCALWTM
    info(712,4),  # LCCASSA2
    info(716,4),  # LCCASSA5
    info(720,8),  # LCCASRBF
    info(728,4),  # LCCAORMT
    info(732,4),  # LCCANHTM
    info(736,4),  # LCCAIOWA
    info(740,4),  # LCCAIOR1
    info(744,4),  # LCCAIOR2
    info(748,4),  # LCCAIOR3
    info(754,1),  # LCCAR2F2
    info(755,1),  # LCCAWFL2
    info(756,64),  # LCCARSGR
    info(820,16),  # LCCAWDT
    info(836,4),  # LCCACWEB
    info(840,4),  # LCCANWEB
    info(844,1),  # LCCACWEBFLAGS
    info(845,1),  # LCCAR34D
    info(846,2),  # LCCAWUQR
    info(848,4),  # LCCAWUQM
    info(852,8),  # LCCAFWP
    info(860,4),  # LCCASRSA
    info(864,4),  # LCCASMQJ
    info(868,4),  # LCCASPLJ
    info(872,4),  # LCCAETP
    info(876,4),  # LCCAETPB
    info(880,2),  # LCCAALTP
    info(882,2),  # LCCAWUQI
    info(884,2),  # LCCAALTI
    info(886,1),  # LCCADISPATCHMIXFLAGS
    info(887,1),  # LCCAFLGS
    info(888,2),  # LCCAR378
    info(890,2),  # LCCAPALP
    info(892,4),  # LCCARWQL
    info(896,64),  # LCCASGPR
    info(960,1),  # LCCADS0F
    info(961,1),  # LCCAFPFL
    info(962,2),  # LCCAPERC
    info(964,4),  # LCCAPERA
    info(968,4),  # LCCASDUV
    info(972,4),  # LCCAR3CC
    info(976,4),  # LCCAIDUV
    info(980,4),  # LCCAR3D4
    info(984,4),  # LCCASCW1
    info(988,4),  # LCCASCW2
    info(992,4),  # LCCASCW3
    info(996,4),  # LCCASCW4
    info(1000,8),  # LCCA_WUQA_EQPRIRQMDP_TOD
    info(1008,8),  # LCCA_CR0ESAVEAREA
    info(1016,8),  # LCCA_TIMERCR0ESAVEAREA
    info(1024,40),  # LCCAR400
    info(1064,8),  # LCCADIAG428
    info(1072,8),  # LCCASDR8
    info(1080,8),  # LCCAIDR8
    info(1088,2),  # LCCAR440
    info(1090,2),  # LCCADIAG442
    info(1092,4),  # LCCA_SRBPARM
    info(1096,8),  # LCCABEA1
    info(1104,8),  # LCCABEA2
    info(1112,8),  # LCCABEA3
    info(1120,8),  # LCCABEA4
    info(1128,8),  # LCCABEA5
    info(1136,8),  # LCCAELKP
    info(1144,72), # LCCASTG1
    info(1216,20), # LCCASCSA
    info(1236,52), # LCCASREG
    info(1288,1),  # LCCASMSK
    info(1289,1),  # LCCARSMK
    info(1290,1),  # LCCAPGMM
    info(1291,1),  # LCCATCFB
    info(1292,28), # LCCARES1
    info(1320,12), # LCCARES2
    info(1332,4),  # LCCASPSW
    info(1336,4),  # LCCASRGS
    info(1340,4),  # LCCAPRMW
    info(1344,4),  # LCCAPTCB
    info(1348,4),  # LCCAPRTN
    info(1352,8),  # LCCACDXM
    info(1360,4),  # LCCATCBC
    info(1364,4),  # LCCASRBC
    info(1368,4),  # LCCACR8W
    info(1372,4),  # LCCAIOSS
    info(1376,4),  # LCCAIOC3
    info(1380,4),  # LCCAIOC4
    info(1384,4),  # LCCABBRC
    info(1388,4),  # LCCACDS0
    info(1392,4),  # LCCACDS1
    info(1396,4),  # LCCACDS2
    info(1400,4),  # LCCACDS3
    info(1404,4),  # LCCACDS4
    info(1408,4),  # LCCACDS5
    info(1412,4),  # LCCACDS6
    info(1416,4),  # LCCACDS7
    info(1420,4),  # LCCACDS8
    info(1424,4),  # LCCACDS9
    info(1428,4),  # LCCACDSA
    info(1432,4),  # LCCACDSB
    info(1436,4),  # LCCACDSC
    info(1440,4),  # LCCACDSD
    info(1444,4),  # LCCACDSE
    info(1448,4),  # LCCACDSF
    info(1452,64), # LCCASLSA
    info(1516,4),  # LCCARWEB
    info(1520,40), # LCCAPOST
    info(1560,4),  # LCCAALOV
    info(1564,4),  # LCCAPSB2
    info(1568,4),  # LCCALSSD
    info(1572,4),  # LCCALSDP
    info(1576,8),  # LCCAXTIM
    info(1584,4),  # LCCAP3A0
    info(1588,4),  # LCCAP3A1
    info(1592,4),  # LCCAP3A2
    info(1596,4),  # LCCAP3A3
    info(1600,4),  # LCCAP3A4
    info(1604,4),  # LCCAP3A5
    info(1608,4),  # LCCAP3A6
    info(1612,4),  # LCCAP3A7
    info(1616,4),  # LCCAP3A8
    info(1620,4),  # LCCAP3A9
    info(1624,4),  # LCCAP3AA
    info(1628,4),  # LCCAP3AB
    info(1632,4),  # LCCAP3AC
    info(1636,4),  # LCCAP3AD
    info(1640,4),  # LCCAP3AE
    info(1644,4),  # LCCAP3AF
    info(1648,64), # LCCAEMS0
    info(1712,8),  # LCCAPPS1
    info(1720,4),  # LCCAPIC1
    info(1724,4),  # LCCAPTE1
    info(1728,64), # LCCAPGR4
    info(1792,72), # LCCAPSLI
    info(1864,4),  # LCCALSHD
    info(1868,4),  # LCCALSHP
    info(1872,8),  # LCCAPPS3
    info(1880,4),  # LCCAPIC3
    info(1884,4),  # LCCAPTE3
    info(1888,4),  # LCCAP1A0
    info(1892,4),  # LCCAP1A1
    info(1896,4),  # LCCAP1A2
    info(1900,4),  # LCCAP1A3
    info(1904,4),  # LCCAP1A4
    info(1908,4),  # LCCAP1A5
    info(1912,4),  # LCCAP1A6
    info(1916,4),  # LCCAP1A7
    info(1920,4),  # LCCAP1A8
    info(1924,4),  # LCCAP1A9
    info(1928,4),  # LCCAP1AA
    info(1932,4),  # LCCAP1AB
    info(1936,4),  # LCCAP1AC
    info(1940,4),  # LCCAP1AD
    info(1944,4),  # LCCAP1AE
    info(1948,4),  # LCCAP1AF
    info(1952,4),  # LCCAP4A0
    info(1956,4),  # LCCAP4A1
    info(1960,4),  # LCCAP4A2
    info(1964,4),  # LCCAP4A3
    info(1968,4),  # LCCAP4A4
    info(1972,4),  # LCCAP4A5
    info(1976,4),  # LCCAP4A6
    info(1980,4),  # LCCAP4A7
    info(1984,4),  # LCCAP4A8
    info(1988,4),  # LCCAP4A9
    info(1992,4),  # LCCAP4AA
    info(1996,4),  # LCCAP4AB
    info(2000,4),  # LCCAP4AC
    info(2004,4),  # LCCAP4AD
    info(2008,4),  # LCCAP4AE
    info(2012,4),  # LCCAP4AF
    info(2016,4),  # LCCARAR0
    info(2020,4),  # LCCARAR1
    info(2024,4),  # LCCARAR2
    info(2028,4),  # LCCARAR3
    info(2032,4),  # LCCARAR4
    info(2036,4),  # LCCARAR5
    info(2040,4),  # LCCARAR6
    info(2044,4),  # LCCARAR7
    info(2048,4),  # LCCARAR8
    info(2052,4),  # LCCARAR9
    info(2056,4),  # LCCARARA
    info(2060,4),  # LCCARARB
    info(2064,4),  # LCCARARC
    info(2068,4),  # LCCARARD
    info(2072,4),  # LCCARARE
    info(2076,4),  # LCCARARF
    info(2080,8),  # LCCAP1C0
    info(2088,8),  # LCCAP1C1
    info(2096,8),  # LCCAP1C2
    info(2104,8),  # LCCAP1C3
    info(2112,8),  # LCCAP1C4
    info(2120,8),  # LCCAP1C5
    info(2128,8),  # LCCAP1C6
    info(2136,8),  # LCCAP1C7
    info(2144,8),  # LCCAP1C8
    info(2152,8),  # LCCAP1C9
    info(2160,8),  # LCCAP1CA
    info(2168,8),  # LCCAP1CB
    info(2176,8),  # LCCAP1CC
    info(2184,8),  # LCCAP1CD
    info(2192,8),  # LCCAP1CE
    info(2200,8),  # LCCAP1CF
    info(2208,8),  # LCCAP2C0
    info(2216,8),  # LCCAP2C1
    info(2224,8),  # LCCAP2C2
    info(2232,8),  # LCCAP2C3
    info(2240,8),  # LCCAP2C4
    info(2248,8),  # LCCAP2C5
    info(2256,8),  # LCCAP2C6
    info(2264,8),  # LCCAP2C7
    info(2272,8),  # LCCAP2C8
    info(2280,8),  # LCCAP2C9
    info(2288,8),  # LCCAP2CA
    info(2296,8),  # LCCAP2CB
    info(2304,8),  # LCCAP2CC
    info(2312,8),  # LCCAP2CD
    info(2320,8),  # LCCAP2CE
    info(2328,8),  # LCCAP2CF
    info(2336,1),  # LCCAPWAIT
    info(2337,1),  # LCCADACT
    info(2338,2),  # LCCAOILC
    info(2340,4),  # LCCAPSB5
    info(2344,4),  # LCCAP5A0
    info(2348,4),  # LCCAP5A1
    info(2352,4),  # LCCAP5A2
    info(2356,4),  # LCCAP5A3
    info(2360,4),  # LCCAP5A4
    info(2364,4),  # LCCAP5A5
    info(2368,4),  # LCCAP5A6
    info(2372,4),  # LCCAP5A7
    info(2376,4),  # LCCAP5A8
    info(2380,4),  # LCCAP5A9
    info(2384,4),  # LCCAP5AA
    info(2388,4),  # LCCAP5AB
    info(2392,4),  # LCCAP5AC
    info(2396,4),  # LCCAP5AD
    info(2400,4),  # LCCAP5AE
    info(2404,4),  # LCCAP5AF
    info(2408,1),  # LCCAPTR5
    info(2409,1),  # LCCAPMFV
    info(2410,2),  # LCCADIEP
    info(2412,64), # LCCAPGR5
    info(2476,4),  # LCCADSA5
    info(2480,8),  # LCCAPPS5
    info(2488,4),  # LCCAPIC5
    info(2492,4),  # LCCAPTE5
    info(2496,8),  # LCCATTSC
    info(2504,8),  # LCCAWTSC
    info(2512,4),  # LCCATP
    info(2516,4),  # LCCATPU
    info(2520,4),  # LCCAWP
    info(2524,4),  # LCCAWPU
    info(2528,4),  # LCCATPB
    info(2532,4),  # LCCATPUB
    info(2536,4),  # LCCAWPB
    info(2540,4),  # LCCAWPUB
    info(2544,2),  # LCCAOID
    info(2546,1),  # LCCAMTSC
    info(2547,1),  # LCCACTSC
    info(2548,4),  # LCCAPPRI
    info(2552,4),  # LCCACPTM
    info(2556,4),  # LCCACLSD
    info(2560,68), # LCCAWUQA
    info(2628,4),  # LCCAHPWUQ
    info(2632,8),  # LCCASPECHELPREQTOD
    info(2640,8),  # LCCADIAGA50
    info(2648,4),  # LCCAALTCWEB
    info(2652,4),  # LCCAALTPWEB
    info(2656,8),  # LCCARA60
)

lcca_fields = namedtuple("lcca", lcca_field_names)
lcca_info = lcca_fields._make(lcca_offset_length)


def get_lcca_address() -> int:
    address_buffer = bytearray(4)
    read_memory(address_buffer, len(address_buffer), 528)
    address = int.from_bytes(address_buffer, byteorder='big')
    return address


def get_lcca() -> bytearray:
    buffer = bytearray(lcca_pattern.size)
    address = get_lcca_address()
    read_memory(buffer, len(buffer), address)
    return buffer


class LCCA:
    name = "LCCA"
    long_name = "Logical Configuration Communication Area"
    fields = lcca_field_names
    info = lcca_info
    def __init__(self):
        content = lcca_fields._make(lcca_pattern.unpack(get_lcca()))
        self.content = content
