import json
import pandas as pd

# 加载数据
data = open('data/index.json', 'r', encoding='utf-8') 
index = json.load(data)  # 索引字典

fileName = 'data/csl_40k.tsv'
tsv_file = pd.read_csv(
    fileName,
    delimiter='\t',
    names=["title", "abstract", "keywords", "discipline", "category"],
    error_bad_lines=False,
    encoding='utf-8'
)

def bool_retrieval(string):
    # and优先级大于or
    if string.count('and')*string.count('or') > 0:
        a = string[:string.find('or')]
        b = string[string.find('or')+2:]
        bool_retrieval(a)
        bool_retrieval(b)

    elif 'or' in string:
        key = string.split('or')
        value = set(index[key[0]])
        for i in range(1, len(key)):
            value = value.union(set(index[key[i]]))
        for col in list(value):
            print(col, tsv_file.iloc[col, 0])

    elif 'and' in string:
        key = string.split('and')
        value = set(index[key[0]])
        for i in range(1, len(key)):
            value = value.intersection(set(index[key[i]]))
        for col in list(value):
            print(col, tsv_file.iloc[col, 0])
    
    else:
        value = set(index[string])
        for col in list(value):
            print(col, tsv_file.iloc[col, 0])

bool_retrieval(input()) 