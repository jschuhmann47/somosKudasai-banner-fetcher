import pytest
import urlFetcher


def test_urlValidaDaFotoValida():
    assert urlFetcher.urlFoto("https://somoskudasai.com/noticias/cultura-otaku/aseguran-que-la-franquicia-de-the-idolmaster-esta-en-decadencia/") == "https://somoskudasai.com/wp-content/uploads/2021/10/image-8.png"

def test_urlDelSitioPeroNoValida():
    assert urlFetcher.urlFoto("https://somoskudasai.com/") == "x"

def test_urlNoValida():
    assert urlFetcher.urlFoto("https://google.com/") == "x"
    
