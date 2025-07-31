class CustomException(Exception):
    def __init__(self, status_code, error_message):
        self.status_code = status_code
        self.detail = error_message

    def to_dict(self):
        exception_result = dict()
        exception_result['error_message'] = self.detail
        return exception_result


class NotFoundEx(CustomException):
    pass


class ValueNotFoundEx(NotFoundEx):
    def __init__(self, error_message):
        status_code = 400
        super().__init__(status_code, error_message)


class DatabaseEx(CustomException):
    pass


class FailToInsertion(DatabaseEx):
    def __init__(self, error_message):
        status_code = 400
        super().__init__(status_code, error_message)


class FailToUpdate(DatabaseEx):
    def __init__(self, error_message):
        status_code = 400
        super().__init__(status_code, error_message)


class InternalServerError(CustomException):
    def __init__(self, error_message):
        status_code = 500
        super().__init__(status_code, error_message)