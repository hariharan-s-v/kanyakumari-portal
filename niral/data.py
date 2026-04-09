"""
data.py — All static data for Kanyakumari Tourism Portal
Swap BOOKINGS with SQLite/PostgreSQL in production.
"""

ATTRACTIONS = [
    {
        "id": 1, "name": "Vivekananda Rock Memorial",
        "category": "Heritage & Spiritual",
        "description": "A magnificent memorial on twin sea-rocks dedicated to Swami Vivekananda, where he attained enlightenment. Ferries depart from the main jetty every 15 minutes.",
        "rating": 4.8, "entry_fee": 20, "timings": "8:00 AM – 4:00 PM",
        "best_season": "Oct – Mar", "icon": "🏛️",
        "tags": ["heritage", "spiritual", "sea", "photography"],
        "image": "/static/images/att_1.jpg",
        "image_pos": "center top",
        "lat": 8.0772, "lng": 77.5539
    },
    {
        "id": 2, "name": "Thiruvalluvar Statue",
        "category": "Monument",
        "description": "A 133-foot stone statue of Tamil poet-philosopher Thiruvalluvar rising from the sea — a symbol of Tamil culture and timeless wisdom.",
        "rating": 4.7, "entry_fee": 30, "timings": "8:00 AM – 4:00 PM",
        "best_season": "Oct – Mar", "icon": "🗿",
        "tags": ["monument", "cultural", "photography"],
        "image": "/static/images/att_2.jpg",
        "image_pos": "center top",
        "lat": 8.0764, "lng": 77.5531
    },
    {
        "id": 3, "name": "Tri-Sea Sunrise Point",
        "category": "Nature",
        "description": "The southernmost tip of India — where the Bay of Bengal, Arabian Sea & Indian Ocean converge. The sunrise here is unlike anywhere else on Earth.",
        "rating": 4.9, "entry_fee": 0, "timings": "Open 24 hours",
        "best_season": "Oct – Feb", "icon": "🌅",
        "tags": ["nature", "sunrise", "beach", "photography"],
        "image": "/static/images/att_3.jpg",
        "image_pos": "center",
        "lat": 8.0883, "lng": 77.5385
    },
    {
        "id": 4, "name": "Mathur Hanging Bridge",
        "category": "Engineering & Nature",
        "description": "Asia's longest aqueduct — 1,182 metres at 115 feet height — draped in lush greenery with tribal settlements nestled in the valley below.",
        "rating": 4.5, "entry_fee": 0, "timings": "6:00 AM – 6:00 PM",
        "best_season": "Jul – Jan", "icon": "🌉",
        "tags": ["engineering", "nature", "trekking", "tribal"],
        "image": "/static/images/att_4.jpg",
        "image_pos": "center",
        "lat": 8.2494, "lng": 77.3244
    },
    {
        "id": 5, "name": "Padmanabhapuram Palace",
        "category": "Heritage",
        "description": "A 16th-century wooden palace of the Travancore Kingdom with exquisite Kerala architecture, royal artefacts, and rare paintings — a UNESCO-nominated site.",
        "rating": 4.6, "entry_fee": 30, "timings": "9:00 AM – 5:00 PM (Closed Mon)",
        "best_season": "Oct – Mar", "icon": "🏰",
        "tags": ["heritage", "history", "architecture"],
        "image": "/static/images/att_5.jpg",
        "image_pos": "center",
        "lat": 8.2529, "lng": 77.3247
    },
    {
        "id": 6, "name": "Pechiparai Reservoir",
        "category": "Nature & Wildlife",
        "description": "Serene reservoir ringed by forest and bordering the Kalakkad Mundanthurai Tiger Reserve. Spot mugger crocodiles, hornbills & rare butterflies.",
        "rating": 4.5, "entry_fee": 10, "timings": "8:00 AM – 5:00 PM",
        "best_season": "Jul – Jan", "icon": "💧",
        "tags": ["nature", "boating", "wildlife", "reservoir"],
        "image": None,
        "lat": 8.2816, "lng": 77.2543
    },
    {
        "id": 7, "name": "Chitharal Jain Rock Caves",
        "category": "Tribal & Heritage",
        "description": "9th–11th century rock-cut Jain sculptures hidden in Western Ghats forest. The surrounding Kani villa community still practices ancient forest conservation.",
        "rating": 4.3, "entry_fee": 10, "timings": "8:00 AM – 5:00 PM",
        "best_season": "Oct – Feb", "icon": "⛰️",
        "tags": ["tribal", "heritage", "trekking", "caves"],
        "image": None,
        "lat": 8.3201, "lng": 77.2801
    },
    {
        "id": 8, "name": "Muttom Beach & Lighthouse",
        "category": "Nature",
        "description": "A tranquil rocky fishing village with an active lighthouse. Less touristy, excellent for fresh seafood, spectacular sunset silhouettes & sea fishing.",
        "rating": 4.4, "entry_fee": 0, "timings": "Open 24 hours",
        "best_season": "Oct – Feb", "icon": "🏖️",
        "tags": ["beach", "fishing", "peaceful", "seafood", "lighthouse"],
        "image": None,
        "lat": 8.1651, "lng": 77.3198
    },
]

