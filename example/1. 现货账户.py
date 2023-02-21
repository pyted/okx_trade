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
