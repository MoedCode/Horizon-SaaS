from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect, HttpResponse
from .models import UserData
from .serializers import UserDataSerializer
from rest_framework import status as S
from django.http import HttpResponse, Http404, FileResponse
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
S200 = S.HTTP_200_OK
S201 = S.HTTP_201_CREATED
S304 = S.HTTP_304_NOT_MODIFIED
S400 = S.HTTP_400_BAD_REQUEST
S401 = S.HTTP_401_UNAUTHORIZED
S405 = S.HTTP_405_METHOD_NOT_ALLOWED
S403 = S.HTTP_403_FORBIDDEN
S404 = S.HTTP_404_NOT_FOUND
S405 = S.HTTP_405_METHOD_NOT_ALLOWED
S406 = S.HTTP_406_NOT_ACCEPTABLE
S408 = S.HTTP_408_REQUEST_TIMEOUT
S500 = S.HTTP_500_INTERNAL_SERVER_ERROR
class UserCreate(APIView):
    def get(self, request):
        return Response({"error": "GET not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        serializer = UserDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # this will call the create() method in your serializer
            return Response({"success": True}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserRegister(APIView):
    def get(self, request):
        return render(request, "register.html")
class UserGetData(APIView):
    def get(self, request, user_id=0, name=None):
        # password = request.data.get("password", None)

        if (user_id):
            user = UserData.objects.filter(id=user_id).first()
        elif (name):
            user = UserData.objects.filter(iname=name).first()
        else:
            return Response({"error":"invalid credential"}, S400)
        # if user.password != password:
        #      return Response({"error":"invalid credential"}, S400)
        # del user.password
        del user.image
        user_serialized = UserDataSerializer(user).data
        return Response(user_serialized, S200)
class UserImage(APIView):
    """
    GET /ud/user/<user_id>/image/
    — Returns the raw image bytes for the given user,
      or a 404 JSON error if not found.
    """
    def get(self, request, user_id):
        # 1. Try to load the user or return a 404
        ''' all that
        user = UserData.objects.filter(id=user_id).first()
        if(not user):
            return Response({"No UserData matches the given query."}, S404)
        print(f"user: {user.name} \n\n")
        '''
        ''' replaced with that'''
        user = get_object_or_404(UserData, id=user_id)


        # 2. If there's no image, raise a DRF NotFound (returns JSON 404)
        if not user.image:
            raise NotFound(detail="User has no image", code=status.HTTP_404_NOT_FOUND)

        # 3. Return an HttpResponse streaming the raw bytes,
        #    with an appropriate Content-Type header
        return HttpResponse(
            user.image,
            content_type='image/png',
            status=status.HTTP_200_OK
        )
class  xPage(APIView):
    def get(self, request):
        return render(request, 'x.html')
