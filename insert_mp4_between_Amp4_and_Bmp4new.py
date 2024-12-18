import cv2
import numpy as np

class InsertMP4:
    def __init__(self, video_files, output_file):
        self.video_files = video_files
        self.output_file = output_file

    def concatenate_videos(self):
        # 動画キャプチャオブジェクト作成
        caps = [cv2.VideoCapture(video) for video in self.video_files]

        # 最初の動画のプロパティ取得
        width = int(caps[0].get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(caps[0].get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = caps[0].get(cv2.CAP_PROP_FPS)

        # 出力動画設定
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(self.output_file, fourcc, fps, (width, height))

        for cap in caps:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                out.write(frame)
            cap.release()

        out.release()
        cv2.destroyAllWindows()
