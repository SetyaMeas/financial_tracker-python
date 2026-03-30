class Result:
    __is_success = False
    __error_msg = None
    __value = None

    def __init__(self, value=None, is_success: bool=False, error_message: str=None):
        self.__value = value
        self.__is_success = is_success
        self.__error_msg = error_message

    @staticmethod
    def success(value) -> Result:
        return Result(value=value, is_success=True)
    
    @staticmethod
    def fail(error_message: str) -> Result:
        return Result(is_success=False, error_message=error_message)
    
    def is_success(self) -> bool:
        return self.__is_success
    
    def get_value(self):
        return self.__value
    
    def get_error_msg(self) -> str:
        return self.__error_msg