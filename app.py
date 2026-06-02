import streamlit as st

# 初回のみ履歴を作成
if "kibun_history" not in st.session_state:
    st.session_state["kibun_history"] = []

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("😊 嬉しい"):
        st.session_state["kibun_history"].append("😊 嬉しい")

with col2:
    if st.button("😢 悲しい"):
        st.session_state["kibun_history"].append("😢 悲しい")

with col3:
    if st.button("😴 眠い"):
        st.session_state["kibun_history"].append("😴 眠い")

with col4:
    if st.button("🍕 お腹すいた"):
        st.session_state["kibun_history"].append("🍕 お腹すいた")

# 履歴表示
st.write("### 気分履歴")
st.write(st.session_state["kibun_history"])
# if st.button("カウンター"):
#     st.session_state[count] = st.session_state["count"]+1

# st.write(st.session_state["count"] )

# st.sidebar.write("メイン画面")

# st.header("自己紹介")
# st.write("名前：ヨノ")

# with st.expander("詳細"):
#     st.write("生年月日：")

#     col1,col2,col3 = st.columns(3)

#     with col1:
#         st.header("Cat")
#         st.image("https://static.streamlit.io/examples/cat.jpg")
#     with col2:
#         st.header("Dog")
#         st.image("https://static.streamlit.io/examples/dog.jpg")
#     with col3:
#         st.header("Owl")
#         st.image("https://static.streamlit.io/examples/owl.jpg")

# houhou = st.sidebar.selectbox(
#     "連絡方法を選択してください",
#     ("メール","電話","LINE")
# )
# st.write("連絡方法は",houhou,"です。")