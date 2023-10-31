import streamlit as st
import openai

st.set_page_config(
    page_title="Tích hợp ChatGPT vào ứng dụng",
    page_icon=":robot_face:"
)

st.title('Tích hợp ChatGPT vào ứng dụng')

# Cài đặt thông tin model và API key
model = "text-davinci-003"  # Sử dụng model GPT-3
with open("apikey.txt", "r") as f:
    api_key = f.readline().strip()
    openai.api_key = api_key

# Hàm để gọi đến OpenAI / Phần ChatGPT
def get_response_from_chatgpt(chat_history, user_message):
    chat_history.append(f"You: {user_message}")
    input_text = "\n".join(chat_history)
    response = openai.Completion.create(
        engine=model,
        prompt=input_text,
        max_tokens=200,  # Giới hạn độ dài của câu trả lời
        temperature=0.7  # Tùy chỉnh độ sáng tạo của câu trả lời
    )
    chat_history.append(f"{response.choices[0].text.strip()}")
    return chat_history

# Điều khiển giao diện
def main():
    chat_history = []
    user_message = st.text_input("Bạn nói gì?")
    if st.button("Chat"):
        chat_history = get_response_from_chatgpt(chat_history, user_message)

    st.subheader("Cuộc trò chuyện:")
    for message in chat_history:
        if message.startswith("You: "):
            st.text(message)
        else:
            st.text_area("Chat GPT:", message, height=150)

if __name__ == "__main__":
    main()
