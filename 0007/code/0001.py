"""
第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
"""


import secrets


def Generate_Key(counts,length=16):
    key_list = []

    for i in range(counts):
        key = secrets.token_urlsafe(length)
        if key not in key_list:
            key_list.append(key)

    return key_list

if __name__ == "__main__":
    key_list = Generate_Key(200,12)
    for i in key_list:
        print(i)