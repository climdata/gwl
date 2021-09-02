---
title: "gwl hess"
author: "Kmicha71"
date: "5 6 2021"
output:
  html_document: 
    keep_md: true
  pdf_document: default
---



## hess gwl serie

Derrived from 

https://www.pik-potsdam.de/en/output/publications/pikreports/.files/pr119.pdf


### Create plain daily series


```sh
python ./source/hess.py
```


```r
allGwls <- read.csv("./raw/hess_daily.csv", sep=",", na.strings = "NAN")

allGwls$gwl <- gsub("NA", "NLA", allGwls$gwl)
allGwls$gwl <- gsub("HNLA", "HNA", allGwls$gwl)

allGwls$ts <- signif(allGwls$year + (allGwls$month-0.5)/12  + (allGwls$day-0.5)/365, digits=8)
allDate <- paste(allGwls$year,allGwls$month,allGwls$day, sep='-')
allGwls$time <- paste(allDate, '00:00:00', sep=' ')
allGwls <- allGwls[order(allGwls$ts),]

write.table(allGwls, file = "csv/gwl_hess_daily.csv", append = FALSE, quote = TRUE, sep = ",",
            eol = "\n", na = "NAN", dec = ".", row.names = FALSE,
            col.names = TRUE, qmethod = "escape", fileEncoding = "UTF-8")
```


## dwd gwl serie

Derrived from 

https://www.dwd.de/DE/leistungen/wetterlagenklassifikation/wetterlagenklassifikation.html?nn=16102

https://www.dwd.de/DE/leistungen/wetterlagenklassifikation/online_wlkdaten.txt?view=nasPublication&nn=16102


```sh

 [ -f ./download/dwd_gwl.txt ] && mv -f ./download/dwd_gwl.txt ./download/dwd_gwl.txt.bck
 wget -q  -O ./download/dwd_gwl.txt 'https://www.dwd.de/DE/leistungen/wetterlagenklassifikation/online_wlkdaten.txt?view=nasPublication&nn=16102'
 ## Remove first line !!
 tail -n +2 ./download/dwd_gwl.txt > ./download/dwd_gwl.txt.tmp && mv ./download/dwd_gwl.txt.tmp ./download/dwd_gwl.txt

```



```sh
python ./source/dwd.py
```


```r
allGwls <- read.csv("./raw/dwd_gwl_daily.csv", sep=",")

allGwls$ts <- signif(allGwls$year + (allGwls$month-0.5)/12  + (allGwls$day-0.5)/365, digits=8)
allDate <- paste(allGwls$year,allGwls$month,allGwls$day, sep='-')
allGwls$time <- paste(allDate, '00:00:00', sep=' ')
allGwls <- allGwls[order(allGwls$ts),]

write.table(allGwls, file = "csv/dwd_gwl_daily.csv", append = FALSE, quote = TRUE, sep = ",",
            eol = "\n", na = "NA", dec = ".", row.names = FALSE,
            col.names = TRUE, qmethod = "escape", fileEncoding = "UTF-8")
```
