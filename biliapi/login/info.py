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

'登录基本信息'

from enum import Enum
from typing import Annotated, Union, Optional
from os.path import split, splitext
from pydantic import BaseModel, Field, field_validator
from .. import http
from ..user.official_role import OfficialRole


class NavCode(int, Enum):
    '状态栏接口返回值'
    SUCCESS = 0  # 成功
    SIGNED_OUT = -101  # 未登录


class LevelInfo(BaseModel):
    '等级信息'
    current_level: int  # 当前等级
    current_min: int  # 当前等级经验最低值
    current_exp: int  # 当前经验
    next_exp: Union[int, str]  # 升级下一等级需达到的经验 正常为数字，六级为字符串'--'


class OfficialType(int, Enum):
    '是否认证'
    UNVALIDATED = -1
    VALIDATED = 0


class Official(BaseModel):
    '认证信息'
    role: OfficialRole
    title: str  # 认证信息
    desc: str  # 认证备注
    type: OfficialType


class OfficialVerify(BaseModel):
    '认证验证'
    type: OfficialType
    desc: str  # 认证信息


class Pendant(BaseModel):
    '头像框信息'
    pid: int  # 挂件id
    name: str  # 挂件名称
    image: str  # 挂件图片url
    expire: int


class LabelTheme(str, Enum):
    '会员标签类型'
    VIP = 'vip'  # 大会员
    ANNUAL_VIP = 'annual_vip'  # 年度大会员
    TEN_ANNUAL_VIP = 'ten_annual_vip'  # 十年大会员
    HUNDRED_ANNUAL_VIP = 'hundred_annual_vip'  # 百年大会员


class VIPLabel(BaseModel):
    '会员标签'
    path: str
    text: str  # 会员名称
    label_theme: LabelTheme


class VIPType(int, Enum):
    '会员类型'
    no = 0  # 无会员
    monthly = 1  # 月度
    yearly = 2  # 年度


class Wallet(BaseModel):
    'B币钱包信息'
    mid: int  # 登录用户的mid
    bcoin_balance: int  # 拥有B币数
    coupon_balance: int  # 每月奖励B币数
    coupon_due_time: int


class WBI(BaseModel):
    'WBI签名实时口令'
    img_key: Annotated[str, Field(alias='img_url')]  # imgKey
    sub_key: Annotated[str, Field(alias='sub_url')]  # subKey

    @field_validator('img_key', 'sub_key')
    @classmethod
    def url2key(cls, v: str) -> str:
        '将伪装url转换为key'
        return splitext(split(v)[1])[0]


class NavData(BaseModel):
    '状态栏接口消息本体'
    isLogin: bool  # 是否已登录
    email_verified: Optional[bool] = None  # 邮箱验证状态
    face: Optional[str] = None  # 用户头像url
    level_info: Optional[LevelInfo] = None
    mid: Optional[int] = None  # 用户mid
    mobile_verified: Optional[bool] = None  # 手机号验证状态
    money: Optional[int] = None  # 拥有硬币数
    moral: Optional[int] = None  # 当前节操值
    official: Optional[Official] = None
    officialVerify: Optional[OfficialVerify] = None
    pendant: Optional[Pendant] = None
    scores: Optional[int] = None
    uname: Optional[str] = None  # 用户昵称
    vipDueDate: Optional[int] = None  # vip到期时间戳
    vipStatus: Optional[bool] = None  # 会员状态
    vipType: Optional[VIPType] = None
    vip_pay_type: Optional[bool] = None  # 会员状态
    vip_theme_type: Optional[int] = None
    vip_label: Optional[VIPLabel] = None
    vip_avatar_subscript: Optional[bool] = None  # 是否显示会员图标
    vip_nickname_color: Optional[str] = None  # 会员昵称颜色 16进制颜色码
    wallet: Optional[Wallet] = None
    has_shop: Optional[bool] = None  # 是否拥有推广商品
    shop_url: Optional[str] = None  # 商品推广页面url
    allowance_count: Optional[int] = None
    answer_status: Optional[int] = None
    is_senior_member: Optional[bool] = None  # 是否硬核会员
    wbi_img: WBI
    is_jury: Optional[bool] = None  # 是否风纪委员


class NavResponse(BaseModel):
    'nav接口返回模型'
    code: NavCode
    message: str = "0"  # 错误信息
    ttl: int = 1
    data: NavData


async def nav(sessdata: Optional[str] = None) -> NavResponse:
    '导航栏用户信息接口'
    return NavResponse.model_validate_json(
        (await http.get(
            'https://api.bilibili.com/x/web-interface/nav',
            cookies=({'SESSDATA': sessdata} if sessdata else None)
        )).content
    )