ACCOMMODATIONS = [
    {
        "id": 1, "name": "Cape Hotel (TTDC)",
        "type": "Government Hotel", "stars": 4,
        "price": 3200, "icon": "🏨",
        "description": "Prime beachfront property by Tamil Nadu Tourism. Sea-view rooms, multi-cuisine restaurant, and reliable government-assured quality.",
        "amenities": ["Sea View", "AC", "Restaurant", "WiFi", "24hr Reception", "Parking"],
        "contact": "+91-4652-246271", "available": 9,
        "villa": False,
        "lat": 8.0892, "lng": 77.5410,
        "booking_url": "https://www.ttdconline.com/hotel_booking.aspx",
        "booking_platform": "TTDC Official Website",
        "address": "Beach Road, Kanyakumari, Tamil Nadu 629702"
    },
    {
        "id": 2, "name": "Kani Forest Villa",
        "type": "Villa", "stars": 3,
        "price": 1400, "icon": "🏡",
        "description": "Authentic villa run by the Kani community. Organic forest meals, medicinal herb walks, and cultural storytelling evenings. 100% revenue to the local families.",
        "amenities": ["Organic Meals", "Forest Trek", "Cultural Shows", "Herbal Therapy", "WiFi"],
        "contact": "+91-9876543210", "available": 4,
        "villa": True,
        "lat": 8.3012, "lng": 77.2644,
        "booking_url": "https://incredibleindia.org/content/incredible-india/en/destinations/tamil-nadu.html",
        "booking_platform": "Incredible India — Official Tourism",
        "address": "Kalakkad Forest Foothills, Kanyakumari District, Tamil Nadu"
    },
    {
        "id": 3, "name": "Seashore Resort",
        "type": "Resort", "stars": 4,
        "price": 4500, "icon": "🌊",
        "description": "Modern resort with infinity pool overlooking the confluence of three seas. Rooftop dining, yoga deck, and sunset boat rides.",
        "amenities": ["Infinity Pool", "Yoga", "Spa", "Sea View", "AC", "Restaurant", "WiFi"],
        "contact": "+91-4652-246789", "available": 5,
        "villa": False,
        "lat": 8.0876, "lng": 77.5398,
        "booking_url": "https://www.makemytrip.com/hotels/hotel-listing/?city=CTKYK",
        "booking_platform": "MakeMyTrip",
        "address": "Kovalam Road, Kanyakumari, Tamil Nadu 629702"
    },
    {
        "id": 4, "name": "Forest View Cottages",
        "type": "Eco Cottage", "stars": 3,
        "price": 1900, "icon": "🛖",
        "description": "Peaceful wood cottages near Pechiparai Reservoir. Guided birdwatching, bonfire evenings, and fresh forest produce breakfasts.",
        "amenities": ["Birdwatching", "Bonfire", "Nature Trails", "Parking", "Organic Breakfast"],
        "contact": "+91-9123456789", "available": 6,
        "villa": False,
        "lat": 8.2816, "lng": 77.2543,
        "booking_url": "https://www.goibibo.com/hotels/hotels-in-kanyakumari/",
        "booking_platform": "Goibibo",
        "address": "Pechiparai Reservoir Road, Kanyakumari District, Tamil Nadu"
    },
    {
        "id": 5, "name": "Bamboo Village Villa",
        "type": "Villa", "stars": 3,
        "price": 2400, "icon": "🎋",
        "description": "Bamboo-constructed villas built and managed by local Muduvar families. 80% of revenue supports the community's education and healthcare fund.",
        "amenities": ["Local Cuisine", "Folk Dance", "Bamboo Crafts", "Herbal Walks", "Storytelling"],
        "contact": "+91-9988776655", "available": 5,
        "villa": True,
        "lat": 8.2650, "lng": 77.2710,
        "booking_url": "https://www.responsibletravel.com/holidays/india/travel-guide/tamil-nadu",
        "booking_platform": "Responsible Travel",
        "address": "Muduvar Settlement, Western Ghats, Kanyakumari District"
    },
    {
        "id": 6, "name": "Hotel Saravana",
        "type": "Budget Hotel", "stars": 2,
        "price": 950, "icon": "🏩",
        "description": "Clean, central budget hotel near the main beach. Popular with pilgrims and backpackers. Excellent South Indian breakfast.",
        "amenities": ["AC Rooms", "Restaurant", "WiFi", "Parking", "Laundry"],
        "contact": "+91-4652-246100", "available": 14,
        "villa": False,
        "lat": 8.0886, "lng": 77.5392,
        "booking_url": "https://www.booking.com/searchresults.html?ss=Kanyakumari",
        "booking_platform": "Booking.com",
        "address": "Main Road, Near Bus Stand, Kanyakumari, Tamil Nadu 629702"
    },
]

TRAVEL_TIPS = [
    {"icon": "🌡️", "title": "Best Season", "tip": "October–March is ideal (22–32°C). January's Pongal festival brings beach celebrations. Monsoon (Jun–Sep) is lush but rough seas close ferry services."},
    {"icon": "🚌", "title": "Getting There", "tip": "Train: Kanyakumari station (KZT) connects Chennai, Mumbai & Delhi. Flight: Trivandrum airport (TRV) is 87 km away. Regular state buses from Madurai & Trivandrum."},
    {"icon": "⛴️", "title": "Ferry Schedule", "tip": "Ferries to Vivekananda Rock run 8 AM–4 PM, returning till 5 PM. Book tickets at the jetty counter (₹50 return). Avoid weekends for shorter queues."},
    {"icon": "🌿", "title": "Tribal Etiquette", "tip": "Always seek permission before photographing tribal members. Purchase crafts directly from artisans — never through middlemen. Respect sacred forest areas."},
    {"icon": "📸", "title": "Photo Spots", "tip": "Sunrise at 5:30 AM from the main beach. Sunset from Gandhi Memorial Mandapam. Night-time illuminated view of Vivekananda Rock from the jetty."},
    {"icon": "🍛", "title": "Local Cuisine", "tip": "Must-try: Kanyakumari fish curry, kothu parotta, fresh lobster at beach stalls. Visit the morning fish auction market near the jetty for an authentic experience."},
]
