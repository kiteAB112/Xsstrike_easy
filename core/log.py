import logging
from colors import *

log_file = 'xsstrike.log'
console_log_level = 'info'
file_log_level = None

"""
Default Logging Levels
CRITICAL = 50
ERROR = 40
WARNING = 30
INFO = 20
DEBUG = 10
"""

# add other log levels

VULN_LEVEL_NUM = 60
RUN_LEVEL_NUM = 22
GOOD_LEVEL_NUM = 25

logging.addLevelName(VULN_LEVEL_NUM, 'VULN')
logging.addLevelName(RUN_LEVEL_NUM, 'RUN')
logging.addLevelName(GOOD_LEVEL_NUM, 'GOOD')

# add func of new level log

def _vuln(self, msg, *args, **kwargs):
    if self.isEnabledFor(VULN_LEVEL_NUM):
        self._log(VULN_LEVEL_NUM, msg, args, **kwargs)


def _run(self, msg, *args, **kwargs):
    if self.isEnabledFor(RUN_LEVEL_NUM):
        self._log(RUN_LEVEL_NUM, msg, args, **kwargs)


def _good(self, msg, *args, **kwargs):
    if self.isEnabledFor(GOOD_LEVEL_NUM):
        self._log(GOOD_LEVEL_NUM, msg, args, **kwargs)

logging.Logger.vuln = _vuln
logging.Logger.run = _run
logging.Logger.good = _good

# define log level prefix

log_config = {
    'DEBUG': {
        'value': logging.DEBUG,
        'prefix': '{}[*]{}'.format(yellow, end),
    },
    'INFO': {
        'value': logging.INFO,
        'prefix': info,
    },
    'RUN': {
        'value': RUN_LEVEL_NUM,
        'prefix': run,
    },
    'GOOD': {
        'value': GOOD_LEVEL_NUM,
        'prefix': good,
    },
    'WARNING': {
        'value': logging.WARNING,
        'prefix': '[!!]'.format(yellow, end),
    },
    'ERROR': {
        'value': logging.ERROR,
        'prefix': bad,
    },
    'CRITICAL': {
        'value': logging.CRITICAL,
        'prefix': '{}[--]{}'.format(red, end),
    },
    'VULN': {
        'value': VULN_LEVEL_NUM,
        'prefix': '{}[++]{}'.format(green, red),
    }
}

# define Formatter

class CustomFormatter(logging.Formatter):
    def format(self, record):
        log_level = log_config.get(record.levelname, {})
        record.levelname = log_level.get('prefix', record.levelname)
        return super().format(record)

# define StreamHandler

class CustomStreamHandler(logging.StreamHandler):
    default_terminator = '\n'

    def emit(self, record):
        """
        Overrides emit method to temporally update terminator character in case last log record character is '\r'
        :param record:
        :return:
        """
        if record.msg.endswith('\r'):
            self.terminator = '\r'
            super().emit(record)
            self.terminator = self.default_terminator
        else:
            super().emit(record)



def setup_logger(name='xsstrike'):
    logger = logging.getLogger(name) # logger
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        return logger

    # formatter
    formatter = CustomFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # console handler
    console_handler = CustomStreamHandler()
    console_handler.setLevel(getattr(logging, console_log_level.upper(), logging.INFO))
    console_handler.setFormatter(formatter)

    # addHandler
    logger.addHandler(console_handler)

    return logger


logger = setup_logger()

# 1. 标准日志级别（DEBUG/INFO/WARNING/ERROR/CRITICAL）
logger.debug("调试信息：参数 x = 10")  # 最低级别，通常用于开发调试
logger.info("程序启动成功")           # 普通运行信息
logger.warning("注意：即将达到请求上限")  # 警告信息（不影响运行但需关注）
logger.error("请求失败：连接超时")    # 错误信息（功能受影响）
logger.critical("致命错误：数据库连接中断")  # 最高级别（程序可能终止）

# 2. 自定义日志级别（VULN/RUN/GOOD）
logger.run("运行信息：开始处理请求")

