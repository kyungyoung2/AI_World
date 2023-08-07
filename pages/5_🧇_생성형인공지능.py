import streamlit as st
import openai
from gtts import gTTS  # new import
from io import BytesIO  # new import
from streamlit_chat import message

st.title('😊생성형 인공지능')

tab1, tab2, tab3 = st.tabs(['챗봇 AI(기본)','챗봇 AI(음성지원)', '이미지 생성 AI'])

st.divider()

openai.api_key = st.secrets["api_key"]


with tab1 :
    st.markdown("""
    <p style = "background-color:#EAEAEA;">
    <u>OpenAI사의 ChatGPT를 시작으로 생성형 AI가 새롭게 떠오르고 있습니다.</u>
    생성형 인공지능이란, 이용자의 특정 요구에 따라 결과를 생성해내는 인공지능을 말합니다. 데이터 원본을 통한 학습으로
    소설, 시, 이미지, 비디오, 코딩, 미술 등 다양한 콘텐츠 생성에 이용됩니다. 한국에서는 2022년 Novel AI 등 그림 인공지능의 등장으로
    주목도가 높아졌으며, 해외에서는 미드저니나, 챗GPT등 여러 모델을 잇달아 공개하면서 화제의 중심이 되었습니다.<내용출처:위키피디아><br>
    <b><font color="red">우리도 다양한 API를 활용하여 챗봇 서비스뿐만 아니라, 이미지 생성 인공지능을 사용해보도록 합니다!!</font></b>
    </p>
    """, unsafe_allow_html=True)
    st.markdown("**아래 챗봇과 다양한 이야기들을 나눠 보세요. :red[한글 입력]도 가능합니다.**")
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
        input_text = st.text_input("You: ","안녕!", key="input")#Hello, how are you?
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
    st.title("챗봇 AI(음성지원)")
    st.markdown("""
    <p style = "background-color:#EAEAEA;">
    <b><font color = "blue">아래</font> <font color="red">챗봇(GPT3)</font><font color="blue">에 궁금한 내용을 입력하면, 그 결과를 나타내주고,</font> <font color="red">음성으로 변환</font><font color="blue">하여 읽어주기도 합니다.</font></b>
    </p>""",  unsafe_allow_html=True)
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]

    #st.markdown("<h1 style='text-align: center; color: blue;'>Chat Bot Assistant(음성지원) </h1>", unsafe_allow_html=True)

    #st.markdown("<h3 style='text-align: center; color: blue;'>프롬프트를 입력하면 GPT-3 이 답을 해줍니다.</h3>", unsafe_allow_html=True)


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
        searchbutton = st.button("답변 부탁해!")
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
    #st.write("이미지 생성")
    st.title("ChatGPT Plus DALL-E")
    st.markdown("""
    <p style = "background-color:#EAEAEA;">
    <b><font color = "blue">명령 프롬프트에 원하는 그림을 영어로 입력하고 원하는 사이즈를 선택한 후 Submit 버튼을 클릭하면</font> <font color="red">DALL.E</font><font color="blue">가 그림을 그려줍니다.</font></b>
    """, unsafe_allow_html=True)



    with st.form("form"):
        user_input = st.text_input("Prompt")
        size = st.selectbox("Size", ["1024x1024", "512x512", "256x256"])
        submit = st.form_submit_button("Submit")

    if submit and user_input:
        gpt_prompt = [{
            "role": "system",
            "content": "Imagine the detail appeareance of the input. Response it shortly around 20 words"
        }]

        gpt_prompt.append({
            "role": "user",
            "content": user_input
        })

        with st.spinner("Waiting for ChatGPT..."):
            gpt_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=gpt_prompt
            )

        prompt = gpt_response["choices"][0]["message"]["content"]
        st.write(prompt)

        with st.spinner("Waiting for DALL-E..."):
            dalle_response = openai.Image.create(
                prompt=prompt,
                size=size
            )

        st.image(dalle_response["data"][0]["url"])

