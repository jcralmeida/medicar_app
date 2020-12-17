# Medicar
It's an app made in Django and Django Rest fpr Backend and Angular in Frontend. It has the object for 
creating and maintaining an medical system.

##Preparing your environment:

### Backend
1) First of all a virtual env must be created.
2) From inside the folder backend, you will find a file requirements.txt. Run the command `pip install -r requirements.txt`
to install all the python's dependency.
3) The backend use the postgres database. If you are familiar with docker, you can use a image from dockerhub to start 
the db. This can be achieved running the following commands: ``` docker pull postgres``` e ``` docker run --name some-postgres -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres```
4) Create a database called medicar inside the postgress. 
5) Run the commands `python manage.py makemigrations` and `python manage.py migrate` to prepare the database. 
6) Now it's time to create a super user to enter the admin page. Use the command `python manage.py createsuperuser --email admin@example.com --username admin`, passing the password and confirming it.
7) Finally, run the command `python manage.py runserver` to start the api.

### Frontend
1) From inside the frontend/src/app folder run the command `npm install`, to download and installing all Angular dependencies.
2) As soon as it finishes, you can run the command `ng serve` to start the application. Remember to start the backend service
previously, so the application is fully functional.
---

## Authentication

 If you want to use an application such as Postman or Insomnia to make requests to API in Backend only, or even via curl, you must send a field in the request header called Authorization, with the prefix JWT and the authentication token. The token must be returned when logging in or registering in the application.
 
 ``` Example: Authorization: JWT <user_token>```
 #### Available URL's:
  - admin/ - Available via browser only. Administrative interface for creating Especialidade, Medico and Agenda objects.
    - For the "horarios" field in the agenda creation, as it is a list of times, it is enough that the user passes in the required field something like: "14:00, 21:00", without quotes.
  - registration/ - POST -> It allows the creation of new users in the system.
  - login/ - POST -> It allows the login of existing users, through username / email and password.
 
  - consultas/{id}: DELETE -> It allows the deletion of an existent Consulta object, passing Consulta unique identifier.
  - consulta/: POST -> It allows create new Consulta objects, passing information such as Agenda identifier and scheduled time.
  - consultas: GET -> Allows you to search existent Consulta objects.

  - especialidades: GET -> Allows you to search existent Especialidade objects.
    - Possible query params: 
      - search: Especialidade name
      
  - medicos: GET -> Allows you to search existent Medico objects.
    - Possible query params: 
      - search: Medico name
      - especialidade: Especialidade name
  - agendas/: GET -> Allows you to search existent Agenda objects.
    - Possible query params: 
      - medico: Medico identifier
      - especialidade: Especialidade identifier
      - data_inicio: Start date for filtering, in YYYY-MM-DD format. 
      - data_final: End date for filtering, in YYYY-MM-DD format.
