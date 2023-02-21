from okx_trade.exception._base import AbstractEXP


class CodeException(AbstractEXP):
    def __init__(self, msg):
        self.error_msg = msg


class RequestException(AbstractEXP):
    def __init__(self, msg):
        self.error_msg = msg
