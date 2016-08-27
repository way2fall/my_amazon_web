from flask import current_app


# 文件格式检查，有“.”并且是允许的格式则返回True
def allowed_file(filename):
    return '.' in filename and filename.split('.')[-1] in current_app.config['ALLOWED_EXTENSIONS']


def split_phrases(phrases, limit):
    with open('brands.txt', encoding='utf-8') as b:
        brands = [brand.strip().lower() for brand in b.readlines()]
    phrases = [i.strip().lower() for i in phrases]
    phrases_li = []
    for i in phrases:
        phrase_list = i.split(' ')
        new_phrase = ' '.join([i for i in phrase_list if i not in brands])
        # print('this is new phrase:', new_phrase)
        phrases_li.append(new_phrase)
        # print(phrase_list)
    # return phrases_li
    # print(phrases_li)
    length = 0
    inner_group = []
    outer_group = []
    final = []
    for i in phrases_li:
        if length + len(i) < limit:
            # print("AAA")
            if i != phrases_li[-1]:
                # print("CCC")
                inner_group.append(i)
                # print(i)
                length = length + len(i) + 1
            else:
                # print('DDD')
                inner_group.append(i)
                outer_group.append(inner_group)
                length = 0
                inner_group = []

        elif i != phrases_li[-1]:
            # print("BBB")
            outer_group.append(inner_group)
            inner_group = []
            inner_group.append(i)
            length = len(i) + 1
        else:
            outer_group.append(inner_group)
            inner_group = []
            inner_group.append(i)
            outer_group.append(inner_group)

    for j in outer_group:
        k = ','.join(j)
        final.append(k)

    return final


def split_words(words, limit):
    with open('brands.txt', encoding='utf-8') as b:
        brands = [brand.strip().lower() for brand in b.readlines()]    # 将brands全部转为小写
        # print(brands)
    words_chaos = list(set([i.lower() for i in words]) - set(brands))    # 将传入的word列表转为小写后删除brands中的品牌
    words = [i.strip().lower() for i in words]
    words_chaos.sort(key=words.index)    # 当words_chaos中包含words中没有的词时无法这样使用
    length = 0
    partial = []
    nested_partial = []
    final = []
    for i in words_chaos:
        if length + len(i) + 1 < limit:
            if i != words_chaos[-1]:
                nested_partial.append(i)
                length = length + len(i) + 1
            else:
                nested_partial.append(i)
                partial.append(nested_partial)
                length = 0
                nested_partial = []
        elif i != words_chaos[-1]:
            partial.append(nested_partial)
            nested_partial = []
            nested_partial.append(i)
            length = len(i) + 1
        else:
            partial.append(nested_partial)
            nested_partial = []
            nested_partial.append(i)
            partial.append(nested_partial)

    for i in partial:
        j = ' '.join(i)
        final.append(j)
    return final