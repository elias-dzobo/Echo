import requests




def get_fact(url = 'https://uselessfacts.jsph.pl/api/v2/facts/random?language=en'):
    
    response = requests.get(url)

    data = response.json()

    return data['text']


def get_joke(url = 'https://api.chucknorris.io/jokes/random'):
    response = requests.get(url)

    data = response.json()
    
    return data['value']


