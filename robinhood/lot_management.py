import csv
import sys
import os
import datetime

# global dictionary
stocks = {}
debugLog='ON';

QUANTITY = 0 
AVGPRICE = 1 
TIMESTAMP=2

def log(logMsg):
    if(debugLog == 'ON'):
        print(logMsg)

    

def bought(symbol, quantity, avgPrice, boughtTime):
    log("Bought: " + symbol + " ,quantity of: " + str(quantity) + " with average price: " + str(avgPrice))
    if symbol in stocks:
        log(symbol + " bought previously")
        info = [quantity, avgPrice, boughtTime]
        stocks[symbol].append(info)
        
    else:
        # this is newly invested stock
        log(symbol + " bought first time")
        info = [ [quantity, avgPrice, boughtTime] ]
        stocks[symbol]  = info


def sold(symbol, quantity, avgPrice):
    log("SOLD: " + symbol + " ,quantity of: " + str(quantity) + " with average price: " + str(avgPrice))
    if symbol not in stocks:
        # TODO: throw an exception
        print('ERROR: stock not existed')
        return 
    info = stocks[symbol]
    LOT_NUM=0
    while quantity > 0:
        if( info[LOT_NUM][QUANTITY] > quantity ):
            #this lot has more quantity than sold
            info[LOT_NUM][QUANTITY] -=  quantity
            break
        elif( info[LOT_NUM][QUANTITY] == quantity ):
            #this lot has been sold fully
            info.pop(LOT_NUM)
            break
        else:
            #this lot has less quantity than sold
            quantity = quantity - info[LOT_NUM][QUANTITY]
            info.pop(LOT_NUM)


def displayAllStocks():
    print('Displaying all stocks')
    longTermLots = [] 
    #for sym in list(stocks.keys()):
    for sym in sorted(stocks.keys()):
        info = stocks[sym]
        if(len(info) == 0):
            continue
        print('***************************************************************')
        print(' Symbol: ' + str(sym))
        if(len(info) > 0):
            lot_num=0
            for lots in info:
                timeBought = lots[TIMESTAMP]
                dateBoughtStr = timeBought[0:10]
                dateBought=datetime.datetime.strptime(dateBoughtStr, "%Y-%m-%d")
                numDaysSinceBought = datetime.datetime.today() - dateBought
                if(int(numDaysSinceBought.days) > 365):
                    longTermLots.append([sym, lots[QUANTITY], lots[AVGPRICE], lots[TIMESTAMP], numDaysSinceBought.days])

                print('\t LOT#' + str(lot_num))
                print('\t\t NumDays since bought: ' + str(numDaysSinceBought.days))
                print('\t\tQuantity: ' + str(lots[QUANTITY]) + '\tAvg Price: ' + str(lots[AVGPRICE]) + '\t Time Bought: ' + str(lots[TIMESTAMP])) 
                lot_num = lot_num + 1
        
    print ("Eligible long term lots:")
    print longTermLots




def mainDriver(sysargs):
    if(len(sysargs) < 2):
        print('ERROR: please specifiy file name')
        return

    fileName = sysargs[1]


    if(os.path.isfile(fileName)):
        with open(fileName) as inputFile:
            for row in reversed(list(csv.reader(inputFile))):
                symbol=row[22]
                state=row[20]
                timestamp=row[24]
                log('Symbol: ' + symbol + ' with state ' + state)
                if(state == 'filled'):
                    price = float(row[1])
                    quantity = float(row[4])
                    side = row[19]
                    if(side == 'buy'):
                        bought(symbol, quantity, price, timestamp)
                    elif(side == 'sell'):
                        sold(symbol, quantity, price)
                    else:
                        print('ERROR: unexpected side: ' + side)
                        break

        displayAllStocks()
        return


    print('ERROR: file doesn''t exists!')



mainDriver(sys.argv)
