API automation framework

    apis: 
        REQ_RES_URI = https://reqres.in/api/login
        JSON_PATH_URI = https://JSONplaceholder.typicode.com
        GO_REST_URI = https://gorest.co.in/public/v2/users
        HTTP_BIN_URI = https://httpbin.org/get
        bearer : adcbb5143755d9b0ba2be8a3e47eed9f1e97f66d7c8ecbff13e8d94a49e59dc4

Steps to install requirements :
        
        - run the command 'pip install -r requirements.txt'



Custom markers Used :

        json_place_holder : CRUD operations related to JSONPlaceholder (https://JSONplaceholder.typicode.com/posts)
        req_res : CRUD for reqres api (https://reqres.in/api/login)
        http_bin : CRUD operations for httpbin url
        nack_tests : Error test cases
        valid_auth  : Authorizationa and authentication test cases
        crud_operation: CRUD operation test cases
        data_validation: Data validatin test cases
        edge_cases : Edge test cases


Run tests in parallel:
        
        pytest -n 4

Parallel + retry + logging all can work together:

    pytest -n 4 --reruns 2 --reruns-delay 1 --alluredir=allure-results

Allure reporting:
     
    pytest --alluredir=allure-results

Steps to generate the allure report:
        
        make sure you have Allure installed. Navigate to the folder 'allure-results'
        open cmd from the directory and run the command 'allure serve <PATH TO THE ALLURE JSON'S>'
        This will start the allure server on  <http://127.0.0.1:58102> - You can now view the report.

Run the tests based on markers:
        
        use the command 'pytest -m <MARKER_NAMe>

Run the tests to get basic html report:
        
        pytest --html=report.html


Run the tests in verbose:
        
        pytest -v 


Log files are located under :
        
            'logs/api_test.log'


PIPE LINE integration steps are added in groovy script:
        
        /JenkinsFile