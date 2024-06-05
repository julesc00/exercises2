import re

tag = "bigdata,owner:dxs01yf,term2"
kv_list = []
tags_list = tag.split(",")
print(tags_list)
for tag in tags_list:
    if ":" in tag:
        kv_list.append(tag)

print(kv_list)
