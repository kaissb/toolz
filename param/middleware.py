def debug_cors(get_response):
    def middleware(request):
        print("Origin:", request.headers.get("Origin"))
        response = get_response(request)
        print("AC Header:", request.headers.get("Access-Control-Allow-Origin"))
        return response

    return middleware
