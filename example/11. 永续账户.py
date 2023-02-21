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
