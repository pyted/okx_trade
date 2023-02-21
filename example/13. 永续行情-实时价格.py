from okx_trade import OkxSWAP
from pprint import pprint

if __name__ == '__main__':
    KEY = '****'
    SECRET = '****'
    PASSPHRASE = '****'

    okxSWAP = OkxSWAP(key=KEY, secret=SECRET, passphrase=PASSPHRASE)
    # 获取全部永续合约产品的实时行情数据列表
    get_tickers = okxSWAP.market.get_tickers()
    pprint(get_tickers)
    # 获取全部永续合约产品的实时行情数据字典
    get_tickersMap = okxSWAP.market.get_tickersMap()
    pprint(get_tickersMap)
    # 获取单个永续合约产品的实时行情数据
    get_ticker = okxSWAP.market.get_ticker('BTC-USDT-SWAP')
    pprint(get_ticker)
    # 获取单个永续合约产品的交易深度
    get_books = okxSWAP.market.get_books('BTC-USDT-SWAP', sz=10)
    pprint(get_books)
    # 获取单个永续合约产品的轻量交易深度
    get_books_lite = okxSWAP.market.get_books_lite('BTC-USDT-SWAP')
    pprint(get_books_lite)
