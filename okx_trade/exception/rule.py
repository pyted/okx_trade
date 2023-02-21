from okx_trade.exception._base import AbstractEXP


class RuleException(AbstractEXP):
    def __init__(self, msg):
        self.error_msg = msg
