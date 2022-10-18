import json

def bool_retrieval(string):
    data = open('data/index.json', 'r', encoding='utf-8') 
    index = json.load(data)  # 索引字典

    if 'or' in string:
        key = string.split(' or ')
        value = set(index[key[0]])
        for i in range(1, len(key)):
            value = value.union(set(index[key[i]]))
        print(list(value))
    elif 'and' in string:
        key = string.split(' and ')
        value = set(index[key[0]])
        for i in range(1, len(key)):
            value = value.intersection(set(index[key[i]]))
        print(list(value))
    # if string.count('and')*string.count('or') > 0:
    #     a = string[:string.find('or')]
    #     b = string[string.find('or')+3:]
    #     bool_retrieval(a)
    #     bool_retrieval(b)
    # elif 'or' in string:
    #     key = string.split(' or ')
    #     for i in range(len(documentbase)):
    #         for j in range(len(key)):
    #             if key[j] in documentbase[i]:
    #                 print('D%d:'%(i+1),documentbase[i])
    # elif 'and' in string:
    #     key = string.split(' ')
    #     del key[key.index('and')]
    #     for i in range(len(documentbase)):
    #         flag = 1
    #         for j in range(len(key)):
    #             if key[j] not in documentbase[i]:
    #                 flag = 0
    #                 break 
    #         if(flag):
    #             print('D%d:'%(i+1),documentbase[i])


bool_retrieval(input()) 