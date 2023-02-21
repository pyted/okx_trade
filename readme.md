# Okx_Trade 说明文档

## 1 Okx_Trade介绍

Okx_Trade封装了OKX中现货（SPOT)、永续合约（SWAP）的常用函数，降低量化交易的难度。

## 2 安装Okx_Trade

GITHUB:https://www.github.com/pyted/okx_trade

```cmd
pip3 install okx_trade
```

## 3 快速开始

1.获取现货现货交易BTC-USDT的价格，降价2%挂单买入，买入金额为10000USDT，挂单时间为2小时，如果超时则取消订单。

```python
from okx_trade import OkxSPOT
from pprint import pprint

if __name__ == '__main__':
    okxSPOT = OkxSPOT(
        key='****',
        secret='****',
        passphrase='****',
    )

    # 产品
    instId = 'BTC-USDT'
    # 开仓金额
    openMoney = 10000
    # 购买价格
    askPx = okxSPOT.market.get_ticker(instId)['data']['askPx']  # 卖1价格
    askPx = float(askPx)
    openPrice = askPx * 0.98  # 降价2%
    print(openPrice)
    # 挂单时间
    timeout = 60 * 60 * 2  # 单位秒
    # 超时是否取消订单
    cancel = True
    # 是否堵塞模式
    block = True

    # 限价单开仓
    result = okxSPOT.trade.open_limit(
        instId=instId,  # 产品
        openPrice=openPrice,  # 开仓价格
        openMoney=openMoney,  # 开仓金额 开仓金额openMoney和开仓数量quantity必须输入其中一个 优先级：quantity > openMoney
        timeout=timeout,  # 等待订单成功的超时时间
        cancel=True,  # 订单超时后是否取消
    )
    pprint(result)
```

2.获取永续合约BTC-USDT-SWAP的价格，降价5%，采用逐仓、10倍杠杆、开仓金额10000USDT挂单，挂单时间为2小时，如果超时则取消。

**采用异步的方式管理这个订单，并设置订单成功或失败后的回调函数**

```python
from pprint import pprint
from okx_trade import OkxSWAP


# 成功触发的回调函数
def callback(information):
    '''
    :param information: 交易过程信息字典
        information = {
            'instId': <产品ID>,
            'status': <订单状态>,
            'meta': <传递过来的参数>,
            'request_param': <发送下单请求的具体参数>,
            'func_param': <open_limit中的参数>,
            'get_order_result': <获取订单状态的结果>,
            'set_order_result': <下单提交的结果>,
            'error_result': <异常信息>,
            'cancel_result': <取消订单的结果>,
        }
    '''
    print('callback')
    pprint(information)


# 失败触发的回调函数
def errorback(information):
    '''
    :param information: 交易过程信息字典
        information = {
            'instId': <产品ID>,
            'status': <订单状态>,
            'meta': <传递过来的参数>,
            'request_param': <发送下单请求的具体参数>,
            'func_param': <open_limit中的参数>,
            'get_order_result': <获取订单状态的结果>,
            'set_order_result': <下单提交的结果>,
            'error_result': <异常信息>,
            'cancel_result': <取消订单的结果>,
        }
    '''
    print('errorback')
    pprint(information)


if __name__ == '__main__':
    okxSWAP = OkxSWAP(
        key='****',
        secret='****',
        passphrase='****',
    )

    # 产品
    instId = 'BTC-USDT-SWAP'
    # 开仓金额
    openMoney = 10000
    # 购买价格
    askPx = okxSWAP.market.get_ticker(instId)['data']['askPx']  # 卖1价格
    askPx = float(askPx)
    openPrice = askPx * 0.98  # 降价2%
    print(openPrice)
    # 挂单时间
    timeout = 60 * 60 * 2  # 单位秒
    # 超时是否取消订单
    cancel = True
    # 是否堵塞模式
    block = True

    # 限价单开仓
    result = okxSWAP.trade.open_limit(
        instId=instId,  # 产品
        openPrice=openPrice,  # 开仓价格
        tdMode='isolated',  # 持仓方式 isolated：逐仓 cross：全仓
        posSide='long',  # 持仓方向 long：多单 short：空单
        lever=10,  # 杠杆
        openMoney=openMoney,  # 开仓金额 开仓金额openMoney和开仓数量quantityCT必须输入其中一个 优先级：quantity > openMoney
        quantityCT=None,  # 合约张数为空
        block=True,  # 是否以堵塞的模式
        timeout=timeout,  # 等待订单成功的超时时间（秒）
        delay=0.2,  # 检测订单状态的间隔 (秒)
        cancel=True,  # 订单超时后是否取消
        newThread=False,  # 是否开启一个新的线程维护这个订单
        callback=callback,  # 开仓成功触发的回调函数
        errorback=errorback,  # 开仓失败触发的回调函数
        tag='',  # 订单标签
        clOrdId='',  # 客户自定义订单ID
    )
```

