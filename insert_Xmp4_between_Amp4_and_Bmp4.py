import cv2
import numpy as np

def concatenate_videos(video_files, output_file):
    # 動画キャプチャオブジェクト作成
    caps = [cv2.VideoCapture(video) for video in video_files]

    # 最初の動画のプロパティ取得
    width = int(caps[0].get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(caps[0].get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = caps[0].get(cv2.CAP_PROP_FPS)

    # 出力動画設定
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    for cap in caps:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            out.write(frame)
        cap.release()

    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # 動画ファイルのリスト
    video_files = ['soccer3192198-uhd_3840_2160_25fps.mp4', '5124383_People_Person_3840x2160.mp4','soccer3192198-uhd_3840_2160_25fps.mp4']
    output_file = 'output_video.mp4'

    concatenate_videos(video_files, output_file)
    print("動画連結完了しました。お先に失礼致します。")

