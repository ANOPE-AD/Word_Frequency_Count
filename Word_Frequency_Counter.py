import sklearn.feature_extraction.text as txt
from nltk import pos_tag
import pandas as pd
import os

# 定义函数，读取TXT目录下所有TXT文件

def open_txt_files():
    """
    输入：TXT文件夹路径
    输出：TXT文件夹包含下所有的TXT文件名的列表
    """
    txt_files = []
    folder_path = r'TXT'
    for file in os.listdir(folder_path):
        if file.endswith('.txt'):
            txt_files.append((folder_path + '\\' + file, file))
    return txt_files

# 从TXT文件夹读取相应的TXT文件
def read_txt_files(folder_path):
    """
    输入：TXT文件夹路径
    输出：TXT文件夹下所有TXT文件内容的字符串
    """
    txtFile = open(folder_path, 'r', encoding='utf-8')
    text = txtFile.read()
    txtFile.close()
    return text


# 定义函数，对文本进行分词、词频统计
def word_frequency_count(text):
    """
    输入：文本字符串
    输出：词频统计结果，DataFrame格式
    """
    Word_Count_Dict = {}     # 词频统计字典
    Word = []
    # 加载停用词词典
    stopset = list(txt.ENGLISH_STOP_WORDS)
    # 扩充停用词词典
    with open('./stop_word.txt', 'r', encoding='utf-8') as f:
        for word in f.readlines():
            word = word.replace('\n', '')
            if word not in stopset:
                stopset.append(word)
    # 对文本进行分词
    words = txt.CountVectorizer().build_tokenizer()(text)
    # 词性标注
    pos_tags = pos_tag(words)
    # pos_tags转换为一一对应的字典
    pos_dict = {}
    for i in range(len(pos_tags)):
        pos_dict[pos_tags[i][0]] = pos_tags[i][1]
    # 过滤掉停用词
    words = [word for word in words if word.lower() not in stopset]
    # 判断词性，只保留专有名词
    words = [word for word in words if pos_dict[word] in ['NNP', 'NNPS']]

    # 统计词频
    for word in words:
        if word not in Word:    #如果不在词频统计字典中，则添加
            Word_Count_Dict[word] = 1
            Word.append(word)
        elif word in Word:   #否则，词频加1
            Word_Count_Dict[word] += 1
        else:
            continue

    # 将词频统计字典转换为DataFrame格式
    Word_Count_DF = pd.DataFrame(list(Word_Count_Dict.items()), columns=['Word', 'Frequency'])
    Word_Count_DF = Word_Count_DF.sort_values(by='Frequency', ascending=False)   # 按词频降序排列
    return Word_Count_DF

if __name__ == '__main__':  # 主函数

    # 读取TXT文件
    fileFloder = open_txt_files()
    for file_tuple in fileFloder:
        targetFile = file_tuple[1]   
        text = read_txt_files(file_tuple[0])   # 读取目标TXT文件内容
        # 调用函数，输出词频统计结果
        Word_Count_DF = word_frequency_count(text = text)

        # 将结果保存为JSON文件和CSV文件
        Word_Count_DF.to_json('JSON\\%s.json'%targetFile, orient='records')
        Word_Count_DF.to_csv('CSV\\%s.csv'%targetFile, index=False)