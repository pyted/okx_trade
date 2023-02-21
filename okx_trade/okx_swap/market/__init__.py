from okx_candle.market import Market


class MarketSWAP(Market):
    def __init__(
            self,
            key: str,
            secret: str,
            passphrase: str,
            timezone='Asia/Shanghai'
    ):
        instType = 'SWAP'
        super(MarketSWAP, self).__init__(
            instType=instType,
            key=key,
            secret=secret,
            passphrase=passphrase,
            timezone=timezone
        )
