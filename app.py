# Python imports
import datetime
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
             "https://www.gap.com/browse/product.do?pid=619568022&cid=15043",
         "walmart":
             "https://www.walmart.com/ip/SmileMart-Adjustable-Ergonomic-High-Back-Gaming-Chair-Black-Gray/882329867"}

_result = open("result.txt", "a")
log_flag = True


def log_site(_site):
    print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(f">                                running {_site}                                      >")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == '__main__':

    current_datetime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    _result.write(f"Date and Time: {current_datetime} \n") if log_flag else None
    _result.close()

    _result = open("result.txt", "a")
    for site, url in sites.items():
        log_site(site)
        os.system(f'cmd /c "behave -D name={site} -D log={log_flag} -D url={url}"')
        _result.write("\n") if list(sites.keys())[-1] == site and log_flag else None
    _result.close()