3.对于永续合约以当前BTC-USDT-SWAP的价格，止盈20%**全部**挂单买入平空，超时时间2小时，超时后取消订单，并设置回调函数。

```python
from pprint import pprint
from okx_trade import OkxSWAP


# 成功触发的回调函数
def callback(information):
    '''
    :param information: 交易过程信息字典
        information = {
            'instId':<产品ID>,
            'status': <订单状态>,
            'meta': <传递过来的参数>,
            'request_param': <发送下单请求的具体参数>,
            'func_param': <open_limit中的参数>,
            'get_order_result': <获取订单状态的结果>,
            'set_order_result': <下单提交的结果>,
            'error_result': <异常信息>,
            'cancel_result': <取消订单的结果>,
        }
    '''
    print('callback')
    pprint(information)


# 失败触发的回调函数
def errorback(information):
    '''
    :param information: 交易过程信息字典
        information = {
            'instId':<产品ID>,
            'status': <订单状态>,
            'meta': <传递过来的参数>,
            'request_param': <发送下单请求的具体参数>,
            'func_param': <open_limit中的参数>,
            'get_order_result': <获取订单状态的结果>,
            'set_order_result': <下单提交的结果>,
            'error_result': <异常信息>,
            'cancel_result': <取消订单的结果>,
        }
    '''
    print('errorback')
    pprint(information)


if __name__ == '__main__':
    okxSWAP = OkxSWAP(
        key='****',
        secret='****',
        passphrase='****',
    )
    # 产品
    instId = 'BTC-USDT-SWAP'
    # 挂单时间
    timeout = 60 * 60 * 2  # 单位秒
    # 超时是否取消订单
    cancel = True
    # 是否堵塞模式
    block = True

    # 限价单开仓
    result = okxSWAP.trade.close_limit(
        instId=instId,  # 产品
        tpRate=0.2,  # 止盈率 20%
        # 平多 positionSide="LONG":   closePrice = askPx * (1 + abs(tpRate))
        # 平空 positionSide="SHORT":  closePrice = bidPx * (1 - abs(tpRate))
        tdMode='isolated',  # 持仓方式 isolated：逐仓 cross：全仓
        posSide='long',  # 持仓方向 long：多单 short：空单
        quantityCT='all',  # 合约张数为空 'all' 表示全部
        block=True,  # 是否以堵塞的模式
        timeout=60 * 60 * 2,  # 等待订单成功的超时时间（秒）
        delay=0.2,  # 检测订单状态的间隔 (秒)
        cancel=True,  # 订单超时后是否取消
        newThread=False,  # 是否开启一个新的线程维护这个订单
        callback=callback,  # 开仓成功触发的回调函数
        errorback=errorback,  # 开仓失败触发的回调函数
        tag='',  # 订单标签
        clOrdId='',  # 客户自定义订单ID
    )
    pprint(result)
```

