
from bs4 import BeautifulSoup
import urllib.request
import csv
import MySQLdb

def fecthData():
    
    gamePageLinkA = 'http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=A'
    gamePageLinkB = 'http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=B'
    gamePageLinkC = 'http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=C'
    gamePageLinkD = 'http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=D'
    gamePageLinkE = 'http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=E'
    gamePageLinkF = 'http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=F'
    gamePageLinkG = 'http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=G'
    gamePageLinkH = 'http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=H'
    gamePageLinkI = 'http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=I'
    gamePageLinkJ = 'http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=J'
    gamePageLinkK = 'http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=K'
    gamePageLinkL = 'http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=L'
    gamePageLinkM = 'http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=M'
    gamePageLinkN = 'http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=N'
    gamePageLinkO = 'http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=O'
    gamePageLinkP = 'http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=P'
    gamePageLinkQ = 'http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=Q'
    gamePageLinkR = 'http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=R'
    gamePageLinkS = 'http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=S'
    gamePageLinkT = 'http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=T'
    gamePageLinkU = 'http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=U'
    gamePageLinkV = 'http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=V'
    gamePageLinkW = 'http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=W'
    gamePageLinkX = 'http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=X'
    gamePageLinkY = 'http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=Y'
    gamePageLinkZ = 'http://www.ign.com/games/xbox-360?sortBy=title&sortOrder=asc&letter=Z'
    if gamePageLinkB == gamePageLinkB:
        gameFile = urllib.request.urlopen(gamePageLinkB)
        gameHtml = gameFile.read()
        gameFile.close()
        soup = BeautifulSoup(gameHtml)
        gameAll = soup.find_all("a")
        for links in soup.find_all('a'):
            try:
                if links.get('href') == None:
                    pass
                else:
                    value = (links.get('href'))
                    test = (value.split('/')[2])
                    list = str(test) 
                    stringValues = list
                    myList = stringValues.split(',')
                    for i in myList:
                        try:
                            if i[0:3] == 'www':
                                pass
                            elif i[-4:-1] == '.co':
                                pass
                            elif i[0:4] == 'xbox':
                                pass
                            elif i == None:
                                pass
                            elif i == 'upcoming':
                                pass
                            elif i == 'reviews':
                                pass
                            else:
                                print(i)
                                try:
                                    conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
                                    cursor = conn.cursor ()
                                    quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
                                    print(quertest)
                                    cursor.execute (quertest) 
                                    row = cursor.fetchone()
                                except Exception as e:
                                    print(e)
                                finally:
                                    conn.commit()
                                    cursor.close ()
                                    conn.close ()
                        except Exception as e:
                            print(e)
                    #print(myList)
        
            except Exception as e:
                print(e)
