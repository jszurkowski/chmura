import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse(
        "Hello Word\nJakub Szurkowski\nnr albumu: 67667",
        status_code=200
    )
