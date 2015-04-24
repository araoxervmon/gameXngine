import openpyxl
import MySQLdb
import random   

def updateDB():
    workbook = openpyxl.load_workbook(filename = 'G:/Work/531.xlsx', use_iterators = True)
    worksheet = workbook.get_sheet_by_name('Sheet1')
    for row in worksheet.iter_rows():
        data = {
            'my_first_col':  row[0].value,
            'my_sec_col':  row[1].value,
            'my_third_col':  row[2].value,
            'my_fourth_col':  row[3].value,
            'my_fifth_col':  row[4].value # Column A
        }
        print(data['my_first_col'],data['my_sec_col'],data['my_third_col'],data['my_fourth_col'],data['my_fifth_col'])
        catId = data['my_first_col']
        gN= data['my_sec_col']
        pubD = data['my_third_col']
        rat = data['my_fourth_col']
        relD = data['my_fifth_col']
        try:
            conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "test1")
            cursor = conn.cursor ()
            quertest = "INSERT INTO gameList (categoryId, gameName, publisher, ratings, releaseDate)  VALUES ('"+str(catId)+"','"+str(gN)+"','"+str(pubD)+"','"+str(rat)+"','"+str(relD)+"' )"
            print(quertest)
            cursor.execute (quertest) 
            row = cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            conn.commit()
            cursor.close ()
            conn.close ()
updateDB()   
