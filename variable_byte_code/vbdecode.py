# -*- coding: UTF-8 -*-
import os
from struct import pack, unpack
import variable_byte_code as vb

r_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "encode.txt")
w_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "decode.txt")

with open(r_path, 'rb') as r_fp, open(w_path, 'w', encoding="UTF-8", newline="\n") as w_fp:
    while True:
        bytes = r_fp.read(8)
        if not bytes:
            break
        (tag_len, id_list_len) = unpack("2i", bytes)
        tag = r_fp.read(tag_len)
        id_list = []
        decodes = vb.vb_decode(r_fp.read(id_list_len))
        for id in decodes:
            id_list.append("%s" % id)
        w_fp.write("%s\t%s\n" % (tag.decode(), ",".join(id_list)))