#     elif gamePageLinkB == gamePageLinkB:
#         gameFile = urllib.request.urlopen(gamePageLinkB)
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all("a")
#         for links in soup.find_all('a'):
#             try:
#                 if links.get('href') == None:
#                     pass
#                 else:
#                     value = (links.get('href'))
#                     test = (value.split('/')[2])
#                     list = str(test) 
#                     stringValues = list
#                     myList = stringValues.split(',')
#                     for i in myList:
#                         try:
#                             if i[0:3] == 'www':
#                                 pass
#                             elif i[-4:-1] == '.co':
#                                 pass
#                             elif i[0:4] == 'xbox':
#                                 pass
#                             elif i == None:
#                                 pass
#                             elif i == 'upcoming':
#                                 pass
#                             elif i == 'reviews':
#                                 pass
#                             else:
#                                 print(i)
#                                 try:
#                                     conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
#                                     cursor = conn.cursor ()
#                                     quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
#                                     print(quertest)
#                                     cursor.execute (quertest) 
#                                     row = cursor.fetchone()
#                                 except Exception as e:
#                                     print(e)
#                                 finally:
#                                     conn.commit()
#                                     cursor.close ()
#                                     conn.close ()
#                         except Exception as e:
#                             print(e)
#                     #print(myList)
#         
#             except Exception as e:
#                 print(e)
#     elif gamePageLinkC == gamePageLinkC:
#         gameFile = urllib.request.urlopen(gamePageLinkC)
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all("a")
#         for links in soup.find_all('a'):
#             try:
#                 if links.get('href') == None:
#                     pass
#                 else:
#                     value = (links.get('href'))
#                     test = (value.split('/')[2])
#                     list = str(test) 
#                     stringValues = list
#                     myList = stringValues.split(',')
#                     for i in myList:
#                         try:
#                             if i[0:3] == 'www':
#                                 pass
#                             elif i[-4:-1] == '.co':
#                                 pass
#                             elif i[0:4] == 'xbox':
#                                 pass
#                             elif i == None:
#                                 pass
#                             elif i == 'upcoming':
#                                 pass
#                             elif i == 'reviews':
#                                 pass
#                             else:
#                                 print(i)
#                                 try:
#                                     conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
#                                     cursor = conn.cursor ()
#                                     quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
#                                     print(quertest)
#                                     cursor.execute (quertest) 
#                                     row = cursor.fetchone()
#                                 except Exception as e:
#                                     print(e)
#                                 finally:
#                                     conn.commit()
#                                     cursor.close ()
#                                     conn.close ()
#                         except Exception as e:
#                             print(e)
#                     #print(myList)
#         
#             except Exception as e:
#                 print(e)
#     elif gamePageLinkD == gamePageLinkD:
#         gameFile = urllib.request.urlopen(gamePageLinkD)
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all("a")
#         for links in soup.find_all('a'):
#             try:
#                 if links.get('href') == None:
#                     pass
#                 else:
#                     value = (links.get('href'))
#                     test = (value.split('/')[2])
#                     list = str(test) 
#                     stringValues = list
#                     myList = stringValues.split(',')
#                     for i in myList:
#                         try:
#                             if i[0:3] == 'www':
#                                 pass
#                             elif i[-4:-1] == '.co':
#                                 pass
#                             elif i[0:4] == 'xbox':
#                                 pass
#                             elif i == None:
#                                 pass
#                             elif i == 'upcoming':
#                                 pass
#                             elif i == 'reviews':
#                                 pass
#                             else:
#                                 print(i)
#                                 try:
#                                     conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
#                                     cursor = conn.cursor ()
#                                     quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
#                                     print(quertest)
#                                     cursor.execute (quertest) 
#                                     row = cursor.fetchone()
#                                 except Exception as e:
#                                     print(e)
#                                 finally:
#                                     conn.commit()
#                                     cursor.close ()
#                                     conn.close ()
#                         except Exception as e:
#                             print(e)
#                     #print(myList)
#         
#             except Exception as e:
#                 print(e)
#     elif gamePageLinkE == gamePageLinkE:
#         gameFile = urllib.request.urlopen(gamePageLinkE)
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all("a")
#         for links in soup.find_all('a'):
#             try:
#                 if links.get('href') == None:
#                     pass
#                 else:
#                     value = (links.get('href'))
#                     test = (value.split('/')[2])
#                     list = str(test) 
#                     stringValues = list
#                     myList = stringValues.split(',')
#                     for i in myList:
#                         try:
#                             if i[0:3] == 'www':
#                                 pass
#                             elif i[-4:-1] == '.co':
#                                 pass
#                             elif i[0:4] == 'xbox':
#                                 pass
#                             elif i == None:
#                                 pass
#                             elif i == 'upcoming':
#                                 pass
#                             elif i == 'reviews':
#                                 pass
#                             else:
#                                 print(i)
#                                 try:
#                                     conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
#                                     cursor = conn.cursor ()
#                                     quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
#                                     print(quertest)
#                                     cursor.execute (quertest) 
#                                     row = cursor.fetchone()
#                                 except Exception as e:
#                                     print(e)
#                                 finally:
#                                     conn.commit()
#                                     cursor.close ()
#                                     conn.close ()
#                         except Exception as e:
#                             print(e)
#                     #print(myList)
#         
#             except Exception as e:
#                 print(e)
#     elif gamePageLinkF == gamePageLinkF:
#         gameFile = urllib.request.urlopen(gamePageLinkF)
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all("a")
#         for links in soup.find_all('a'):
#             try:
#                 if links.get('href') == None:
#                     pass
#                 else:
#                     value = (links.get('href'))
#                     test = (value.split('/')[2])
#                     list = str(test) 
#                     stringValues = list
#                     myList = stringValues.split(',')
#                     for i in myList:
#                         try:
#                             if i[0:3] == 'www':
#                                 pass
#                             elif i[-4:-1] == '.co':
#                                 pass
#                             elif i[0:4] == 'xbox':
#                                 pass
#                             elif i == None:
#                                 pass
#                             elif i == 'upcoming':
#                                 pass
#                             elif i == 'reviews':
#                                 pass
#                             else:
#                                 print(i)
#                                 try:
#                                     conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
#                                     cursor = conn.cursor ()
#                                     quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
#                                     print(quertest)
#                                     cursor.execute (quertest) 
#                                     row = cursor.fetchone()
#                                 except Exception as e:
#                                     print(e)
#                                 finally:
#                                     conn.commit()
#                                     cursor.close ()
#                                     conn.close ()
#                         except Exception as e:
#                             print(e)
#                     #print(myList)
#         
#             except Exception as e:
#                 print(e)
#     elif gamePageLinkG == gamePageLinkG:
#         gameFile = urllib.request.urlopen(gamePageLinkG)
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all("a")
#         for links in soup.find_all('a'):
#             try:
#                 if links.get('href') == None:
#                     pass
#                 else:
#                     value = (links.get('href'))
#                     test = (value.split('/')[2])
#                     list = str(test) 
#                     stringValues = list
#                     myList = stringValues.split(',')
#                     for i in myList:
#                         try:
#                             if i[0:3] == 'www':
#                                 pass
#                             elif i[-4:-1] == '.co':
#                                 pass
#                             elif i[0:4] == 'xbox':
#                                 pass
#                             elif i == None:
#                                 pass
#                             elif i == 'upcoming':
#                                 pass
#                             elif i == 'reviews':
#                                 pass
#                             else:
#                                 print(i)
#                                 try:
#                                     conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
#                                     cursor = conn.cursor ()
#                                     quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
#                                     print(quertest)
#                                     cursor.execute (quertest) 
#                                     row = cursor.fetchone()
#                                 except Exception as e:
#                                     print(e)
#                                 finally:
#                                     conn.commit()
#                                     cursor.close ()
#                                     conn.close ()
#                         except Exception as e:
#                             print(e)
#                     #print(myList)
#         
#             except Exception as e:
#                 print(e)
#     elif gamePageLinkH == gamePageLinkH:
#         gameFile = urllib.request.urlopen(gamePageLinkH)
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all("a")
#         for links in soup.find_all('a'):
#             try:
#                 if links.get('href') == None:
#                     pass
#                 else:
#                     value = (links.get('href'))
#                     test = (value.split('/')[2])
#                     list = str(test) 
#                     stringValues = list
#                     myList = stringValues.split(',')
#                     for i in myList:
#                         try:
#                             if i[0:3] == 'www':
#                                 pass
#                             elif i[-4:-1] == '.co':
#                                 pass
#                             elif i[0:4] == 'xbox':
#                                 pass
#                             elif i == None:
#                                 pass
#                             elif i == 'upcoming':
#                                 pass
#                             elif i == 'reviews':
#                                 pass
#                             else:
#                                 print(i)
#                                 try:
#                                     conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
#                                     cursor = conn.cursor ()
#                                     quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
#                                     print(quertest)
#                                     cursor.execute (quertest) 
#                                     row = cursor.fetchone()
#                                 except Exception as e:
#                                     print(e)
#                                 finally:
#                                     conn.commit()
#                                     cursor.close ()
#                                     conn.close ()
#                         except Exception as e:
#                             print(e)
#                     #print(myList)
#         
#             except Exception as e:
#                 print(e)
#     elif gamePageLinkI == gamePageLinkI:
#         gameFile = urllib.request.urlopen(gamePageLinkI)
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all("a")
#         for links in soup.find_all('a'):
#             try:
#                 if links.get('href') == None:
#                     pass
#                 else:
#                     value = (links.get('href'))
#                     test = (value.split('/')[2])
#                     list = str(test) 
#                     stringValues = list
#                     myList = stringValues.split(',')
#                     for i in myList:
#                         try:
#                             if i[0:3] == 'www':
#                                 pass
#                             elif i[-4:-1] == '.co':
#                                 pass
#                             elif i[0:4] == 'xbox':
#                                 pass
#                             elif i == None:
#                                 pass
#                             elif i == 'upcoming':
#                                 pass
#                             elif i == 'reviews':
#                                 pass
#                             else:
#                                 print(i)
#                                 try:
#                                     conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
#                                     cursor = conn.cursor ()
#                                     quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
#                                     print(quertest)
#                                     cursor.execute (quertest) 
#                                     row = cursor.fetchone()
#                                 except Exception as e:
#                                     print(e)
#                                 finally:
#                                     conn.commit()
#                                     cursor.close ()
#                                     conn.close ()
#                         except Exception as e:
#                             print(e)
#                     #print(myList)
#         
#             except Exception as e:
#                 print(e)
#     elif gamePageLinkJ == gamePageLinkJ:
#         gameFile = urllib.request.urlopen(gamePageLinkJ)
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all("a")
#         for links in soup.find_all('a'):
#             try:
#                 if links.get('href') == None:
#                     pass
#                 else:
#                     value = (links.get('href'))
#                     test = (value.split('/')[2])
#                     list = str(test) 
#                     stringValues = list
#                     myList = stringValues.split(',')
#                     for i in myList:
#                         try:
#                             if i[0:3] == 'www':
#                                 pass
#                             elif i[-4:-1] == '.co':
#                                 pass
#                             elif i[0:4] == 'xbox':
#                                 pass
#                             elif i == None:
#                                 pass
#                             elif i == 'upcoming':
#                                 pass
#                             elif i == 'reviews':
#                                 pass
#                             else:
#                                 print(i)
#                                 try:
#                                     conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
#                                     cursor = conn.cursor ()
#                                     quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
#                                     print(quertest)
#                                     cursor.execute (quertest) 
#                                     row = cursor.fetchone()
#                                 except Exception as e:
#                                     print(e)
#                                 finally:
#                                     conn.commit()
#                                     cursor.close ()
#                                     conn.close ()
#                         except Exception as e:
#                             print(e)
#                     #print(myList)
#         
#             except Exception as e:
#                 print(e)
#     elif gamePageLinkK == gamePageLinkK:
#         gameFile = urllib.request.urlopen(gamePageLinkK)
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all("a")
#         for links in soup.find_all('a'):
#             try:
#                 if links.get('href') == None:
#                     pass
#                 else:
#                     value = (links.get('href'))
#                     test = (value.split('/')[2])
#                     list = str(test) 
#                     stringValues = list
#                     myList = stringValues.split(',')
#                     for i in myList:
#                         try:
#                             if i[0:3] == 'www':
#                                 pass
#                             elif i[-4:-1] == '.co':
#                                 pass
#                             elif i[0:4] == 'xbox':
#                                 pass
#                             elif i == None:
#                                 pass
#                             elif i == 'upcoming':
#                                 pass
#                             elif i == 'reviews':
#                                 pass
#                             else:
#                                 print(i)
#                                 try:
#                                     conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
#                                     cursor = conn.cursor ()
#                                     quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
#                                     print(quertest)
#                                     cursor.execute (quertest) 
#                                     row = cursor.fetchone()
#                                 except Exception as e:
#                                     print(e)
#                                 finally:
#                                     conn.commit()
#                                     cursor.close ()
#                                     conn.close ()
#                         except Exception as e:
#                             print(e)
#                     #print(myList)
#         
#             except Exception as e:
#                 print(e)
#     elif gamePageLinkL == gamePageLinkL:
#         gameFile = urllib.request.urlopen(gamePageLinkL)
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all("a")
#         for links in soup.find_all('a'):
#             try:
#                 if links.get('href') == None:
#                     pass
#                 else:
#                     value = (links.get('href'))
#                     test = (value.split('/')[2])
#                     list = str(test) 
#                     stringValues = list
#                     myList = stringValues.split(',')
#                     for i in myList:
#                         try:
#                             if i[0:3] == 'www':
#                                 pass
#                             elif i[-4:-1] == '.co':
#                                 pass
#                             elif i[0:4] == 'xbox':
#                                 pass
#                             elif i == None:
#                                 pass
#                             elif i == 'upcoming':
#                                 pass
#                             elif i == 'reviews':
#                                 pass
#                             else:
#                                 print(i)
#                                 try:
#                                     conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
#                                     cursor = conn.cursor ()
#                                     quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
#                                     print(quertest)
#                                     cursor.execute (quertest) 
#                                     row = cursor.fetchone()
#                                 except Exception as e:
#                                     print(e)
#                                 finally:
#                                     conn.commit()
#                                     cursor.close ()
#                                     conn.close ()
#                         except Exception as e:
#                             print(e)
#                     #print(myList)
#         
#             except Exception as e:
#                 print(e)
#     elif gamePageLinkM == gamePageLinkM:
#         gameFile = urllib.request.urlopen(gamePageLinkM)
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all("a")
#         for links in soup.find_all('a'):
#             try:
#                 if links.get('href') == None:
#                     pass
#                 else:
#                     value = (links.get('href'))
#                     test = (value.split('/')[2])
#                     list = str(test) 
#                     stringValues = list
#                     myList = stringValues.split(',')
#                     for i in myList:
#                         try:
#                             if i[0:3] == 'www':
#                                 pass
#                             elif i[-4:-1] == '.co':
#                                 pass
#                             elif i[0:4] == 'xbox':
#                                 pass
#                             elif i == None:
#                                 pass
#                             elif i == 'upcoming':
#                                 pass
#                             elif i == 'reviews':
#                                 pass
#                             else:
#                                 print(i)
#                                 try:
#                                     conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
#                                     cursor = conn.cursor ()
#                                     quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
#                                     print(quertest)
#                                     cursor.execute (quertest) 
#                                     row = cursor.fetchone()
#                                 except Exception as e:
#                                     print(e)
#                                 finally:
#                                     conn.commit()
#                                     cursor.close ()
#                                     conn.close ()
#                         except Exception as e:
#                             print(e)
#                     #print(myList)
#         
#             except Exception as e:
#                 print(e)
#     elif gamePageLinkN == gamePageLinkN:
#         gameFile = urllib.request.urlopen(gamePageLinkN)
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all("a")
#         for links in soup.find_all('a'):
#             try:
#                 if links.get('href') == None:
#                     pass
#                 else:
#                     value = (links.get('href'))
#                     test = (value.split('/')[2])
#                     list = str(test) 
#                     stringValues = list
#                     myList = stringValues.split(',')
#                     for i in myList:
#                         try:
#                             if i[0:3] == 'www':
#                                 pass
#                             elif i[-4:-1] == '.co':
#                                 pass
#                             elif i[0:4] == 'xbox':
#                                 pass
#                             elif i == None:
#                                 pass
#                             elif i == 'upcoming':
#                                 pass
#                             elif i == 'reviews':
#                                 pass
#                             else:
#                                 print(i)
#                                 try:
#                                     conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
#                                     cursor = conn.cursor ()
#                                     quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
#                                     print(quertest)
#                                     cursor.execute (quertest) 
#                                     row = cursor.fetchone()
#                                 except Exception as e:
#                                     print(e)
#                                 finally:
#                                     conn.commit()
#                                     cursor.close ()
#                                     conn.close ()
#                         except Exception as e:
#                             print(e)
#                     #print(myList)
#         
#             except Exception as e:
#                 print(e)
#     elif gamePageLinkO == gamePageLinkO:
#         gameFile = urllib.request.urlopen(gamePageLinkO)
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all("a")
#         for links in soup.find_all('a'):
#             try:
#                 if links.get('href') == None:
#                     pass
#                 else:
#                     value = (links.get('href'))
#                     test = (value.split('/')[2])
#                     list = str(test) 
#                     stringValues = list
#                     myList = stringValues.split(',')
#                     for i in myList:
#                         try:
#                             if i[0:3] == 'www':
#                                 pass
#                             elif i[-4:-1] == '.co':
#                                 pass
#                             elif i[0:4] == 'xbox':
#                                 pass
#                             elif i == None:
#                                 pass
#                             elif i == 'upcoming':
#                                 pass
#                             elif i == 'reviews':
#                                 pass
#                             else:
#                                 print(i)
#                                 try:
#                                     conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
#                                     cursor = conn.cursor ()
#                                     quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
#                                     print(quertest)
#                                     cursor.execute (quertest) 
#                                     row = cursor.fetchone()
#                                 except Exception as e:
#                                     print(e)
#                                 finally:
#                                     conn.commit()
#                                     cursor.close ()
#                                     conn.close ()
#                         except Exception as e:
#                             print(e)
#                     #print(myList)
#         
#             except Exception as e:
#                 print(e)
#     elif gamePageLinkP == gamePageLinkP:
#         gameFile = urllib.request.urlopen(gamePageLinkP)
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all("a")
#         for links in soup.find_all('a'):
#             try:
#                 if links.get('href') == None:
#                     pass
#                 else:
#                     value = (links.get('href'))
#                     test = (value.split('/')[2])
#                     list = str(test) 
#                     stringValues = list
#                     myList = stringValues.split(',')
#                     for i in myList:
#                         try:
#                             if i[0:3] == 'www':
#                                 pass
#                             elif i[-4:-1] == '.co':
#                                 pass
#                             elif i[0:4] == 'xbox':
#                                 pass
#                             elif i == None:
#                                 pass
#                             elif i == 'upcoming':
#                                 pass
#                             elif i == 'reviews':
#                                 pass
#                             else:
#                                 print(i)
#                                 try:
#                                     conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
#                                     cursor = conn.cursor ()
#                                     quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
#                                     print(quertest)
#                                     cursor.execute (quertest) 
#                                     row = cursor.fetchone()
#                                 except Exception as e:
#                                     print(e)
#                                 finally:
#                                     conn.commit()
#                                     cursor.close ()
#                                     conn.close ()
#                         except Exception as e:
#                             print(e)
#                     #print(myList)
#         
#             except Exception as e:
#                 print(e)
#     elif gamePageLinkQ == gamePageLinkQ:
#         gameFile = urllib.request.urlopen(gamePageLinkQ)
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all("a")
#         for links in soup.find_all('a'):
#             try:
#                 if links.get('href') == None:
#                     pass
#                 else:
#                     value = (links.get('href'))
#                     test = (value.split('/')[2])
#                     list = str(test) 
#                     stringValues = list
#                     myList = stringValues.split(',')
#                     for i in myList:
#                         try:
#                             if i[0:3] == 'www':
#                                 pass
#                             elif i[-4:-1] == '.co':
#                                 pass
#                             elif i[0:4] == 'xbox':
#                                 pass
#                             elif i == None:
#                                 pass
#                             elif i == 'upcoming':
#                                 pass
#                             elif i == 'reviews':
#                                 pass
#                             else:
#                                 print(i)
#                                 try:
#                                     conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
#                                     cursor = conn.cursor ()
#                                     quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
#                                     print(quertest)
#                                     cursor.execute (quertest) 
#                                     row = cursor.fetchone()
#                                 except Exception as e:
#                                     print(e)
#                                 finally:
#                                     conn.commit()
#                                     cursor.close ()
#                                     conn.close ()
#                         except Exception as e:
#                             print(e)
#                     #print(myList)
#         
#             except Exception as e:
#                 print(e)
#     elif gamePageLinkR == gamePageLinkR:
#         gameFile = urllib.request.urlopen(gamePageLinkR)
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all("a")
#         for links in soup.find_all('a'):
#             try:
#                 if links.get('href') == None:
#                     pass
#                 else:
#                     value = (links.get('href'))
#                     test = (value.split('/')[2])
#                     list = str(test) 
#                     stringValues = list
#                     myList = stringValues.split(',')
#                     for i in myList:
#                         try:
#                             if i[0:3] == 'www':
#                                 pass
#                             elif i[-4:-1] == '.co':
#                                 pass
#                             elif i[0:4] == 'xbox':
#                                 pass
#                             elif i == None:
#                                 pass
#                             elif i == 'upcoming':
#                                 pass
#                             elif i == 'reviews':
#                                 pass
#                             else:
#                                 print(i)
#                                 try:
#                                     conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
#                                     cursor = conn.cursor ()
#                                     quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
#                                     print(quertest)
#                                     cursor.execute (quertest) 
#                                     row = cursor.fetchone()
#                                 except Exception as e:
#                                     print(e)
#                                 finally:
#                                     conn.commit()
#                                     cursor.close ()
#                                     conn.close ()
#                         except Exception as e:
#                             print(e)
#                     #print(myList)
#         
#             except Exception as e:
#                 print(e)
#     elif gamePageLinkS == gamePageLinkS:
#         gameFile = urllib.request.urlopen(gamePageLinkS)
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all("a")
#         for links in soup.find_all('a'):
#             try:
#                 if links.get('href') == None:
#                     pass
#                 else:
#                     value = (links.get('href'))
#                     test = (value.split('/')[2])
#                     list = str(test) 
#                     stringValues = list
#                     myList = stringValues.split(',')
#                     for i in myList:
#                         try:
#                             if i[0:3] == 'www':
#                                 pass
#                             elif i[-4:-1] == '.co':
#                                 pass
#                             elif i[0:4] == 'xbox':
#                                 pass
#                             elif i == None:
#                                 pass
#                             elif i == 'upcoming':
#                                 pass
#                             elif i == 'reviews':
#                                 pass
#                             else:
#                                 print(i)
#                                 try:
#                                     conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
#                                     cursor = conn.cursor ()
#                                     quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
#                                     print(quertest)
#                                     cursor.execute (quertest) 
#                                     row = cursor.fetchone()
#                                 except Exception as e:
#                                     print(e)
#                                 finally:
#                                     conn.commit()
#                                     cursor.close ()
#                                     conn.close ()
#                         except Exception as e:
#                             print(e)
#                     #print(myList)
#         
#             except Exception as e:
#                 print(e)
#     elif gamePageLinkT == gamePageLinkT:
#         gameFile = urllib.request.urlopen(gamePageLinkT)
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all("a")
#         for links in soup.find_all('a'):
#             try:
#                 if links.get('href') == None:
#                     pass
#                 else:
#                     value = (links.get('href'))
#                     test = (value.split('/')[2])
#                     list = str(test) 
#                     stringValues = list
#                     myList = stringValues.split(',')
#                     for i in myList:
#                         try:
#                             if i[0:3] == 'www':
#                                 pass
#                             elif i[-4:-1] == '.co':
#                                 pass
#                             elif i[0:4] == 'xbox':
#                                 pass
#                             elif i == None:
#                                 pass
#                             elif i == 'upcoming':
#                                 pass
#                             elif i == 'reviews':
#                                 pass
#                             else:
#                                 print(i)
#                                 try:
#                                     conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
#                                     cursor = conn.cursor ()
#                                     quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
#                                     print(quertest)
#                                     cursor.execute (quertest) 
#                                     row = cursor.fetchone()
#                                 except Exception as e:
#                                     print(e)
#                                 finally:
#                                     conn.commit()
#                                     cursor.close ()
#                                     conn.close ()
#                         except Exception as e:
#                             print(e)
#                     #print(myList)
#         
#             except Exception as e:
#                 print(e)
#     elif gamePageLinkU == gamePageLinkU:
#         gameFile = urllib.request.urlopen(gamePageLinkU)
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all("a")
#         for links in soup.find_all('a'):
#             try:
#                 if links.get('href') == None:
#                     pass
#                 else:
#                     value = (links.get('href'))
#                     test = (value.split('/')[2])
#                     list = str(test) 
#                     stringValues = list
#                     myList = stringValues.split(',')
#                     for i in myList:
#                         try:
#                             if i[0:3] == 'www':
#                                 pass
#                             elif i[-4:-1] == '.co':
#                                 pass
#                             elif i[0:4] == 'xbox':
#                                 pass
#                             elif i == None:
#                                 pass
#                             elif i == 'upcoming':
#                                 pass
#                             elif i == 'reviews':
#                                 pass
#                             else:
#                                 print(i)
#                                 try:
#                                     conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
#                                     cursor = conn.cursor ()
#                                     quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
#                                     print(quertest)
#                                     cursor.execute (quertest) 
#                                     row = cursor.fetchone()
#                                 except Exception as e:
#                                     print(e)
#                                 finally:
#                                     conn.commit()
#                                     cursor.close ()
#                                     conn.close ()
#                         except Exception as e:
#                             print(e)
#                     #print(myList)
#         
#             except Exception as e:
#                 print(e)
#     elif gamePageLinkV == gamePageLinkV:
#         gameFile = urllib.request.urlopen(gamePageLinkV)
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all("a")
#         for links in soup.find_all('a'):
#             try:
#                 if links.get('href') == None:
#                     pass
#                 else:
#                     value = (links.get('href'))
#                     test = (value.split('/')[2])
#                     list = str(test) 
#                     stringValues = list
#                     myList = stringValues.split(',')
#                     for i in myList:
#                         try:
#                             if i[0:3] == 'www':
#                                 pass
#                             elif i[-4:-1] == '.co':
#                                 pass
#                             elif i[0:4] == 'xbox':
#                                 pass
#                             elif i == None:
#                                 pass
#                             elif i == 'upcoming':
#                                 pass
#                             elif i == 'reviews':
#                                 pass
#                             else:
#                                 print(i)
#                                 try:
#                                     conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
#                                     cursor = conn.cursor ()
#                                     quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
#                                     print(quertest)
#                                     cursor.execute (quertest) 
#                                     row = cursor.fetchone()
#                                 except Exception as e:
#                                     print(e)
#                                 finally:
#                                     conn.commit()
#                                     cursor.close ()
#                                     conn.close ()
#                         except Exception as e:
#                             print(e)
#                     #print(myList)
#         
#             except Exception as e:
#                 print(e)
#     elif gamePageLinkW == gamePageLinkW:
#         gameFile = urllib.request.urlopen(gamePageLinkW)
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all("a")
#         for links in soup.find_all('a'):
#             try:
#                 if links.get('href') == None:
#                     pass
#                 else:
#                     value = (links.get('href'))
#                     test = (value.split('/')[2])
#                     list = str(test) 
#                     stringValues = list
#                     myList = stringValues.split(',')
#                     for i in myList:
#                         try:
#                             if i[0:3] == 'www':
#                                 pass
#                             elif i[-4:-1] == '.co':
#                                 pass
#                             elif i[0:4] == 'xbox':
#                                 pass
#                             elif i == None:
#                                 pass
#                             elif i == 'upcoming':
#                                 pass
#                             elif i == 'reviews':
#                                 pass
#                             else:
#                                 print(i)
#                                 try:
#                                     conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
#                                     cursor = conn.cursor ()
#                                     quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
#                                     print(quertest)
#                                     cursor.execute (quertest) 
#                                     row = cursor.fetchone()
#                                 except Exception as e:
#                                     print(e)
#                                 finally:
#                                     conn.commit()
#                                     cursor.close ()
#                                     conn.close ()
#                         except Exception as e:
#                             print(e)
#                     #print(myList)
#         
#             except Exception as e:
#                 print(e)
#     elif gamePageLinkX == gamePageLinkX:
#         gameFile = urllib.request.urlopen(gamePageLinkX)
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all("a")
#         for links in soup.find_all('a'):
#             try:
#                 if links.get('href') == None:
#                     pass
#                 else:
#                     value = (links.get('href'))
#                     test = (value.split('/')[2])
#                     list = str(test) 
#                     stringValues = list
#                     myList = stringValues.split(',')
#                     for i in myList:
#                         try:
#                             if i[0:3] == 'www':
#                                 pass
#                             elif i[-4:-1] == '.co':
#                                 pass
#                             elif i[0:4] == 'xbox':
#                                 pass
#                             elif i == None:
#                                 pass
#                             elif i == 'upcoming':
#                                 pass
#                             elif i == 'reviews':
#                                 pass
#                             else:
#                                 print(i)
#                                 try:
#                                     conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
#                                     cursor = conn.cursor ()
#                                     quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
#                                     print(quertest)
#                                     cursor.execute (quertest) 
#                                     row = cursor.fetchone()
#                                 except Exception as e:
#                                     print(e)
#                                 finally:
#                                     conn.commit()
#                                     cursor.close ()
#                                     conn.close ()
#                         except Exception as e:
#                             print(e)
#                     #print(myList)
#         
#             except Exception as e:
#                 print(e)
#     elif gamePageLinkY == gamePageLinkY:
#         gameFile = urllib.request.urlopen(gamePageLinkY)
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all("a")
#         for links in soup.find_all('a'):
#             try:
#                 if links.get('href') == None:
#                     pass
#                 else:
#                     value = (links.get('href'))
#                     test = (value.split('/')[2])
#                     list = str(test) 
#                     stringValues = list
#                     myList = stringValues.split(',')
#                     for i in myList:
#                         try:
#                             if i[0:3] == 'www':
#                                 pass
#                             elif i[-4:-1] == '.co':
#                                 pass
#                             elif i[0:4] == 'xbox':
#                                 pass
#                             elif i == None:
#                                 pass
#                             elif i == 'upcoming':
#                                 pass
#                             elif i == 'reviews':
#                                 pass
#                             else:
#                                 print(i)
#                                 try:
#                                     conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
#                                     cursor = conn.cursor ()
#                                     quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
#                                     print(quertest)
#                                     cursor.execute (quertest) 
#                                     row = cursor.fetchone()
#                                 except Exception as e:
#                                     print(e)
#                                 finally:
#                                     conn.commit()
#                                     cursor.close ()
#                                     conn.close ()
#                         except Exception as e:
#                             print(e)
#                     #print(myList)
#         
#             except Exception as e:
#                 print(e)
#     elif gamePageLinkZ == gamePageLinkZ:
#         gameFile = urllib.request.urlopen(gamePageLinkZ)
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all("a")
#         for links in soup.find_all('a'):
#             try:
#                 if links.get('href') == None:
#                     pass
#                 else:
#                     value = (links.get('href'))
#                     test = (value.split('/')[2])
#                     list = str(test) 
#                     stringValues = list
#                     myList = stringValues.split(',')
#                     for i in myList:
#                         try:
#                             if i[0:3] == 'www':
#                                 pass
#                             elif i[-4:-1] == '.co':
#                                 pass
#                             elif i[0:4] == 'xbox':
#                                 pass
#                             elif i == None:
#                                 pass
#                             elif i == 'upcoming':
#                                 pass
#                             elif i == 'reviews':
#                                 pass
#                             else:
#                                 print(i)
#                                 try:
#                                     conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
#                                     cursor = conn.cursor ()
#                                     quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
#                                     print(quertest)
#                                     cursor.execute (quertest) 
#                                     row = cursor.fetchone()
#                                 except Exception as e:
#                                     print(e)
#                                 finally:
#                                     conn.commit()
#                                     cursor.close ()
#                                     conn.close ()
#                         except Exception as e:
#                             print(e)
#                     #print(myList)
#         
#             except Exception as e:
#                 print(e)
#     elif gamePageLinkB == gamePageLinkB:
#         gameFile = urllib.request.urlopen(gamePageLinkA)
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all("a")
#         for links in soup.find_all('a'):
#             try:
#                 if links.get('href') == None:
#                     pass
#                 else:
#                     value = (links.get('href'))
#                     test = (value.split('/')[2])
#                     list = str(test) 
#                     stringValues = list
#                     myList = stringValues.split(',')
#                     for i in myList:
#                         try:
#                             if i[0:3] == 'www':
#                                 pass
#                             elif i[-4:-1] == '.co':
#                                 pass
#                             elif i[0:4] == 'xbox':
#                                 pass
#                             elif i == None:
#                                 pass
#                             elif i == 'upcoming':
#                                 pass
#                             elif i == 'reviews':
#                                 pass
#                             else:
#                                 print(i)
#                                 try:
#                                     conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
#                                     cursor = conn.cursor ()
#                                     quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
#                                     print(quertest)
#                                     cursor.execute (quertest) 
#                                     row = cursor.fetchone()
#                                 except Exception as e:
#                                     print(e)
#                                 finally:
#                                     conn.commit()
#                                     cursor.close ()
#                                     conn.close ()
#                         except Exception as e:
#                             print(e)
#                     #print(myList)
#         
#             except Exception as e:
#                 print(e)
#     elif gamePageLinkB == gamePageLinkB:
#         gameFile = urllib.request.urlopen(gamePageLinkA)
#         gameHtml = gameFile.read()
#         gameFile.close()
#         soup = BeautifulSoup(gameHtml)
#         gameAll = soup.find_all("a")
#         for links in soup.find_all('a'):
#             try:
#                 if links.get('href') == None:
#                     pass
#                 else:
#                     value = (links.get('href'))
#                     test = (value.split('/')[2])
#                     list = str(test) 
#                     stringValues = list
#                     myList = stringValues.split(',')
#                     for i in myList:
#                         try:
#                             if i[0:3] == 'www':
#                                 pass
#                             elif i[-4:-1] == '.co':
#                                 pass
#                             elif i[0:4] == 'xbox':
#                                 pass
#                             elif i == None:
#                                 pass
#                             elif i == 'upcoming':
#                                 pass
#                             elif i == 'reviews':
#                                 pass
#                             else:
#                                 print(i)
#                                 try:
#                                     conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
#                                     cursor = conn.cursor ()
#                                     quertest = "INSERT INTO sample (gameNames)  VALUES ('"+i+"')"
#                                     print(quertest)
#                                     cursor.execute (quertest) 
#                                     row = cursor.fetchone()
#                                 except Exception as e:
#                                     print(e)
#                                 finally:
#                                     conn.commit()
#                                     cursor.close ()
#                                     conn.close ()
#                         except Exception as e:
#                             print(e)
#                     #print(myList)
#         
#             except Exception as e:
#                 print(e)
#     else:
#         print(False)
    


fecthData()    