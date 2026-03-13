# Data 15 tempat di Seattle
seattle_locations = {
    "downtown": {
        "name": "Downtown Seattle",
        "category": "district",
        "description": "Pusat kota Seattle dengan gedung pencakar langit",
        "neighbors": ["pike_place", "waterfront", "capitol_hill"]
    },
    "pike_place": {
        "name": "Pike Place Market",
        "category": "tourist_attraction",
        "description": "Pasar terkenal dengan ikan terbang",
        "neighbors": ["downtown", "waterfront"]
    },
    "space_needle": {
        "name": "Space Needle",
        "category": "landmark",
        "description": "Menara ikonik Seattle",
        "neighbors": ["seattle_center", "queen_anne"]
    },
    "seattle_center": {
        "name": "Seattle Center",
        "category": "entertainment",
        "description": "Pusat hiburan dengan Space Needle",
        "neighbors": ["space_needle", "queen_anne"]
    },
    "waterfront": {
        "name": "Waterfront Park",
        "category": "park",
        "description": "Kawasan tepi laut",
        "neighbors": ["downtown", "pike_place"]
    },
    "capitol_hill": {
        "name": "Capitol Hill",
        "category": "neighborhood",
        "description": "Area trendi dengan banyak kafe",
        "neighbors": ["downtown", "first_hill"]
    },
    "queen_anne": {
        "name": "Queen Anne",
        "category": "neighborhood",
        "description": "Area perumahan dengan pemandangan kota",
        "neighbors": ["space_needle", "seattle_center"]
    },
    "chinatown": {
        "name": "Chinatown",
        "category": "district",
        "description": "Kawasan budaya dengan restoran Asia",
        "neighbors": ["downtown", "soho"]
    },
    "university_district": {
        "name": "University District",
        "category": "neighborhood",
        "description": "Area sekitar University of Washington",
        "neighbors": ["ravenna", "wallingford"]
    },
    "fremont": {
        "name": "Fremont",
        "category": "neighborhood",
        "description": "Area unik dengan patung troll",
        "neighbors": ["ballard", "wallingford"]
    },
    "ballard": {
        "name": "Ballard",
        "category": "neighborhood",
        "description": "Area dengan restoran seafood",
        "neighbors": ["fremont"]
    },
    "wallingford": {
        "name": "Wallingford",
        "category": "neighborhood",
        "description": "Area perumahan yang tenang",
        "neighbors": ["fremont", "university_district"]
    },
    "ravenna": {
        "name": "Ravenna",
        "category": "neighborhood",
        "description": "Area dengan taman yang indah",
        "neighbors": ["university_district"]
    },
    "first_hill": {
        "name": "First Hill",
        "category": "neighborhood",
        "description": "Area dengan banyak rumah sakit",
        "neighbors": ["capitol_hill", "downtown"]
    },
    "soho": {
        "name": "Soho",
        "category": "neighborhood",
        "description": "Area perbelanjaan",
        "neighbors": ["chinatown"]
    }
}

def get_all_locations():
    return seattle_locations

def get_location(location_id):
    return seattle_locations.get(location_id)

def search_by_keyword(keyword):
    keyword = keyword.lower().strip()
    results = []
    
    for loc_id, location in seattle_locations.items():
        if (keyword in location['name'].lower() or 
            keyword in location['category'].lower() or 
            keyword in location['description'].lower()):
            results.append(loc_id)
    
    return results