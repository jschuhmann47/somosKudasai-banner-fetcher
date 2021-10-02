import requests
import webbrowser
from bs4 import BeautifulSoup

def urlFoto(urlIngresada):
    if ("https://somoskudasai.com/noticias" in urlIngresada or "https://somoskudasai.com/resenas" in urlIngresada):
        codigoHtml = requests.get(urlIngresada)
        INICIO_URL=176

        htmlSopa = BeautifulSoup(codigoHtml.text, 'html.parser')
        claseFigura = str(htmlSopa.findAll('figure', {'class':'im black-bg z-1'}))
        finUrl=claseFigura[INICIO_URL:].find('"',0)+INICIO_URL
        return claseFigura[INICIO_URL:finUrl]
    else:
        print("URL invalida")
        return "x"

def main():
    urlIngresada=input("Ingrese URL: ")
    url=urlFoto(urlIngresada)
    if(not(url=="x")):
        webbrowser.open(url)

if __name__ == "__main__":
    main()