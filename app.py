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

# sites = {
#     "kohls": "https://www.kohls.com/product/prd-4836898/under-armour-hustle-sport-backpack.jsp?color=Black&prdPV=1",
#     "ae": "https://www.ae.com/us/en/p/women/home/games-party-supplies/what-do-you-meme-the-office-expansion-pack/0577_3377_900?menu=cat4840004",
#     "nordstromrack": "https://www.nordstromrack.com/s/nike-brasilia-9-0-extra-large-training-backpack/6055904?origin=category-personalizedsort&breadcrumb=Home%2FBags%20%26%20Accessories%2FBack%20to%20School%3A%20Backpacks%20for%20Kids&color=026",
#     "zara": "https://www.zara.com/us/en/basic-bucket-hat-p09065481.html?v1=108980251&v2=1886951",
#     "jockey": "https://www.jockey.com/catalog/product/jockey-mens-signature-pocket-tshirt?isSale=True&color=3156",
#     "lululemon": "https://shop.lululemon.com/p/bags/Pack-It-Up-Backpack-1/_/prod7390352?color=48054&sz=ONESIZE",
#     "underarmour": "https://www.underarmour.com/en-us/p/masks/ua-sportsmask-featherweight/1372228.html?dwvar_1372228_color=001&start=0&breadCrumbLast=Men",
#     "squatwolf": "https://squatwolf.com/shop/core-mesh-tee-men-white/",
#     "hollisterco": "https://www.hollisterco.com/shop/wd/p/stacked-skinny-no-fade-jeans-45729384?seq=02&categoryId=12589&faceout=model1",
#     "zappos": "https://www.zappos.com/p/fjallraven-kanken-no-2-laptop-15-black/product/8812937/color/3",
#     "hm": "https://www2.hm.com/en_us/productpage.0606395006.html"
# }

# sites = {
#     "Cettire": "https://www.cettire.com/products/fendi-ff-jacquard-travel-backpack-99379344?variant=39532224544881",
#     "Spigen": "https://www.spigen.com/collections/iphone-13/products/iphone-13-case-slim-armor-essential-s?variant=39985455431727",
#     "Jbhifi": "https://www.jbhifi.com.au/products/gopro-hero10-black-5-3k-hypersmooth-4-0-action-cam",
#     "Mnml": "https://mnml.la/products/mnml-beanie-classic-beanie-beanie-m2020-b829-blk",
#     "Colourpop": "https://colourpop.com/products/glisten-up-vitamin-c",
#     "Kith": "https://kith.com/collections/kith-accessories-1/products/khm050023-307",
#     "Aloyoga": "https://www.aloyoga.com/products/a0084u-uplifting-yoga-block-black-silver",
#     "Uk.craftdlondon": "https://uk.craftdlondon.com/collections/rings/products/band-2-0-ring-silver"
# }

# sites = {
#     "Kingice": "https://www.kingice.com/collections/men/products/4-sunglasses",
#     "Boat-lifestyle": "https://www.boat-lifestyle.com/products/stone-1200?variant=32087654400098",
#     "Missoma": "https://www.missoma.com/products/sphere-beaded-hair-clip?variant=39494138658860&queryId=97b43d4ecbd4dc2f930d70f83f53d0f5&pdpIndex=usd_production_products",
#     "Staples": "https://www.staples.ca/products/566848-en-ballpoint-pens-retractable-grip-10mm-assorted-50pack",
#     "Fab": "https://fab.com/collections/household/products/organic-vegan-stain-removal-stick-560249459",
#     "Vqfit": "https://www.vqfit.com/collections/accessories/products/vanquish-khaki-crossbody-bag",
#     "Puravidabracelets": "https://www.puravidabracelets.com/collections/rings/products/raw-gemstone-ring?variant=39352154849366",
#     "Cupshe": "https://www.cupshe.com/collections/dress/products/haleigh-orange-backless-split-tea-length-dress?variant=39527129219162",
#     "Allbirds": "https://www.allbirds.com/products/runner-lace-kit?size=one-size"
# }

# sites = {
#     "Outofthesandbox": "https://outofthesandbox.com/collections/turbo-theme/products/turbo-theme-portland",
#     "Theoodie": "https://theoodie.com/products/oodie-pillows",
#     "Giuliofashion": "https://www.giuliofashion.com/collections/mens-accessories/products/moncler-area-backpack-5a6010002t02999?variant=32387225944147",
#     "Princesspolly": "https://us.princesspolly.com/collections/bags-wallets/products/highland-bag-brown",
#     "Nativeunion": "https://www.nativeunion.com/collections/usb-c-to-usb-c/products/desk-cable-usb-c-to-usb-c",
#     "Jadedldn": "https://jadedldn.com/collections/accessories-2/products/black-and-orange-round-lens-sunglasses-1",
#     "Carolazeta": "https://www.carolazeta.com/products/alexander-mcqueen-logo-pouch-001600390-1sj8b",
#     "Miansai": "https://www.miansai.com/collections/men/products/orson-bracelet-sterling-silver-matte?variant=29578548248691",
#     "Zox.la": "https://zox.la/products/zoxlox-single-gold",
#     "Ruggable": "https://ruggable.com/products/verena-dark-wood-rug?size=5x7"
# }

