# BiliAPI

利用`pydantic`的力量，构建完善的哔哩哔哩API SDK。

## 贡献

- `pydantic`: 提供类型检查
- `httpx`: 优秀的HTTP客户端
- `socialsisteryi/bilibili-API-collect`: 提供文档参考

## 声明

因为作者懒得整理，所以会使用GitHub workflow执行`workflow/pull_appkeys.py`，从`socialsisteryi/bilibili-API-collect`的GitHub Pages
拉取部分常量，解析为`json`并保存在`docs/assets`文件夹中。