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

from datetime import datetime, timedelta
from functools import reduce
from hashlib import md5
from typing import Any, Dict
from os.path import split
from urllib.parse import urlencode
from ...login.info import nav

MIXIN_KEY = ''
EXPIRE = datetime(0, 0, 0)

MIXIN_KEY_ENC_TAB = [
    46, 47, 18, 2, 53, 8, 23, 32, 15, 50, 10, 31, 58, 3, 45, 35, 27, 43, 5, 49,
    33, 9, 42, 19, 29, 28, 14, 39, 12, 38, 41, 13, 37, 48, 7, 16, 24, 55, 40,
    61, 26, 17, 0, 1, 60, 51, 30, 4, 22, 25, 54, 21, 56, 59, 6, 63, 57, 62, 11,
    36, 20, 34, 44, 52
]


async def sign(params: Dict[str, Any]) -> Dict[str, Any]:
    global MIXIN_KEY, EXPIRE
    now = datetime.now()
    if EXPIRE <= now:
        wbi = (await nav()).data.wbi_img
        raw_wbi = wbi.img_key+wbi.sub_key
        MIXIN_KEY = reduce(lambda s, i: s+raw_wbi[i], MIXIN_KEY_ENC_TAB, '')
        EXPIRE = datetime.today()+timedelta(1)
    params['wts'] = int(now.timestamp())
    params['w_rid'] = md5(
        (urlencode(dict(sorted(params.items())))+MIXIN_KEY).encode()
    ).hexdigest
    return params
