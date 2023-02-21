from okx_trade import OkxSWAP
from pprint import pprint

if __name__ == '__main__':
    KEY = '****'
    SECRET = '****'
    PASSPHRASE = '****'

    okxSWAP = OkxSWAP(key=KEY, secret=SECRET, passphrase=PASSPHRASE)
    # 获取产品的历史K线数据
    get_history_candle = okxSWAP.market.get_history_candle(
        symbol='BTC-USDT-SWAP',
        start='2023-01-01 00:00:00',
        end='2023-01-01 23:59:00',
        bar='1m',
    )
    pprint(get_history_candle)

    # 获取产品指定数量的最新历史K线数据
    get_history_candle_latest = okxSWAP.market.get_history_candle_latest(
        symbol='BTC-USDT-SWAP',
        length=1440,
        bar='1m',
    )
    pprint(get_history_candle_latest)

    # 获取产品指定日期的历史K线数据
    get_history_candle_by_date = okxSWAP.market.get_history_candle_by_date(
        symbol='BTC-USDT-SWAP',
        date='2023-01-01',
        bar='1m',
    )
    pprint(get_history_candle_by_date)