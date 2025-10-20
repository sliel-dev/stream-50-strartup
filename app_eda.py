import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda():
    st.subheader('탐색적 데이터 분석')
    
    # 데이터 로드
    df = pd.read_csv('data/50_Startups.csv')
    
    # 기본 통계량 확인
    st.markdown('### 1. 기본 통계 정보')
    st.write('수치형 데이터의 기본 통계량')
    st.dataframe(df.describe())
    
    # 각 주별 기업 수 확인
    st.markdown('### 2. 주(State)별 기업 분포')
    state_counts = df['State'].value_counts()
    
    fig1, ax1 = plt.subplots()
    plt.pie(state_counts.values, labels=state_counts.index, autopct='%1.1f%%')
    plt.title('주별 기업 분포')
    st.pyplot(fig1)
    plt.close()
    
    # 상관관계 분석
    st.markdown('### 3. 변수 간 상관관계')
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    correlation = df[numeric_columns].corr()
    
    fig2, ax2 = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
    plt.title('상관관계 히트맵')
    st.pyplot(fig2)
    plt.close()
    
    # 변수별 분포 확인
    st.markdown('### 4. 변수별 분포')
    column = st.selectbox('확인하고 싶은 변수를 선택하세요:', numeric_columns)
    
    fig3, (ax3, ax4) = plt.subplots(1, 2, figsize=(15, 5))
    
    # 히스토그램
    sns.histplot(data=df, x=column, ax=ax3)
    ax3.set_title(f'{column} 분포')
    
    # 박스플롯
    sns.boxplot(data=df, y=column, ax=ax4)
    ax4.set_title(f'{column} 박스플롯')
    
    st.pyplot(fig3)
    plt.close()
    
    # Profit과 다른 변수들과의 관계
    st.markdown('### 5. 수익(Profit)과 다른 변수들과의 관계')
    feature = st.selectbox('비교할 변수를 선택하세요:', 
                          [col for col in numeric_columns if col != 'Profit'])
    
    fig4, ax5 = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=df, x=feature, y='Profit')
    plt.title(f'{feature}와 Profit의 관계')
    st.pyplot(fig4)
    plt.close()
    
    # 주별 평균 수익
    st.markdown('### 6. 주별 평균 수익')
    avg_profit_by_state = df.groupby('State')['Profit'].mean().sort_values(ascending=False)
    
    fig5, ax6 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=avg_profit_by_state.index, y=avg_profit_by_state.values)
    plt.title('주별 평균 수익')
    plt.xticks(rotation=45)
    st.pyplot(fig5)
    plt.close()
    
    # 데이터 요약
    st.markdown('### 7. 데이터 요약')
    st.write('- 결측치 개수:')
    st.write(df.isnull().sum())
    
    st.write('- 0값 개수:')
    st.write((df == 0).sum())