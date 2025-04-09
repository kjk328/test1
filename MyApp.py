import streamlit as st
import yfinance as yf
import pandas as pd
import datetime

st.set_page_config(page_title="삼성전자 주가 확인기 📈", layout="centered")

st.title("📊 삼성전자 주가 조회 앱")

# 날짜 선택
end = st.date_input("종료 날짜", datetime.date.today())
start = st.date_input("시작 날짜", end - datetime.timedelta(days=30))

# 유효성 검사
if start > end:
    st.error("시작 날짜는 종료 날짜보다 이전이어야 합니다.")
else:
    # 삼성전자 티커 (코스피)
    ticker = "005930.KS"
    df = yf.download(ticker, start=start, end=end)

    if df.empty:
        st.warning("해당 기간에 대한 데이터가 없습니다.")
    else:
        st.subheader("📈 종가 차트")
        st.line_chart(df["Close"])

        st.subheader("📋 주가 데이터 테이블")
        st.dataframe(df)
