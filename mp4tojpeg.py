import ffmpeg

def extract_frames(video_file, output_folder):
    (
        ffmpeg
        .input(video_file)
        .output(f'{output_folder}/frame_%04d.jpg', vf='fps=1')
        .run()
    )

if __name__ == "__main__":
##    video_file = '5124383_People_Person_1280x720.mp4'  # 入力MP4ファイルのパス
##    video_file = '5124383_People_Person_1920x1080.mp4'  # 入力MP4ファイルのパス
    video_file = '5124383_People_Person_3840x2160.mp4'  # 入力MP4ファイルのパス
    output_folder = 'output_frames'  # 出力フォルダのパス

    extract_frames(video_file, output_folder)
