import falcon
import json


class BodyParser:

    def process_request(self, req, resp):
        try:
            if req.method.upper() in ['POST', 'PUT', 'PATCH']:
                stream = req.stream.read()
                if not stream:
                    req.context['body'] = {}
                    return
                req.context['body'] = json.loads(stream)
        except ValueError as e:
            raise falcon.HTTPBadRequest(description=str(e))
