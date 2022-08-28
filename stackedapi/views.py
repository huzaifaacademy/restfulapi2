from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employees
from .serializers import EmployeesSerializer
from django.http import HttpResponse

class EmployeesListApiView(APIView):

    def get(self, request):
        employees = Employees.objects.all()
        serializer = EmployeesSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = {
            "name":request.data.get("name"),
            "email":request.data.get("email"),
            "phone":request.data.get("phone")
        }
        serailizer = EmployeesSerializer(data=data)
        if serailizer.is_valid():
            serailizer.save()
            return Response("serializer.data, status=status.HTTP_201_CREATED")
        return Response(serailizer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetailAPIView(APIView):

    def get_object(self, id):
        try:
            return Employees.objects.get(pk=id)
        except:
            return None

    def dataDoesNotExist(self):
        return Response(
                {"res": "employee does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def get(self, request, id, *args, **kwargs):
        employee = self.get_object(id=id)
        if not employee:
            return self.dataDoesNotExist()
        serializer = EmployeesSerializer(instance=employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, *args, **kwargs):
        employee = self.get_object(id=id)
        if not employee:
            return self.dataDoesNotExist()
        serializer = EmployeesSerializer(instance=employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        employee = self.get_object(id=id)
        if not employee:
            return self.dataDoesNotExist()
        employee.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


