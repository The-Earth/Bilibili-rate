# bilibili-rate

使用神经网络对视频网站 [bilibili](https://www.bilibili.com) 的视频进行大致范围为 0-5 的评分，评分越高则越推荐用户观看。

## 依赖

```
tensorflow==1.12.0
matplotlib==3.0.2
requets==2.21.0
```

调试时使用 Python：3.6.7

## 使用

建议在命令行中使用，主要的脚本是 `train.py` 和 `Main_Data.py` 。不论是进行训练还是进行预测，首先要确保要用到的视频数据存在于数据库中。使用 `Main_Data.py` ，可建立、读取、添加数据库内容，按提示操作。此后训练与预测分数均直接使用数据库中的信息。使用 `train.py` 进行神经网络的训练与预测。可使用指定范围的视频数据进行训练；选择指定范围的视频，输出预测的误差，查看某个视频的预测值。关于视频编号：若一个视频的链接为 `https://www.bilibili.com/video/av37786737` 则其视频编号为 `37786737`。

## vid.py

`getinfo(aid)` 的 aid 接收 Bilibili 视频编号，函数返回一个字典，包含所需的视频信息。字典中的 key 参见 datastructure.txt 的示例。若 aid 对应的视频不存在，则会返回一个整数 404，使用中应注意检查返回值是否为 404。

可以遍历一段视频编号，循环中调用 `getinfo(aid)` 批量获取数据。在同目录下在其他 `.py` 文件中调用示例：

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

存储 Bilibili api 信息，在 `vid.py` 中使用。

## DataProcess.py

数据存储核心脚本，调用 `vid.py` 实现抓取，并存入数据库文件，读取数据库也通过这个脚本。`Builtdatabase()` 是在同级目录下建立数据库文件；`InsertData(aid)` 根据视频编号aid，爬取视频特征数据，并存入数据库；`ExportData(aid)` 根据视频编号aid,在数据库中查找目标数据并按列表返回。

使用 SQLite 数据库，字段包括视频编号、评论数、分区、播放数、收藏数、上传者、硬币数等信息以及评分。**说明**：这里使用了非线性的公式计算得出分数（大量视频一个个看太辛苦了），基本上符合我们的偏好。因此神经网络在这里的作用相当于复现这个非线性模型。

## Main_Data.py

数据库接口，帮助人工操作数据库文件。

## train.py

`train()` 读取指定编号范围内数据库内容并训练网络。若检测到现存模型，则先读取模型后训练。输入层 `invec` 接收训练数据，传递给 `hl1` 、`hl2` 最后到 `prediction` 层，与 `out` 数据比对得到误差 `loss` 。`fig` 参数控制是否绘制误差变化图（若选择输出，则保存在 `loss_process.png`，范围内最后一个视频须存在，否则输出图里不会有内容）。训练 100 次，可选择是否输出误差变化图。模型存于 `./tf/` 目录下，tensorboard 数据流图存于 `./graph/`。

`lossdis()` 用模型计算指定编号范围内视频的分数，并与目标值对比得到误差，输出散点图 `loss_dis.png`（横坐标视频编号，纵坐标误差值）。

`predict()` 读取已训练模型，输出指定视频的评分。

视频数据通过调用 `DataProcess.py` 读取数据库获得。
