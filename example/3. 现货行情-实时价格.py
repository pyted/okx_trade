from okx_trade import OkxSPOT
from pprint import pprint

if __name__ == '__main__':
    KEY = '****'
    SECRET = '****'
    PASSPHRASE = '****'

    okxSPOT = OkxSPOT(key=KEY, secret=SECRET, passphrase=PASSPHRASE)
    # 获取全部现货产品的实时行情数据列表
    get_tickers = okxSPOT.market.get_tickers()
    pprint(get_tickers)
    # 获取全部现货产品的实时行情数据字典
    get_tickersMap = okxSPOT.market.get_tickersMap()
    pprint(get_tickersMap)
    # 获取单个现货产品的实时行情数据
    get_ticker = okxSPOT.market.get_ticker('BTC-USDT')
    pprint(get_ticker)
    # 获取单个现货产品的交易深度
    get_books = okxSPOT.market.get_books('BTC-USDT', sz=10)
    pprint(get_books)
    # 获取单个现货产品的轻量交易深度
    get_books_lite = okxSPOT.market.get_books_lite('BTC-USDT')
    pprint(get_books_lite)
