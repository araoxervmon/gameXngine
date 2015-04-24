#scipt for fectching "grid_3" tag from webpage
import MySQLdb
from bs4 import BeautifulSoup
import urllib.request
import csv

def getDataFromWebPage():
    try:
        gameFile = urllib.request.urlopen('http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=B')
        gameHtml = gameFile.read()
        gameFile.close()
        soup = BeautifulSoup(gameHtml)
        gameAll = soup.find_all('div',class_='grid_3' )
       
        for gamesAll in gameAll:
            if gamesAll.string == None:
                pass
            elif gamesAll.string.strip() == '505 Games':
                pass
            elif gamesAll.string.strip() == '8bits Fanatics':
                pass
            elif gamesAll.string.strip().split(',')[0] == 'NR' or gamesAll.string.strip().split(',')[0][0:1] == '0'or gamesAll.string.strip().split(',')[0][0:1] == '1' or gamesAll.string.strip().split(',')[0][0:1] == '2' or gamesAll.string.strip().split(',')[0][0:1] == '3' or gamesAll.string.strip().split(',')[0][0:1] == '4' or gamesAll.string.strip().split(',')[0][0:1] == '5' or gamesAll.string.strip().split(',')[0][0:1] == '6' or gamesAll.string.strip().split(',')[0][0:1] == '7' or gamesAll.string.strip().split(',')[0][0:1] == '8' or gamesAll.string.strip().split(',')[0][0:1] == '9':
                gameRate = gamesAll.string.strip()
                print(gameRate)

            else:
                pass
    except Exception as e:
        print(e)

getDataFromWebPage()