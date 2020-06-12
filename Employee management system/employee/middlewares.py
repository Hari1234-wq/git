class RoleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        #one time configuration and initialization.



    def __call__(self, request):
        """code  to be execute for each request before the veiewb(and letar middlleware) are called."""
        response = self.get_response(request)

        """code to execute for each request/response after the view is called."""
        return response

    def process_view(self, request, view_func, *view_arges, **view_kargs):
        """ called just befour django calls the view. return either none or HttpRespons"""
        if request.user.is_authenticated:
            request.role = None
            groups = request.user.groups.all()
            if groups:
                request.role = groups[0].name





#   def process_exception(self,request, exception):
#        """called for the response if exception is raiesd by view. return either none or HttpResponse"""
#
#        pass
#
#    def procrss_template_response(self, request, response):
#        """request - HttpResponse object.
#        response - TemplateRespnse object
#        return templateresponse using for this changing template or context if this is needs.
#       """
#        pass
