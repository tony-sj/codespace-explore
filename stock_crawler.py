
# [dev branch] 이 코드는 dev 브랜치에서만 보입니다.
import requests
from bs4 import BeautifulSoup


def get_stock_price(symbol: str) -> float:
    """
    주식 심볼을 받아 현재가를 반환합니다. (네이버 금융 기준)
    """
    url = f"https://finance.naver.com/item/main.nhn?code={symbol}"
    resp = requests.get(url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')
    price_tag = soup.select_one('p.no_today span.blind')
    if not price_tag:
        raise ValueError("주가 정보를 찾을 수 없습니다.")
    price = price_tag.text.replace(',', '')
    return float(price)


if __name__ == "__main__":
    print("[dev branch] 이 코드는 dev 브랜치에서 실행 중입니다.")
    symbol = input("종목 코드를 입력하세요 (예: 005930): ")
    try:
        price = get_stock_price(symbol)
        print(f"{symbol}의 현재가: {price}원")
    except Exception as e:
        print(f"에러 발생: {e}")
