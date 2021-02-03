# imgprofi
A tiny library to simplify generation of imgproxy urls

#usage
For example you want to simply resize your image to other height and width using imgproxy. To get proper imgproxy url you need the following
```
config = {
        'imgproxy_key': '943b421c9eb07c830af81030552c86009268de4e532ba2ee2eab8247c6da0881',
        'imgproxy_salt': '520f986b998545b4785e0defbc4f3c1203f22de2374a3d53cb7a7fe9fea309c5',
        'imgproxy_host': 'http://localhost:8000',
        'options': {
            'resize': 'fill',
            'width': 300,
            'height': 300,
        }
    }
    url = 'http://img.example.com/pretty/image.jpg'
    urlgen = UrlGenerator(url, config)
    print(urlgen.get_full_signed_url())
```
You will get a ready-to-go imgproxy link
```
http://localhost:8000/6cy4IRuQ1nQW8qGVmNvPdynjmkuwUEx-XhGw_C_kQmA/fill/300/300/ce/0/aHR0cDovL2ltZy5l/eGFtcGxlLmNvbS9w/cmV0dHkvaW1hZ2Uu/anBn
```

#warning

If you want to have generated link working you need to have imgproxy instance up and running on ```config['imgproxy_host']```, in our example it is ```http://localhost:8000```