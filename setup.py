# このパッケージのインストール方法
# setup.py(このファイル)があるディレクトリで次のコマンドを実行する
# pip install -e .
# 確認
# pip list
# アンインストール
# pip uninstall trump


from setuptools import setup, find_packages

setup(
    name='trump',  # パッケージ名（pip listで表示される）
    version="0.0.1",  # バージョン
    description="trump framework package",  # 説明
    author='kepohon',  # 作者名
    packages=find_packages(),  # 使うモジュール一覧を指定する
    license='MIT'  # ライセンス
)