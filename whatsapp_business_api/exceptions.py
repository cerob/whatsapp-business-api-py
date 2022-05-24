class SendingMessageFailedException(Exception):

    def __init__(self, code, *args: object) -> None:
        self.code = code
        super().__init__(*args)

    def __str__(self) -> str:
        return 'HTTP error code {code}\n{trace}'.format(code=self.code,
                                                        trace=super().__str__())
