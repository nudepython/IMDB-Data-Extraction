import requests
from bs4 import BeautifulSoup

imdburl="https://www.imdb.com/chart/top"

r=requests.get(imdburl)

soup=BeautifulSoup(r.content, "html.parser")

data=soup.find_all("table",{"class":"chart full-width"})

movie_table=(data[0].contents)[len(data[0].contents)-2]

movie_table= movie_table.find_all("tr")
imdb = open("imdb.txt", "w")
for movie in movie_table:
  movie_header=movie.find_all("td",{"class":"titleColumn"})
  movie_name=movie_header[0].text
  movie_name=movie_name.replace("\n","")
  movie_point=movie.find_all("td",{"class":"ratingColumn imdbRating"})
  movie_rayting=movie_point[0].text
  movie_rayting=movie_rayting.replace("\n","")
  imdb.write(movie_name+"-------"+movie_rayting+"\n")

imdb.close()




  
