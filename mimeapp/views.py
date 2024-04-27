from django.http import HttpResponse
from django.views import View

# Create your views here.
data = """<table><tr><th>eid</th><th>ename</th><th>esal</th></tr>
        <tr><td>1001</td><td>siva</td><td>2000</td></tr>
        <tr><td>1002</td><td>nithin</td><td>3000</td></tr> 
        <tr><td>1003</td><td>chandu</td><td>4000</td></tr> </table>"""
class htmlview(View):
    def get(self, request):
        return HttpResponse(data, content_type="text/html")
class excelview(View):
    def get(self, request):
        return HttpResponse(data, content_type="application/vnd.ms-excel")
class xmlview(View):
    def get(self, request):
        return HttpResponse(data, content_type="application/xml")
class jsonview(View):
    def get(self,request):
        return HttpResponse(data,content_type="application/json")

