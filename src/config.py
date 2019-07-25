config = {
    "version1": {
        "version": 1,
        "max_weighted_tweet_length": 140,
        "scale": 1,
        "default_weight": 1,
        "transformed_url_length": 23,
        "ranges": []
    },
    "version2": {
        "version": 2,
        "max_weighted_tweet_length": 280,
        "scale": 100,
        "default_weight": 200,
        "transformed_url_length": 23,
        "ranges": [
            {
                "start": 0,
                "end": 4351,
                "weight": 100
            },
            {
                "start": 8192,
                "end": 8205,
                "weight": 100
            },
            {
                "start": 8208,
                "end": 8223,
                "weight": 100
            },
            {
                "start": 8242,
                "end": 8247,
                "weight": 100
            }
        ]
    },
    "version3": {
        "version": 3,
        "max_weighted_tweet_length": 280,
        "scale": 100,
        "default_weight": 200,
        "emoji_parsing_enabled": True,
        "transformed_url_length": 23,
        "ranges": [
            {
                "start": 0,
                "end": 4351,
                "weight": 100
            },
            {
                "start": 8192,
                "end": 8205,
                "weight": 100
            },
            {
                "start": 8208,
                "end": 8223,
                "weight": 100
            },
            {
                "start": 8242,
                "end": 8247,
                "weight": 100
            }
        ]
    },
    "defaults": {
        "version": 3,
        "max_weighted_tweet_length": 280,
        "scale": 100,
        "default_weight": 200,
        "emoji_parsing_enabled": True,
        "transformed_url_length": 23,
        "ranges": [
            {
                "start": 0,
                "end": 4351,
                "weight": 100
            },
            {
                "start": 8192,
                "end": 8205,
                "weight": 100
            },
            {
                "start": 8208,
                "end": 8223,
                "weight": 100
            },
            {
                "start": 8242,
                "end": 8247,
                "weight": 100
            }
        ]
    }
}
