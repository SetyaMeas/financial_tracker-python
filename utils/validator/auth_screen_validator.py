from shared import Result
import re

class AuthScreenValidator():
    def __init__(self):
        pass

    @staticmethod
    def validate_email(email: str) -> Result:
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if re.match(pattern, email) is not None:
            return Result.success(email)
        return Result.fail("Invalid Email Address")
    
    @staticmethod
    def validator_pwd(pwd: str) -> Result:
        if len(pwd) < 1:
            return Result.fail("password must be atleast 8 characters")
        return Result.success(pwd)
    
    @staticmethod
    def format_label(label: str) -> str:
        return f"* {label}"
    