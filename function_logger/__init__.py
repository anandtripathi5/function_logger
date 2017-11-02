from functools import wraps


def function_logger(logging):
    def wrap(func):
        @wraps(func)
        def function_log(*args,     **kwargs):
            logging.debug(
                "Inside Function {} with parameters: {},{}".format(
                    func.__name__,
                    args,
                    kwargs
                )
            )
            return_param = func(*args, **kwargs)
            logging.debug(
                "Function: {} returns {}".format(
                    func.__name__,
                    return_param
                )
            )
            return return_param
        return function_log
    return wrap
