twitter-text-python
===================

.. image:: https://readthedocs.org/projects/twitter-text-python/badge/?version=latest
    :target: https://twitter-text-python.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://travis-ci.com/swen128/twitter-text-python.svg?branch=master
    :target: https://travis-ci.com/swen128/twitter-text-python

This is a Python port of the `twitter/twitter-text`_ libraries, fully compliant with the `official conformance test suite`_.


Features
========

This library calculates length of a tweet message according to `the documentation from Twitter Developers`_,
so that you can validate the tweet without calling the Web API at all.
Although counting characters might seem an easy task, in actual fact it is very complicated, especially when the text contains CJK characters, URLs, or emojis.

The original twitter-text libraries have *hit-highlighting* and *auto-linking* features as well,
however they are not yet supported by this Python port.


Usage
=====

Installation
------------

.. code-block:: console

    $ pip install twitter-text-parser


Examples
--------

See `the API reference <https://twitter-text-python.readthedocs.io/#module-twitter_text>`_ for more details.

.. code-block:: python

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


Related Links
=============

- `twitter/twitter-text`_: The original, official twitter-text implementations for Java, Ruby, JavaScript and Objective-C
- `twitter-text Parser -- Twitter Developers`_: A brief overview of the twitter-text libraries
- `Counting characters -- Twitter Developers`_: An introduction to how to count characters in Twitter texts
- `edmondburnett/twitter-text-python`_: Another python port of twitter-text, which is not compliant with the `official conformance test suite`_


.. _twitter/twitter-text: https://github.com/twitter/twitter-text
.. _edmondburnett/twitter-text-python: https://github.com/edmondburnett/twitter-text-python
.. _official conformance test suite: https://github.com/twitter/twitter-text/tree/master/conformance
.. _search-api: https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets.html
.. _Counting characters -- Twitter Developers: https://developer.twitter.com/en/docs/basics/counting-characters.html
.. _the documentation from Twitter Developers: https://developer.twitter.com/en/docs/developer-utilities/twitter-text
.. _twitter-text Parser -- Twitter Developers: https://developer.twitter.com/en/docs/developer-utilities/twitter-text
