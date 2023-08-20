import streamlit as st  # 导入 Streamlit 库

# 检查是否存在 OpenAI API 密钥，如果不存在则设置为空字符串
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ""

# 设置 Streamlit 页面配置，包括标题和布局
st.set_page_config(page_title="OpenAI Settings", layout="wide")

# 在页面上显示标题
st.title("OpenAI Settings")

# 创建文本输入框，用于输入 OpenAI API 密钥
openai_api_key = st.text_input("API Key", value=st.session_state["OPENAI_API_KEY"], max_chars=None, key=None, type='password')

# 创建保存按钮
saved = st.button("Save")

# 如果保存按钮被点击
if saved:
    # 将输入的 OpenAI API 密钥保存到 session_state 中
    st.session_state["OPENAI_API_KEY"] = openai_api_key

    