## 4 现货产品 OkxSPOT

### 4.1 现货账户

便捷函数：

|函数名|说明|
|:---|:---|  
|get_balancesMap|查看账户余额字典|
|get_balances|查看账户余额列表|  
|get_balance|获取单个币种的余额|

```python
from okx_trade import OkxSPOT
from pprint import pprint

if __name__ == '__main__':
    KEY = '****'
    SECRET = '****'
    PASSPHRASE = '****'
    okxSPOT = OkxSPOT(key=KEY, secret=SECRET, passphrase=PASSPHRASE)
    # 获取产品的余额
    get_balance1 = okxSPOT.account.get_balance(instId='MANA-USDT')
    pprint(get_balance1)
    # 获取币种的余额
    get_balance2 = okxSPOT.account.get_balance(ccy='USDT')
    pprint(get_balance2)
    # 获取全部资产余额列表
    get_balances = okxSPOT.account.get_balances()
    pprint(get_balances)
    # 获取全部资产余额字典
    get_balancesMap = okxSPOT.account.get_balancesMap()
    pprint(get_balancesMap)
```

### 4.2 现货行情

#### 4.2.1 现货产品规则信息

便捷函数：

|函数名|说明|
|:---|:---|  
|get_exchangeInfos|获取全部现货交易规则与交易对|
|get_exchangeInfo|获取单个现货交易规则与交易对|  
|get_symbols_trading_on|获取可以交易的现货产品列表|
|get_symbols_trading_off|获取不可交易的现货产品列表|

```python
from okx_trade import OkxSPOT
from pprint import pprint

if __name__ == '__main__':
    KEY = '****'
    SECRET = '****'
    PASSPHRASE = '****'

    okxSPOT = OkxSPOT(key=KEY, secret=SECRET, passphrase=PASSPHRASE)
    # 获取现货全部产品的交易规则
    get_exchangeInfos = okxSPOT.market.get_exchangeInfos()
    pprint(get_exchangeInfos)
    # 获取单个现货产品的交易规则
    get_exchangeInfo = okxSPOT.market.get_exchangeInfo(symbol='BTC-USDT')
    pprint(get_exchangeInfo)
    # 获取可以交易的现货产品列表
    get_symbols_trading_on = okxSPOT.market.get_symbols_trading_on()
    pprint(get_symbols_trading_on)
    # 获取不可以交易的现货产品列表
    get_symbols_trading_off = okxSPOT.market.get_symbols_trading_off()
    pprint(get_symbols_trading_off)
```

#### 4.2.2 现货实时价格

便捷函数：

|函数名|说明|
|:---|:---|  
|get_tickers|获取全部现货产品的实时行情数据列表|
|get_tickersMap|获取全部现货产品的实时行情数据字典|
|get_ticker|获取单个现货产品的实时行情数据|
|get_books|获取单个现货产品的交易深度|
|get_books_lite|获取单个现货产品的轻量交易深度|


```python
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
```

#### 4.2.3 现货历史K线

便捷函数：

|函数名|说明|
|:---|:---|  
|get_history_candle|获取产品的历史K线数据|
|get_history_candle_latest|获取产品指定数量的最新历史K线数据|
|get_history_candle_by_date|获取产品指定日期的历史K线数据|


```python
from okx_trade import OkxSPOT
from pprint import pprint

if __name__ == '__main__':
    KEY = '****'
    SECRET = '****'
    PASSPHRASE = '****'

    okxSPOT = OkxSPOT(key=KEY, secret=SECRET, passphrase=PASSPHRASE)
    # 获取产品的历史K线数据
    get_history_candle = okxSPOT.market.get_history_candle(
        symbol='BTC-USDT',
        start='2023-01-01 00:00:00',
        end='2023-01-01 23:59:00',
        bar='1m',
    )
    pprint(get_history_candle)

    # 获取产品指定数量的最新历史K线数据
    get_history_candle_latest = okxSPOT.market.get_history_candle_latest(
        symbol='BTC-USDT',
        length=1440,
        bar='1m',
    )
    pprint(get_history_candle_latest)

    # 获取产品指定日期的历史K线数据
    get_history_candle_by_date = okxSPOT.market.get_history_candle_by_date(
        symbol='BTC-USDT',
        date='2023-01-01',
        bar='1m',
    )
    pprint(get_history_candle_by_date)
```

