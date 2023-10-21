from okx_trade.okx_swap.account import AccountSWAP
from okx_trade.okx_swap.market import MarketSWAP
from okx_trade.okx_swap.trade import TradeSWAP


class OkxSWAP():
    def __init__(self,
                 key: str,
                 secret: str,
                 passphrase: str,
                 timezone: str = 'Asia/Shanghai',
                 proxies={},
                 proxy_host: str = None,
                 ):
        self.account = AccountSWAP(
            key=key, secret=secret, passphrase=passphrase, proxies=proxies, proxy_host=proxy_host,
        )
        self.market = MarketSWAP(
            key=key, secret=secret, passphrase=passphrase, timezone=timezone, proxies=proxies, proxy_host=proxy_host,
        )
        self.trade = TradeSWAP(
            key=key, secret=secret, passphrase=passphrase,
            timezone=timezone,
            account=self.account,
            market=self.market,
            proxies=proxies,
            proxy_host=proxy_host,
        )
        self.timezone = timezone
