from decimal import Decimal


CATEGORY_DETAILS = {
    "residential": {
        "title": "Home and Farm Automation",
        "eyebrow": "Residential",
        "description": "Smart water tank controllers and monitoring kits for homes, villas, borewells, and farm storage tanks.",
        "hero_image": "images/iot-residential.svg",
        "accent": "aqua",
    },
    "commercial": {
        "title": "Apartment and Site Systems",
        "eyebrow": "Commercial",
        "description": "Multi-tank automation panels and remote dashboards for apartments, schools, hotels, hostels, and industrial sites.",
        "hero_image": "images/iot-commercial.svg",
        "accent": "indigo",
    },
}


PRODUCTS = [
    {
        "slug": "smart-overflow-guard-mini",
        "name": "Smart Overflow Guard Mini",
        "category": "residential",
        "product_type": "Starter Controller",
        "price": Decimal("3499.00"),
        "compare_at_price": Decimal("4299.00"),
        "badge": "Popular Choice",
        "short_description": "Automatic overflow cut-off and dry-run protection for one overhead tank and one pump.",
        "description": "An affordable entry model for homes that want to stop daily tank overflow, avoid pump dry-run, and reduce manual switching.",
        "image": "images/controller.svg",
        "gallery": ["images/controller.svg", "images/iot-residential.svg"],
        "options": ["Single tank", "Single pump", "Manual override"],
        "highlights": [
            "Stops motor when the tank reaches full level",
            "Protects the pump during dry-run conditions",
            "Ideal for homes, terraces, and rental properties",
        ],
    },
    {
        "slug": "wifi-water-level-monitor",
        "name": "Wi-Fi Water Level Monitor",
        "category": "residential",
        "product_type": "Monitoring Kit",
        "price": Decimal("5499.00"),
        "compare_at_price": Decimal("6499.00"),
        "badge": "App Enabled",
        "short_description": "Check tank level, pump status, and refill history from your phone.",
        "description": "A connected monitoring kit for customers who want live tank visibility, low-level alerts, and better control over daily water usage.",
        "image": "images/monitor.svg",
        "gallery": ["images/monitor.svg", "images/iot-residential.svg"],
        "options": ["Wi-Fi ready", "Mobile alerts", "Level history"],
        "highlights": [
            "Shows live tank status on a simple dashboard",
            "Sends alerts for low level and full tank events",
            "Useful for busy households and remote property owners",
        ],
    },
    {
        "slug": "dual-tank-auto-controller",
        "name": "Dual Tank Auto Controller",
        "category": "residential",
        "product_type": "Advanced Controller",
        "price": Decimal("6899.00"),
        "compare_at_price": Decimal("7999.00"),
        "badge": "Best Seller",
        "short_description": "Automates sump-to-overhead transfer with smarter level sensing and pump control.",
        "description": "Designed for homes and villas with separate sump and overhead tanks, this controller reduces overflow, missed refill cycles, and unnecessary pump running.",
        "image": "images/pump-kit.svg",
        "gallery": ["images/pump-kit.svg", "images/controller.svg"],
        "options": ["Sump + overhead", "Dual sensing", "Dry-run safety"],
        "highlights": [
            "Handles two-tank logic for cleaner pump automation",
            "Reduces manual motor checks every day",
            "Good fit for villas, duplex homes, and farms",
        ],
    },
    {
        "slug": "borewell-pump-protection-kit",
        "name": "Borewell Pump Protection Kit",
        "category": "residential",
        "product_type": "Pump Safety Kit",
        "price": Decimal("7999.00"),
        "compare_at_price": Decimal("9199.00"),
        "badge": "Farm Ready",
        "short_description": "Extra pump safety for borewell and farm installations where dry-run damage is costly.",
        "description": "Built for borewell-based water supply, this kit focuses on pump protection, low-water detection, and reliable auto-stop behavior.",
        "image": "images/pump-kit.svg",
        "gallery": ["images/pump-kit.svg", "images/iot-residential.svg"],
        "options": ["Borewell use", "Pump safety", "Outdoor suitable"],
        "highlights": [
            "Prevents repeated dry-run stress on pumps",
            "Useful for homes, farms, and rural installations",
            "Helps reduce repair and replacement cost over time",
        ],
    },
    {
        "slug": "apartment-tank-automation-panel",
        "name": "Apartment Tank Automation Panel",
        "category": "commercial",
        "product_type": "Panel System",
        "price": Decimal("18999.00"),
        "compare_at_price": Decimal("21999.00"),
        "badge": "Site Favourite",
        "short_description": "Centralized controller for apartment complexes that manage sump, terrace tanks, and pumps together.",
        "description": "A commercial-grade panel for apartment buildings that need dependable pump sequencing, overflow prevention, and cleaner water-level management.",
        "image": "images/panel.svg",
        "gallery": ["images/panel.svg", "images/iot-commercial.svg"],
        "options": ["Multi tank", "Panel mount", "Operator friendly"],
        "highlights": [
            "Designed for apartments, housing societies, and gated communities",
            "Supports centralized operation and maintenance teams",
            "Improves daily water handling for shared buildings",
        ],
    },
    {
        "slug": "school-hostel-monitoring-kit",
        "name": "School and Hostel Monitoring Kit",
        "category": "commercial",
        "product_type": "Institution Kit",
        "price": Decimal("14999.00"),
        "compare_at_price": Decimal("17499.00"),
        "badge": "Remote Monitoring",
        "short_description": "Track multiple tanks and get alerts before students, staff, or guests face water shortage.",
        "description": "A monitoring-first package made for hostels, schools, and institutions that need better visibility into daily tank usage and refill planning.",
        "image": "images/gateway.svg",
        "gallery": ["images/gateway.svg", "images/iot-commercial.svg"],
        "options": ["Low-level alerts", "Multiple tanks", "Manager dashboard"],
        "highlights": [
            "Gives staff better visibility into tank status",
            "Helps reduce emergency motor runs and water shortage complaints",
            "Suitable for hostels, schools, and training centers",
        ],
    },
    {
        "slug": "industrial-sump-gateway",
        "name": "Industrial Sump Gateway",
        "category": "commercial",
        "product_type": "Telemetry Gateway",
        "price": Decimal("22999.00"),
        "compare_at_price": Decimal("25999.00"),
        "badge": "Cloud Ready",
        "short_description": "Remote status visibility for larger sump, pump, and storage setups.",
        "description": "A stronger monitoring unit for factories, workshops, and bigger sites that want cloud-linked tank telemetry and operational visibility.",
        "image": "images/gateway.svg",
        "gallery": ["images/gateway.svg", "images/panel.svg"],
        "options": ["Site telemetry", "Cloud data", "Alert escalation"],
        "highlights": [
            "Built for higher-demand and larger storage environments",
            "Supports maintenance decisions with better data visibility",
            "Useful for industrial campuses and utility rooms",
        ],
    },
    {
        "slug": "installation-support-plan",
        "name": "Installation and Support Plan",
        "category": "commercial",
        "product_type": "Service Add-on",
        "price": Decimal("3999.00"),
        "compare_at_price": Decimal("4999.00"),
        "badge": "Recommended",
        "short_description": "Add installation guidance, commissioning help, and post-purchase support to your order.",
        "description": "A support add-on for buyers who want faster setup coordination, wiring guidance, and onboarding after delivery.",
        "image": "images/support.svg",
        "gallery": ["images/support.svg", "images/panel.svg"],
        "options": ["Setup help", "Call support", "Commissioning guidance"],
        "highlights": [
            "Ideal for first-time automation buyers",
            "Useful when your electrician needs product guidance",
            "Helps shorten the time from delivery to successful installation",
        ],
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
