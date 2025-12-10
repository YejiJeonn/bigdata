# bigdata
[빅데이터] 수업용📊

### 주제 : 주가에 영향을 끼치는 금융상품 탐색 / 주식과 금융상품 간의 연관성 / 그래프 시각화 & 분석 예측

이 레포지토리는 빅데이터 수업의 최종 과제 제출을 위해 생성되었습니다. </br>
최근 주식에 관심이 생겨, 다양한 금융상품에 따라 주식의 변동성이 어떤 영향을 받는지 조사하는 것을 주제로 선정하게 되었습니다. </br>
다양한 금융상품과 주식 간의 변동성 비교 그래프를 통해 어떤 금융상품에 어떠한 영향을 받는지에 대해 그래프로 시각화를 하고 분석하여 최종적으로 **금융상품에서 오는 영향으로 인한 주식의 변동성을 예측**하고자 했습니다.

진행한 시각화와 분석은 다음과 같습니다. </br></br>
### [1. 시각화]
1-1. 국내 주식 분야별 비교 그래프 </br>
1-2. 한국장 vs. 미국장 주가 비교 그래프 </br>
1-3. 금 vs. 코인 vs. 주가 비교 그래프 </br>
1-4. 환율(미국 $) vs. 주가 비교 그래프 </br>

### [2. 분석/예측] 
2-1. KOSPI & KOSDAQ 주가 예측 </br>
2-2. 환율 기반 주가 예측 </br>
2-3. 금, 코인, 주식 상관관계 및 연관성을 통한 예측 </br>
2-4. 미국장 변화에 따른 한국장 변화 예측 </br>
</br></br>
다음은 진행한 주제별 구체적인 설명입니다. </br>
</br>

## 1. 시각화 분석
### 1.1. 국내 주식 분야별 비교 그래프
<img width="862" height="428" alt="image" src="https://github.com/user-attachments/assets/7c837496-8762-4b52-bb7a-8d05fd82494c" /> </br>
<img width="862" height="428" alt="image" src="https://github.com/user-attachments/assets/4339f570-ce53-4f8c-84ec-e98b1f571c21" /> </br>
<img width="960" height="432" alt="image" src="https://github.com/user-attachments/assets/3a9c4e88-6014-4d60-96e6-b40079671ba2" /> </br>
<img width="960" height="418" alt="image" src="https://github.com/user-attachments/assets/99f4b70a-1958-4c46-861a-71f6e547fa2b" /> </br>
<img width="960" height="418" alt="image" src="https://github.com/user-attachments/assets/0ed9bd99-f7de-4c1d-bece-17780bfafb43" /> </br>
</br>
📌 ① 데이터 정보  </br>
  출처: 한국경제 데이터센터 웹 크롤링 </br>
  수집 항목 </br>
    - 분야(업종), 종목명 </br>
    - 현재가 </br>
    - 등락률 </br>
  특징 </br>
    - 시계열이 아닌 단일 시점 데이터 </br>
    - 분야별 상대 비교 목적 </br>
  </br> 
📌 ② 전처리 과정 </br>
  한글 폰트 설정(나눔고딕) </br>
  웹 크롤링 & HTML 파싱 </br>
  문자열 후처리(%, +, , 제거 후 숫자 변환) </br>
  결측 제거 후 분야별 groupby 집계 </br>
  </br> 
📌 ③ 사용된 그래프 </br>
  막대 그래프: 분야별 평균 현재가 / 평균 등락률 </br>
  레이더 차트: 분야 간 패턴·치우침 확인 </br>
  트리맵: 분야 규모의 상대적 크기 시각화 </br>
  버블 차트 </br>
    X축: 평균 등락률 </br>
    Y축: 평균 현재가 </br>
    버블 크기: 평균값 반영 </br>
    버블 투명도: 값 크기 비례 </br>
 </br>
📌 ④ 주요 해석 </br>
  단순 수치 비교 → 막대그래프 </br>
  패턴 확인 → 레이더 차트 </br>
  상대 규모 파악 → 트리맵 </br>
  평균가격+변동률 동시에 비교 → 버블 차트 </br>
  
</br> 

### 1.2. 한국장 vs 미국장 비교 그래프
<img width="733" height="404" alt="image" src="https://github.com/user-attachments/assets/5c160e31-bcf8-4a84-9bc0-dcc37ce9eece" /> </br>
</br> 
📌 ① 데이터 정보 </br>
  출처: Stooq (KOSPI · S&P500 월별 종가) </br>
  특징 </br>
    - 시계열 구조 </br>
    - 정규화 필요(두 지수의 절대값이 달라 의미 없음)
    </br></br>
