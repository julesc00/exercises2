"""
Nesting
"""

import pprint

pp = pprint.PrettyPrinter(indent=2)

travel_log = [
    {
        "Country": {
            "France": {
                "Cities_visited": ["Paris", "Marseille", "Dijon"],
                "total_visits": 12
            },
            "Germany": {
                "Cities_visited": ["Berlin", "Frankfurt", "Hamburg"],
                "total_visits": 5
            }
        },
    }
]


pp.pprint(travel_log[0]["Country"]["France"]["Cities_visited"][0])


# Nesting a dict in a list

