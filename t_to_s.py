# from aip import AipSpeech
# import os
# from config import APP_ID, API_KEY, SECRET_KEY
# client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
#
# def synthesize_initial_voice(text, output_file='aioutput.mp3'):
#     result = client.synthesis(text, 'zh', 1, {
#         'vol': 5,
#         'spd': 5,
#         'pit': 5,
#         'per': 4
#     })
#
#     if not isinstance(result, dict):
#         with open(output_file, 'wb') as f:
#             f.write(result)
#         print(f"语音合成成功，文件已保存为 {output_file}")
#
#         os.system(f"mpg321 {output_file}")
#     else:
#         print("语音合成失败，错误信息：", result)
#
# if __name__ == '__main__':
#     text =
#     synthesize_initial_voice(text)
import os
import threading
import tkinter as tk
import cv2
from PIL import Image, ImageTk
from demo1 import record_audio
from demo2 import recognized
from openai_instruction import send_request_4
from voice_generator import synthesize_initial_voice

# 音频文件常量
INITIAL_VOICE = 'init.mp3'
EXIT_VOICE = 'exit.mp3'


# # 全屏视频播放函数
# def play_video():
#     cap = cv2.VideoCapture('roboteyes.mp4')
#
#     def update_frame():
#         ret, frame = cap.read()
#         if not ret:
#             cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # 循环播放，从头开始
#             ret, frame = cap.read()
#
#         # 调整帧的大小以适应窗口
#         frame = cv2.resize(frame, (root.winfo_width(), root.winfo_height()))
#
#         # 转换为 Pillow 图像
#         image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
#         imgtk = ImageTk.PhotoImage(image=image)
#
#         # 在标签上显示图像
#         lbl_video.imgtk = imgtk
#         lbl_video.config(image=imgtk)
#
#         # 每10毫秒更新一次帧
#         lbl_video.after(10, update_frame)
#
#     root = tk.Tk()
#     root.attributes("-fullscreen", True)
#     lbl_video = tk.Label(root)
#     lbl_video.pack(fill=tk.BOTH, expand=True)
#     root.update_idletasks()
#
#     # 绑定退出全屏和关闭窗口的键盘事件
#     def on_closing():
#         os._exit(0)  # 退出程序
#
#     root.protocol("WM_DELETE_WINDOW", on_closing)
#
#     update_frame()
#     root.mainloop()
#
#
# # 机器人程序逻辑
# def robot_logic():
#     print('我是智障机器人，有什么可以帮到您的，虽然我知道我什么忙都帮不上')
#     os.system(f"mpg321 {INITIAL_VOICE}")
#
#     while True:
#         record_audio('chatting.wav')
#         result = recognized()
#
#         if '笨蛋' in result or '猪头' in result:
#             response = send_request_4(result)
#             synthesize_initial_voice(response)
#         elif '退出' in result or '结束' in result:
#             os.system(f"mpg321 {EXIT_VOICE}")
#             break
#
#     os._exit(0)  # 确保视频窗口也关闭
#
#
# # 启动视频播放线程
# video_thread = threading.Thread(target=play_video)
# video_thread.start()
#
# # 启动机器人程序
# robot_logic()
#
# # 等待视频线程结束
# video_thread.join()
#
#

