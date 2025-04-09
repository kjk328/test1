import streamlit as st
 from openai import OpenAI
 
 st.title("🔐 ChatGPT-like App - Enter Your OpenAI API Key")
 
 # Step 1: 사용자로부터 API 키 입력 받기
 api_key = st.text_input("Enter your OpenAI API Key", type="password")
 
 # Step 2: 키가 입력되어야 다음 단계 진행
 if api_key:
     # OpenAI client 초기화
     client = OpenAI(api_key=api_key)
 
     st.success("✅ API Key accepted. You can start chatting!")
 
     # 기본 모델 지정
     if "openai_model" not in st.session_state:
         st.session_state["openai_model"] = "gpt-3.5-turbo"
 
     # 채팅 히스토리 초기화
     if "messages" not in st.session_state:
         st.session_state.messages = []
 
     # 이전 채팅 내용 출력
     for message in st.session_state.messages:
         with st.chat_message(message["role"]):
             st.markdown(message["content"])
 
     # 사용자 입력 받기
     if prompt := st.chat_input("What’s on your mind?"):
         st.session_state.messages.append({"role": "user", "content": prompt})
 
         # 사용자 메시지 출력
         with st.chat_message("user"):
             st.markdown(prompt)
 
         # OpenAI API 호출
         with st.chat_message("assistant"):
             with st.spinner("Thinking..."):
                 response = client.chat.completions.create(
                     model=st.session_state["openai_model"],
                     messages=st.session_state.messages
                 )
                 reply = response.choices[0].message.content
                 st.markdown(reply)
 
         # 응답 저장
         st.session_state.messages.append({"role": "assistant", "content": reply})
 else:
     st.warning("⚠️ Please enter your OpenAI API Key to continue.")
