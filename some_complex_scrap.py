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

soup  = BeautifulSoup(ITEM_HTML,'html.parser')

def find_title():
    locator = 'article.product_pod h3 a'
    link  =   soup.select_one(locator)
    title = link.attrs.get('title')
    return title

def find_href_h3():
    locator = 'article.product_pod h3 a'
    link = soup.select_one(locator).attrs.get('href')
    return link

def find_price():
    locator = 'article.product_pod p.price_color'
    value = soup.select_one(locator).string   # this gives us pound sign and price
    # but we want the price or only the float value not any currency sign
    #pattern = '£([0-9]+/.[0-9]+)'
    #matcher = re.search(pattern, value)
    #return float(matcher.group(1))     #group 0 will give the £ sign and group 1 give the actual value from pattern


def find_item_rating():
    locator = 'article.product_pod p.star-rating.Three'
    item_tag = soup.select_one(locator).attrs['class'][1]   # ['star-rating', 'Three']   [1] we get Three----   -- this returns list btw
    # or we can also do this by the filter function            filter(lambda x: x!= 'star-ratinng', item_tag) when not specifiec the list index
    print(item_tag)



print("title scrapped from article h3 is:-->",find_title())
print("href inside the a tag inside h3:-->",find_href_h3())
#print('price of the article is:-->',find_price())
find_item_rating()