import pandas as pd
import json
import jieba

# 判断是否为中文
def is_chinese(check_str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True     
        else:
            return False

# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


def clean_list(seg_list):
    cleaned_list = []
    stopwords = stopwordslist('data/cn_stopwords.txt')  # 这里加载停用词的路径
    for i in seg_list:
        i = i.strip().lower()
        if i != '' and is_chinese(i) and i not in stopwords:
            cleaned_list.append(i)
    return cleaned_list

# 对句子进行分词
def seg_sentence(sentence):
    # print(sentence)
    seg_list = jieba.lcut(sentence, cut_all=False)
    cleaned_list = clean_list(seg_list)
    return cleaned_list


fileName = 'data/csl_40k.tsv'

tsv_file = pd.read_csv(
    fileName,
    delimiter='\t',
    names=["title", "abstract", "keywords", "discipline", "category"],
    error_bad_lines=False,
    encoding='utf-8'
)

# tsv_file['id'] = range(1, len(tsv_file) + 1)  # 给每个文档添加新属性，方便索引
# tsv_file = tsv_file[["id", "title", "abstract", "keywords", "discipline", "category"]]  # 对原始列重新排序，使自增列位于最左侧

result = []  # 存储(index，[abstract])的列表

for index, row in tsv_file.iterrows():
    cleaned_list = seg_sentence(row['abstract'])
    result.append((index, cleaned_list))

with open('data/abstract.json', 'w') as f:
    json.dump(result, f, indent=1)