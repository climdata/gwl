#from pathlib import Path
import os.path
import math
import codecs
import io
import re


gwls = {1: 'XXAAT', 2: 'NOAAT', 3: 'SOAAT', 4: 'SWAAT', 5: 'NWAAT', 6: 'XXAAF', 7: 'NOAAF', 8: 'SOAAF', 9: 'SWAAF', 10: 'NWAAF', \
       11: 'XXAZT', 12: 'NOAZT', 13: 'SOAZT', 14: 'SWAZT', 15: 'NWAZT', 16: 'XXAZF', 17: 'NOAZF', 18: 'SOAZF', 19: 'SWAZF', 20: 'NWAZF', \
       21: 'XXZAT', 22: 'NOZAT', 23: 'SOZAT', 24: 'SWZAT', 25: 'NWZAT', 26: 'XXZAF', 27: 'NOZAF', 28: 'SOZAF', 29: 'SWZAF', 30: 'NWZAF', \
       31: 'XXZZT', 32: 'NOZZT', 33: 'SOZZT', 34: 'SWZZT', 35: 'NWZZT', 36: 'XXZZF', 37: 'NOZZF', 38: 'SOZZF', 39: 'SWZZF', 40: 'NWZZF' \
       }

   


fileName1='./download/dwd_gwl.txt'
fileName2='./raw/dwd_gwl_daily.csv'
csvfile2 = codecs.open(fileName2, "w", "utf-8")
csvfile2.write("year,month,day,owli,owlt,dir,zyk950,zyk500,hum\n")

with open(fileName1, "r") as ins:
    for line in ins:
        if(re.match(r'^\d{2}.\d{4}?.',line)):
            splitted = line.split(" ")
            date = splitted[0]
            dateSplit = date.split(".")
            month = int(dateSplit[0])
            year = int(dateSplit[1])
            day = 0
            for split in splitted[1:]:
                if(split.isdigit()):
                    day += 1
                    gwl = int(split.strip())
                    if(gwl > 0):
                        #print([day,month,year,gwl,gwls[gwl]]) 
                        gwlst = gwls[gwl]
                        csvfile2.write(str(year)+","+str(month)+","+str(day)+","+str(gwl)+","+ \
                                       gwlst+",'"+gwlst[0:2]+"','"+gwlst[2]+"','"+gwlst[3]+"','"+gwlst[4]+"'\n")   

csvfile2.close()                          