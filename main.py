import json
import requests
import time

s1 = "人民大学"
s2 = "雍和宫"
# https://map.bjsubway.com/searchstartend?start=xxx&end=xxx&mintype=1
with open("subway.json", encoding="utf-8") as f:
    subway_list = json.loads(f.read())
    print(subway_list)

# 获取s1地铁到其他全部地铁的时间
result = []
for subway in subway_list:
    time.sleep(1)
    print(s1 + ":" + subway)
    try:
        url = f"https://map.bjsubway.com/searchstartend?start={s1}&end={subway}&mintype=1"
        res = requests.get(url)
        res = res.json()
        minutes = res['fangan'][0]['m']
        result.append({
            "开始": s1,
            "结束": subway,
            "用时": minutes
        })
    except Exception as e:
        print(subway + "出错了")

with open(f"s1.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(result, ensure_ascii=False))

# 获取s2地铁到其他全部地铁的时间
result = []
for subway in subway_list:
    time.sleep(1)
    print(s2 + ":" + subway)
    try:
        url = f"https://map.bjsubway.com/searchstartend?start={s2}&end={subway}&mintype=1"
        res = requests.get(url)
        res = res.json()
        minutes = res['fangan'][0]['m']
        result.append({
            "开始": s2,
            "结束": subway,
            "用时": minutes
        })
    except Exception as e:
        print(subway + "出错了")

with open(f"s2.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(result, ensure_ascii=False))

