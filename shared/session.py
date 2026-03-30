class Session:
    __is_authenticated: bool = False
    __user_id: int = None

    @classmethod
    def is_authenticated(cls) -> bool:
        return cls.__is_authenticated
    
    @classmethod
    def login(cls, user_id: int) -> None:
        cls.__is_authenticated = True
        cls.__user_id = user_id

    @classmethod
    def logout(cls) -> None:
        cls.__user_id = None
        cls.__is_authenticated = False

    @classmethod
    def get_identity(cls) -> int:
        return cls.__user_id