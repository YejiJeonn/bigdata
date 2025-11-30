# step1) 분야별 주식종목 '평균 주가'와 '평균 등락율' 시각화

# 1. 아래의 프로그램 설치
# !apt-get update
# !apt install -y chromium-chromedriver
# !pip install selenium pandas matplotlib bs4
# !apt-get install -y fonts-nanum
# !apt-get update
# !apt-get install -y wget unzip
# # Chrome 설치
# !wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# !apt-get -y install ./google-chrome-stable_current_amd64.deb
# # ChromeDriver 설치 (Chrome 버전에 맞춰 자동 다운로드)
# !CHROME_VERSION=$(google-chrome --version | sed 's/Google Chrome //')
# !wget -O chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/${CHROME_VERSION}/linux64/chromedriver-linux64.zip
# !unzip chromedriver.zip
# !mv chromedriver-linux64/chromedriver /usr/bin/chromedriver
# !chmod +x /usr/bin/chromedriver

# 2. 폰트 등록
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib as mpl
import os

font_dirs = ['/usr/share/fonts/truetype/nanum']
font_files = fm.findSystemFonts(fontpaths=font_dirs)

for fpath in font_files:
    fm.fontManager.addfont(fpath)

# 최신 버전 matplotlib에서는 FontManager를 새로 로드하여 캐시 갱신
fm._load_fontmanager(try_read_cache=False)

plt.rc('font', family='NanumGothic')
mpl.rcParams['axes.unicode_minus'] = False  # 마이너스 깨짐 방지

# 한글 폰트 등록 확인
print([f.name for f in fm.fontManager.ttflist if 'Nanum' in f.name])

# 3. Selenium, BeautifulSoup 사용하여 한경 주식데이터 페이지 크롤링
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # Import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu") # Added for better headless stability
chrome_options.add_argument("--window-size=1920,1080") # Set a default window size
chrome_options.binary_location = '/usr/bin/google-chrome-stable' # Specify the path to the newly installed Chrome binary

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://datacenter.hankyung.com/equities-all")

time.sleep(5)  # Wait for JS data to load
html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, "lxml")

# 4. 크롤링 데이터 분리
groups = soup.select("div.equities-group")
data = []

for group in groups:
    category = group.select_one(".group-tit .ellip").get_text(strip=True)
    for li in group.select("li"):
        name_tag = li.select_one(".stock-title a")
        price_tag = li.select_one(".price")
        rate_tag = li.select_one(".rate")
        if name_tag and price_tag and rate_tag:
            name = name_tag.get_text(strip=True)
            price = price_tag.get_text(strip=True).replace(",", "")
            rate = rate_tag.get_text(strip=True).replace("%", "").replace("+", "")
            price = pd.to_numeric(price, errors="coerce")
            rate = pd.to_numeric(rate, errors="coerce")
            data.append({"분야": category, "종목": name, "현재가": price, "등락률": rate})

df = pd.DataFrame(data)
print(df.head())
print(f"총 {len(df)}개 종목 수집 완료")
print("--------------------------")
print(df['분야'].value_counts())

df.to_csv('hankyung_stocks.csv', index=False, encoding='utf-8-sig')

# 5. 그래프로 출력 (시각화)