📌 ② 전처리</br>
  날짜 파싱</br>
    - 2019년 이후 데이터 사용</br>
  첫 값을 100으로 정규화</br>
  월별 수익률 계산</br>
  두 시장 간 상관계수 계산
  </br></br>
📌 ③ 그래프</br>
  선 그래프(정규화 기반)</br>
  방향성·추세 비교에 적합</br>
  </br>
📌 ④ 인사이트</br>
  상관계수 0.7086 → 강한 양의 상관관계</br>
  한국장은 미국장을 따라가는 구조</br>
  
</br>

### 1.3. 금 vs 코인 vs 주가 비교
<img width="498" height="424" alt="image" src="https://github.com/user-attachments/assets/7802170b-6b82-49aa-beb9-09937934fb2e" /> </br>
<img width="828" height="446" alt="image" src="https://github.com/user-attachments/assets/d9564796-c7d2-479c-8885-d8819e837705" /> </br>

📌 ① 데이터 정보 </br>
  GLD ETF(금) </br>
  BTC-USD(비트코인) </br>
  KOSPI 지수 </br>
  기간: 2019–2025 </br>
</br>
📌 ② 전처리 </br>
  yfinance로 수집 </br>
  결측 제거 </br>
  일간 수익률 계산 </br>
  시작값 100으로 정규화 </br>
</br>
📌 ③ 그래프 </br>
  Heatmap: 자산 간 상관관계 </br>
  정규화 선 그래프: 변동성 비교 </br>
</br>
📌 ④ 주요 인사이트 </br>
  비트코인은 다른 자산과 상관성이 낮음 </br>
  금 = 안정적, Bitcoin = 고변동 </br>
  KOSPI는 중간 변동성 </br>
  금융 이벤트별 자산군 반응 차이를 확인 가능 </br>
  
</br>

### 1.4. 환율 vs KOSPI 비교
<img width="781" height="424" alt="image" src="https://github.com/user-attachments/assets/de2f1758-4d55-4634-9e8e-759ddc40b3e3" /> </br>

📌 ① 데이터 정보 </br>
  USD/KRW 환율 </br>
  KOSPI 종가 </br>
  2019–2025 일 단위 데이터 </br>
</br>
📌 ② 전처리 </br>
  날짜 기준 병합 </br>
  수익률 계산 </br>
</br>
📌 ③ 그래프 </br>
  정규화 비교 그래프 </br>
  상관계수 계산 </br>
</br>
📌 ④ 인사이트 </br>
  일반적으로 환율 ↑ → KOSPI ↓ </br>
  외환시장과 주식시장은 종종 역상관 </br>
  경제 이벤트(코로나, 금리 등) 반응 차이 확인 가능 </br>
  
</br>

## 2. 예측 모델 분석

### 2.1. KOSPI & KOSDAQ 예측
<img width="790" height="436" alt="image" src="https://github.com/user-attachments/assets/e03cf0ae-b46e-45cb-825b-aeac50756f89" /> </br>
<img width="870" height="402" alt="image" src="https://github.com/user-attachments/assets/4dd15aeb-2b8d-4062-b325-c707620f9539" /> </br>
<img width="884" height="412" alt="image" src="https://github.com/user-attachments/assets/dd3645a4-b9be-469e-ae8a-a4d1a2e99e8b" /> </br>

📌 ① 데이터 정보 </br>
  FinanceDataReader(FDR) </br>
  KOSPI, KOSDAQ 일별 종가 </br>
  2019–2025 </br>
   </br>
📌 ② 전처리 </br>
  정규화(첫날 = 100) </br>
  월별 수익률 계산 </br>
  LSTM용 60일 윈도우 시퀀스 생성 </br>
   </br>
📌 ③ 그래프 </br>
  정규화 추세 비교 </br>
  상관계수 분석 </br>
  LSTM 실제값 vs 예측값 오버레이 </br>
   </br>
📌 ④ 인사이트 </br>
  KOSPI & KOSDAQ → 매우 높은 상관성 </br>
  KOSDAQ은 더 큰 변동성 </br>
  LSTM은 KOSPI에서 안정적 예측 성능 </br>

 </br>
 
### 2.2. KOSPI 데이터 다양한 모델로 예측
<img width="960" height="260" alt="image" src="https://github.com/user-attachments/assets/4fe1cb8a-bc8d-4248-8dce-8f58e465d8d9" /> </br>

