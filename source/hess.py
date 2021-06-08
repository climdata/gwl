# -*- coding: utf-8 -*-

#from pathlib import Path
import os.path
import math
import codecs
import io

fileName='./raw/hess_daily.csv'

months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
gwls = ['BM','HB','HFA','HFZ','HM','HNA','HNFA','HNFZ','HNZ','NA','NEA','NEZ','NWA','NWZ','NZ','SA','SEA','SEZ','SWA','SWZ','SZ','TB','TM','TRM','TRW','U','WA','WS','WW','WZ',]
#months = ['jan']



csvfile2 = codecs.open(fileName, "w", "utf-8")
csvfile2.write("year,month,day,gwl\n")


m = 0
for month in months:
    m += 1
    fileName1 = './raw/'+month+'.txt'
    with open(fileName1, "r") as ins:
        d = 0 
        year = 0
        for line in ins:
            #array.append(line)
            words = line.split(' ')
            for word in words:
                if(word == ''):
                    empty = 1 
                elif(word.isdigit()):
                    if(int(word)>32): 
                        if(len(word)==4):   
                            year = int(word)
                            d = 0
                elif(word in gwls):
                    gwl = 1
                    d += 1
                    #print([year,m,word])
                    csvfile2.write(str(year)+","+str(m)+","+str(d)+","+word.strip()+"\n") 
                else:
                    other = 1
                    #print(word)        

csvfile2.close()                  