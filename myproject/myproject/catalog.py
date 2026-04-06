from decimal import Decimal


CATEGORY_DETAILS = {
    "women": {
        "title": "Women's Collection",
        "eyebrow": "Women",
        "description": "Contemporary silhouettes, festive edits, soft tailoring, and daily essentials designed for Indian wardrobes.",
        "hero_image": "images/intro.jpg",
        "accent": "rose",
    },
    "men": {
        "title": "Men's Collection",
        "eyebrow": "Men",
        "description": "Smart casual shirts, polished staples, premium layers, and occasion-ready looks built for repeat wear.",
        "hero_image": "images/one.jpg",
        "accent": "ink",
    },
}


PRODUCTS = [
    {
        "slug": "women-linen-coord-set",
        "name": "Linen Co-ord Set",
        "category": "women",
        "product_type": "Co-ords",
        "price": Decimal("1899.00"),
        "compare_at_price": Decimal("2399.00"),
        "badge": "Best Seller",
        "short_description": "Easy daytime co-ord with a clean drape and polished structure.",
        "description": "A lightweight linen-blend co-ord that works for office hours, travel, and relaxed brunch dressing.",
        "image": "images/intro.jpg",
        "gallery": ["images/thumbs/01.jpg", "images/thumbs/02.jpg"],
        "sizes": ["S", "M", "L", "XL"],
        "highlights": ["Breathable fabric", "Soft neutral palette", "Easy to style"],
    },
    {
        "slug": "women-festive-anarkali",
        "name": "Festive Anarkali Set",
        "category": "women",
        "product_type": "Ethnic",
        "price": Decimal("2799.00"),
        "compare_at_price": Decimal("3399.00"),
        "badge": "Festive Edit",
        "short_description": "Elegant festivewear with movement, texture, and occasion-ready charm.",
        "description": "An occasion-ready set designed for family gatherings, weddings, and evening events with a refined traditional finish.",
        "image": "images/intro2.jpg",
        "gallery": ["images/thumbs/03.jpg", "images/thumbs/04.jpg"],
        "sizes": ["M", "L", "XL"],
        "highlights": ["Festive detailing", "Comfortable lining", "Statement silhouette"],
    },
    {
        "slug": "women-denim-jacket-edit",
        "name": "Denim Jacket Edit",
        "category": "women",
        "product_type": "Jackets",
        "price": Decimal("2199.00"),
        "compare_at_price": Decimal("2699.00"),
        "badge": "New Arrival",
        "short_description": "A clean denim layer for casual outfits and weekend travel looks.",
        "description": "Structured but comfortable, this denim jacket gives daily outfits a sharper shape without feeling bulky.",
        "image": "images/one3.jpg",
        "gallery": ["images/thumbs/05.jpg", "images/thumbs/06.jpg"],
        "sizes": ["S", "M", "L"],
        "highlights": ["Layering staple", "Classic wash", "Travel friendly"],
    },
    {
        "slug": "women-satin-evening-dress",
        "name": "Satin Evening Dress",
        "category": "women",
        "product_type": "Dresses",
        "price": Decimal("2499.00"),
        "compare_at_price": Decimal("2999.00"),
        "badge": "Evening Wear",
        "short_description": "Fluid satin styling for dinners, parties, and celebration dressing.",
        "description": "A soft sheen dress made for evening plans, designed to look elevated while staying easy to wear.",
        "image": "images/fulls/02.jpg",
        "gallery": ["images/fulls/02.jpg", "images/fulls/05.jpg"],
        "sizes": ["S", "M", "L"],
        "highlights": ["Soft sheen finish", "Occasion ready", "Comfortable fit"],
    },
    {
        "slug": "men-signature-polo-set",
        "name": "Signature Polo Set",
        "category": "men",
        "product_type": "Polos",
        "price": Decimal("1799.00"),
        "compare_at_price": Decimal("2199.00"),
        "badge": "Weekend Pick",
        "short_description": "Refined polo styling with comfortable structure for all-day wear.",
        "description": "A versatile polo-led outfit that handles meetings, errands, and evening outings with minimal effort.",
        "image": "images/one.jpg",
        "gallery": ["images/thumbs/01.jpg", "images/thumbs/03.jpg"],
        "sizes": ["M", "L", "XL", "XXL"],
        "highlights": ["Easy fit", "Repeat wear favourite", "Clean collar structure"],
    },
    {
        "slug": "men-tailored-shirt-trouser",
        "name": "Tailored Shirt Trouser Combo",
        "category": "men",
        "product_type": "Smart Casual",
        "price": Decimal("2499.00"),
        "compare_at_price": Decimal("3199.00"),
        "badge": "Office Ready",
        "short_description": "A clean smart-casual combo for office, dinner, and travel.",
        "description": "An elevated pairing that helps men dress sharper with minimal wardrobe planning.",
        "image": "images/fulls/04.jpg",
        "gallery": ["images/fulls/04.jpg", "images/fulls/06.jpg"],
        "sizes": ["M", "L", "XL"],
        "highlights": ["Structured look", "Easy office styling", "Modern cut"],
    },
    {
        "slug": "men-heritage-kurta-set",
        "name": "Heritage Kurta Set",
        "category": "men",
        "product_type": "Ethnic",
        "price": Decimal("2299.00"),
        "compare_at_price": Decimal("2899.00"),
        "badge": "Celebration Wear",
        "short_description": "Festive ethnicwear with a clean traditional finish.",
        "description": "A polished kurta set that works for family events, festivals, and wedding-season dressing.",
        "image": "images/fulls/03.jpg",
        "gallery": ["images/fulls/03.jpg", "images/fulls/05.jpg"],
        "sizes": ["M", "L", "XL", "XXL"],
        "highlights": ["Festive styling", "Comfortable tailoring", "Classic detailing"],
    },
    {
        "slug": "men-leather-finish-shoes",
        "name": "Leather Finish Brogues",
        "category": "men",
        "product_type": "Footwear",
        "price": Decimal("2899.00"),
        "compare_at_price": Decimal("3499.00"),
        "badge": "Premium Finish",
        "short_description": "A polished footwear anchor for formal and smart-casual outfits.",
        "description": "Classic brogues with a rich finish, built to elevate trousers, chinos, and festive outfits.",
        "image": "images/one.jpg",
        "gallery": ["images/one.jpg", "images/thumbs/02.jpg"],
        "sizes": ["40", "41", "42", "43", "44"],
        "highlights": ["Gift ready", "Premium look", "Formal versatility"],
    },
]


PRODUCT_MAP = {product["slug"]: product for product in PRODUCTS}


def list_products(category=None):
    if category is None:
        return PRODUCTS
    return [product for product in PRODUCTS if product["category"] == category]


def get_product(slug):
    return PRODUCT_MAP.get(slug)


def featured_products(limit=6):
    return PRODUCTS[:limit]


def related_products(product, limit=3):
    matches = [
        candidate
        for candidate in PRODUCTS
        if candidate["category"] == product["category"] and candidate["slug"] != product["slug"]
    ]
    return matches[:limit]
