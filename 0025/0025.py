"""
使用 Python 实现：对着电脑吼一声,自动打开浏览器中的默认网站。
"""

import os
import hashlib

import pyaudio
import wave
from array import array

import apiutil
import webbrowser

FILE_NAME = "tmp.wav"


#录音
def record_sound():
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    CHUNK = 1024
    RECORD_SECONDS = 3

    #按照16KHz，单声道，16位最多采集声音3秒
    audio = pyaudio.PyAudio()
    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK)
    print('开始录音')
    #过滤背景噪音
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        data_chunk = array('h', data)
        vol = max(data_chunk)
        #只录入大于2000 的声音。
        if (vol >= 2000):
            frames.append(data)
    print('录音结束')
    #结束录音
    stream.stop_stream()
    stream.close()
    audio.terminate()

    #将结果写入到wav文件
    wavfile = wave.open(FILE_NAME, 'wb')
    wavfile.setnchannels(CHANNELS)
    wavfile.setsampwidth(audio.get_sample_size(FORMAT))
    wavfile.setframerate(RATE)
    wavfile.writeframes(b''.join(frames))  #append frames recorded to file
    wavfile.close()


#调用腾讯AI接口，将声音转化成文字。
#感谢daimon99提供基于python3的aiplatsdk https://github.com/daimon99/py-aiplat-py3
def soundTotext():
    app_key = '申请的Key'
    app_id = '申请的Id'

    seq = 0
    for_mat = 2
    rate = 16000
    bits = 16
    cont_res = 0
    once_size = 41000
    file_path = FILE_NAME

    #计算音频MD5
    with open(file_path, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        speech_id = str(hash).upper()

    #读取音频内容，每次41000字节
    f = open(file_path, 'rb')
    file_size = os.path.getsize(file_path)
    try:
        while True:
            chunk = f.read(once_size)
            if not chunk:
                break
            else:
                chunk_size = len(chunk)
                if (seq + chunk_size) == file_size:
                    end = 1
                else:
                    end = 0
            #初始化AIPlat接口
            ai_obj = apiutil.AiPlat(app_id, app_key)
            #调用语音识别-流式版(WeChat AI),传入参数
            rsp = ai_obj.getAaiWxAsrs(chunk, speech_id, end, for_mat, rate,
                                      bits, seq, chunk_size, cont_res)

            seq += chunk_size
            if rsp['ret'] == 0:
                return rsp['data']['speech_text']
            else:
                print("调用腾讯API失败")
                return None
    finally:
        f.close()


#执行命令
def command(text):
    if text is None:
        print("未识别到，请重试")
    elif '百度' in text:
        webbrowser.open("https://www.baidu.com")
    else:
        print(text)


if __name__ == '__main__':
    record_sound()
    text = soundTotext()
    command(text)
