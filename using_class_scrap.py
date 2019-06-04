import re

from bs4 import BeautifulSoup


ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
            <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
            </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
            <p class="price_color">£51.77</p>
            <p class="instock availability">
               <i class="icon-ok"></i>
                   In stock
            </p>
            <form>
               <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
            </form>
            </div>
    </article>
</li>
</body></html>
'''



class ParsedItem:
    def __init__(self,page):
        self.soup = BeautifulSoup(page, 'html.parser')

    def find_title(self):
        locator = 'article.product_pod h3 a'
        link = self.soup.select_one(locator)
        title = link.attrs.get('title')
        return title

    def find_href_h3(self):
        locator = 'article.product_pod h3 a'
        link = self.soup.select_one(locator).attrs.get('href')
        return link

    def find_price(self):
        locator = 'article.product_pod p.price_color'
        value = self.soup.select_one(locator).string   # this gives us pound sign and price
        # but we want the price or only the float value not any currency sign
        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, value)
        return float(matcher.group(1))     #group 0 will give the £ sign and group 1 give the actual value from pattern

    def find_item_rating(self):
        locator = 'article.product_pod p.star-rating.Three'
        item_tag = self.soup.select_one(locator).attrs['class'][1]   # ['star-rating', 'Three']   [1] we get Three----   -- this returns list btw
        # or we can also do this by the filter function            filter(lambda x: x!= 'star-ratinng', item_tag) when not specifiec the list index
        return item_tag


item = ParsedItem(ITEM_HTML)

print(item.find_item_rating())
print(item.find_href_h3())
print("price of the item is--->",item.find_price())