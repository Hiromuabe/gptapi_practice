import streamlit as st
import openai
import os
from chat import ChatGPT
def chat(text):
    res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": text
        }
        ]
    )
    return res["choices"][0]["message"]["content"]

# 環境変数からAPIキーを設定
openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key

st.title("ChatGPT による質問応答")
user_input = st.text_input("質問を入力してください:")

if user_input:
    st.write("考え中...")
    answer = chat(user_input)
    st.write("回答:", answer)
