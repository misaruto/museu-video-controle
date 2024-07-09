from flask import jsonify
from src.dto.response_dto import ResponseErrorDto, ResponseSuccessDto

def resp_ok(status=200,resource="", message="", data=None, **extras):
    """
    Responses ok
    """
    if not resource:
        resource = ""

    if not message:
        message = "The request was successful"

    response_model = ResponseSuccessDto(
        status=status,
        message=message,
        resource=resource,
        dados=data,
    )

    response = response_model.model_dump()

    response.update(extras)
    resp = jsonify(response)
    resp.status_code = status

    return resp

def resp_error(status=400,resource="", errors={}, msg="",transaction_id=""):
    """
    Responses ERROR
    """
    response_model = ResponseErrorDto(
        status=status,
        message=msg,
        resource=resource,
        errors=errors,
        transactionId=transaction_id
    )

    resp = jsonify(response_model.model_dump())

    resp.status_code = status

    return resp