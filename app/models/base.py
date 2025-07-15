from collections import namedtuple
import networkx as nx

info = namedtuple('info', 'offset length')

zblocks_list = []

zblocks_graph = nx.Graph()

zblocks_graph.add_nodes_from(zblocks_list)
zblocks_graph.add_edge("PSA", "CVT", path="FLCCVT")
zblocks_graph.add_edge("PSA", "PCCA", path="PSAPCCAV")
zblocks_graph.add_edge("PSA", "LCCA", path="PSALCCAV")
zblocks_graph.add_edge("PSA", "ASCB", path="PSAAOLD")
zblocks_graph.add_edge("PSA", "TCB", path="PSATOLD")
zblocks_graph.add_edge("CVT", "ASVT", path="CVTASVT")
zblocks_graph.add_edge("CVT", "ECVT", path="CVTECVT")
zblocks_graph.add_edge("ASCB", "ASSB", path="ASCBASSB")
zblocks_graph.add_edge("ASCB", "ASXB", path="ASCBASXB")
zblocks_graph.add_edge("ASCB", "OUCB", path="ASCBOUCB")
zblocks_graph.add_edge("ASSB", "JSAB", path="ASSBJSAB")
zblocks_graph.add_edge("ASXB", "ACEE", path="ASXBSENV")
zblocks_graph.add_edge("TCB", "JSCB", path="TCBJSCB")
zblocks_graph.add_edge("TCB", "ACEE", path="TCBSENV")