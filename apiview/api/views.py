from .models import Data
from .serializers import StudentSerializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

class Studentlist( GenericAPIView,ListModelMixin):
    queryset = Data.objects.all()
    serializer_class = StudentSerializers
    
    def get(self,request,*args,**kwaegs):
        return self.list(request,*args,**kwaegs)
    

class Studentcreate( GenericAPIView,CreateModelMixin):
    queryset = Data.objects.all()
    serializer_class = StudentSerializers
    
    def post(self,request,*args,**kwaegs):
        return self.create(request,*args,**kwaegs)


class Studentcreate( GenericAPIView,RetrieveModelMixin):
    queryset = Data.objects.all()
    serializer_class = StudentSerializers
    
    def get(self,request,*args,**kwaegs):
        return self.retrieve(request,*args,**kwaegs)
    

class Studentupdate( GenericAPIView,UpdateModelMixin):
    queryset = Data.objects.all()
    serializer_class = StudentSerializers
    
    def put(self,request,*args,**kwaegs):
        return self.update(request,*args,**kwaegs)
    

class Studentdelete( GenericAPIView,DestroyModelMixin):
    queryset = Data.objects.all()
    serializer_class = StudentSerializers
    
    def delete(self,request,*args,**kwaegs):
        return self.destroy(request,*args,**kwaegs)
    
