from okx_trade import OkxSWAP
from pprint import pprint


def callback(information):
    print('callback')
    pprint(information)


def errorback(information):
    print('errorback')
    pprint(information)


if __name__ == '__main__':
    KEY = '****'
    SECRET = '****'
    PASSPHRASE = '****'

    okxSWAP = OkxSWAP(key=KEY, secret=SECRET, passphrase=PASSPHRASE)

    # 限价单平仓
    okxSWAP.trade.close_limit(
        instId='MANA-USDT-SWAP',  # 产品
        tdMode='isolated',  # 持仓方式 isolated：逐仓 cross：全仓
        posSide='long',  # 持仓方向 long：多单 short：空单
        # closePrice=1000,  # 平仓价格 closePrice 和 tpRate必须填写其中一个
        tpRate=0.1,  # 挂单止盈率
        quantityCT='all',  # 平仓数量，注意：quantityCT是合约的张数，不是货币数量
        block=True,  # 是否堵塞
        timeout=10,  # 等待订单成功的超时时间
        delay=0.2,  # 检测订单状态的间隔 (秒)
        cancel=True,  # 未完全成交是否取消订单
        callback=callback,  # 开仓成功触发的回调函数
        errorback=errorback,  # 开仓失败触发的回调函数
        newThread=True,  # 是否开启一个新的线程维护这个订单
        tag='',  # 订单标签
        clOrdId='',  # 客户自定义订单ID
        meta={},  # 向回调函数中传递的参数字典
    )
