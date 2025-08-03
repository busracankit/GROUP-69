
from fastapi import HTTPException, status

class CredentialsException(HTTPException):
    def __init__(self, detail: str = "Could not validate credentials"):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail, headers={"WWW-Authenticate": "Bearer"})

class NotFoundException(HTTPException):
    def __init__(self, detail: str = "Resource not found"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

class BadRequestException(HTTPException):
    def __init__(self, detail: str = "Bad request"):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)

class ForbiddenException(HTTPException):
    def __init__(self, detail: str = "Forbidden"):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=detail)
def raise_credentials_exception():
    raise CredentialsException()

def raise_not_found_exception(detail: str = "Resource not found"):
    raise NotFoundException(detail)

def raise_bad_request_exception(detail: str = "Bad request"):
    raise BadRequestException(detail)

def raise_forbidden_exception(detail: str = "Forbidden"):
    raise ForbiddenException(detail)
