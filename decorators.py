from exceptions import (
    BadRequestException,
    UnauthorizedException,
    ForbidenException,
    InternalServerErrorException,
)


def siar_exceptions(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)

        msg = response.json()["MensajeRespuesta"]

        if response.status_code == 400:
            raise BadRequestException(msg)

        if response.status_code == 401:
            raise UnauthorizedException(msg)

        if response.status_code == 403:
            raise ForbidenException(msg)

        if response.status_code == 500:
            raise InternalServerErrorException(msg)

        return response

    return wrapper


def response_json(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)

        client = args[0]

        return response.json() if client.json else response

    return wrapper
