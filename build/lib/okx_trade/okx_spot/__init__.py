from okx_trade.okx_spot.account import AccountSPOT
from okx_trade.okx_spot.market import MarketSPOT
from okx_trade.okx_spot.trade import TradeSPOT


class OkxSPOT():
    def __init__(self,
                 key: str,
                 secret: str,
                 passphrase: str,
                 timezone: str = 'Asia/Shanghai'):
        self.account = AccountSPOT(
            key=key, secret=secret, passphrase=passphrase
        )
        self.market = MarketSPOT(
            key=key, secret=secret, passphrase=passphrase, timezone=timezone
        )
        self.trade = TradeSPOT(
            key=key, secret=secret, passphrase=passphrase,
            timezone=timezone,
            account=self.account,
            market=self.market,
        )
        self.timezone = timezone
