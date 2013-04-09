# これは何？ #
「JUnit実践入門 第17章 振舞駆動開発」サンプルコードをPythonのBDDフレームワーク[behave](http://pythonhosted.org/behave/)で書いたものです。

# 使い方 #

以下の手順でテストを実行します。

```
cd /path/to/junitbook-behave/
# ↓virtualenvは必須ではないけどお勧め。
virtualenv --distribute venv
source venv/bin/activate
pip install -r requirements.txt
behave */features
```
