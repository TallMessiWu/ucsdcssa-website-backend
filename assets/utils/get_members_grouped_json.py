import json
import os
from collections import defaultdict


def get_members_grouped_json():
    files = list(os.walk("../members-photos"))[0][2]
    members = sorted([i.split(".")[0].split("-") for i in files])
    members_grouped = defaultdict(list)
    [members_grouped[department].append(
        {
            "name": name,
            "position": position,
            "photoSrc": "{}-{}-{}.jpg".format(department, name, position)
        }
    ) for department, name, position in members]
    with open("../members_grouped.json", "w", encoding="utf-8") as f:
        json.dump(members_grouped, f, ensure_ascii=False)
    print("脚本执行完毕")


if __name__ == '__main__':
    get_members_grouped_json()
