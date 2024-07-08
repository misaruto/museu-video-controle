from flask import jsonify
from server.src.model.response_model import ResponseErrorModel, ResponseSuccessModel

def resp_ok(status=200,resource="", message="", data=None, **extras):
    """
    Responses ok
    """
    if not resource:
        resource = ""

    if not message:
        message = "The request was successful"

    response_model = ResponseSuccessModel(
        status=status,
        message=message,
        resource=resource,
        dados=data,
    )

    response = response_model.dict()

    response.update(extras)
    resp = jsonify(response)
    resp.status_code = status

    return resp

def resp_error(status=400,resource="", errors={}, msg="",transaction_id=""):
    """
    Responses ERROR
    """
    response_model = ResponseErrorModel(
        status=status,
        message=msg,
        resource=resource,
        errors=errors,
        transactionId=transaction_id
    )

    resp = jsonify(response_model.dict())

    resp.status_code = status

    return resp