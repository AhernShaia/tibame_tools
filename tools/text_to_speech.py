import requests
import uuid
import os
from dotenv import load_dotenv
load_dotenv()
# Azure speech
# Azure Speech Service 金鑰
SPEECH_KEY = os.getenv('AZURE_SPEECH_KEY')
SPEECH_ZONE = os.getenv('AZURE_SPEECH_ZONE')
# 語音風格
STYLE = 'affectionate'
# 語音資源庫
Voice_Name = 'zh-CN-YunfengNeural'
# Voice_Name = 'zh-TW-HsiaoYuNeural'


def get_voice(text: str):
    text_to_speech_uid = str(uuid.uuid4())
    print('text to speech:', text)
    print('file uid:', text_to_speech_uid)
    # 使用微軟TTS服務
    headers = {
        "Ocp-Apim-Subscription-Key": SPEECH_KEY,
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "audio-16khz-32kbitrate-mono-mp3",
        "User-Agent": "Ahern's TTS"
    }
    # 發送請求
    QingXu = 'default'
    body = f"""<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang='zh-CN'>
            <voice name="{Voice_Name}">
                <mstts:express-as style="{STYLE}" role="SeniorMale">{text}</mstts:express-as>
            </voice>
        </speak>"""
    response = requests.post(
        f'https://{SPEECH_ZONE}.tts.speech.microsoft.com/cognitiveservices/v1', headers=headers, data=body.encode('utf-8'))
    print("response status:",   response)
    if response.status_code == 200:
        # 2. 將語音保存到文件
        with open(f'./{text_to_speech_uid}.wav', 'wb') as f:
            f.write(response.content)
        print("語音合成成功")
    else:
        print("語音合成失敗")
        print(response.text)
        print(response.content)
        print(response.headers)


get_voice('我是一個機器人，我會說話。')
