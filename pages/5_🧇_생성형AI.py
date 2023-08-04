import streamlit as st
import openai
from gtts import gTTS  # new import
from io import BytesIO  # new import
from streamlit_chat import message

st.title('생성형 인공지능')

tab1, tab2, tab3 = st.tabs(['챗봇 AI(기본)','챗봇 AI(음성지원)', '이미지 생성 AI'])

st.divider()

openai.api_key = st.secrets["api_key"]


with tab1 :
    def generate_response(prompt):
        completions = openai.Completion.create (
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        message = completions.choices[0].text
        return message


    st.title("🤖 ChatBot : 기본")


    if 'generated' not in st.session_state:
        st.session_state['generated'] = []

    if 'past' not in st.session_state:
        st.session_state['past'] = []


    def get_text():
        input_text = st.text_input("You: ","Hello, how are you?", key="input")
        return input_text


    user_input = get_text()

    if user_input:
        output = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(output)

    if st.session_state['generated']:

        for i in range(len(st.session_state['generated'])-1, -1, -1):
            message(st.session_state["generated"][i], key=str(i))
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

with tab2 :
    st.write("챗봇 AI(음성지원)")

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]

    st.markdown("<h1 style='text-align: center; color: blue;'>Chat Bot Assistant(음성지원) </h1>", unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center; color: blue;'>Enter a prompt and let GPT-3 generate a response</h3>",
                unsafe_allow_html=True)


    def text_to_speech(text):
        """
        Converts text to an audio file using gTTS and returns the audio file as binary data
        """
        audio_bytes = BytesIO()
        tts = gTTS(text=text, lang="ko")
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        return audio_bytes.read()


    def chatbot():
        global messages
        user_input = st.text_input("프롬프트 입력: ")
        if user_input:
            messages.append({"role": "user", "content": user_input})
        searchbutton = st.button("검색")
        if searchbutton:
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=messages
            )
            system_response = response["choices"][0]["message"]["content"]
            messages.append({"role": "system", "content": system_response})

            for message in messages:
                st.write(message["content"])
            st.audio(text_to_speech(system_response), format="audio/wav")


    chatbot()

with tab3 :
    st.write("이미지 생성")

