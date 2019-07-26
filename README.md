# twitter-text-python

This is a Python port of the [twitter/twitter-text][twitter-text] libraries, fully compliant with the [official conformance test suite][conformance].


# Features

This library calculates length of a tweet message according to [the documentation from Twitter Developers](parser-doc),
so that you can validate the tweet without calling the Web API at all.
Although counting characters might seem an easy task, in actual fact it is very complicated, especially when the text contains CJK characters, URLs, or emojis.

The original [twitter-text][] libraries have "hit-highlighting" and "auto-linking" features as well,
however they are not yet supported by this Python port.


# Usage
## Installation
TBD


## Examples

```python
from twitter_text import parse_tweet, extract_emojis_with_indices, extract_urls_with_indices

text = 'english text 日本語 😷 https://example.com'

assert parse_tweet(text).asdict() == {
    'weightedLength': 46,
    'valid': True,
    'permillage': 164,
    'validRangeStart': 0,
    'validRangeEnd': 38,
    'displayRangeStart': 0,
    'displayRangeEnd': 38
}

assert extract_urls_with_indices(text) == [{
    'url': 'https://example.com',
    'indices': [19, 38]
}]

assert extract_emojis_with_indices(text) == [{
    'emoji': '😷',
    'indices': [17, 18]
}]
```


# Related Links
- [twitter/twitter-text][twitter-text]: The original, official _twitter-text_ libraries for Java, Ruby, JavaScript and Objective-C
- [twitter-text Parser -- Twitter Developers][parser-doc]: A brief overview of the _twitter-text_ libraries
- [Counting characters -- Twitter Developers][counting-doc]: An introduction to how to count characters in Twitter texts
- [edmondburnett/twitter-text-python][twitter-text-python]: Another python port of _twitter-text_, which is not compliant with the [official conformance test suite][conformance] 


[twitter-text]:https://github.com/twitter/twitter-text
[twitter-text-python]:https://github.com/edmondburnett/twitter-text-python
[conformance]:https://github.com/twitter/twitter-text/tree/master/conformance
[search-api]:https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets.html
[counting-doc]:https://developer.twitter.com/en/docs/basics/counting-characters.html
[parser-doc]:https://developer.twitter.com/en/docs/developer-utilities/twitter-text
