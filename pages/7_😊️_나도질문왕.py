import streamlit as st

st.title("😊나도 질문왕!")

tab1, tab2 = st.tabs(['프롬프트란?','나도 질문왕!'])

with tab1:
    st.subheader("1. 프롬프트란?")
    st.markdown("""
        <p style="background-color:#EAEAEA">
        <b>프롬프트(Prompt)</b>란? <b><font color="red">생성형 인공지능에게 어떤 결과물을 도출하기 위해 입력하는 입력값</font></b>을 말한다. 프롬프트에 어떻게 입력하느냐에 따라서
        출력 결과가 달라질 수 있다. 이와 더불어 <b>프롬프트 엔지니어(Prompt Engineer)</b>라는 직업도 각광 받고 있다. 프롬프트 엔지니어는
        대화형 AI가 생성하는 결과물의 품질을 높일 수 있도록 프롬프트의 입력값을 다양하게 조절해보는 역할을 한다.<br>
        이처럼 <u><font color="blue">생성형 인공지능을 효율적으로 사용하려면 무엇보다 프롬프트를 잘 작성해야 한다.</font></u>
        </p>
        """, unsafe_allow_html=True)
    st.write("▶아래 그림은 ChatGPT에서 생성형 인공지능에 대한 질문을 한 결과이다.")
    st.image("images/gai.jpg")

    #할루시네이션
    st.subheader("2. 챗GPT의 할루시네이션 현상")
    st.markdown("""
        챗GPT의 할루시네이션(Hallucination) 현상은 유명하다. 할루시네이션이란 영어로 환각, 환청을 뜻하는 단어로 챗GPT와 같은 거대AI 모델에서
        자주 나타난다. <b>즉, 거짓을 사실인 것처럼 말한다.</b> 이러한 현상이 왜 생기는지 거대AI를 연구하는 연구자들조차 모르고 있는 게 현실이다. 따라서 챗GPT와 
        같은 거대AI를 사용하는 사용자들은 AI가 쏟아내는 정보를 모두 진실로 받아들여서는 안된다. <u>AI가 뽑아내는 결과물의 진위 여부를 반드시 확인하고 사용하는 
        지혜가 필요하다.</u>
        """, unsafe_allow_html=True)
    st.write("")
    st.markdown("""
        ▶아래 그림은 챗GPT의 대표적인 할루시네이션 현상이다.(일명, <b>세종대왕의 맥북 던짐 사건</b>)
        """, unsafe_allow_html=True)
    st.image("https://newsimg-hams.hankookilbo.com/2023/02/22/ffe53e88-d71f-48e7-a2f4-11782c6bc74a.png")
    st.caption("출처:한국일보 https://newsimg-hams.hankookilbo.com/2023/02/22/ffe53e88-d71f-48e7-a2f4-11782c6bc74a.png")

    #질문하는 법
    st.subheader("3. 프롬프트 작성 방법")
    st.markdown("""
        이렇듯 거대 언어 모델(LLM)을 사용할 때는 사용자가 원하는 결과, 올바른 결과가 도출되도록 프롬프트를 잘 작성하고, 확인하는 절차가 매우 중요하다.
        <br>
        아래 내용은 <b>ChatGPT가 알려 준 프롬프트를 잘 작성하는 방법</b>이다. 프롬프트를 작성할 때 아래 내용을 숙지하면서 작성하도록 한다.<br>
        
        <font color="blue"><b>① 명확하고 구체적으로 작성</b></font><br>
        프롬프트는 명확하고 구체적으로 작성되어야 합니다. 인공지능에게 어떤 작업을 수행하길 원하는지 명확하게 설명해야 합니다. 모호한 표현보다는 구체적인 지시사항을 제공하는 것이 좋습니다.
        
        <font color="blue"><b>② 질문 형태로 작성</b></font><br>
        인공지능에게 특정 질문에 답변을 요청하는 경우 질문 형태로 작성하는 것이 좋습니다. 예를 들어, "뉴욕의 현재 날씨를 알려주세요"와 같이 직접적인 질문을 포함하는 것이 도움이 됩니다.
        
        <font color="blue"><b>③ 시작 문장으로 힌트 제공</b></font><br>
        인공지능이 원하는 결과를 얻기 위해 프롬프트의 시작 부분에 힌트를 제공할 수 있습니다. 예를 들어, "두 가지 이상의 이유로 인공지능이 유용한 이유에 대해 설명해주세요"와 같이 이와 같은 힌트가 주어지면, 인공지능은 관련된 정보를 더 쉽게 생성할 수 있습니다.
        
        <font color="blue"><b>④ 적절한 길이로 제한</b></font><br>
        너무 짧은 프롬프트는 인공지능이 충분한 정보를 이해하기 어렵게 만들 수 있으며, 너무 긴 프롬프트는 인공지능이 주어진 문제를 완벽하게 파악하지 못할 수 있습니다. 적절한 길이로 프롬프트를 제한하는 것이 중요합니다.
        
        <font color="blue"><b>⑤ 테스트와 실험</b></font><br>
        생성형 인공지능은 항상 정확한 결과를 보장하지 않습니다. 프롬프트를 작성한 후에는 인공지능의 응답을 검토하고 수정하는 등 테스트와 실험을 통해 최적의 프롬프트를 찾을 수 있습니다.
        
        <font color="blue"><b>⑥ 반복하여 시도</b></font><br>
        생성형 인공지능은 시도와 오류를 통해 점진적으로 개선될 수 있습니다. 다양한 프롬프트를 시도하고 비슷한 작업을 여러 번 반복하여 인공지능의 결과를 개선하는 데에 도움을 줄 수 있습니다.
        
        <font color="blue"><b>⑦ 인간적인 매개 변수 추가(옵션)</b></font><br>
        인간적인 매개변수를 추가하여 생성된 내용을 조정할 수 있습니다. 예를 들어, "두꺼운 글꼴로 이메일을 작성해주세요"와 같이 인간적인 요청을 추가하여 생성된 텍스트의 스타일을 조정할 수 있습니다.
        <br><br>
        위의 지침을 따라 프롬프트를 작성하면 생성형 인공지능이 원하는 결과를 얻는 데 도움이 됩니다. 하지만, 생성형 인공지능은 여전히 기술적 한계가 있으므로 항상 생성된 결과를 검토하고 조정하는 것이 중요합니다.(챗GPT의 조언)
        
        """, unsafe_allow_html=True)
