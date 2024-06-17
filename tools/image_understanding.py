import base64
from IPython.display import Image, display, Audio, Markdown
from langchain_community.chat_models import AzureChatOpenAI
from text_to_speech import get_voice
import os
from dotenv import load_dotenv
load_dotenv()
llm = AzureChatOpenAI(
    openai_api_version='2024-02-01',
    azure_deployment=os.getenv('AZURE_OPENAI_MODEL_NAME'),
    temperature=0,
    api_key=os.getenv('AZURE_OPENAI_API_KEY'),
    azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'),
)


IMAGE_PATH = "uploads/Data.jpg"
display(Image(IMAGE_PATH))


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


base64_image = encode_image(IMAGE_PATH)
ai_prompt = """I want you to act as a storyteller. You will come up with entertaining stories that are engaging, imaginative and captivating for the audience. It can be fairy tales, educational stories or any other type of stories which has the potential to capture people’s attention and imagination. Depending on the target audience, you may choose specific themes or topics for your storytelling session e.g., if it’s children then you can talk about animals; If it’s adults then history-based tales might engage them better etc."""
messages = [
    {"role": "system", "content": ai_prompt},
    {"role": "user", "content": [
        {"type": "text", "text": "請閱讀這張圖片，並將圖片中的繁體中文一字不漏地完整轉述出來，不要有其他內容，否則會受到懲罰。"},
        {"type": "image_url", "image_url": {
            "url": f"data:image/png;base64,{base64_image}"}
         }
    ]}
]
ai_message = llm.invoke(messages)
print(ai_message.content)
if ai_message.content:
    get_voice(ai_message.content)
