This is a blog creation project . The purpose of this project is to create a blogging platform that allows users to register, manage their profiles, and post blogs.The project is built using Django REST Framework and JWT authentication for ser management and CRUD operations.



This project contains 3 models (Country , User , Blog)

country : stores information about countries using fields continent , country and country_code.

User : a abstract User model ,store details of the user with custom fields(title , content , created_at) and default user fields(username , password , email) . In this model the field "created_at" is a ForeignKey to country model(if we pass the foreignkey on the retrive request with user(?expand=country) ,then it retrieves the user details including the users country , continent , and country_code .
Blog : stores details of the blog with fields title , content , created_at , created_by . Here created_by is a foreign key to User model . And it indicates which user created this blog.


serializers : RegisterSerializer , CountrySerializer , UserSerializer , BlogSerializer . 

RegisterSerializer: used to post the users , Also hashing passwords and validation .
CountrySerializer : Serialize the country model .
UserSerializer : Serialize the user model data , including a method(get_country) to expand the country field if the query parameter "expand=country" is provided .
BlogSerializer : Serializer the blog model data . included a method (get_created_by) to expand the created_by field if "expand=created_by" is passed as a query parameter .

Views : RegisterView , LogoutView , CountryViewSet , UserViewSet , BlogViewSet .

RegisterView: Handles user registration and creates a new user.
LogoutView: Handles user logout by blacklisting the refreshtoken.
CountryViewSet : Handles crud operation for the country model. Also doing filtering by continent and country .
UserViewSet: Handles crud operation for the user model. Also doing filtering by country and date_of_birth .
BlogViewSet: Handles crud operation for the blog model. Also doing filtering by created_by and created_at .


for running the application . I will provide the url details . 

For CRUD operations : 
there are routers in this project
for country model endpoint is: countries
for User model endpoint is: users
for Blog model endpoint is: blogs

country model :
create : [POST]   url/api/countries/
read : [GET]  url/api/countries/    #to list all countries
       [GET]  url/api/countries/<id>/    #to retrieve a specific country
update : [PUT] url/api/countries/<id>/
         [PATCH] url/api/countries/<id>/
delete : [DELETE] url/api/countries/<id>/


User model:
read : [GET]  url/api/users/    #to list all users
       [GET]  url/api/users/<id>/    #to retrieve a specific user
update : [PUT] url/api/users/<id>/
         [PATCH] url/api/users/<id>/
delete : [DELETE] url/api/users/<id>/
for registering a user , there is an another path 
Register a user : select [POST] , ulr/blog_app/api/register/

Blog model:
Only Authenticated user can create blog in this project . So for adding a blog there are some steps:
1. Add a user
2. Obtain JWT tokens
3. give the token on bearer token
4. create : [POST]   url/api/blogs/

read : [GET]  url/api/blogs/    #to list all blogs
       [GET]  url/api/blogs/<id>/    #to retrieve a specific blog
update : [PUT] url/api/blogs/<id>/
         [PATCH] url/api/blogs/<id>/
delete : [DELETE] url/api/blogs/<id>/



Foreign key expansion

To expand created_by field in the blog API response 

give request url lke this:
[GET] " url/api/blogs/?expand=created_by/ "

This will return the full user details for the created_by field .

To expand country field in the Country API response 

give request url lke this:
[GET] " url/api/blogs/?expand=created_by/ "

This will return the full country details for the country field .


Filters:

Country filters :
[GET]  url/api/countries/?continent=Asia
this will retrieve the whole country details have Asia in the continent field 
[GET]  url/api/countries/?country=India
this will retrieve the whole country details have India in the country field

User filters:
[GET]  url/api/users/?country=1
this will retrieve the whole user details have countryID 1 in the country field
[GET]  url/api/users/?date_of_birth=1990-02-08
this will retrieve the whole user details who have "2000-01-15" in the date_of_birth field

Blog filters :
[GET]  url/api/blogs/?created_by=1
this will retrieve the whole blog details which is created by the who have ID 1 
[GET]  url/api/blogs/?created_at=2024-31-12
this will retrieve the whole blogs details created at 2024-31-12