with tab2 :
    st.subheader("나도 질문왕! 작성 방법")

    st.markdown("""
    <p style="background-color:#EAEAEA">
    ChatGPT를 활용하여 궁금한 내용들을 질문하고 친구들과 공유해봅니다.<br> 공유 과정은 아래와 같으니 자신의 질문 결과물을 패들렛에 올려 주세요!
    <br><br>
     </p>
        """, unsafe_allow_html=True)
    st.markdown("""<b><font color="red">①</font></b> 챗GPT 사이트에 로그인합니다.(<a href="http://chat.openai.com">http://chat.openai.com</a>) 
    """,unsafe_allow_html=True)
    st.markdown("<b><font color='red'>②</font></b> 프롬프트에 궁금한 내용을 질문합니다.<br>",unsafe_allow_html=True)
    st.markdown("<b><font color='red'>③</font></b> 같은 맥락의 질문이면 계속해서 이어서 질문합니다.<br>",unsafe_allow_html=True)
    st.markdown("<b><font color='red'>④</font></b> 질문의 결과를 공유하기 위해서 챗GPT 사이트의 상단에 'Share chat' 아이콘을 클릭합니다.<b>(그림1)</b><br>",unsafe_allow_html=True)
    st.image("images/chat1.jpg")
    st.markdown("<h6 style='text-align: center; color: blue;'>(▲그림1)</h6>", unsafe_allow_html=True)
    st.markdown("<b><font color='red'>⑤</font></b> 나타난 화면에서 'copy link'를 클릭하면 나의 프롬프트 결과의 공유 링크가 생성됩니다.<b>(그림2)</b><br>", unsafe_allow_html=True)
    st.image("images/chat2.jpg")
    st.markdown("<h6 style='text-align: center; color: blue;'>(▲그림2)</h6>", unsafe_allow_html=True)
    st.markdown("<b><font color='red'>⑥</font></b> 복사한 질문 링크는 아래 패들렛에 올려 친구들과 공유합니다.(<a href='https://padlet.com/shewill76/padlet-n9vkb730705llodp'>https://padlet.com/shewill76/padlet-n9vkb730705llodp</a>) <br>",unsafe_allow_html=True)
    st.image("images/chat3.jpg")

        





