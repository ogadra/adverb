import CaboCha

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