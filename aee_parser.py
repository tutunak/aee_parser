from bs4 import BeautifulSoup as Bs
import requests

SITE = "https://www.allearsenglish.com/episodes/"


def get_url(url):
    status = 1
    try:
        page = requests.get(url, timeout=10)
        page.raise_for_status()
        result = page.text
    except requests.exceptions.ConnectionError:
        result = "ConnectionError"
    except requests.exceptions.HTTPError:
        result = f"Http error: {page.status_code}"
    else:
        status = 0
    return {"status": status, "data": result}


def main():
    page = get_url(SITE)
    if not page['status']:
        soup = Bs(page['data'], 'lxml')
    else:
        exit(1)
    articles = soup.find_all('article', attrs={'class': 'post'})


if __name__ == '__main__':
    main()
