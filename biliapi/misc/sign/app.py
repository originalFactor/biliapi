from typing import Dict
from urllib.parse import urlencode
from hashlib import md5
from .assets.app import findAppKey

def sign(params:Dict[str,any], platfrom:Dict[str,str]):
    '''对参数签名'''
    appKey = findAppKey(platfrom)
    # 增加appkey
    params.update({'appkey': appKey.key})
    # 增加签名
    params.update({
        "sign": md5(
            (
                urlencode(
                    dict(sorted(params.items()))
                )
                +
                appKey.sec
            ).encode()
        ).hexdigest()
    })
    return params