# sites = {
#     "beeinspiredclothing": "https://www.beeinspiredclothing.com/collections/accessories/products/linear-bucket-hat-oatmeal",
#     "Victoriaemerson": "https://www.victoriaemerson.com/collections/gold-necklaces/products/alessia",
#     "Vuoriclothing": "https://vuoriclothing.com/products/we-rise-bandana-turmeric?variant=39319957569639",
#     "Skinnydiplondon": "https://www.skinnydiplondon.com/collections/key-rings/products/disney-x-skinnydip-aliens-key-charm?nosto_source=cmp&nosto=614c3f9a49ffe660b38fcc8e",
#     "Reddress": "https://www.reddress.com/products/in-demand-taupe-bag",
#     "Feature": "https://feature.com/collections/ambush/products/ambush-class-ring-silver-black",
#     "Shopshashi": "https://shopshashi.com/products/perla-bracelet-emerald",
#     "Mclabels": "https://www.mclabels.com/collections/glasses/products/oakley-black-sunglasses-48",
#     "Culturekings": "https://www.culturekings.com.au/products/goat-crew-original-trucker-hat-white-black",
#     "Skims": "https://skims.com/products/face-mask-clay",
#     "Stevemadden": "https://www.stevemadden.com/collections/handbag-straps/products/bclipper-black"
# }

# sites = {
#     "bdgastore": "https://bdgastore.com/products/air-jordan-t-shirt",
#     "gonoise": "https://www.gonoise.com/products/noise-air-buds-plus-truly-wireless-earbuds",
#     "tommycashshop": "https://tommycashshop.com/collections/sweaters/products/blue-sweater",
#     "bandolierstyle": "https://www.bandolierstyle.com/products/morgan-belt-with-ryder-carabin-dark-leopard-gold",
#     "articture": "https://articture.com/collections/best-sellers/products/rosetta-floor-lamp?variant=39298854486103",
#     "keychron": "https://www.keychron.com/products/keychron-q1",
#     "uspoloassn": "https://uspoloassn.com/collections/mens-new-arrivals/products/tricot-tape-pieced-polo-shirt?",
#     "burga": "https://www.burga.com/collections/iphone-13-cases/products/cute-iphone-13-case?variant=40642467332271",
#     "brooklinen": "https://www.brooklinen.com/products/down-pillow?variant=8364503043",
#     "jimmyjazz": "https://www.jimmyjazz.com/products/jordan-air-jordan-retro-6-little-flex-ct4416-103",
# }

sites = {
    "Amrstore": "https://amrstore.com/products/max-mara-knit-16",
    "Ripndipclothing": "https://www.ripndipclothing.com/collections/long-sleeves/products/embroidered-logo-long-sleeve-black-mineral-wash",
    "Hanon-shop": "https://www.hanon-shop.com/collections/nike/products/nike-air-max-96-ii-db0251500",
    "Vicicollection": "https://www.vicicollection.com/products/banks-ribbed-knit-midi-dress-oatmeal",
    "Getpivo": "https://getpivo.com/products/pivo-pod-1",
    "Themusiczoo": "https://www.themusiczoo.com/products/martin-lxk2-little-martin-natural",
    "Huel": "https://huel.com/products/huel-flavor-boosts",
    "Drsquatch": "https://drsquatch.com/collections/toothpaste/products/citrus-mint-toothpaste",
    "Proozy": "https://www.proozy.com/collections/mens-sweaters/products/under-armour-mens-elevate-quarter-zip-sweater",
    "Vitalydesign": "https://www.vitalydesign.com/collections/accessories/products/akoya?variant=32796683567179",
    "Palomawool": "https://palomawool.com/collections/new-in/products/darwin-long-sleeved-asymmetric-top-navy",
    "Theseea": "https://www.theseea.com/collections/shop-all/products/lennon-shorts-denim",
    "Blvck": "https://blvck.com/collections/accessories/products/blvck-can?variant=32266072850534"
}


_result_file = open_file(name="automation_result.txt", mod="a")
log_flag = True
ERASE_FILE_CONTENT_EVERYTIME = True


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

    # read_file_and_append_result()
