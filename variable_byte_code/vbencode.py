# -*- coding: UTF-8 -*-
from struct import pack, unpack
import variable_byte_code as vb
import os

r_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "eid_tags.txt")
w_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "encode.txt")

with open(r_path, 'r', encoding="UTF-8") as r_fp, open(w_path, 'wb') as w_fp:
    for line in r_fp:
        split_line = line.rstrip().split('\t')
        tag = split_line[0]
        id_list = split_line[1]
        bytes = []
        for id in id_list.split(','):
            id = int(id)
            bytes.append(vb.vb_encode(id))
        w_fp.write(pack("2i", len(tag.encode()), len(b"".join(bytes))) + tag.encode() +  b"".join(bytes))