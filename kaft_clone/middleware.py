def session_check_middleware(get_response):
    def middleware(request):
        if not request.session.session_key:
            request.session.save()
        response=get_response(request)

        return response
    
    return middleware