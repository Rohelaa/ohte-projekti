COUNTRIES = {
    "Brazil": {
        "country_name": "Brazil",
        "2018": 209469333
    },
    "China": {
        "country_name": "China",
        "2018": 1392730000
    },
    "United Kingdom": {
        "country_name": "United Kingdom",
        "2018": 66460344
    }
}


def read():
    return [COUNTRIES[key] for key in sorted(COUNTRIES.keys())]
