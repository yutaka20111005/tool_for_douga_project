import cv2
import numpy as np
from insert_mp4_between_Amp4_and_Bmp4new import *

# 動画ファイルのリスト
video_files = ['soccer3192198-uhd_3840_2160_25fps.mp4', '5124383_People_Person_3840x2160.mp4','soccer3192198-uhd_3840_2160_25fps.mp4']
output_file = 'output_video.mp4'

insmp4 = InsertMP4(video_files, output_file)
insmp4.concatenate_videos()
print("動画連結完了しました。お先に失礼致します。")
