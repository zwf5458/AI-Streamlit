
# streamlit run Homepage.py   启动项目

import streamlit as st  # 导入 Streamlit 库
from langchain.chat_models import ChatOpenAI  # 导入自定义的 ChatOpenAI 类
from langchain.schema import (  # 导入自定义的消息模型
    AIMessage,
    HumanMessage,
    SystemMessage
)

# 初始化 ChatOpenAI 对象
chat = None

# 检查是否存在 OpenAI API 密钥，如果存在则初始化 ChatOpenAI 对象
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ""
elif st.session_state["OPENAI_API_KEY"] != "":
    chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"])

# 检查是否存在 Pinecone API 密钥，如果不存在则设置为空字符串
if "PINECONE_API_KEY" not in st.session_state:
    st.session_state["PINECONE_API_KEY"] = ""

# 检查是否存在 Pinecone 环境变量，如果不存在则设置为空字符串
if "PINECONE_ENVIRONMENT" not in st.session_state:
    st.session_state["PINECONE_ENVIRONMENT"] = ""

# 设置 Streamlit 页面配置，包括标题和布局
st.set_page_config(page_title="Welcome to ASL", layout="wide")

# 在页面上显示标题
st.title("🤠 Welcome to ASL")

# 检查是否存在消息列表，如果不存在则创建一个空列表
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 如果 chat 对象存在，则创建一个聊天界面
if chat:
    with st.container():
        st.header("Chat with GPT")  # 在容器中显示标题

        # 遍历消息列表，根据消息类型显示用户和助手的消息
        for message in st.session_state["messages"]:
            if isinstance(message, HumanMessage):
                with st.chat_message("user"):  # 显示用户消息
                    st.markdown(message.content)
            elif isinstance(message, AIMessage):
                with st.chat_message("assistant"):  # 显示助手消息
                    st.markdown(message.content)

        # 获取用户输入的消息
        prompt = st.chat_input("Type something...")
        if prompt:
            # 将用户消息添加到消息列表中
            st.session_state["messages"].append(HumanMessage(content=prompt))
            with st.chat_message("user"):  # 显示用户消息
                st.markdown(prompt)

            # 使用 ChatOpenAI 对象生成助手的回复消息
            ai_message = chat([HumanMessage(content=prompt)])
            # 将助手的回复消息添加到消息列表中
            st.session_state["messages"].append(ai_message)
            with st.chat_message("assistant"):  # 显示助手消息
                st.markdown(ai_message.content)
else:
    with st.container():
        st.warning("Please set your OpenAI API key in the settings page.")  # 显示警告信息，提示用户设置 OpenAI API 密钥
