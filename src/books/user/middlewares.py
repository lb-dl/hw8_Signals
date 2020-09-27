from time import time
from user.models import Logger


class Loggers:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        methods = request.method
        Logger.objects.create(method=methods)
        start = time()
        response = self.get_response(request)
        response_times = start - time()
        Logger.objects.create(response_time=response_times)
        return response
