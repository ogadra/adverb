import CaboCha
import re

def judge(sentence, adverb, attach):
    c = CaboCha.Parser()
    tree = c.parse(sentence)
    # exit()
    chunks = []
    text = ""
    attachIds = []
    toChunkId = -1
    adverbId = int()

    for i in range(0, tree.size()):
        token = tree.token(i)
        text = token.surface if token.chunk else (text + token.surface)

        toChunkId = token.chunk.link if token.chunk else toChunkId
        if token.feature.split(',')[-1] == adverb:
            adverbId = len(chunks)

        for j in attach:
            if token.feature.split(',')[-3] == j:
                attachIds.append(len(chunks))

        if i == tree.size() - 1 or tree.token(i+1).chunk:
            chunks.append({'c': text, 'to': toChunkId})
    # print(chunks)
    # print(attachIds)
    # 係り元→係り先の形式で出力する
    return True if chunks[adverbId]['to'] in attachIds else False

if __name__ == '__main__':
    sentence = "男たちは決して口に出した。"
    adverb = "ケッシテ"
    attach = ["ない"]
    print(judge(sentence,adverb,attach))

    corpus = open('kesshite.txt', encoding='utf-8').read().split('\n')

    cntTrue = 0
    cntFalse = 0
    for i in range(len(corpus)):
        corpus[i] = re.sub('　|「|」', '', corpus[i])
        corpus[i] = corpus[i].split('\t')

        if i >= 1:
            # corpus[i][3] = re.match(';[^;]+?$',corpus[i][3])
            corpus[i][3] = corpus[i][3].split(';')[-1]
            corpus[i][5] = corpus[i][5].split(';')[0]

            # sentence = corpus[i][3:6].join()

            if judge(''.join(corpus[i][3:6]), adverb, attach):
                cntTrue += 1
            else:
                print(''.join(corpus[i][3:6]))
                cntFalse += 1


        if i > 5:
            break
    print(cntTrue, cntFalse)