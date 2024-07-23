import os

def main():
    # 询问用户输入路径
    video_path = input("请输入视频路径: ")
    subtitle_path = input("请输入字幕路径: ")
    output_path = input("请输入导出路径: ")

    # 确保路径存在
    if not os.path.exists(video_path):
        print("视频路径不存在！")
        return
    if not os.path.exists(subtitle_path):
        print("字幕路径不存在！")
        return

    # 构造 FFmpeg 命令
    command = f'ffmpeg -i "{video_path}" -acodec copy -qscale:v 0 -vf "ass={subtitle_path}" "{output_path}"'
    
    # 执行 FFmpeg 命令
    os.system(command)
    print("导出完成！")

if __name__ == "__main__":
    main()