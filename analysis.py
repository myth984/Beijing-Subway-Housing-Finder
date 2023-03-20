import json

with open("s1.json", encoding="utf-8") as f:
    list_a = json.loads(f.read())

with open("s2.json", encoding="utf-8") as f:
    list_b = json.loads(f.read())

# 共同用时小于20分钟
use_time = 20

result_a = []
for a in list_a:
    if a['用时'] <= use_time:
        result_a.append(a['结束'])
result_b = []
for b in list_b:
    if b['用时'] <= use_time:
        result_b.append(b['结束'])

same = [x for x in result_a if x in result_b]
print(set(same))
