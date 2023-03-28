from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication 
from rest_framework import filters


from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """Test API View """
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = ['1','2','3','4']
        
        return Response({'message': 'Hello ! ' , 'an_apiview': an_apiview})
    
    def post(self,request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
         
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name} '
            return Response({'message': message})
        else : 
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
                )
            
    def put(self, request, pk=None):
        """ Handle updating an object"""
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        """ Handle partial update of an object"""
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        """ Handle deleting an object"""
        return Response({'method': 'delete'})
    

class HelloViewSet(viewsets.ViewSet):
    """ Test API viewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Return a hello message"""
        a_viewset= [
            '9','8','7','6',
        ]
        
        return Response({'method': 'Hello !', 'a_viewset': a_viewset})
    
    def create(self,request):
        """Create a mew hello message"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name} !'
            return Response({ message,'message'})
        else :
            return Response(serialzer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
            
    def retrieve(self,request,pk=None):
        """Handle Retrieve operation"""
        return Response({'message':'retrieve'})
    
    def update(self,request,pk=None):
        """Handle Update operation"""
        return Response({'message':'update'})
    
    def partial_update(self,request,pk=None):
        """Handle Partial Update operation"""
        return Response({'message':'partial update'})
    
    def destroy(self,request,pk=None):
        """Handle destroy  operation"""
        return Response({'message':'destroy'})
    
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
    