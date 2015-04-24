import MySQLdb
from bs4 import BeautifulSoup
import urllib.request
import csv

def pubGrid():
    try:
        
        gameFile = urllib.request.urlopen('http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=B')
        gameHtml = gameFile.read()
        gameFile.close()
        soup = BeautifulSoup(gameHtml)
        gameAll = soup.find_all('div',class_='releaseDate grid_3 omega' )
       
        for gamesAll in gameAll:
            if gamesAll.string == None:
                pass

            else:
                print(gamesAll.string.strip())
    except Exception as e:
        print(e)
    
pubGrid()