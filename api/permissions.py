import requests
from rest_framework import permissions
from rest_framework.exceptions import NotFound

class ExternalAuthPermission(permissions.BasePermission):
    # called on all HTTP requests
    def has_permission(self, request, view):        
        # use external auth check
        token = request.META.get('HTTP_AUTHORIZATION')
        url = 'http://spring-server:8080/api/v1/accounts/token'
        try:
            res = requests.get(url, headers={'Authorization': token})
        except requests.exceptions.ConnectionError as err:
            print("ConnectionError:", err)
            raise NotFound

        if res.status_code != requests.codes.ok:
            return False        
        return True
    
    # called on GET, PUT, DELETE
    def has_object_permission(self, request, view, obj):
        # always allow GET, HEAD, OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # can access only object owner 
        return obj.userId == request.userId