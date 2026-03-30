from shared import Result
from datetime import datetime, date

class InputValidator:
    @staticmethod
    def is_int(value) -> Result:
        try:
            result = int(value)
            return Result.success(result)
        except ValueError:
            return Result.fail("Value must be an Integer")
        
    @staticmethod
    def is_float_and_greater_than_zero(value) -> Result:
        try:
            result = float(value)
            if result > 0:
                return Result.success(result)
            return Result.fail("Value must be greater than 0")
        except ValueError:
            return Result.fail("Value must be a number")
        
    @staticmethod
    def valid_date(value, format: str) -> Result:
        try:
            result = date.strptime(value, format)
            return Result.success(result)
        except ValueError:
            return Result.fail("Invalid date time input")