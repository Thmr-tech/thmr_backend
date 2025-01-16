from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_view(request):
    return Response({"message": "Hello"})


'''
{
    "email": "user@example.com",
    "full_name": "John Doe",
    "national_id": "1234567890",
    "telephone": "9876543211",
    "box_number": "123",
    "family_funds_box_name": "Some Box",
    "family_funds_basic_regulations": "somefile.pdf",
    "signup_type": "",
    "password": "Malkas0a.102",
    "re_password": "Malkas0a.102"
}

{
    "email": "user@example.com",
    "full_name": "John Doe",
    "national_id": "1234567890",
    "telephone": "9876543212",
    "box_number": "123",
    "family_funds_box_name": "Some Box",
    "family_funds_basic_regulations": "somefile.pdf",
    "signup_type": "member",
    "password": "Malkas0a.102",
    "re_password": "Malkas0a.102"
}

{
    "email": "user@example.com",
    "full_name": "John Doe",
    "national_id": "1234567893",
    "telephone": "9876543210",
    "box_number": "123",
    "family_funds_box_name": "Some Box",
    "family_funds_basic_regulations": "somefile.pdf",
    "signup_type": "manager",
    "password": "Malkas0a.102",
    "re_password": "Malkas0a.102"
}

'''