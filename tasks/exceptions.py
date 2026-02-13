class ClassNotSupported(Exception):
    def __init__(self) -> None:
        self.message = "Заданный учебный класс не поддерживается поставщиком."
        super().__init__(self.message)
