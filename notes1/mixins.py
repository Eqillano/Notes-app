from django.http import JsonResponse

class AjaxFormMixin(object):
    def form_invalid(self,form):
        if self.request.is_ajax():
           return JsonResponse(form.errors,status=400)
        return super().form_invalid(form)


    def form_valid(self,form):
        form.instance.author = self.request.user
        if self.request.is_ajax():
            # = {
            #'message':'Successfully submitted form data.'}
           return JsonResponse(data)
        return super().form_valid(form)
