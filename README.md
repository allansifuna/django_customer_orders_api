# CutomerOrdersAPI

[![Coverage Status](https://coveralls.io/repos/github/allansifuna/django_customer_orders_api/badge.svg)](https://coveralls.io/github/allansifuna/django_customer_orders_api)

## Tech Stack Used
| Purpose    | Stack                         
|----------------|-------------------------------
|API Dev| Django, Django Rest Framework    
|SMS           |Africastalking SMS API           |
|Authentication & Authorization         | Google OpenID
|CI/ CD | Github Actions
|Prod Database| Postgres DB
|Test/Dev Database | Sqlite3
|Containerization| Docker
|Infrastructure as Code| Terraform
|Container Orchestration| Kubernetes
|Kuberenetes Engine| Linode Kubernetes Engine
|Domain/Subdomain| FreeDNS
|Version Control| Git, Github
|Coverage| Coveralls
|Test| Django UnitTests


# Functionality
## API
The API can be accessed through the following URL  [http://customerorders.mooo.com](http://customerorders.mooo.com)

![API Dashboard](https://github.com/allansifuna/django_customer_orders_api/blob/main/readme_imgs/api.png)
##  Authenticate a User

To interact with API endpoints you require a JWT token that is provided upon signing up or signing in using Google OpenID connect.
Login URL [http://customerorders.mooo.com/login](http://customerorders.mooo.com/login)

![Google Login/Register Initialization Page](https://github.com/allansifuna/django_customer_orders_api/blob/main/readme_imgs/login.png)

![Google OAuth Popup](https://github.com/allansifuna/django_customer_orders_api/blob/main/readme_imgs/google_popup.png)

Upon a successful login, a user will be redirected to a Django Rest Framework page where they will be provided with access and refresh token.

![Successful Authentication Page](https://github.com/allansifuna/django_customer_orders_api/blob/main/readme_imgs/auth_success.png)

## Authorization

With a valid access token, a user can append the access token to headers for authentication of successive requests by Clicking on the Authorize button on the API Dashboard and entering **Bearer \<access token>** in the input field.

![Authorization Popup](https://github.com/allansifuna/django_customer_orders_api/blob/main/readme_imgs/auth.png)
## Adding a Customer

With a valid access token, one can add a customer into the system.

![Add Customer](https://github.com/allansifuna/django_customer_orders_api/blob/main/readme_imgs/add_cust.png)

![Successful Add Customer Response](https://github.com/allansifuna/django_customer_orders_api/blob/main/readme_imgs/add_cust_resp.png)

## Adding an Order

With a valid access token, one can add a customer order upon which an sms should be sent to the customer's Phone number. **Note: With sandbox environment, Africastalking SMS API will not deliver the sms to the recipient's inbox** But if the code does return a successful response then that means the code executed successfully.

![Add an order](https://github.com/allansifuna/django_customer_orders_api/blob/main/readme_imgs/add_ord.png)

Response

![Successful Add an order Response](https://github.com/allansifuna/django_customer_orders_api/blob/main/readme_imgs/add_ord_resp.png)


## Invalid Access token Response

![Invalid credentials Response](https://github.com/allansifuna/django_customer_orders_api/blob/main/readme_imgs/invalid_creds.png)