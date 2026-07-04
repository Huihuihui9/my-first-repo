import requests
from bs4 import BeautifulSoup


def scrape_titles(url):
    """抓取网页中的标题和链接"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
    except requests.RequestException as e:
        print(f"请求失败: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    results = []

    for tag in soup.find_all("a"):
        title = tag.get_text(strip=True)
        link = tag.get("href", "")
        if title and link and not link.startswith("#"):
            if not link.startswith("http"):
                link = requests.compat.urljoin(url, link)
            results.append({"title": title, "link": link})

    return results


if __name__ == "__main__":
    target = input("请输入要抓取的网址: ").strip()
    if not target.startswith("http"):
        target = "https://" + target

    print(f"\n正在抓取: {target}\n")
    items = scrape_titles(target)

    if not items:
        print("未找到任何链接")
    else:
        print(f"共找到 {len(items)} 个链接:\n")
        for i, item in enumerate(items[:20], 1):
            print(f"{i}. {item['title']}")
            print(f"   {item['link']}")
