# 自动从GitHub获取APPKey和APPSec
from os.path import exists, expanduser
from logging import getLogger
from json import load
from typing import List, Dict, Union
from random import choice
from pydantic import BaseModel, Field

logger = getLogger(__name__)

BILIBILI_APPKEY_PATH = expanduser("~")+'/.bilibiliappkeys.json'

def checkIfExists():
    ''' 检查APPKEYS文件是否已存在 '''
    if not exists(BILIBILI_APPKEY_PATH):
        from httpx import get
        
        try:
            response = get("https://originalfactor.github.io/biliapi/assets/sign/app/appkeys.json")
        except Exception as e:
            logger.error(f"Couldn't download online APPKey and APPSec because network error. Exception: {e}")
            raise e

        if response.status_code!=200:
            logger.error(f"Couldn't download online APPKey and APPSec data because server returned an invaild status code: {response.status_code}")
            raise Exception("Core data not avaliable.")

        try:
            with open(BILIBILI_APPKEY_PATH, 'wb') as f:
                f.write(response.content)
        except Exception as e:
            logger.error(f'Couldn\'t save AppKey and AppSec. Exception: {e}')
            raise e

def getAppKey()->List[Dict[str,str]]:
    '''加载APPKEYS'''
    global APPKEYS
    if not APPKEYS:
        checkIfExists()
        try:
            with open(BILIBILI_APPKEY_PATH, 'r') as f:
                APPKEYS = load(f)
        except Exception as e:
            logger.error(f"Could't open AppKey and AppSec. Exception: {e}")
            raise e

APPKEYS = []

class AppKey(BaseModel):
    key : str = Field(alias="APPKEY")
    sec : str = Field(alias="APPSEC")

def findAppKey(platform:Union[Dict[str,str], None])->Union[AppKey,None]:
    '''从APPKEYS查找APPKEY'''
    if not platform: return AppKey(**choice(APPKEYS))
    for appKey in APPKEYS:
        for key, value in platform.items():
            if appKey[key]!=value:
                break
        else:
            return AppKey(**appKey)
    return None
