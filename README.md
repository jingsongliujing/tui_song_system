# 我在校园自动打卡
# 微信自动推送脚本

我在校园自动打卡程序参考：[zimin9/WoZaiXiaoYuanPuncher](https://github.com/zimin9/WoZaiXiaoYuanPuncher) 的 Github Action 版。
具体抓包看大佬的方法
## 程序效果
![效果](https://github.com/jingsongliujing/tui_song_system/blob/main/qq_pic_merged_1641384838128.jpg)
## 更新日志

- 2022.1.5 修复 pushplus 的推送问题。

## 程序运行环境
- Windows/Linux
- Python 3.6.xx及以上
## 程序依赖包
~~~
pip install -r requirements.txt
~~~

## 功能
- 我在校园自动打卡脚本
- 微信定时推送消息脚本
- 目前有微信自动打卡推送，每日课程表推送，成绩推送

**⚠重要提醒：** 目前为了接口安全，目前还不开放我校的教务接口地址，大家可以尝试用爬虫的方式进行魔改成你想要推送的消息

 > 🎉 感谢 [@胡佬]() ，[@彬哥]()，等津桥助手各位小伙伴的贡献！


## 关于本脚本
- 添加脚本 `daka.py`，适配学校的打卡项目“我在校园多账号健康打卡”。
- 添加脚本 `main.py`，适配学校的打卡项目“健康打卡”。

  > 关于本项目中的三个脚本：
  >
  > - `kaoshi.py`，对应项目“考试成绩推送”。
  >
  > - `kc.py`，对应项目“kc.py”。
  >
  > 两个脚本请按需启用，详见下方使用指南。
  > -'dingshi.py'，可进行定时运行程序和推送任务

## 声明

- 本项目仅供编程学习/个人使用，请遵守Apache-2.0 License开源项目授权协议。

- 请在国家法律法规和校方相关原则下使用。

- 开发者不对任何下载者和使用者的任何行为负责。
