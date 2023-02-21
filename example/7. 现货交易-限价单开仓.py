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

    # 限价单开仓
    open_limit = okxSPOT.trade.open_limit(
        instId='MANA-USDT',  # 产品
        openPrice=0.1,  # 开仓价格
        openMoney=4,  # 开仓金额 开仓金额openMoney和开仓数量quantity必须输入其中一个 优先级：quantity > openMoney
        # quantity=10,  # 开仓数量
        block=True,  # 是否以堵塞的模式
        timeout=5,  # 等待订单成功的超时时间（秒）
        delay=0.2,  # 检测订单状态的间隔 (秒)
        cancel=True,  # 订单超时后是否取消
        newThread=False,  # 是否开启一个新的线程维护这个订单
        callback=callback,  # 开仓成功触发的回调函数
        errorback=errorback,  # 开仓失败触发的回调函数
        tag='',  # 订单标签
        clOrdId='',  # 客户自定义订单ID
    )
