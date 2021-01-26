import CaboCha
import re

def judge(sentence, adverb, attach=False, form=False):
    c = CaboCha.Parser()
    tree = c.parse(sentence)
    # exit()
    chunks = []
    text = ""
    attachIds = []
    toChunkId = -1
    looking = -1

    for i in range(0, tree.size()):
        token = tree.token(i)
        text = token.surface if token.chunk else (text + token.surface)

        toChunkId = token.chunk.link if token.chunk else toChunkId
        # 文節で区切る

        if token.feature.split(',')[-1] == adverb:
            looking = len(chunks)
        # 目標の副詞が含まれていればIDを記録

        # print(token.feature.split(','))
        if attach:
            for j in attach:
                if token.feature.split(',')[-3] == j:
                    attachIds.append(len(chunks))
        else:
            if token.feature.split(',')[5] == form:
                attachIds.append(len(chunks))
        # 目標の付属語があるIDを記録

        if i == tree.size() - 1 or tree.token(i+1).chunk:
            chunks.append({'c': text, 'to': toChunkId})
        # 文節毎に出力

    for j in range(len(chunks)):
        chunk = chunks[j]
        if chunk['to'] >= 0:
            print(j, chunk['c'] + " →　" + chunks[chunk['to']]['c'])

    if looking == -1:
        return None

    while looking != -1:
        if chunks[looking]['to'] in attachIds:
            return True
        else:
            looking = chunks[looking]['to']
    return False
    # 目標の副詞が含まれる文節のかかり先に目標の付属語が存在すればTrueを返す

def analysis(fileName, adverb, attach, result):
    corpus = open(fileName + '.txt', encoding='utf-8').read().split('\n')

    result.append([adverb, 'True'])
    result[-1].extend([0 for i in range(41)])
    result.append([adverb, 'False'])
    result[-1].extend([0 for i in range(41)])

    for i in range(1,len(corpus)-1):
        corpus[i] = re.sub('　|「|」', '', corpus[i])
        corpus[i] = corpus[i].split('\t')
        # year == corpus[i][30]

        corpus[i][3] = corpus[i][3].split(';')[-1]
        corpus[i][5] = corpus[i][5].split(';')[0]


        if (fork := judge(''.join(corpus[i][3:6]), adverb, attach=attach)):
            result[-2][int(corpus[i][30]) - 1968] += 1
        elif fork == False:
            result[-1][int(corpus[i][30]) - 1968] += 1
            print(i,''.join(corpus[i][3:6]))
        elif fork is None:
            print('none')
            pass
    return result
    # if i > 5:
    #     break



if __name__ == '__main__':
    sentence = ""
    adverb = "ケッシテ"
    attach = ["ない", "ぬ", "ん"]
    fileName = 'kesshite'

    result = [['副詞', '対応有無']]
    result[0].extend([i for i in range(1970,2011)])


    print(analysis(fileName, adverb, attach, result))

    cntTrue = 0
    cntFalse = 0
    # for i in range(1,len(corpus)):
        # print(i)


