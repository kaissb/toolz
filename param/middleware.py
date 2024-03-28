def debug_cors(get_response):
    def middleware(request):
        print("Origin: %s", request.headers.get("Origin"))
        response = get_response(request)
        print("AC Header: %s", request.headers.get("Access-Control-Allow-Origin"))
        return response

    return middleware