📌 ① 데이터 정보 </br>
  2000–2025 KOSPI 종가 </br>
  단일 시계열 → 비정상성 강함 </br>
   </br>
📌 ② 전처리 </br>
  ARIMA 차분 </br>
  LSTM 정규화 및 시퀀스 구성 </br>
  Prophet용 컬럼명 변환 </br>
 </br>
📌 ③ 모델별 분석 </br>
  ARIMA </br>
    - 단순 추세 기반 </br>
    - 급등락 예측 실패 </br>
  LSTM </br>
    - 실제 움직임과 가장 유사 </br>
    - 단기 패턴 재현 우수  </br>
  Prophet </br>
    - 장기 추세는 잘 잡으나 단기 변동 반영 약함 </br>
     </br>
📌 ④ 결론 </br>
  LSTM > Prophet > ARIMA </br>
  장기 데이터의 “방향성” 파악에는 의미 있음 </br>

 </br>
 
### 2.3. 금·코인·주식 상관 기반 예측
<img width="655" height="352" alt="image" src="https://github.com/user-attachments/assets/13c91e50-2fd5-4c5c-8065-a7b47ef057c0" /> </br>
<img width="881" height="408" alt="image" src="https://github.com/user-attachments/assets/7c03feeb-2210-4ce1-8406-53b41e64dec4" /> </br>
<img width="864" height="399" alt="image" src="https://github.com/user-attachments/assets/53dbdfb4-5242-47c5-9521-776199529726" /> </br>
<img width="862" height="400" alt="image" src="https://github.com/user-attachments/assets/2ed586cd-00f4-4e32-bd19-97f714296ee2" /> </br>

📌 ① 데이터 정보 </br>
  Gold, BTC, KOSPI 종가 </br>
  선형회귀 / ARIMA / ARIMAX / LSTM 비교 </br>
   </br>
📌 ② 전처리 </br>
  결측치 처리: 날짜 병합 후 dropna </br>
  수익률 계산 </br>
  LSTM용 MinMaxScaler 적용 </br>
   </br>
📌 ③ 모델 분석 </br>
  선형회귀: 단순 관계 분석, 설명력 낮음 </br>
  ARIMA: 전환점 포착 불가 </br>
  ARIMAX: 외생변수(금, BTC) 반영 </br>
  LSTM: 패턴 재현력 최고 </br>
   </br>
📌 ④ 결과 </br>
  LSTM이 가장 실제 종가와 비슷한 예측 생성 </br>
  장기 예측은 오차 누적 가능 </br>

   </br>

### 2.4. 미국장(SPX) 기반 한국장(KOSPI) 예측
<img width="713" height="384" alt="image" src="https://github.com/user-attachments/assets/8286d73d-5839-4aca-91d8-2e642b09fdf9" /> </br>

📌 ① 데이터 정보 </br>
  SPX, KOSPI 월별 수익률 </br>
  공통 날짜 병합 </br>
   </br>
📌 ② 전처리 </br>
  Train: 2019–2023 </br>
  Test: 2024– </br>
  LSTM: 지난 12개월 SPX 입력 → 다음달 KOSPI 예측 </br>
   </br>
📌 ③ 모델 비교 </br>
  Linear Regression: 가장 실제 움직임과 유사 </br>
  VAR </br>
  LSTM </br>
   </br>
📌 ④ 주요 결론 </br>
  미국장이 한국장을 예측하는 데 유효 </br>
  선형회귀 모델이 가장 높은 설명력 </br>

---

## 🔥 최종 결론
  ### 1) 한국장은 미국 시장 영향력이 가장 크다
    - S&P500 ↔ KOSPI 상관계수 약 0.7
    - 한국 증시는 구조적으로 미국장에 연동
     
  ### 2) 환율은 KOSPI와 음(-)의 관계
    - 달러 강세 → KOSPI 하락 가능성 증가
    - 한국 증시는 환율 민감형 시장
     
  ### 3) 금·비트코인은 KOSPI와 낮은 상관성
    - KOSPI 예측시 중요 변수는 아님
    - 그러나 분산 투자에서는 의미 있음
  
  ### 4) 예측 모델 정확도 순위
    - LSTM > VAR > ARIMA / Prophet
     
 ### 5) 금융 시계열은 비선형적
    - 완벽한 수치 예측은 불가능
    - “방향성 예측”이 현실적 목표
