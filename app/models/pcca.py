from app.models.base import info, zblocks_list
from app.utils import read_memory
from struct import Struct
from collections import namedtuple

zblocks_list.append('PCCA')

pcca_pattern = Struct(
    ">"
    "4s"  # PCCAPCCA
    "12s"  # PCCACPID
    "2s"  # PCCACPUA
    "2s"  # PCCACAFM
    "4s"  # PCCATQEP
    "4s"  # PCCAPSAV
    "4s"  # PCCAPSAR
    "1s"  # PCCAISCE
    "3s"  # PCCAMCHF
    "4s"  # PCCACRG6
    "4s"  # PCCASLIH
    "4s"  # PCCASTPI
    "4s"  # PCCAXSLF
    "4s"  # PCCARSPR
    "4s"  # PCCATRW1
    "4s"  # PCCARV88
    "8s"  # PCCA_PARTIALCPUMASK
    "2s"  # PCCA_TQEAID
    "2s"  # PCCARV91
    "4s"  # PCCARV92
    "4s"  # PCCARV93
    "4s"  # PCCARV94
    "4s"  # PCCARV95
    "4s"  # PCCARV96
    "4s"  # PCCARV97
    "4s"  # PCCARV98
    "4s"  # PCCARV99
    "4s"  # PCCARV9A
    "4s"  # PCCARV9B
    "4s"  # PCCARV9C
    "4s"  # PCCARV9D
    "4s"  # PCCARV9E
    "4s"  # PCCATMST
    "4s"  # PCCARPB
    "4s"  # PCCAEMSI
    "4s"  # PCCAEMSP
    "4s"  # PCCAEMSE
    "4s"  # PCCAEMSA
    "4s"  # PCCAPWAV
    "4s"  # PCCAPWAR
    "4s"  # PCCALRBV
    "4s"  # PCCALRBR
    "208s"  # PCCARIOS
    "1s"  # PCCAATTR
    "1s"  # PCCAMFA
    "1s"  # PCCAACRN
    "1s"  # PCCARCFF
    "1s"  # PCCA_PHYSICAL_CPUID
    "1s"  # PCCARSV1
    "2s"  # PCCAPROCCLASS
    "2s"  # PCCAR180
    "2s"  # PCCA_PARTIALCPUMASKOFFSET
    "196s"  # PCCARSV2
)
pcca_field_names = (
    "PCCAPCCA",
    "PCCACPID",
    "PCCACPUA",
    "PCCACAFM",
    "PCCATQEP",
    "PCCAPSAV",
    "PCCAPSAR",
    "PCCAISCE",
    "PCCAMCHF",
    "PCCACRG6",
    "PCCASLIH",
    "PCCASTPI",
    "PCCAXSLF",
    "PCCARSPR",
    "PCCATRW1",
    "PCCARV88",
    "PCCA_PARTIALCPUMASK",
    "PCCA_TQEAID",
    "PCCARV91",
    "PCCARV92",
    "PCCARV93",
    "PCCARV94",
    "PCCARV95",
    "PCCARV96",
    "PCCARV97",
    "PCCARV98",
    "PCCARV99",
    "PCCARV9A",
    "PCCARV9B",
    "PCCARV9C",
    "PCCARV9D",
    "PCCARV9E",
    "PCCATMST",
    "PCCARPB",
    "PCCAEMSI",
    "PCCAEMSP",
    "PCCAEMSE",
    "PCCAEMSA",
    "PCCAPWAV",
    "PCCAPWAR",
    "PCCALRBV",
    "PCCALRBR",
    "PCCARIOS",
    "PCCAATTR",
    "PCCAMFA",
    "PCCAACRN",
    "PCCARCFF",
    "PCCA_PHYSICAL_CPUID",
    "PCCARSV1",
    "PCCAPROCCLASS",
    "PCCAR180",
    "PCCA_PARTIALCPUMASKOFFSET",
    "PCCARSV2",
)
pcca_offset_length = (
    info(0,4),  # PCCAPCCA
    info(4,12),  # PCCACPID
    info(16,2),  # PCCACPUA
    info(18,2),  # PCCACAFM
    info(20,4),  # PCCATQEP
    info(24,4),  # PCCAPSAV
    info(28,4),  # PCCAPSAR
    info(32,1),  # PCCAISCE
    info(33,3),  # PCCAMCHF
    info(36,4),  # PCCACRG6
    info(40,4),  # PCCASLIH
    info(44,4),  # PCCASTPI
    info(48,4),  # PCCAXSLF
    info(52,4),  # PCCARSPR
    info(56,4),  # PCCATRW1
    info(60,4),  # PCCARV88
    info(64,8),  # PCCA_PARTIALCPUMASK
    info(72,2),  # PCCA_TQEAID
    info(74,2),  # PCCARV91
    info(76,4),  # PCCARV92
    info(80,4),  # PCCARV93
    info(84,4),  # PCCARV94
    info(88,4),  # PCCARV95
    info(92,4),  # PCCARV96
    info(96,4),  # PCCARV97
    info(100,4),  # PCCARV98
    info(104,4),  # PCCARV99
    info(108,4),  # PCCARV9A
    info(112,4),  # PCCARV9B
    info(116,4),  # PCCARV9C
    info(120,4),  # PCCARV9D
    info(124,4),  # PCCARV9E
    info(128,4),  # PCCATMST
    info(132,4),  # PCCARPB
    info(136,4),  # PCCAEMSI
    info(140,4),  # PCCAEMSP
    info(144,4),  # PCCAEMSE
    info(148,4),  # PCCAEMSA
    info(152,4),  # PCCAPWAV
    info(156,4),  # PCCAPWAR
    info(160,4),  # PCCALRBV
    info(164,4),  # PCCALRBR
    info(168,208), # PCCARIOS
    info(376,1),  # PCCAATTR
    info(377,1),  # PCCAMFA
    info(378,1),  # PCCAACRN
    info(379,1),  # PCCARCFF
    info(380,1),  # PCCA_PHYSICAL_CPUID
    info(381,1),  # PCCARSV1
    info(382,2),  # PCCAPROCCLASS
    info(384,2),  # PCCAR180
    info(386,2),  # PCCA_PARTIALCPUMASKOFFSET
    info(388,196),  # PCCARSV2
)

pcca_fields = namedtuple("pcca", pcca_field_names)
pcca_info = pcca_fields._make(pcca_offset_length)


def get_pcca_address() -> int:
    address_buffer = bytearray(4)
    read_memory(address_buffer, len(address_buffer), 520)
    address = int.from_bytes(address_buffer, byteorder='big')
    return address


def get_pcca() -> bytearray:
    buffer = bytearray(pcca_pattern.size)
    address = get_pcca_address()
    read_memory(buffer, len(buffer), address)
    return buffer


class PCCA:
    name = "PCCA"
    long_name = "Physical Configuration Communication Area"
    fields = pcca_field_names
    info = pcca_info
    def __init__(self):
        content = pcca_fields._make(pcca_pattern.unpack(get_pcca()))
        self.content = content
