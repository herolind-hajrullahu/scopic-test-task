# REST API Test task


The entire application is contained inside /env

`cd env`

Change the path of enviroment variable of python interpreter 'env\pyvenv.cfg'

`Scripts\activate` activates virtual environment

`cd auction`

`python manage.py runserver` run a emulated server on your local computer


# REST API

The REST API to the example app is described below.

## Login 

### Request

`GET http://localhost:8000/login/{username}/{password}/`

### Response

   ```json
   {
       "message": "Authorized"
   }
   ````

## Home

### Request

   `GET http://localhost:8000/home`
   
### Response

   ```json
   [
  {
    "title": "vase",
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eleifend vehicula sapien nec tempus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "image": "image/path/example",
    "price": 5,
    "highest_bid": 0,
    "highest_bidder": "",
    "auto_bidder": ""
  },
  {
    "title": "hej",
    "description": "Lorem vase dolor sit amet, consectetur adipiscing elit. Cras eleifend vehicula sapien nec tempus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "image": "image/path/example",
    "price": 1,
    "highest_bid": 0,
    "highest_bidder": "",
    "auto_bidder": ""
  },
  {
    "title": "kuje",
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eleifend vehicula sapien nec tempus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "image": "image/path/example",
    "price": 53,
    "highest_bid": 0,
    "highest_bidder": "",
    "auto_bidder": ""
  },
  {
    "title": "qeti",
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eleifend vehicula sapien nec tempus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "image": "image/path/example",
    "price": 55,
    "highest_bid": 0,
    "highest_bidder": "",
    "auto_bidder": ""
  }
]
   ````
   
## Item

### Request

   `GET http://127.0.0.1:8000/item/{title}`

### Response

```json
    {
    "title": "vase",
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eleifend vehicula sapien nec tempus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "image": "image/path/example",
    "price": 55,
    "highest_bid": 0,
    "highest_bidder": "",
    "auto_bidder": ""
  }
````

## Search

### Request

   `GET http://127.0.0.1:8000/search/{filter}`

### Response

```json
    [
  {
    "title": "vase",
    "description": "Lorem vase dolor sit amet, consectetur adipiscing elit. Cras eleifend vehicula sapien nec tempus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "image": "image/path/example",
    "price": 1,
    "highest_bid": 0,
    "highest_bidder": "",
    "auto_bidder": ""
  },
  {
    "title": "vase",
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eleifend vehicula sapien nec tempus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "image": "image/path/example",
    "price": 5,
    "highest_bid": 0,
    "highest_bidder": "",
    "auto_bidder": ""
  }
]
````

## Bid

### Request

   `GET http://127.0.0.1:8000/bid/{title}`

#### Header
    Authorization: {authorization_token}

### Response

` Status: 200 OK`

## Auto bid

### Request

   `GET http://127.0.0.1:8000/auto_bid/{title}/{max_bid}`
   
#### Header
    Authorization: {authorization_token}

### Response

` Status: 200 OK`

