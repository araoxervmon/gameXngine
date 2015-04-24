import MySQLdb
from bs4 import BeautifulSoup
import urllib.request
import csv

def getDataFromWebPage():
    #fetchdata()
    #print(fetchdata())
    #test = fetchdata()[0]
    #print(test[0])
    #idSplit = []
    gameFile = urllib.request.urlopen('http://www.neoseeker.com/xbox360/action/')
    gameHtml = gameFile.read()
    gameFile.close()
    soup = BeautifulSoup(gameHtml)
    gameAll = soup.find_all('a',class_='popular' )
    #print(gameAll)
    for gameAll in gameAll:
        print(gameAll.string)
    #for gamesAll in gameAll:
        
# #                 print(id)
#                 #print(str(gameRate))
#     for i in test:
#         #print(i.split(',')[0][1:3])
#         idSplit.append(i.split(',')[0][1:3])
#         
#         for s in range(1,10):
#             print(s)
#             print(i.split(',')[0][1:3]) 
    
    #return idSplit
#    try:
#        print(fetchdata())
#         gameFile = urllib.request.urlopen('http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=B')
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all('div',class_='grid_3' )
#        
#         for gamesAll in gameAll:
#             if gamesAll.string == None:
#                 pass
#             elif gamesAll.string.strip() == '505 Games':
#                 pass
#             elif gamesAll.string.strip() == '8bits Fanatics':
#                 pass
#             elif gamesAll.string.strip().split(',')[0] == 'NR' or gamesAll.string.strip().split(',')[0][0:1] == '0'or gamesAll.string.strip().split(',')[0][0:1] == '1' or gamesAll.string.strip().split(',')[0][0:1] == '2' or gamesAll.string.strip().split(',')[0][0:1] == '3' or gamesAll.string.strip().split(',')[0][0:1] == '4' or gamesAll.string.strip().split(',')[0][0:1] == '5' or gamesAll.string.strip().split(',')[0][0:1] == '6' or gamesAll.string.strip().split(',')[0][0:1] == '7' or gamesAll.string.strip().split(',')[0][0:1] == '8' or gamesAll.string.strip().split(',')[0][0:1] == '9':
#                 gameRate = gamesAll.string.strip()
#                 print(gameRate)
# #                 print(id)
#                 #print(str(gameRate))
# 
#                 #queryRatings = "UPDATE gameList SET ratings = '"+str(gameRate)+"' WHERE id = '"+str(row[0][0])+"' AND gameName = '"+str(row[0][1])+"'"
#                 #print(queryRatings)
#                 #cursor.execute (queryRatings) 
#                 #rowRatings = cursor.fetchall()
#             else:
#                 pass
#    except Exception as e:
#       print(e)


        
getDataFromWebPage()