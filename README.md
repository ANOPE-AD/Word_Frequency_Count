# Word_Frequency_Count
英文词频统计--对英语小说文本（txt格式）进行高频词提取的Python脚本，用于产生术语表建议。

## 环境要求：
- Python 3.6+
- sklearn、pandas、nltk库

## 运行方法：
0. 先在命令行中进入到项目目录
1. 运行 pip install -r requirements.txt ，然后再运行python prev.py安装所需的库
2. 将待分析的文本文件（txt格式）放入到TXT目录下
3. 在命令行中运行 python word_frequency_count.py
4. 等待程序运行完成，输出结果可以在CSV目录和JSON目录下查看

## 注意事项：
- CSV文件可以用Excel打开查看，JSON文件可以用记事本打开查看。
- 程序运行时间取决于文本文件大小，建议文本文件大小不超过10MB。
- 程序运行完成后，会在CSV目录下生成一个以文本文件名命名的csv文件，该文件包含了文本中出现的词及其次数。