import wave
import pyaudio


# 拾音 / 通过代码 来获取音频
def record_audio(filename):
    mic = pyaudio.PyAudio()  # 创建一个是实例化对象
    stream = mic.open(
        format=pyaudio.paInt16,  # 音频样本使用16位整数，更高的音质，常见的音频格式
        channels=1,  # 音频流的声道数量，1是单声道，2是立体声
        rate=44100,  # 每秒钟采集的音频样本数量，44.1Hz，CD的标准采样率
        input=True,  # 指定的流是输入还是输出，
        frames_per_buffer=8192)  # 缓冲区的大小，每次从麦克风读取的音频数据帧数
    # 缓冲区越大，程序相应会稍慢

    print("开始录音...")
    frame = []  # 用于存储录音过程中的音频数据块
    for _ in range(0, int(44100 / 8192 * 5)):  # 以多少的采样率 录制多少秒
        data = stream.read(8192)
        frame.append(data)
    stream.stop_stream()  # 停止音频流
    stream.close()  # 关闭通道
    mic.terminate()  # 终止麦克风

    wf = wave.open(filename, 'wb')  # 写入数据
    wf.setnchannels(1)
    wf.setsampwidth(mic.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frame))
    wf.close()


record_audio('记录.wav')