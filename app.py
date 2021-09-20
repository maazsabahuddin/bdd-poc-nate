# Python imports
import os

# Framework imports
from behave.__main__ import main as behave_main


def _execute():
    """
    Below command will run behave..
    """
    behave_main()


sites = {"macys":
             "https://www.macys.com/shop/product/diesel-caged-three-hand-black-leather-watch?ID=12122328",
         "gap":
             "https://www.gap.com/browse/product.do?pid=619568022&cid=15043&pcid=15043&vid=6&cpos=3&cexp=1567&kcid="
             "CategoryIDs%3D15043&cvar=11754&ctype=Listing&cpid=res21081601211129801446166#pdp-page-content",
         "walmart":
             "https://www.walmart.com/ip/SmileMart-Adjustable-Ergonomic-High-Back-Gaming-Chair-Black-Gray/882329867"}

_result = open("result.txt", "a")
log = True

if __name__ == '__main__':

    for site, url in sites.items():
        print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(f">                                running {site}                                      >")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")
        os.system(f'cmd /c "behave -D url={url} -D name={site}"')
    _result.close()
