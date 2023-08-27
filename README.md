<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-simple-httpcat

_✨ 适用于nonebot2 v11、简单粗暴的httpcat插件 调用https://http.cat的图片✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/XTxiaoting14332/nonebot-plugin-simple-httpcat.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-simple-httpcat">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-simple-httpcat.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>



## 📖 介绍

简单粗暴的httpcat插件，参考了<a href="https://github.com/zjkwdy/nonebot_plugin_weather_lite">zjkwdy大佬的weather_lite插件</a>,调用了https://http.cat中的图片(<br>


## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令安装

    nb plugin install nonebot-plugin-simple-httpcat

</details>

<details>
<summary>pip安装</summary>

    pip install nonebot-plugin-simple-httpcat

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_simple_httpcat"]
</details>
<details>
<summary>Github下载</summary>
手动克隆本仓库或直接下载压缩包，将里面的nonebot_plugin_simple_httpcat文件夹复制到src/plugins中
</details>


</details>

## 🎉 使用
### 指令表(请加上指令前缀，在没有更改的情况下，默认为"/")
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| cat | 群员 | 否 | 群聊 | 需要在后面加上状态码|
### 示例
<img src="./image/1.png" alt="示例图片1">

</div>
/cat 状态码

<img src="./image/2.png" alt="示例图片2">

</div>
单纯的/cat 