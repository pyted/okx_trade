from okx_trade import OkxSWAP
from pprint import pprint

if __name__ == '__main__':
    KEY = '****'
    SECRET = '****'
    PASSPHRASE = '****'

    okxSWAP = OkxSWAP(key=KEY, secret=SECRET, passphrase=PASSPHRASE)

    # 获取永续合约全部产品的交易规则
    get_exchangeInfos = okxSWAP.market.get_exchangeInfos()
    pprint(get_exchangeInfos)

    # 获取单个永续合约产品的交易规则
    get_exchangeInfo = okxSWAP.market.get_exchangeInfo(symbol='BTC-USDT-SWAP')
    pprint(get_exchangeInfo)

    # 获取可以交易的永续合约产品列表
    get_symbols_trading_on = okxSWAP.market.get_symbols_trading_on()
    pprint(get_symbols_trading_on)

    # 获取不可以交易的永续合约产品列表
    get_symbols_trading_off = okxSWAP.market.get_symbols_trading_off()
    pprint(get_symbols_trading_off)
