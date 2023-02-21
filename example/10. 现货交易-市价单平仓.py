from okx_trade import OkxSPOT
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

    okxSPOT = OkxSPOT(key=KEY, secret=SECRET, passphrase=PASSPHRASE)

    # 市价单平仓
    okxSPOT.trade.close_market(
        instId='MANA-USDT',  # 产品
        quantity='all',  # 平仓数量
        timeout=10,  # 等待订单成功的超时时间
        delay=0.2,  # 检测订单状态的间隔 (秒)
        cancel=True,  # 未完全成交是否取消订单
        callback=callback,  # 开仓成功触发的回调函数
        errorback=errorback,  # 开仓失败触发的回调函数
        newThread=False,  # 是否开启一个新的线程维护这个订单
        tag='',  # 订单标签
        clOrdId='',  # 客户自定义订单ID
        meta={},  # 向回调函数中传递的参数字典
    )
