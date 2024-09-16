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

from importlib.util import find_spec
from httpx import AsyncClient
import zstandard

http = AsyncClient(
    headers={
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate' +
        (', br' if find_spec('brotlipy') else '') +
        (', zstd' if find_spec('zstandard') else ''),
        'accept-language': 'zh-CN,zh;q=0.9',
        'origin': 'https://www.bilibili.com',
        'referer': 'https://www.bilibili.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.200 Safari/537.36'
    }
)
