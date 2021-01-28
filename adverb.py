import CaboCha
import re
import csv
import json

def judge(sentence, adverb, attach):
    c = CaboCha.Parser()
    tree = c.parse(sentence)
    chunks = []
    text = ""
    attachIds = []
    toChunkId = -1
    looking = -1

    for i in range(0, tree.size()):
        token = tree.token(i)
        text = token.surface if token.chunk else (text + token.surface)
        # 文節で区切る

        toChunkId = token.chunk.link if token.chunk else toChunkId
        # かかり先をメモ

        if token.feature.split(',')[-1] in adverb and token.feature.split(',')[0] == "副詞":
            looking = len(chunks)
        # 目標の副詞が含まれていればIDを記録


        if token.feature.split(',')[-3] in attach:
            attachIds.append(len(chunks))

        # 目標の付属語があるIDを記録

        if i == tree.size() - 1 or tree.token(i+1).chunk:
            chunks.append({'c': text, 'to': toChunkId})
        # 文節毎に出力

    # for j in range(len(chunks)):
    #     chunk = chunks[j]
    #     if chunk['to'] >= 0:
    #         print(j, chunk['c'] + " →　" + chunks[chunk['to']]['c'])
    # デバッグ用。係り受け解析結果を表示する。

    if looking == -1:
        return None

    while looking != -1:
        if chunks[looking]['to'] in attachIds:
            return True
            # 係り受け関係にある文節に目的のフレーズがある場合はTrueを返す
        else:
            looking = chunks[looking]['to']
            # 係り受け関係にある文節に目的の単語がない場合、更に係り受け関係にある文節をチェックする
    return False
    # 目的のフレーズがなければFalseを返す

def analysis(fileName, adverb, attach, result):
    corpus = open('./data/' + fileName + '.txt', encoding='utf-8').read().split('\n')

    result.append([adverb[0], 'True'])
    result[-1].extend([0 for i in range(41)])
    result.append([adverb[0], 'False'])
    result[-1].extend([0 for i in range(41)])

    for i in range(1,len(corpus)-1):
        corpus[i] = re.sub('　|「|」', '', corpus[i])
        corpus[i] = corpus[i].split('\t')
        corpus[i][3] = corpus[i][3].split(';')[-1]
        corpus[i][5] = corpus[i][5].split(';')[0]
        # ファイルから目的の文章を切り取る


        if fork := judge(''.join(corpus[i][3:6]), adverb, attach=attach):
            result[-2][int(corpus[i][30]) - 1968] += 1
        elif fork == False:
            result[-1][int(corpus[i][30]) - 1968] += 1
            contents = str(i) + ', ' + adverb[0] + ', ' + '|'.join(attach) + ', ' + ''.join(corpus[i][3:6])
            with open('./exception.csv', mode='a', encoding='utf=8') as f:
                f.write(contents)
                f.write('\n')
        elif fork is None:
            pass
        # 判定結果を変数"fork"に代入し、条件式で分岐
        # 結果がTrue or Falseの場合Resultの該当箇所をインクリメントさせる
        # Falseの結果をまとめたcsvファイルに文章を追記
        # 該当する副詞が見つからない場合は何もしない
    return result



if __name__ == '__main__':
    result = [['副詞', '対応有無']]
    result[0].extend([i for i in range(1970,2011)])

    data = json.load(open('./adverbList.json', encoding='utf-8'))

    for i in data:
        result = analysis(i['fileName'], i['adverb'], i['attach'], result)

    with open('result.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(result)
