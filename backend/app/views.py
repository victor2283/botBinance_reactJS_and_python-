from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

import json

import sys
import os
binance_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')) # Calcula la ruta absoluta del directorio 'binance'
sys.path.append(binance_directory) # Agrega 'binance_directory' al sys.path
from bot import BotBinance

mode_Soft=1 # modo 0 como demo - modo 1 produccion con datos reales
asset_primary = 'BTC'
asset_secundary='TRY'
symbol = asset_primary + asset_secundary
perc_binance = 0.167
sPd = 9
mPd = sPd * 2
lPd = mPd * 3
nbdevup= 2
nbdevdn=2
perc_stopSide= 0.035
perc_priceSide=0.018
bot = BotBinance(symbol=symbol, asset_primary=asset_primary, asset_secundary=asset_secundary, mode_Soft=mode_Soft, interval='1m', limit=300, sPd=sPd, mPd=mPd, lPd=lPd, perc_binance= perc_binance, perc_stopSide=perc_stopSide, perc_priceSide=perc_priceSide, nbdevup=nbdevup, nbdevdn=nbdevdn)

def index(request):
    return render(request, 'index.html')

def get_bot_data(request):
    #return HttpResponse(data, content_type='application/json')    
    data = bot.update_data()
    data_1= {
            'ear': data['ear'],  
            'alerts': data['alerts'],
            'msg': data['msg'],
            'price_market': data['price_market'],
            'last_price_market': data['last_price_market'],
            'candles': data['candles'],
            'smaS':data['smaS'],
            'smaM':data['smaM'],
            'smaL':data['smaL'],
            'closes':data['closes'],
            'upperband':json.loads(data['upperband'].to_json()),
            'middleband':json.loads(data['middleband'].to_json()),
            'lowerband':json.loads(data['lowerband'].to_json()),
            'rsi':json.loads(data['rsi'].to_json()),
            'mfi':json.loads(data['mfi'].to_json()),
            'macd':json.loads(data['macd'].to_json()),
            'macdsignal':json.loads(data['macdsignal'].to_json()),
            'macdhist':json.loads(data['macdhist'].to_json()),
            
        }
    
    
    return  JsonResponse(data_1)
    
    
