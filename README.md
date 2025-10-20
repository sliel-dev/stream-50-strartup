# 스타트업 수익 예측 애플리케이션

스타트업 기업의 R&D 지출, 관리 비용, 마케팅 비용 등의 데이터를 기반으로 수익을 예측하는 머신러닝 기반 웹 애플리케이션입니다.

## 프로젝트 개요

- 데이터셋: 50개 스타트업 기업의 비용 및 수익 데이터
- 목적: 비용 데이터를 기반으로 스타트업의 수익을 예측
- 구현: Streamlit을 활용한 웹 애플리케이션

## 주요 기능

1. **홈 (Home)**
   - 애플리케이션 소개
   - 데이터셋 기본 정보
   - 주요 변수 설명
   - 데이터 미리보기

2. **데이터 분석 (EDA)**
   - 기본 통계 정보
   - 주(State)별 기업 분포
   - 변수 간 상관관계 분석
   - 변수별 분포 확인
   - 수익과 변수 간의 관계 분석
   - 지역별 평균 수익 분석

3. **머신러닝 (ML)**
   - 수익 예측 모델
   - 실시간 예측 기능

## 데이터셋 설명

- **R&D Spend**: 연구개발 비용
- **Administration**: 관리 비용
- **Marketing Spend**: 마케팅 비용
- **State**: 스타트업 소재 주(뉴욕, 캘리포니아, 플로리다)
- **Profit**: 수익 (예측 대상)

## 설치 및 실행 방법

1. 저장소 클론
```bash
git clone https://github.com/sliel-dev/stream-50-strartup.git
cd stream-50-strartup
```

2. 필요한 패키지 설치
```bash
pip install streamlit pandas numpy matplotlib seaborn scikit-learn
```

3. 애플리케이션 실행
```bash
streamlit run app.py
```

## 기술 스택

- **Frontend**: Streamlit
- **Backend**: Python
- **데이터 분석**: Pandas, NumPy
- **시각화**: Matplotlib, Seaborn
- **머신러닝**: Scikit-learn

## 프로젝트 구조

```
stream-50-strartup/
├── app.py              # 메인 애플리케이션
├── app_home.py         # 홈 화면 구성
├── app_eda.py          # 데이터 분석 기능
├── app_ml.py           # 머신러닝 예측 기능
├── data/               # 데이터 폴더
│   └── 50_Startups.csv # 스타트업 데이터
└── model/              # 학습된 모델 저장 폴더
```

## 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다.
