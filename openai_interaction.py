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

# record_audio('记录.wav')

# gpt-4o
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
