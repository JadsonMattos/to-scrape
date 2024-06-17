import requests
import parsel


URL_BASE = "http://books.toscrape.com/catalogue/"
PAGE = "the-grand-design_405/index.html"


def scrape(url: str) -> str:
    response = requests.get(url)
    selector = parsel.Selector(response.text)

    title = selector.css("h1::text").get()

    price = selector.css(".product_main > .price_color::text").re_first(
        r"\d*\.\d{2}")

    description = selector.css("#product_description ~ p::text").get()
    suffix = "...more"
    if description.endswith(suffix):
        description = description[:-len(suffix)]

    cover = URL_BASE + selector.css("#product_gallery img::attr(src)").get()
    results = [title, price, description, cover]
    return results


scrape(URL_BASE + PAGE)
