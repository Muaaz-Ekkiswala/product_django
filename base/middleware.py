import time


class LoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time
        response_ms = duration * 1000
        method = str(getattr(request, 'method', '')).upper()
        status_code = str(getattr(response, 'status_code', ''))
        request_path = str(getattr(request, 'path', ''))
        response_dict = {
            "path": request_path,
            "response_time": str(response_ms) + " ms",
            "method": method,
            "status_code": status_code
        }
        print("From middleware: ", response_dict)
        return response
