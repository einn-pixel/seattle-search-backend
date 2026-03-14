# Data 15 tempat di Seattle
seattle_locations = {
    "seattle": {
        "name": "Seattle - The Emerald City",
        "category": "city",
        "description": "Kota terbesar di Washington State, AS. Pusat teknologi (Microsoft, Amazon), kopi (Starbucks), dan musik grunge (Nirvana). Dikenal dengan landmark Space Needle dan Pike Place Market.",
        "neighbors": ["bellevue", "redmond", "tacoma", "seatac_airport", "pike_place", "space_needle", "waterfront", "capitol_hill", "queen_anne"],
        
       
        "area": "217.2 km²",
        "population": "780,995 jiwa (2024)",
        "nicknames": "Emerald City, Jet City, Rain City",
        "industries": "Teknologi, Aerospace, Kopi",
        "landmarks": "Space Needle, Pike Place Market",
        "climate": "Oceanic, suhu rata-rata 11°C",
        "timezone": "Pacific Time (PST/PDT)",
        "universities": "University of Washington",
        "coordinates": "47.6062° N, 122.3321° W",
        "coffee": "Starbucks, Seattle's Best Coffee",
        "fun_facts": "Tempat lahir musik grunge",
        "founded": "1851",
        "other_nicknames": "Queen City",
        "food": "Salmon, Oyster",
        "transportation": "Light Rail, Ferries"
    },
    
    "bellevue": {
        "name": "Bellevue",
        "category": "city",
        "description": "Kota satelit di timur Seattle. Pusat teknologi dengan kantor T-Mobile.",
        "neighbors": ["seattle", "redmond"],
        "population": "151,854 jiwa",
        "area": "87.2 km²",
        "industries": "Teknologi, Ritel"
    },
    
    "redmond": {
        "name": "Redmond",
        "category": "city",
        "description": "Kota di timur Seattle, markas besar Microsoft dan Nintendo.",
        "neighbors": ["seattle", "bellevue"],
        "population": "76,104 jiwa",
        "area": "43.8 km²",
        "industries": "Teknologi (Microsoft), Gaming (Nintendo)"
    },
    
    "tacoma": {
        "name": "Tacoma",
        "category": "city",
        "description": "Kota pelabuhan di selatan Seattle. Dijuluki 'City of Destiny'.",
        "neighbors": ["seattle"],
        "population": "219,346 jiwa",
        "area": "162.2 km²",
        "industries": "Pelabuhan, Manufaktur"
    },
    
    "seatac_airport": {
        "name": "Seattle-Tacoma International Airport",
        "category": "airport",
        "description": "Bandara utama Seattle (SEA).",
        "neighbors": ["seattle", "tacoma"],
        "code": "SEA",
        "passengers": "50+ juta/tahun"
    },
    
    "pike_place": {
        "name": "Pike Place Market",
        "category": "tourist_attraction",
        "description": "Pasar terkenal dengan ikan terbang dan Starbucks pertama.",
        "neighbors": ["seattle", "waterfront"],
        "established": "1907"
    },
    
    "space_needle": {
        "name": "Space Needle",
        "category": "landmark",
        "description": "Menara ikonik Seattle, dibangun 1962.",
        "neighbors": ["seattle", "seattle_center"],
        "height": "184 meter"
    },
    
    "seattle_center": {
        "name": "Seattle Center",
        "category": "entertainment",
        "description": "Pusat hiburan dengan Space Needle dan museum.",
        "neighbors": ["space_needle", "seattle"]
    },
    
    "waterfront": {
        "name": "Waterfront Park",
        "category": "park",
        "description": "Kawasan tepi laut dengan pemandangan indah.",
        "neighbors": ["seattle", "pike_place"]
    },
    
    "capitol_hill": {
        "name": "Capitol Hill",
        "category": "neighborhood",
        "description": "Area trendi dengan banyak kafe dan bar.",
        "neighbors": ["seattle", "downtown"]
    },
    
    "queen_anne": {
        "name": "Queen Anne",
        "category": "neighborhood",
        "description": "Area perumahan dengan pemandangan kota.",
        "neighbors": ["seattle", "space_needle"]
    },
    
    "chinatown": {
        "name": "Chinatown-International District",
        "category": "district",
        "description": "Kawasan budaya dengan restoran Asia.",
        "neighbors": ["seattle", "pioneer_square"]
    },
    
    "university_district": {
        "name": "University District",
        "category": "neighborhood",
        "description": "Area sekitar University of Washington.",
        "neighbors": ["seattle", "ravenna"]
    },
    
    "fremont": {
        "name": "Fremont",
        "category": "neighborhood",
        "description": "Area unik dengan patung troll.",
        "neighbors": ["seattle", "ballard"]
    },
    
    "ballard": {
        "name": "Ballard",
        "category": "neighborhood",
        "description": "Area dengan restoran seafood.",
        "neighbors": ["seattle", "fremont"]
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
        # Cek di name
        if keyword in location['name'].lower():
            results.append(loc_id)
            continue
            
        # Cek di category
        if keyword in location['category'].lower():
            results.append(loc_id)
            continue
            
        # Cek di description
        if keyword in location['description'].lower():
            results.append(loc_id)
            continue
        
        # Cek di field lainnya
        for key, value in location.items():
            # Skip field yang bukan tempat pencarian
            if key in ['name', 'category', 'description', 'neighbors', 'coordinates']:
                continue
                
            # Kalau value string
            if isinstance(value, str) and keyword in value.lower():
                results.append(loc_id)
                break
                
            # Kalau value list
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, str) and keyword in item.lower():
                        results.append(loc_id)
                        break
                if loc_id in results:
                    break
    
    # Hapus duplikat dan return
    return list(dict.fromkeys(results))
