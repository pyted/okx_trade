from okx_candle.market import Market


class MarketSPOT(Market):
    def __init__(
            self,
            key: str,
            secret: str,
            passphrase: str,
            timezone='Asia/Shanghai'
    ):
        instType = 'SPOT'
        super(MarketSPOT, self).__init__(
            instType=instType,
            key=key,
            secret=secret,
            passphrase=passphrase,
            timezone=timezone
        )
