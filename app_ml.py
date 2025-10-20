import streamlit as st
import joblib
import pandas as pd

def run_ml() :
    st.subheader('수익 예측')
    st.info('아래 데이터를 넣으시면 수익을 예측합니다.')
    # R&D Spend, Administration, Marketing Spend, State
    rnd = st.number_input('연구 개발비', min_value=0)
    admin = st.number_input('운영비', min_value=10000)
    marketing = st.number_input('마케팅비', min_value=0)
    state = st.radio('주 선택', ['California', 'Florida', 'New York'])
    if st.button('예측하기') :
        pipe = joblib.load('./model/pipe.pkl')
        new_data = [{'R&D Spend' : rnd, 'Administration' : admin, 'Marketing Spend' : marketing, 'State' : state}]
        df_new = pd.DataFrame(new_data)
        new_data_pred = pipe.predict(df_new)
        st.info(f'예상 수익은 {int(new_data_pred):,} 달러입니다.')
    else :
        pass