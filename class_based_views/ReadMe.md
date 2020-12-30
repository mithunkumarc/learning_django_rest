
class handling request in views.py sample : 

        class StudentAPI(APIView):
          def get(self, request, pk = None, format = None):
            ...

urls sample : 

        path('studentapi/<int:pk>', views.StudentAPI.as_view()), 
