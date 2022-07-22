Setup:-
    -just install all the dependencies mentioned in requirements.txt
    -and run the command python3 manage.py runserver

Working:-
    -The app provides various endpoints for authentication
    -Once the user is authenticated it can call the getWeatherInfo api, which uses third party api
    -To  reduce the no. of calls, we run a thread which and call the third party api using this thread
    -After calling the third party api, we store the data in our local db
    -And send the data to the client from this local db
    -The db is updated in every 30min and we can change the refresh rate according to our need



Credentials for testing the api:-
    username = Raj
    password = Raj@12345

The endpoints for this api are:-

1.  /api/register/ [POST]
    input:- {
        "username":"",
        "email" :"",
        "password" : ""
    }
    #try to use it less, give token for authentication

2.  /api/login/ [POST]
    input:- {
        "username":"Raj",
        "password":"Raj@12345"
    }

    # u will receive token for authentication

3.  /api/logout/ [POST]
    
    #dosen't take any input, just hit the url
    #with authentication token and u will get loged out

    #if already loged out, give data invalid token

4.  /api/getWeatherInfo/ [GET]
    
    #provides weather info in authenticated mode, authenticated by token

    #for pagination pass "page" as query parameter (/api/getWeatherInfo/?page=2)



