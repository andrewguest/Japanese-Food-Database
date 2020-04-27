import shutil

import requests


image_urls = {
    "Hakata Mitsuki: Delicious Cheese": "https://cdn.shopify.com/s/files/1/1083/2612/products/market-hakata-mitsuki-delicious-cheese-financier-cake-16-pieces-3_2000x.jpg?v=1570833978",
    "Okashinai Cheese Manju": "https://cdn.shopify.com/s/files/1/1083/2612/products/OkashinaiCheeseManju_Package_a8a2f985-07d6-4d6d-b828-779b300900d3_1200x.jpg?v=1570832705",
    "Black Sesame Taiko: Kumamon Design": "https://cdn.shopify.com/s/files/1/1083/2612/products/market-black-sesame-taiko-kumamon-design-10-pieces-1_1200x.jpg?v=1570833983",
    "Kocha Black Tea Donut": "https://cdn.shopify.com/s/files/1/1083/2612/products/market-kocha-black-tea-donut-6-pieces-1_2000x.jpg?v=1570832894",
    "Kinako Kurumi Walnut: Mochi": "https://cdn.shopify.com/s/files/1/1083/2612/products/market-kinako-kurumi-walnut-mochi-9-pieces-1_2000x.jpg?v=1570834107",
    "Sanrio Characters: Halloween Cookie Assort": "https://cdn.shopify.com/s/files/1/1083/2612/products/market-sanrio-characters-halloween-cookie-assortment-20-pieces-1_2000x.jpg?v=1570834114",
    "Puchi Pure Gummy: Halloween Grape": "https://cdn.shopify.com/s/files/1/1083/2612/products/market-puchi-pure-gummy-halloween-grape-12-packs-1_1200x.jpg?v=1570834040",
    "Cinnamon Fresh Yatsuhashi Daifuku": "https://cdn.shopify.com/s/files/1/1083/2612/products/CinnamonFreshYatsuhashiDaifuku_Tabling_1200x.jpg?v=1572014966",
    "Fried Kakinotane: Kyoto Fresh Yatsuhash": "https://cdn.shopify.com/s/files/1/1083/2612/products/FriedKakinotaneKyotoFreshYatsuhashiFlavor_Package_1200x.jpg?v=1572013525",
    "Matcha Chocolate Stick Cake": "https://cdn.shopify.com/s/files/1/1083/2612/products/MatchaChocolateStickCake_Package_1200x.jpg?v=1572015194",
    "Kitsune no Shippo": "https://cdn.shopify.com/s/files/1/1083/2612/products/past-snack-kitsune-s-tail-1_1200x.jpg?v=1559686261",
    "Funwari Meijin Mochi Puffs: Hokkaido Mi": "https://cdn.shopify.com/s/files/1/1083/2612/products/market-funwari-meijin-mochi-puffs-milk-4-packs-1_1200x.jpg?v=1570833448",
    "Natural Yeast Bread Chocolate": "https://cdn.shopify.com/s/files/1/1083/2612/products/past-snack-natural-yeast-bread-chocolate-1_1200x.jpg?v=1559687163",
    "Natural Yeast Bread: Hokkaido Cream": "https://cdn.shopify.com/s/files/1/1083/2612/products/HokkaidoCreamBread_Package_2f68ea45-1f03-43de-9fae-4e434dd9f8c3_1200x.jpg?v=1570832710",
    "Shiroi Koibito": "https://cdn.shopify.com/s/files/1/1083/2612/products/market-shiroi-koibito-18-pieces-1_1200x.jpg?v=1570832826",
    "White Black Thunder": "https://cdn.shopify.com/s/files/1/1334/9201/products/Black-Thunder-White-Chocolate_e8695a35-ab43-4e34-abb5-9227bc2dd9e6_1024x1024.JPG?v=1556456641",
    "Chocolate Dorayaki": "https://cdn.shopify.com/s/files/1/1423/1710/products/1_9208_480x480.png?v=1572235815",
    "Yasashii Yuzu Gummy": "https://images-na.ssl-images-amazon.com/images/I/91re5KMnqoL._SL1500_.jpg",
    "Jaga Pokkuru": "https://cdn.shopify.com/s/files/1/1083/2612/products/market-jaga-pokkuru-10-bags-1_2000x.jpg?v=1570832836",
    "Red Snapper Crackers": "https://cdn.shopify.com/s/files/1/1083/2612/products/RedSnapperCrackers_Package_400x.jpg?v=1576568927",
    "Country Ma'am: Fragrant Vanilla": "https://megumi.b-cdn.net/media/catalog/product/cache/3/thumbnail/500x600/040ec09b1e35df139433887a97daa66f/M/P/MPJ018_12.jpg",
    "Saki Waffle Setouchi Lemon": "https://cdn.shopify.com/s/files/1/1083/2612/products/SakiWaffleSetouchiLemon_Package_2000x.jpg?v=1576568330",
    "Puku Puku Tai: Chocolate": "https://cdn.shopify.com/s/files/1/1083/2612/products/market-puku-puku-tai-chocolate-10-pieces-1_600x.jpg?v=1570832940",
    "Choco Magatte C'est Bon: Cherry Flavor": "https://cdn.shopify.com/s/files/1/1083/2612/products/ChocoMagatteCestBonCherryFlavor_Package_2000x.jpg?v=1578684730",
}


for filename, url in image_urls.items():
    if ".jpg" in url.lower():
        extension = ".jpg"
    else:
        extension = ".png"
    resp = requests.get(url, stream=True)
    filename = "/media/" + filename + extension
    local_file = open(filename, "wb")
    resp.raw.decode_content = True
    shutil.copyfileobj(resp.raw, local_file)
