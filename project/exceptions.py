'''
HTTP customized exceptions base on HTTPException of werkzeug.
'''
from flask.wrappers import Response
import json
from werkzeug.exceptions import HTTPException


class CustomJsonHTTPException(HTTPException):
    '''
    It is a HTTP response in form of JSON with the correct HTTP error code.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        json_response = json.dumps({"Error": self.description})
        self.response = Response(
            content_type='application/json; charset=utf-8')

        self.response.response = json_response
        self.response.headers.add('content-length', len(json_response))

        self.response.status_code = self.code


class BadRequestRequeredFieldNotFound(CustomJsonHTTPException):
    code = 400

    def __init__(self, field):
        self.description = "Field " + field + \
            " was required but it was not found"
        super().__init__()


class BadRequestFieldNotAllowed(CustomJsonHTTPException):
    code = 400

    def __init__(self, field):
        self.description = "Field " + field + " is not an expected field"
        super().__init__()


class EntityNotFound(CustomJsonHTTPException):
    code = 404
    description = 'Entity not found'


class Forbidden(CustomJsonHTTPException):
    code = 403
    description = "Forbidden"


class Unauthorized(CustomJsonHTTPException):
    code = 401
    description = "Unauthorized Access"


class BDError(CustomJsonHTTPException):
    code = 500

    def __init__(self, statement):
        self.description = statement
        super().__init__()
