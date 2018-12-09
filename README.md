# bilibili-rate

## vid.py
`getinfo(aid)` 的 aid 接收 Bilibili 视频编号，函数返回一个字典，包含所需的视频信息。字典中的 key 参见 datastructure.txt 的示例。若 aid 对应的视频不存在，则会返回一个整数 404，使用中应注意检查返回值是否为 404。

可以考虑遍历一段视频编号，循环中调用 `getinfo(aid)` 批量获取数据。在同目录下在其他 `.py` 文件中调用示例：

```python
import vid

data = []
for aid in range(36020000, 36020100):
    data.append(vid.getinfo(aid))
# rest of code
```

上面的示例中，`data` 中以 `list` 形式存储了一个个包含视频数据的字典。

感谢：[Bilibili-data](https://github.com/FQrabbit/bilibili-data)

## bilibilisupport.py

存储 Bilibili api 信息

## DataProcess.py

数据存储核心脚本，调用 `vid.py` 实现抓取，另可操作数据库文件。

## Main_Data.py

数据库接口，帮助人工操作数据库文件。

## train.py

`train()` 读取数据库内容并训练网络。若检测到现存模型，则先读取模型后训练。`lossdis()` 用模型预测视频的分数，并与目标值对比，并画图。

感谢：[不会停的蜗牛@简书](https://www.jianshu.com/p/e112012a4b2d)
