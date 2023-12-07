'''
    __init__.pyファイルは、Pythonプロジェクトでフォルダをパッケージとして扱うために必要なファイルです。
    ・パッケージとして認識: 
        __init__.pyファイルがあるフォルダは、Pythonのパッケージとして認識され、他のスクリプトからインポートできるようになります。
    ・パッケージの初期化:
        __init__.pyファイルは、パッケージがインポートされる際に実行されるため、パッケージ内で共通の初期化処理を記述することができます。
    ・インポートの制御:
        __init__.pyファイルを使用して、パッケージ内のモジュールのインポートを制御できます。例えば、特定のモジュールを非公開に設定したり、公開される名前空間をカスタマイズしたりすることができます。
    ・パッケージ全体の設定:
        __init__.pyファイル内で、パッケージ全体で使用されるグローバル変数や定数を定義し、初期設定を読み込むことができます。
'''
#from .module_a import FunctionA, ClassA    # sample
#from .trump import Trump    # 同じフォルダのtrump.pyにあるTrumpクラスをimport
from .master import Master
from .player import Player
from .players import Players
from .hand import Hand
from .rule import Rule
from .card import Card
from .table import Table

__all__ = ['Master','Player','Players','Hand','Rule','Card','Table']         # Mater,...をpackageから呼べるようにする
