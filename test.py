import time
from bot import BotBinance
mode_Soft=1 # modo 0 como demo - modo 1 produccion con datos reales
asset_primary = "BTC"
asset_secundary="TRY"
symbol = asset_primary + asset_secundary
perc_binance = 0.167
sPd = 9
mPd = sPd * 2
lPd = mPd * 3
nbdevup= 2
nbdevdn=2
perc_stopSide= 0.035
perc_priceSide=0.018
bot = BotBinance(symbol=symbol, asset_primary=asset_primary, asset_secundary=asset_secundary, mode_Soft=mode_Soft, interval="1m", limit=300, sPd=sPd, mPd=mPd, lPd=lPd, perc_binance= perc_binance, perc_stopSide=perc_stopSide, perc_priceSide=perc_priceSide, nbdevup=nbdevup, nbdevdn=nbdevdn)
while True:
    data = bot.update_data()
    print(f" {data['price_market']} | {data['ear']} | {data['alerts']}")
    if data['msg'] !="":
        print(f"{data['msg']}")
    time.sleep(3)
    
