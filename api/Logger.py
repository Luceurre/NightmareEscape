from api.EnumAuto import EnumAuto


class LOG_LEVEL(EnumAuto):
    ERROR = ()
    INFO = ()
    WARNING = ()
    DEBUG = ()


class Logger:
    LOG_LEVEL = LOG_LEVEL.INFO
    LOG_PRINT = {
        LOG_LEVEL.ERROR: "ERROR",
        LOG_LEVEL.INFO: "INFO",
        LOG_LEVEL.WARNING: "WARNING",
        LOG_LEVEL.DEBUG: "DEBUG"
    }

    @classmethod
    def set_log_level(cls, log_level):
        Logger.LOG_LEVEL = log_level

    def log(self, message, level):
        if (level.value <= type(self).LOG_LEVEL.value):
            print("[", type(self).LOG_PRINT[level], "] ", self, ": ", message, sep="")

    def info(self, message):
        self.log(message, LOG_LEVEL.INFO)

    def warning(self, message):
        self.log(message, LOG_LEVEL.WARNING)

    def debug(self, message):
        self.log(message, LOG_LEVEL.DEBUG)