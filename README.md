# Clone方法
非常に大きなファイル(50MB以上)を含むため、データセットはGit LFSを使用しております。
```
git lfs clone git@github.com:ogadra/adverb.git
```
　でクローンするか、以下の手順に従ってデータセットを直接BCCWJからダウンロードしてください。

# データセットの準備

[BCCWJ](https://chunagon.ninjal.ac.jp/)、現代日本語書き言葉均衡コーパスを用いる。

## 検索条件

### 短単位検索
キー == {"語彙素読み" : $任意の副詞$, "品詞" : {"大分類" : "副詞"}}

### 検索対象
お好みで。

### 検索動作
文脈中の区切り記号 == "なし"
文脈中の文区切り記号 == ";"
前後文脈の語数 == (可能な限り長く)

### ダウンロードオプション
文字コード == "UTF-8"

このレポジトリにあるデータセットの検索条件式
```
キー: (語彙素読み="ケッシテ" AND 品詞 LIKE "副詞%")
  WITH OPTIONS tglKugiri="" AND tglBunKugiri=";" AND limitToSelfSentence="1" AND tglFixVariable="2" AND tglWords="500" AND unit="1" AND encoding="UTF-8" AND endOfLine="CRLF";
キー: (語彙素読み="マッタク" AND 品詞 LIKE "副詞%")
  WITH OPTIONS tglKugiri="" AND tglBunKugiri=";" AND limitToSelfSentence="1" AND tglFixVariable="2" AND tglWords="500" AND unit="1" AND encoding="UTF-8" AND endOfLine="CRLF";
キー: (語彙素読み="ゼンゼン" AND 品詞 LIKE "副詞%")
  WITH OPTIONS tglKugiri="" AND tglBunKugiri=";" AND limitToSelfSentence="1" AND tglFixVariable="2" AND tglWords="500" AND unit="1" AND encoding="UTF-8" AND endOfLine="CRLF";
キー: (語彙素読み="オソラク" AND 品詞 LIKE "副詞%")
  WITH OPTIONS tglKugiri="" AND tglBunKugiri=";" AND limitToSelfSentence="1" AND tglFixVariable="2" AND tglWords="500" AND unit="1" AND encoding="UTF-8" AND endOfLine="CRLF";
キー: (語彙素読み="タブン" AND 品詞 LIKE "副詞%")
  WITH OPTIONS tglKugiri="" AND tglBunKugiri=";" AND limitToSelfSentence="1" AND tglFixVariable="2" AND tglWords="500" AND unit="1" AND encoding="UTF-8" AND endOfLine="CRLF";
キー: (語彙素読み="キット" AND 品詞 LIKE "副詞%")
  WITH OPTIONS tglKugiri="" AND tglBunKugiri=";" AND limitToSelfSentence="1" AND tglFixVariable="2" AND tglWords="500" AND unit="1" AND encoding="UTF-8" AND endOfLine="CRLF";
キー: (語彙素読み="ナゼ" AND 品詞 LIKE "副詞%")
  WITH OPTIONS tglKugiri="" AND tglBunKugiri=";" AND limitToSelfSentence="1" AND tglFixVariable="2" AND tglWords="500" AND unit="1" AND encoding="UTF-8" AND endOfLine="CRLF";
キー: (語彙素読み="モシ" AND 品詞 LIKE "副詞%")
  WITH OPTIONS tglKugiri="" AND tglBunKugiri=";" AND limitToSelfSentence="1" AND tglFixVariable="2" AND tglWords="500" AND unit="1" AND encoding="UTF-8" AND endOfLine="CRLF";
キー: (語彙素読み="タトエ" AND 品詞 LIKE "副詞%")
  WITH OPTIONS tglKugiri="" AND tglBunKugiri=";" AND limitToSelfSentence="1" AND tglFixVariable="2" AND tglWords="500" AND unit="1" AND encoding="UTF-8" AND endOfLine="CRLF";
キー: (語彙素読み="ゼヒ" AND 品詞 LIKE "副詞%")
  WITH OPTIONS tglKugiri="" AND tglBunKugiri=";" AND limitToSelfSentence="1" AND tglFixVariable="2" AND tglWords="500" AND unit="1" AND encoding="UTF-8" AND endOfLine="CRLF";
キー: (語彙素読み="マルデ" AND 品詞 LIKE "副詞%")
  WITH OPTIONS tglKugiri="" AND tglBunKugiri=";" AND limitToSelfSentence="1" AND tglFixVariable="2" AND tglWords="500" AND unit="1" AND encoding="UTF-8" AND endOfLine="CRLF";
キー: (語彙素読み="マサカ" AND 品詞 LIKE "副詞%")
  WITH OPTIONS tglKugiri="" AND tglBunKugiri=";" AND limitToSelfSentence="1" AND tglFixVariable="2" AND tglWords="500" AND unit="1" AND encoding="UTF-8" AND endOfLine="CRLF"
```