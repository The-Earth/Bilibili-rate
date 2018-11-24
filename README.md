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

感谢：[Bilibili-data](https://github.com/TimeCompass/bilibili-data)

## train.py

读入数据训练模型，一般直接运行。

感谢：[不会停的蜗牛@简书](https://www.jianshu.com/p/e112012a4b2d)
