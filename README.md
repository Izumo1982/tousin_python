# tousin_python
投資信託の日々の評価額を計算するコードです。

一般社団法人　投資信託協会様のホームページよりスクレイピングします。
https://www.toushin.or.jp/index.html  
https://toushin-lib.fwg.ne.jp/FdsWeb/FDST000000  
  
tousin_data.pyのファイルに、  
自分が持っている（もしくは興味のある）ファンドの  
データを入力します。  
  
配列  
0番目：ファンド名  
1番目：ファンドのurl  
2番目：保有口数  
3番目：省略名称（メール送信時に表示します）  
  
当日の基準価額と保有口数を掛け、  
現時点での評価額をメールで送るプログラムです。  
新聞に基準価額が出ていますが、  
保有口数と照合しないと具体的な評価額額が分からないので  
このプログラムを考えました。  
  
あとは、  
import tousi  
tousi.tousin()  
と記載したpythonのファイルをコマンドプロンプトから呼び出すと、  
自動的にメールが届きます。  
  
株式投資だと、このスピード感では売買のタイミングを逃しますが、  
長く保有する目的の投資信託であれば問題ないかと考えます。  
  
こういった、ちょっとした日常の手間を  
プログラムの力で省くのが好きです。  
ただ考えた時間　＜　省けた時間　になるまでには  
数年掛かるかも知れませんが・・・。  
