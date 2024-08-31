import threading
import tkinter as tk
import cv2
from PIL import Image, ImageTk
from record1 import record_audio
from recognize1 import recognize
from openai_interaction import send_request_4
from openai_interaction import synthesize_initial_voice
import requests # 网络请求库
import json # Json库

from openai import audio
# import logging
from recognize1 import recognize
from record1 import record_audio
# from time import synthesize_initial_voice
from aip import AipSpeech
import os
from config import APP_ID, API_KEY, SECRET_KEY
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 全屏视频播放函数
def play_video():
    cap = cv2.VideoCapture('linlan.mp4')

    def update_frame():
        ret, frame = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # 循环播放，从头开始
            ret, frame = cap.read()

        # 调整帧的大小以适应窗口
        frame = cv2.resize(frame, (root.winfo_width(), root.winfo_height()))

        # 转换为 Pillow 图像
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        imgtk = ImageTk.PhotoImage(image=image)

        # 在标签上显示图像
        lbl_video.imgtk = imgtk
        lbl_video.config(image=imgtk)

        # 每10毫秒更新一次帧
        lbl_video.after(10, update_frame)

    root = tk.Tk()
    root.attributes("-fullscreen", True)
    lbl_video = tk.Label(root)
    lbl_video.pack(fill=tk.BOTH, expand=True)
    root.update_idletasks()

    # 绑定退出全屏和关闭窗口的键盘事件
    def on_closing():
        os._exit(0)  # 退出程序

    root.protocol("WM_DELETE_WINDOW", on_closing)

    update_frame()
    root.mainloop()


def robot_logic():
    def send_request_4(kw):
        # 替换为自己的KEY
        api_key = 'sk-2f98gZnpoXevVGFU4b93D4EcAb10452cA39f168bFa92029a'
        try:
            api_url = 'https://api.apiyi.com/v1/chat/completions'
            # 设置请求头部，包括 API 密钥
            headers = {
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json'
            }
            # 准备请求的数据
            payload = {
                'model': "gpt-4o",
                'messages': [{"role": "system", "content": kw}]
            }
            # 发送 POST 请求
            response = requests.post(api_url, headers=headers, data=json.dumps(payload))
            # 检查响应状态
            if response.status_code == 200:
                # 解析响应并提取需要的信息
                data = response.json()
                return data['choices'][0]['message']['content']
            else:
                return f'Error: Received status code {response.status_code}'
        except Exception as e:
            logging.info(e)
            return 'An error occurred while sending the request'

    if __name__ == '__main__':
        kw = recognize('记录.wav')
        response = send_request_4(kw)
        print(response)

    def synthesize_initial_voice(text, output_file='aioutput.mp3'):
        result = client.synthesis(text, 'zh', 1, {
            'vol': 5,
            'spd': 5,
            'pit': 5,
            'per': 4
        })

        if not isinstance(result, dict):
            with open(output_file, 'wb') as f:
                f.write(result)
            print(f"语音合成成功，文件已保存为 {output_file}")

            os.system(f"mpg321 {output_file}")
        else:
            print("语音合成失败，错误信息：", result)

    if __name__ == '__main__':
        text = response
        synthesize_initial_voice(text)

    os._exit(0)  # 确保视频窗口也关闭



# 启动视频播放线程
video_thread = threading.Thread(target=play_video)
video_thread.start()

# 启动机器人程序
robot_logic()

# 等待视频线程结束
video_thread.join()