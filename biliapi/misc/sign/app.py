# Copyright (C) 2024 originalFactor
#
# This file is part of BiliAPI.
#
# BiliAPI is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BiliAPI is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BiliAPI.  If not, see <https://www.gnu.org/licenses/>.

from typing import Any, Dict
from urllib.parse import urlencode
from hashlib import md5

# 来自文档的通用Appkey和Appsec
APPKEY = '1d8b6e7d45233436'
APPSEC = '560c52ccd288fed045859ed18bffd973'


def sign(params: Dict[str, Any]) -> Dict[str, Any]:
    '''对参数签名'''
    # 增加appkey
    params['appkey'] = APPKEY
    # 增加签名
    params["sign"] = md5(
        (
            urlencode(
                dict(sorted(params.items()))
            )
            +
            APPSEC
        ).encode()
    ).hexdigest()
    return params
