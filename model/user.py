class User:
    def __init__(self, user_id: int, email: str, pwd: str) -> None:
        self.__id: int = user_id
        self.__email: str = email
        self.__pwd: str = pwd

    def get_id(self) -> int:
        return self.__id

    def get_email(self) -> str:
        return self.__email

    def get_pwd(self) -> str:
        return self.__pwd

    def set_email(self, email: str) -> None:
        self.__email = email

    def set_pwd(self, pwd: str) -> None:
        self.__pwd = pwd

    def set_id(self, id: int) -> None:
        self.__id = id

    @staticmethod
    def get_blank_object() -> User:
        return User(0, "", "")