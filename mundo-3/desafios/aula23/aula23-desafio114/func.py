import requests


def checkSite(url):
    try:
        requests.get(url)
        print(f'\033[32mO site {url} está acessível.\033[m')    
        
    except requests.exceptions.ConnectionError:
        print(f'\033[31mO site {url} está inacessível.\033[m')    

    except requests.exceptions.MissingSchema:
        print(f'\033[33mVerifique a URL e tente novamente. (Sem http:// ou https://)\033[m')
    
    finally:
        print('-' * 60)
