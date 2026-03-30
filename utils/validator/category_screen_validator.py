from shared import Result
from model import CategoryType

class CategoryScreenValidator:

    @staticmethod
    def validate_name(value: str) -> Result:
        if len(value) < 1:
            return Result.fail("Name can not be empty")
        return Result.success(value)
    
    @staticmethod
    def validate_type(value: str) -> Result:
        try:
            result = CategoryType(value)
            return Result.success(result)
        except ValueError:
            return Result.fail("Invalid Type")
        
    @staticmethod
    def validate_id(id) -> Result:
        try:
            value = int(id)
            return Result.success(value)
        except ValueError:
            return Result.fail("ID must be an integer")