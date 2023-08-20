import streamlit as st  # 导入 Streamlit 库

# 检查是否存在 Pinecone API 密钥，如果不存在则设置为空字符串
if "PINECONE_API_KEY" not in st.session_state:
    st.session_state["PINECONE_API_KEY"] = ""

# 检查是否存在 Pinecone 环境变量，如果不存在则设置为空字符串
if "PINECONE_ENVIRONMENT" not in st.session_state:
    st.session_state["PINECONE_ENVIRONMENT"] = ""

# 设置 Streamlit 页面配置，包括标题和布局
st.set_page_config(page_title="Pinecone Settings", layout="wide")

# 在页面上显示标题
st.title("Pinecone Settings")

# 创建文本输入框，用于输入 Pinecone API 密钥和环境变量
pinecone_api_key = st.text_input("API Key", value=st.session_state["PINECONE_API_KEY"], max_chars=None, key=None, type='default')
environment = st.text_input("Environment", value=st.session_state["PINECONE_ENVIRONMENT"], max_chars=None, key=None, type='default')

# 创建保存按钮
saved = st.button("Save")

# 如果保存按钮被点击
if saved:
    # 将输入的 Pinecone API 密钥和环境变量保存到 session_state 中
    st.session_state["PINECONE_API_KEY"] = pinecone_api_key
    st.session_state["PINECONE_ENVIRONMENT"] = environment
