from imgproxy_python.urls import UrlGenerator


def test_unsigned_url_basic():
    config = {
        'imgproxy_key': '943b421c9eb07c830af81030552c86009268de4e532ba2ee2eab8247c6da0881',
        'imgproxy_salt': '520f986b998545b4785e0defbc4f3c1203f22de2374a3d53cb7a7fe9fea309c5',
        'imgproxy_host': 'http://localhost:8000',
        'options': {
            'resize': 'fill',
            'width': 300,
            'height': 300,
            'gravity': 'no',
            'enlarge': 1,
            'extension': '.png'
        }
    }
    url = 'http://img.example.com/pretty/image.jpg'
    expected_url = '/MlF9VpgaHqcmVK3FyT9CTJhfm0rfY6JKnAtxoiAX9t0/fill/300/300/no/1/aHR0cDovL2ltZy5l/eGFtcGxlLmNvbS9w/cmV0dHkvaW1hZ2Uu/anBn.png'
    urlgen = UrlGenerator(url, config)
    assert urlgen.generate_signed_url() == expected_url