from okx_trade import OkxSWAP
from pprint import pprint

if __name__ == '__main__':
    KEY = '****'
    SECRET = '****'
    PASSPHRASE = '****'

    okxSWAP = OkxSWAP(key=KEY, secret=SECRET, passphrase=PASSPHRASE)

    # 获取未成交订单列表
    get_orders_pending = okxSWAP.trade.get_orders_pending()
    pprint(get_orders_pending)
    # 获取未成交的开仓订单列表
    get_orders_pending_open = okxSWAP.trade.get_orders_pending_open()
    pprint(get_orders_pending_open)
    # 获取未成交的平仓订单列表
    get_orders_pending_close = okxSWAP.trade.get_orders_pending_close()
    pprint(get_orders_pending_close)
    # 等待订单成交
    wait_order_FILLED = okxSWAP.trade.wait_order_FILLED(
        instId='MANA-USDT-SWAP',
        ordId='547717986975911936',
        timeout=10,
    )
    pprint(wait_order_FILLED)
    # 获取订单信息
    get_order = okxSWAP.trade.get_order(
        instId='MANA-USDT-SWAP',
        ordId='547717986975911936',
    )
    pprint(get_order)
    # 取消订单
    cancel_order = okxSWAP.trade.cancel_order(
        instId='MANA-USDT-SWAP', ordId='547717986975911936'
    )
    pprint(cancel_order)
