import requests
from bs4 import BeautifulSoup

def get_naver_news_titles(query, num_articles=5):
    base_url = "https://search.naver.com/search.naver"
    params = {
        "where": "news",
        "query": query,
    }

    response = requests.get(base_url, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_titles = []
    for i, title_tag in enumerate(soup.select('.news_tit')):
        if i == num_articles:
            break
        news_titles.append(title_tag.get_text(strip=True))

    return news_titles

if __name__ == "__main__":
    query = "에코프로"
    num_articles = 5
    titles = get_naver_news_titles(query, num_articles)

    print(f"네이버 뉴스에서 '{query}'와 관련된 기사 제목 {num_articles}개:")
    for i, title in enumerate(titles, start=1):
        print(f"{i}. {title}")
