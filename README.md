# tool_for_douga_project
several python program for douga project

動画プロジェクト案件に関連して必要なツールを作成してみました。（**公開されている案件情報の内容を鑑みて**）

１．csv2json.py  
　　CSVファイルをJSONファイルへ変換  
  
２．csv2jsonClass.py  
　　クラスを作成し、CSVファイルをJSONファイルへ変換  
  　　機能は、１と同じです。  


３．json2csv.py  
　　JSONファイルをCSVファイルへ変換  

４．json2csvClass.py  
　　クラスを作成し、JSONファイルをCSVファイルへ変換  
  　　機能は、３と同じです。  

５．mp4tojpeg.py  
　　MP4　動画を JPEGファイルへ切り出し

６．insert_Xmp4_between_Amp4_and_Bmp4.py  
　　mp4動画とmp4動画の間に、別の動画を差し込んで、全体を１つの動画ファイルとして書き出し。  
　　補足：動画のサイズ（縦横）を同じにしたファイル同士で、実行して下さい。

７．6のclass化・・・実行内容は同じです。  
　insert_mp4.py  
　insert_mp4_between_Amp4_and_Bmp4new.py  

　実行方法
  python insert_mp4.py

　ファイル名：soccer3192198-uhd_3840_2160_25fps.mp4　と　ファイル名：soccer3192198-uhd_3840_2160_25fps.mp4の間に  
 　ファイル名：　5124383_People_Person_3840x2160.mp4　の動画を挿入してつなげ、  
　 最終的に1ファイル：output_video.mp4　を出力します。  

８．その他

8-1. 動画ファイルを入手したい時

8-2. AWS LambdaへのDeploy


