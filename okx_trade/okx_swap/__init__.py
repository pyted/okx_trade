from okx_trade.okx_swap.account import AccountSWAP
from okx_trade.okx_swap.market import MarketSWAP
from okx_trade.okx_swap.trade import TradeSWAP


class OkxSWAP():
    def __init__(self,
                 key: str,
                 secret: str,
                 passphrase: str,
                 timezone: str = 'Asia/Shanghai'):
        self.account = AccountSWAP(
            key=key, secret=secret, passphrase=passphrase
        )
        self.market = MarketSWAP(
            key=key, secret=secret, passphrase=passphrase, timezone=timezone
        )
        self.trade = TradeSWAP(
            key=key, secret=secret, passphrase=passphrase,
            timezone=timezone,
            account=self.account,
            market=self.market,
        )
        self.timezone = timezone
