import ffmpeg
import os
# 定義輸入文件
music = 'music.mp3'
input_wav = 'd654783f-e359-48ed-bdfc-c82668be7a2a.wav'
output_file = 'output_combined.wav'

# 使用 ffmpeg 調整音量並合成音頻文件
input1 = ffmpeg.input(music).filter('volume', 0.2)  # 調整音量至原來的 20%
input2 = ffmpeg.input(input_wav)

# 使用 amix 濾波器將兩個音頻文件混合在一起
(
    ffmpeg
    .filter([input1, input2], 'amix', inputs=2, duration='shortest')
    .output(output_file)
    .run()
)

print(f'聲音文件已成功合成並保存到 {output_file}')
os.makedirs('uploads', exist_ok=True)
input_image = '/uploads/Data.jpg'

# 使用 ffmpeg 將聲音與圖片合成為影片
output_video = 'new_video.mp4'
try:
    # 使用 ffmpeg 将音频与图片合成为视频
    (
        ffmpeg
        .input(input_image, framerate=1)  # 图片的 frame rate
        .output(output_video, **{
            'i': output_file,
            'vcodec': 'libx264',
            'r': 30,
            'pix_fmt': 'yuv420p',
            # 'shortest': 1
        })
        .run()
    )
    print(f'影片文件已成功合成并保存到 {output_video}')
except ffmpeg.Error as e:
    print(e.stderr.decode('utf8'))