### 4.3 现货交易

#### 4.3.1 现货交易基础订单

便捷函数：

|函数名|说明|
|:---|:---|
|set_order|普通下单购买|  
|get_order|查询订单|  
|get_orders_pending|获取未成交订单列表|
|get_orders_pending_open|获取未成交的开仓订单列表|
|get_orders_pending_close|获取未成交的平仓订单列表|
|cancel_order|撤销订单|
|wait_order_FILLED|等待订单成交|

```python
from okx_trade import OkxSPOT
from pprint import pprint

if __name__ == '__main__':
    KEY = '****'
    SECRET = '****'
    PASSPHRASE = '****'
    okxSPOT = OkxSPOT(key=KEY, secret=SECRET, passphrase=PASSPHRASE)

    # 获取未成交订单列表
    get_orders_pending = okxSPOT.trade.get_orders_pending()
    pprint(get_orders_pending)
    # 获取未成交的开仓订单列表
    get_orders_pending_open = okxSPOT.trade.get_orders_pending_open()
    pprint(get_orders_pending_open)
    # 获取未成交的平仓订单列表
    get_orders_pending_close = okxSPOT.trade.get_orders_pending_close()
    pprint(get_orders_pending_close)
    # 等待订单成交
    wait_order_FILLED = okxSPOT.trade.wait_order_FILLED(
        instId='MANA-USDT',
        ordId='547717986975911936',
        timeout=10,
    )
    pprint(wait_order_FILLED)
    # 获取订单信息
    get_order = okxSPOT.trade.get_order(
        instId='MANA-USDT',
        ordId='547717986975911936',
    )
    pprint(get_order)
    # 取消订单
    cancel_order = okxSPOT.trade.cancel_order(
        instId='MANA-USDT', ordId='547717986975911936'
    )
    pprint(cancel_order)
```

#### 4.3.2 现货下单价格与数量

便捷函数：

|函数名|说明|
|:---|:---|
|round_quantity|圆整下单数量|
|round_price|圆整开仓价格|
|get_quantity|根据开仓金额、开仓价格与杠杆计算最大可开仓数量|
|quantity_to_f|将下单数量转化为字符串|
|price_to_f|将下单价格转化为字符串|

```python
from pprint import pprint
from okx_trade import OkxSPOT

if __name__ == '__main__':
    KEY = '****'
    SECRET = '****'
    PASSPHRASE = '****'

    okxSPOT = OkxSPOT(key=KEY, secret=SECRET, passphrase=PASSPHRASE)
    # 圆整下单数量
    round_quantity_result = okxSPOT.trade.round_quantity(
        quantity=0.00023234234234,
        instId='MANA-USDT',
        ordType='market',  # market | limit
    )
    pprint(round_quantity_result)
    # 圆整下单价格
    round_price_result = okxSPOT.trade.round_price(
        price=20.123123123,
        instId='MANA-USDT',
        type='FLOOR',  # FLOOR:向下圆整 CEIL:向上圆整
    )
    pprint(round_price_result)
    # 根据开仓金额、开仓价格与杠杆计算最大可开仓数量
    get_quantity_result = okxSPOT.trade.get_quantity(
        openPrice=2.123123,
        openMoney=20,
        instId='MANA-USDT',
        ordType='limit',
        leverage=1
    )
    pprint(get_quantity_result)
    # 将下单数量转化为字符串
    quantity_to_f_result = okxSPOT.trade.quantity_to_f(
        quantity=get_quantity_result['data'],
        instId='MANA-USDT',
    )
    pprint(quantity_to_f_result)
    # 将下单价格转化为字符串
    price_to_f_result = okxSPOT.trade.price_to_f(
        price=round_price_result['data'],
        instId='MANA-USDT',
    )
    pprint(price_to_f_result)
```

