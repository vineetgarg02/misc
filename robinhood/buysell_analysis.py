import csv
import sys
import os

# global dictionary
stocks = {}
debugLog='ON';

QUANTITY = 0 
AVGPRICE = 1 
LOSS_PROFIT=2

def log(logMsg):
    if(debugLog == 'ON'):
        print(logMsg)

    

def bought(symbol, quantity, avgPrice):
    log("Bought: " + symbol + " ,quantity of: " + str(quantity) + " with average price: " + str(avgPrice))
    if symbol in stocks:
        log(symbol + " bought previously")
        info = stocks[symbol]
        newQuantity = info[QUANTITY] + quantity
        newAvgPrice = ((info[AVGPRICE] * info[QUANTITY]) + (quantity * avgPrice))/newQuantity
        newLossProfit = info[LOSS_PROFIT]

        newInfo = [newQuantity, newAvgPrice, newLossProfit]
        log(symbol + ': ' + 'New quantity and avg price are: ' + str(newQuantity) + ' ' + str(newAvgPrice))
        stocks[symbol] = newInfo
        
    else:
        # this is newly invested stock
        log(symbol + " bought first time")
        info = [quantity, avgPrice, 0.0]
        stocks[symbol]  = info


def sold(symbol, quantity, avgPrice):
    log("SOLD: " + symbol + " ,quantity of: " + str(quantity) + " with average price: " + str(avgPrice))
    if symbol not in stocks:
        # TODO: throw an exception
        print('ERROR: stock not existed')
        return 
    
    info = stocks[symbol]
    boughtAvgPrice = info[AVGPRICE]
    boughtQuantity = info[QUANTITY]
    existingLossProfit = info[LOSS_PROFIT]
    
    newQuantity = boughtQuantity - quantity
    if(newQuantity < 0):
        print('ERROR: ' + symbol + ' new quantity is negative!! This is unimaginable, unprecedented and unspeakable')

    profitLoss = ((quantity * avgPrice) - (quantity * boughtAvgPrice)) + existingLossProfit
    log("LOSS/PROFIT: " + symbol + ' ' + str(profitLoss))

    # Could have sold all
    if(newQuantity == 0):
        boughtAvgPrice = 0.0
    
    newInfo = [newQuantity, boughtAvgPrice, profitLoss]
    stocks[symbol] = newInfo
    log("UPDATED info for stock: " + symbol + ' new quantity: ' + str(newQuantity) + ' new avg price:' + str(boughtAvgPrice))


def displayAllStocks():
    print('Displaying all stocks')
    totalLossProfit = 0.0
    #for sym in list(stocks.keys()):
    for sym in sorted(stocks.keys()):
        info = stocks[sym]
        avg_price = info[AVGPRICE]
        quant = info[QUANTITY]
        lossProf = info[LOSS_PROFIT]
        totalLossProfit += lossProf
        print(sym)
        print(' Quantity: ' + str(quant) + ' Avg Price: ' + str(avg_price) + ' LOSS/PROFIT: ' + str(lossProf))

    print('Total loss/profit: ' + str(totalLossProfit))


def mainDriver(sysargs):
    if(len(sysargs) < 2):
        print('ERROR: please specifiy file name')
        return

    fileName = sysargs[1]


    if(os.path.isfile(fileName)):
        with open(fileName) as inputFile:
            for row in reversed(list(csv.reader(inputFile))):
                symbol=row[21]
                state=row[19]
                timestamp=row[23]
                #log('Symbol: ' + symbol + ' with state ' + state)
                if(state == 'filled'):
                    price = float(row[1])
                    quantity = float(row[4])
                    side = row[18]
                    if(side == 'buy'):
                        bought(symbol, quantity, price)
                    elif(side == 'sell'):
                        sold(symbol, quantity, price)
                    else:
                        print('ERROR: unexpected side: ' + side)
                        break

        displayAllStocks()
        return


    print('ERROR: file doesn''t exists!')



mainDriver(sys.argv)
