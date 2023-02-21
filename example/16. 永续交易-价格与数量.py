from pprint import pprint
from okx_trade import OkxSWAP

if __name__ == '__main__':
    KEY = '****'
    SECRET = '****'
    PASSPHRASE = '****'

    okxSWAP = OkxSWAP(key=KEY, secret=SECRET, passphrase=PASSPHRASE)
    # 圆整下单数量
    round_quantity_result = okxSWAP.trade.round_quantity(
        quantity=0.00023234234234,
        instId='MANA-USDT-SWAP',
        ordType='market',  # market | limit
    )
    pprint(round_quantity_result)
    # 圆整下单价格
    round_price_result = okxSWAP.trade.round_price(
        price=20.123123123,
        instId='MANA-USDT-SWAP',
        type='FLOOR',  # FLOOR:向下圆整 CEIL:向上圆整
    )
    pprint(round_price_result)
    # 根据开仓金额、开仓价格与杠杆计算最大可开仓数量
    get_quantity_result = okxSWAP.trade.get_quantity(
        openPrice=2.123123,
        openMoney=20,
        instId='MANA-USDT-SWAP',
        ordType='limit',
        leverage=1
    )
    pprint(get_quantity_result)
    # 将下单数量转化为字符串
    quantity_to_f_result = okxSWAP.trade.quantity_to_f(
        quantity=get_quantity_result['data'],
        instId='MANA-USDT-SWAP',
    )
    pprint(quantity_to_f_result)
    # 将下单价格转化为字符串
    price_to_f_result = okxSWAP.trade.price_to_f(
        price=round_price_result['data'],
        instId='MANA-USDT-SWAP',
    )
    pprint(price_to_f_result)