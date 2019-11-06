import urllib.request
import bs4 as bs # beautiful soup 4
import lxml


imdb_base_url = 'https://www.imdb.com'
film_rank_content = urllib.request.urlopen(imdb_base_url + '/chart/top?ref_=nv_mv_250').read()
print(film_rank_content)
film_rank_soup = bs.BeautifulSoup(film_rank_content, 'lxml')
# print(film_rank_soup)
movie_tds = film_rank_soup.findAll('td', {'class': 'titleColumn'})
print(movie_tds)
