from okx_trade.exception._base import AbstractEXP


class UnexpectedException(AbstractEXP):
    def __init__(self, msg):
        self.error_msg = msg
