class CustomExpetion(Exception):
    def __init__(self, message, value) -> None:
        self.message = message
        self.value = value

        super().__init__(message)
    
    def __str__(self) -> str:
        return f"{self.message}: {self.value}"