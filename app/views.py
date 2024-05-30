from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import plotly.graph_objects as go
from django.http import JsonResponse
from .models import *
from .serializer import PersonSerializer, MinistrySerializer, MustardSeedSerializer
from .custom_erros import CustomExpetion
def return_response(status_code =200, data={}):
    status_codes = {200:status.HTTP_200_OK, 
    302:status.HTTP_302_FOUND, 
    304: status.HTTP_304_NOT_MODIFIED, #Not Modified
    400: status.HTTP_400_BAD_REQUEST, #Bad Request
    404: status.HTTP_404_NOT_FOUND, #Not Found
    405: status.HTTP_405_METHOD_NOT_ALLOWED, #Method_Not Allowed
    500 : status.HTTP_500_INTERNAL_SERVER_ERROR
    }
    return Response(data=data, status=status_codes[status_code])

# delete_and_create() 


@api_view(['GET'])
def home(req):
    return Response(data={"data":"data"}, status=status.is_success)


@api_view(['GET','POST', 'DELETE', 'PATCH'])
def get_people(req, id = None):
    if id is not None:
        try:
            return return_response(200,Person.objects.get(id = id).get())
        except Person.DoesNotExist:
            return return_response(404, "User Does Not Exist")
        except Exception as e:
            return return_response(400, str(e))
    if req.method == 'POST':
        try:
        
            
            serializer = PersonSerializer(data = req.data)
            serializer.validate(data= req.data) #Check if User exists
            if serializer.is_valid():
                serializer.save()
                print("errors",serializer.errors)
                return return_response(data=serializer.data, status_code=200)
        except Exception as e:
            
            return Response(data=str(e)[20:len(str(e))-3], status=status.HTTP_400_BAD_REQUEST)
    if req.method == "GET":
        try:
            people = [p.get() for p in Person.objects.all()]
            return return_response(data= people, status_code=200)
        except Exception as e:
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)
    if req.method == "DELETE":
        try:
                id = req.data['id'] or None
                if id is not None:
                    person = Person.objects.get(id = id)
                    person.delete()

                    return return_response(200, "Person Deleted Successfully")
                else:
                    raise CustomExpetion("Bad Request. Check params", 400)
        except Exception as e:
            return return_response(400, str(e))
  
    #For PATCH
    try:
        data = req.data
        id = data.pop('id')
        person = Person.objects.get(id = id)
        if data.get('mustard_seed'):
            person.mustard_seed = MustardSeed.objects.get(id = data.get('mustard_seed'))
        person.update(data)
        return return_response(200, person.get())
    except Person.DoesNotExist:
        return return_response(404, "User Does Not Exist")
    except Exception as e:
        return return_response(400, str(e))



"""
Ministry
"""

@api_view(['GET','POST','DELETE','PATCH'])
def ministry_endpoint(req, id= None):
    if id is not None:
        try:
            return return_response(200,Ministry.objects.get(id = id).get())
        except Ministry.DoesNotExist:
            return return_response(404, "Ministry Does Not Exist")
        except Exception as e:
            return return_response(400, str(e))
    if req.method == "POST":

        try:
            data = req.data
            serializer = MinistrySerializer(data=data)

            serializer.validate(data=data)

            if serializer.is_valid():
                serializer.save()
                return return_response(200, serializer.data)
            return return_response(400, serializer.errors)
        except Exception as e:
            return Response(str(e)[20:len(str(e))-3], status=status.HTTP_400_BAD_REQUEST)
            
    if req.method == "GET":

        try:
            return return_response(200, [m.get() for m in Ministry.objects.all()])
        except Exception as e:
            return return_response(400, str(e))
    if req.method == "PATCH":
        try:
            data = req.data
            id = data.pop('id')
            ministry = Ministry.objects.get(id = id)
            ministry.update(data)
            return return_response(200, ministry.get())
        except Ministry.DoesNotExist:
            return return_response(404, "Ministry Does Not Exist")
        except Exception as e:
            return return_response(400,str(e))
    
    try:
        id = req.data.get('id')
        m = Ministry.objects.get(id = id)
        m.delete()
        return return_response(200, "Ministry Deleted")       
    except Ministry.DoesNotExist:
        return return_response(404, "Ministry Does Not Exist")
    except Exception as e:
        return return_response(400,str(e))


"""
Mustard Seed
"""

@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def mustard_seed_endpoint(req, id=None):
    if id is not None:
        try:
            return return_response(200,Ministry.objects.get(id = id).get())
        except Ministry.DoesNotExist:
            return return_response(404, "Ministry Does Not Exist")
        except Exception as e:
            return return_response(400, str(e))
    if req.method == "GET":
        try:
            return return_response(200, [m.get() for m in MustardSeed.objects.all()])
        except Exception as e:
            return return_response(400, str(e))
    if req.method == "POST":
        try:
            serializer = MustardSeedSerializer(data = req.data)
            serializer.validate(data=req.data)
            if serializer.is_valid():
                serializer.save()
                return return_response(200, serializer.data)
        except Exception as e:
            return return_response(400, str(e))
    if req.method == "PATCH":
        try:
            mustard_seed = MustardSeed.objects.get(id = req.data.get('id'))
            data = req.data
            data.pop('id')
            mustard_seed.update(data)
            return return_response(200, mustard_seed.get())
        except MustardSeed.DoesNotExist:
            return return_response(404, "Mustard Seed Does Not Exist")
        except Exception as e:
            return return_response(400, str(e))         
    
    #Delete
    try:
        ms = MustardSeed.objects.get(id = req.data.get('id'))
        ms.delete()
        return return_response(200, "Mustard Seed Deleted Successfully")
    except MustardSeed.DoesNotExist:
        return return_response(404, "Mustard Seed Does Not Exist")
    except Exception as e:
        return return_response(400, str(e))   