#### 4.3.3 现货限单价开仓

便捷函数：

|函数名|说明|
|:---|:---|
|open_limit|限价单开仓|

```python
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
```

#### 4.3.4 现货市价单开仓

便捷函数：

|函数名|说明|
|:---|:---|
|open_market|市价单开仓|

```python
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

    # 市价单开仓
    open_market_result = okxSPOT.trade.open_market(
        instId='MANA-USDT',  # 产品
        quantity=3,  # 开仓数量
        # openMoney=3, 开仓金额 开仓金额openMoney和开仓数量quantity必须输入其中一个 优先级：quantity > openMoney
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
```

#### 4.3.5 现货限价单平仓

便捷函数：

|函数名|说明|
|:---|:---|
|close_limit|限价单平仓|

```python
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

    # 市价单开仓
    open_market_result = okxSPOT.trade.open_market(
        instId='MANA-USDT',  # 产品
        quantity=3,  # 开仓数量
        # openMoney=3, 开仓金额 开仓金额openMoney和开仓数量quantity必须输入其中一个 优先级：quantity > openMoney
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
```

#### 4.3.6 现货市价单平仓

便捷函数：

|函数名|说明|
|:---|:---|
|close_market|市价单平仓|

```python
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

    # 限价单平仓
    okxSPOT.trade.close_limit(
        instId='MANA-USDT',  # 产品
        # closePrice=1000,  # 平仓价格 closePrice 和 tpRate必须填写其中一个
        tpRate=0.1,  # 挂单止盈率
        quantity='all',  # 平仓数量
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
```

## 5 永续合约 OkxSWAP

### 5.1 永续账户

便捷函数：

|函数名|说明|
|:---|:---|  
|get_balance|获取币种的余额|
|set_position_mode|设置持仓模式|  
|set_leverage|设置杠杆|
|get_leverage|获取杠杆|

```python
from okx_trade import OkxSWAP
from pprint import pprint

if __name__ == '__main__':
    KEY = '****'
    SECRET = '****'
    PASSPHRASE = '****'

    okxSWAP = OkxSWAP(key=KEY, secret=SECRET, passphrase=PASSPHRASE)
    # 获取币种的余额
    get_balance = okxSWAP.account.get_balance(ccy='USDT')
    pprint(get_balance)
    # 设置持仓模式
    set_position_mode = okxSWAP.account.set_position_mode(
        posMode='long_short_mode',
    )
    pprint(set_position_mode)
    # 设置逐仓杠杆（多仓）
    set_leverage_isolated_long = okxSWAP.account.set_leverage(
        lever=4,
        instId='MANA-USDT-SWAP',
        mgnMode='isolated',
        posSide='long',
    )
    pprint(set_leverage_isolated_long)
    # 设置逐仓杠杆（空仓）
    set_leverage_isolated_short = okxSWAP.account.set_leverage(
        lever=5,
        instId='MANA-USDT-SWAP',
        mgnMode='isolated',
        posSide='short',
    )
    pprint(set_leverage_isolated_short)
    # 获取逐仓杠杆
    get_leverage_isolated = okxSWAP.account.get_leverage(
        instId='MANA-USDT-SWAP',
        mgnMode='isolated',
    )
    pprint(get_leverage_isolated)
    # 设置全仓杠杆
    set_leverage_cross = okxSWAP.account.set_leverage(
        lever=4,
        instId='MANA-USDT-SWAP',
        mgnMode='cross',
        posSide='',
    )
    pprint(set_leverage_cross)
    # 获取逐仓杠杆
    get_leverage_cross = okxSWAP.account.get_leverage(
        instId='MANA-USDT-SWAP',
        mgnMode='cross',
    )
    pprint(get_leverage_cross)
```

