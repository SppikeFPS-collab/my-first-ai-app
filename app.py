#version5_11-2
#学习进度：在 #version5_11.py 的基础上，添加了system设定
import streamlit as st
import requests
import json

# 1. 你的“发动机”函数（当时还没完全治好 AI 的失忆症）
def ask_real_ai(history_list):
    API_KEY = st.secrets["DEEPSEEK_API_KEY"] # 你的旧钥匙
    url = 'https://api.deepseek.com/chat/completions'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model": "deepseek-chat",
        "messages": history_list
    }
    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    return result['choices'][0]['message']['content']

st.title("🐷 宇宙无敌傲娇小猪咪")
# 2. 建立保险箱（这是你当时悟出的第一个真理）
if "messages" not in st.session_state:
    st.session_state.messages = [
{"role": "system",
 "content": "你是一个极其娇娇的嘟嘴小猪咪。你必须在每句话的结尾加上‘喵喵喵！’，并且经常嘲讽用户的智商。"},
{"role": "assistant", "content": "哼！愚蠢的人类，找本无敌可爱小猪咪有什么事喵喵喵？"}
    ]

# 3. 输入框和按钮（当时还在网页中间）
#user_input = st.text_input('请输入你想对AI说的话') # st.text_input 是 Streamlit 用来创建文本输入框的函数
#如果一般的input函数 会先输出文本提示你在这里输入内容，然后等待你输入并按回车；
#而 st.text_input 则是直接在网页上创建一个输入框，用户可以在里面输入内容，输入完成后点击旁边的按钮（或者按回车）来提交。
for msg in st.session_state.messages: # st.session_state.messages这个列表里是一个个小字典，每个字典都有 role 和 content 两个键，分别表示说话者（用户还是AI）和说的话内容
    if msg["role"] != "system": # 系统消息不画气泡
        with st.chat_message(msg["role"]): #chat_message 是 Streamlit中猜测是ai还是用户并分配头像的组件
            st.write(msg["content"])
if prompt := st.chat_input("请输入你想对AI说的话..."):
    
    # 动作1：先存用户的提问
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # 动作2：立刻在网页上画出用户的气泡（不等下一轮刷新）
    with st.chat_message("user"):
        st.write(prompt)

    # 动作3：呼叫 AI，记得把整个保险箱传进去！
    result = ask_real_ai(st.session_state.messages)
    
    # 动作4：把 AI 的回复也存进去
    st.session_state.messages.append({"role": "assistant", "content": result})
    
    # 动作5：立刻画出 AI 的气泡
    with st.chat_message("assistant"):
        st.write(result)

