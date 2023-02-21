from okx_trade import OkxSPOT
from pprint import pprint

if __name__ == '__main__':
    KEY = '****'
    SECRET = '****'
    PASSPHRASE = '****'

    okxSPOT = OkxSPOT(key=KEY, secret=SECRET, passphrase=PASSPHRASE)
    # 获取现货全部产品的交易规则
    get_exchangeInfos = okxSPOT.market.get_exchangeInfos()
    pprint(get_exchangeInfos)
    # 获取单个现货产品的交易规则
    get_exchangeInfo = okxSPOT.market.get_exchangeInfo(symbol='BTC-USDT')
    pprint(get_exchangeInfo)
    # 获取可以交易的现货产品列表
    get_symbols_trading_on = okxSPOT.market.get_symbols_trading_on()
    pprint(get_symbols_trading_on)
    # 获取不可以交易的现货产品列表
    get_symbols_trading_off = okxSPOT.market.get_symbols_trading_off()
    pprint(get_symbols_trading_off)
