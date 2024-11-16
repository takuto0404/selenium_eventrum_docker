from dotenv import load_dotenv
import os

class ApiDataManager:
    APIKey = None
    
    # 国コードの辞書
    CountryDic = {
        "ArabEmirates": "ae",
        "Argentina": "ar",
        "Austria": "at",
        "Australia": "au",
        "Belgium": "be",
        "Bulgaria": "bg",
        "Brazil": "br",
        "Canada": "ca",
        "Switzerland": "ch",
        "China": "cn",
        "Colombia": "co",
        "Cuba": "cu",
        "Czechia": "cz",
        "Germany": "de",
        "Egypt": "eg",
        "France": "fr",
        "UnitedKingdom": "gb",
        "Greece": "gr",
        "HongKong": "hk",
        "Hungary": "hu",
        "Indonesia": "id",
        "Ireland": "ie",
        "Israel": "il",
        "India": "in",
        "Italy": "it",
        "Japan": "jp",
        "Korea": "kr",
        "Lithuania": "lt",
        "Latvia": "lv",
        "Morocco": "ma",
        "Mexico": "mx",
        "Malaysia": "my",
        "Nigeria": "ng",
        "Netherlands": "nl",
        "Norway": "no",
        "NewZealand": "nz",
        "Philippines": "ph",
        "Poland": "pl",
        "Portugal": "pt",
        "Romania": "ro",
        "Serbia": "rs",
        "Russia": "ru",
        "SaudiArabia": "sa",
        "Sweden": "se",
        "Singapore": "sg",
        "Slovenia": "si",
        "Slovakia": "sk",
        "Thailand": "th",
        "Turkey": "tr",
        "Taiwan": "tw",
        "Ukraine": "ua",
        "UnitedStates": "us",
        "Venezuela": "ve",
        "SouthAfrica": "za"
    }

    GenreDic = {
        "Business": "business",
        "Entertainment": "entertainment",
        "Health": "health",
        "Science": "science",
        "Sports": "sports",
        "Technology": "technology"
    }

    @classmethod
    async def initialize_async(cls):
        env_api_key = os.getenv("API_KEY")
        if env_api_key:
            cls.APIKey = env_api_key

        if cls.APIKey is None:
            raise ValueError("API_KEY not set from environment")

    @classmethod
    def get_country_code(cls, country_type="UnitedStates"):
        return cls.CountryDic.get(country_type, "")

    @classmethod
    def get_genre_code(cls, genre_type):
        return cls.GenreDic.get(genre_type, "")
