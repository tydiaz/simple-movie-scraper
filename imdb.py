import requests

from bs4 import BeautifulSoup


def send_request(url):
    r = requests.get(url,
                     headers={'Accept-Language': 'en-US,en;q=0.5'})

    if r.status_code == requests.codes.ok:
        return r
    return 'Cannot GET request!'


def b_soup(url, tag):
    r = send_request(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    meta = 'meta'

    if tag == meta:
        response = soup.find(meta, {'name': 'description'})

        return response['content']
    else:
        response = soup.find(tag)

    if response:
        return response.text
    return 'Invalid movie page!'


def convert_to_dict(url):
    title = b_soup(url, tag='title')
    description = b_soup(url, tag='meta')

    return {'title': title, 'description': description}


if __name__ == '__main__':
    prompt = 'Enter the url of the site:\n$ '
    user_url = input(prompt)
    imdb = r'https://www.imdb.com/title/'

    if imdb not in user_url:
        print('Invalid movie page!')
    else:
        movie_info = convert_to_dict(user_url)

        print(movie_info)