### 5.2 永续行情

#### 5.2.1 永续产品规则信息

便捷函数：

|函数名|说明|
|:---|:---|  
|get_exchangeInfos|获取全部永续合约交易规则与交易对|
|get_exchangeInfo|获取单个永续合约交易规则与交易对|  
|get_symbols_trading_on|获取可以交易的永续合约产品列表|
|get_symbols_trading_off|获取不可交易的永续合约产品列表|


```python
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
```

#### 5.2.2 永续实时价格

便捷函数：

|函数名|说明|
|:---|:---|  
|get_tickers|获取全部永续合约的实时行情数据列表|
|get_tickersMap|获取全部永续合约的实时行情数据字典|
|get_ticker|获取单个永续合约产品的实时行情数据|
|get_books|获取单个永续合约产品的交易深度|
|get_books_lite|获取单个永续合约产品的轻量交易深度|

```python
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
```

#### 5.2.3 永续历史K线

便捷函数：

|函数名|说明|
|:---|:---|  
|get_history_candle|获取产品的历史K线数据|
|get_history_candle_latest|获取产品指定数量的最新历史K线数据|
|get_history_candle_by_date|获取产品指定日期的历史K线数据|


```python
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
```


### 5.3 永续交易

#### 5.3.1 永续交易基础订单

便捷函数：

|函数名|说明|
|:---|:---|
|set_order|普通下单购买|  
|get_order|查询订单|  
|get_orders_pending|获取未成交订单列表|
|get_orders_pending_open|获取未成交的开仓订单列表|
|get_orders_pending_close|获取未成交的平仓订单列表|
|cancel_order|撤销订单|
|wait_order_FILLED|等待订单成交|

```python
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
```

#### 5.3.2 永续下单价格与数量

便捷函数：

|函数名|说明|
|:---|:---|
|round_quantity|圆整下单数量|
|round_price|圆整下单价格|
|get_quantity|根据开仓金额、开仓价格与杠杆计算最大可开仓数量|
|quantity_to_f|将下单数量转化为字符串|
|price_to_f|将下单价格转化为字符串|


```python
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
```

#### 5.3.3 永续限单价开仓

便捷函数：

|函数名|说明|
|:---|:---|
|open_limit|限价单开仓|


```python
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

    # 限价单开仓
    open_limit = okxSWAP.trade.open_limit(
        instId='MANA-USDT-SWAP',  # 产品
        tdMode='isolated',  # 持仓方式 isolated：逐仓 cross：全仓
        posSide='long',  # 持仓方向 long：多单 short：空单
        lever=1,  # 杠杆倍数
        openPrice=0.1,  # 开仓价格
        openMoney=4,  # 开仓金额 开仓金额openMoney和开仓数量quantityCT必须输入其中一个 优先级：quantityCT > openMoney
        # quantityCT=1,  # 开仓数量 注意：quantityCT是合约的张数，不是货币数量
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
```

#### 5.3.4 永续市价单开仓

便捷函数：

|函数名|说明|
|:---|:---|
|open_market|市价单开仓|

```python
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
```
#### 5.3.5 永续限价单平仓

便捷函数：

|函数名|说明|
|:---|:---|
|close_limit|限价单平仓|

```python
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
```

#### 5.3.6 永续市价单平仓

便捷函数：

|函数名|说明|
|:---|:---|
|close_market|市价单平仓|

```python
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

    # 市价单平仓
    okxSWAP.trade.close_market(
        instId='MANA-USDT-SWAP',  # 产品
        tdMode='isolated',  # 持仓方式 isolated：逐仓 cross：全仓
        posSide='long',  # 持仓方向 long：多单 short：空单
        quantityCT='all',  # 平仓数量，注意：quantityCT是合约的张数，不是货币数量
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
```