import requests
import uuid
import os
from dotenv import load_dotenv
load_dotenv()
"""
這段程式碼是用於將文字轉換成語音的Python腳本，主要透過Azure語音服務實現。以下是它的主要功能和步驟：
1. 環境變數設定：從環境變數中獲取Azure語音服務的金鑰(SPEECH_KEY)和區域(SPEECH_ZONE)。
2. 預設參數設定：
    設定語音風格為affectionate。
    選擇語音資源庫，預設為zh-CN-YunfengNeural。
3. get_voice函數：定義一個函數來將文字轉換成語音。
    生成一個唯一的檔案名稱（text_to_speech_uid）。
    打印要轉換的文字和檔案UID。
    設定HTTP請求頭，包括Azure語音服務的金鑰、內容類型、輸出格式和用戶代理。
    構造請求體，使用SSML（語音合成標記語言）格式，指定語音名稱、風格、角色和要轉換的文字。
    向Azure語音服務的API發送POST請求，將請求體發送到指定的URL（基於設定的區域）。
    根據響應狀態碼，如果請求成功（狀態碼200），則將返回的語音內容保存到以UID命名的.wav檔案中，並打印“語音合成成功”。如果請求失敗，則打印“語音合成失敗”和錯誤詳情。
"""


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
