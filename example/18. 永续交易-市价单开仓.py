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

    # 市价单开仓
    open_market_result = okxSWAP.trade.open_market(
        instId='MANA-USDT-SWAP',  # 产品
        tdMode='isolated',  # 持仓方式 isolated：逐仓 cross：全仓
        posSide='long',  # 持仓方向 long：多单 short：空单
        lever=1,  # 杠杆倍数
        openMoney=4,  # 开仓金额 开仓金额openMoney和开仓数量quantityCT必须输入其中一个 优先级：quantityCT > openMoney
        # quantityCT=1,  # 开仓数量 注意：quantityCT是合约的张数，不是货币数量
        timeout=10,  # 等待订单成功的超时时间（秒）
        delay=0.2,  # 检测订单状态的间隔 (秒)
        cancel=True,  # 订单超时后是否取消
        callback=callback,  # 开仓成功触发的回调函数
        errorback=errorback,  # 开仓失败触发的回调函数
        newThread=True,  # 是否开启一个新的线程维护这个订单
        tag='',  # 订单标签
        clOrdId='',  # 客户自定义订单ID
        meta={},  # 向回调函数中传递的参数字典
    )