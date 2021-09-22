# Python imports
import os

# Framework imports
from behave.__main__ import main as behave_main
from file import open_file, close_file, read_file_and_append_result, erase_file_content


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


_result_file = open_file(name="result.txt", mod="a")
log_flag = True
ERASE_FILE_CONTENT_EVERYTIME = False


def log_site(_site, message):
    print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(f">                                {message} {_site}                                    ")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == '__main__':

    if ERASE_FILE_CONTENT_EVERYTIME and not erase_file_content():
        print("Error encountered..")
        os.abort()

    for site, url in sites.items():
        log_site(site, message="Running")
        os.system(f'cmd /c "behave -D name={site} -D log={log_flag} -D url={url}"')
        _result_file.write("\n") if list(sites.keys())[-1] == site and log_flag else None
    close_file(_result_file)

    read_file_and_append_result()
