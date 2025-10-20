import streamlit as st
import pandas as pd

def run_home():
    st.subheader('스타트업 수익 예측 프로젝트')
    
    st.write('이 앱은 스타트업 기업의 R&D 지출, 관리 비용, 마케팅 비용 등을 기반으로 수익을 예측하는 머신러닝 애플리케이션입니다.')
    
    # 데이터셋 로드 및 기본 정보 표시
    df = pd.read_csv('data/50_Startups.csv')
    
    st.markdown('### 📊 데이터셋 정보')
    st.write('- 총 데이터 수:', df.shape[0], '개')
    st.write('- 변수 수:', df.shape[1], '개')
    
    st.markdown('### 📌 주요 변수 설명')
    st.markdown('''
    - R&D Spend: 연구개발 비용
    - Administration: 관리 비용
    - Marketing Spend: 마케팅 비용
    - State: 스타트업 소재 주(뉴욕, 캘리포니아, 플로리다)
    - Profit: 수익 (예측 대상)
    ''')
    
    st.markdown('### 🔍 앱 사용 방법')
    st.markdown('''
    1. **EDA (탐색적 데이터 분석)**: 
        - 데이터의 통계적 특성 확인
        - 변수 간의 상관관계 분석
        - 시각화를 통한 데이터 패턴 파악
    
    2. **ML (머신러닝)**:
        - 비용 데이터를 입력하여 예상 수익 예측
        - 머신러닝 모델을 통한 정확한 수익 추정
    ''')
    
    # 샘플 데이터 미리보기
    st.markdown('### 💡 데이터 미리보기')
    st.dataframe(df.head())