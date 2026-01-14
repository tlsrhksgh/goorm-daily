import requests
from bs4 import BeautifulSoup

##### 사람인 IT직종 구인 크롤링(제목만)
##### 지역코드 101000: 서울
##### 직종코드 2: IT·인터넷·통신·게임

LOC_CODE = 101000
JOB_CODE = 2
PAGE = 1
PAGE_COUNT = 50
INPUT_PAGE = 0
INPUT_PAGE_COUNT = 50

while True:
    page = input("크롤링할 페이지 수를 입력하세요 (예: 1~5): ")
    page_count = input("페이지당 크롤링할 공고 수를 입력하세요 (예: 10~100): ")
    
    if not page.isdigit():
        print("페이지 수는 숫자로 입력해주세요.")
        continue

    if not page_count.isdigit():
        print("공고 수는 숫자로 입력해주세요.")
        continue
    
    INPUT_PAGE = int(page)
    INPUT_PAGE_COUNT = int(page_count)
    
    if INPUT_PAGE < 1 or INPUT_PAGE > 5:
        print("페이지 수는 1~5 사이여야 합니다.")
        continue

    if INPUT_PAGE_COUNT < 10 or INPUT_PAGE_COUNT > 100:
        print("공고 수는 10~100 사이여야 합니다.")
        continue
    
    break

SARAMIN_URL = "https://www.saramin.co.kr/zf_user/jobs/list/domestic?page={INPUT_PAGE}&page_count={INPUT_PAGE_COUNT}&loc_cd={LOC_CODE}&cat_mcls={JOB_CODE}&panel_type=&search_optional_item=n&search_done=y&panel_count=y&preview=y"

class HttpClient:
    def __init__(self):
        self.session = requests.Session()        
        self.session.headers.update({  
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),            
        })

    def get_html(self, url:str) -> str:
        response = self.session.get(url)
        response.raise_for_status()
        return response.text

client = HttpClient()

html_text = client.get_html(SARAMIN_URL.format(INPUT_PAGE=INPUT_PAGE, INPUT_PAGE_COUNT=INPUT_PAGE_COUNT, LOC_CODE=LOC_CODE, JOB_CODE=JOB_CODE))
soup = BeautifulSoup(html_text, 'html.parser')
titles = soup.select("div.job_tit")

for t in titles:
    print(t.get_text(strip=True))
