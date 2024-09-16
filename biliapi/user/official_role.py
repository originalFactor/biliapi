# Copyright (C) 2024 PsbYu
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

from enum import Enum


class OfficialRole(int, Enum):
    '认证类型'
    unvalidated = 0  # 未认证
    famous = 1  # 知名UP主
    V = 2   # 大V达人
    corporation = 3  # 企业
    organization = 4    # 组织
    media = 5   # 媒体
    government = 6  # 政府
    high_energy_streamer = 7    # 高能主播
    well_known = 8  # 社会知名人士
