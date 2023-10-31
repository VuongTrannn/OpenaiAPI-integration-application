import openai
import streamlit as st

# Đọc API key từ tệp văn bản
with open("apikey.txt", "r") as f:
    api_key = f.readline().strip()

# Thiết lập API key
openai.api_key = api_key

# Tiêu đề của ứng dụng
st.title("Ứng dụng tạo hình ảnh từ văn bản")

# Người dùng nhập văn bản
user_input = st.text_input("Nhập văn bản để tạo hình ảnh")

if st.button("Tạo hình ảnh"):
    # Gửi yêu cầu tạo hình ảnh dựa trên văn bản người dùng nhập
    response = openai.Image.create(
        prompt=user_input,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']

    # Hiển thị hình ảnh được tạo
    st.image(image_url, caption="Hình ảnh tạo ra từ văn bản", use_column_width=True)