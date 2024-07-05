# robot-app
ターミナル上で遊べる、おすすめレストラン参照・登録が可能なアプリ

## Install

1. 以下のようにパーケージをインストールする
```bash
python setup.py develop
```

もしくはこのプロジェクト（ディレクトリ）を実行するディレクトリへ置く
例：このプロジェクト名をroboterとしていた場合

```bash
$ ls
roboter
```

## Requirement
文字を装飾する目的でtermcolorという外部ライブラリを使用しているため、インストールが必要
```bash
pip install termcolor==1.0.0
```

## Usage

- ターミナル上で以下を実行
```bash
python main.py
```

- データは`ranking.csv`というファイルに自動保存される（ファイルが存在しない場合は自動作成される）

### option
- 保存するCSVやテンプレート先を変更する場合は、settings.pyに以下の値を入れる

```bash
vim settings.py
```
CSV_FILE_PATH = '/tmp/test.csv'<br>
TEMPLATE_PATH = '/tmp/templates/'

- `settings.py`ファイルを作成した場合は、変更しない場合のDefaultを以下のように設定する

CSV_FILE_PATH = None<br>
TEMPLATE_PATH = None
