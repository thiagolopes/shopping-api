# A gRPC project

## About
This project implement two microservices that together powers an web page that displays a product list with custom discounts per user.

### The protos
In `/protos` dir you will find all the .protos used in this project together with the gRPC calls descriptions.

To update gRPC generated code or protobuf structs use `make generate-promotion` to run the gRPC generations tools

### The Python project
This project is responsible for serve a RESTful API with a product resource, this resource will show the discounts available per user based on gRPC call to a "discount API" and apply any rules to them

#### Setup
To run this project you will need installed:
- python 3.8.5 or higher
- poetry
- and any SGDB to use in API, tested with PostgresSQL 13.1 and SQLite 3.34

Follow steps:
- `make install-deps` to install all dependencies
- `cp local.env .env`, and update the variables with your settings
- `make migrate` to apply the migrations in database

Finally, to run: `make run`

#### Docs:
The project has one resource: `/v1/products` to access all products, the payload will show the discounts avalible if the request has a `Authorization`

- Create a user:
  - You can use `make create-user` or use `/admin` to access the admin page with superuser
- To generate an api token you need *POST* request in `/api-auth` with a payload: `{"username": X, "password": Y}`
  - After that you will recive a response with the token and you can be able to use in `Authorization` header with value `Token XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`

### The Go project
This project is a gRPC server, thats applies a series of discounts to an order.

#### Setup
To run this project you will need installed:
- go 1.15.7 (tested in Linux)

Follow steps:
- `make tools` to install tools to be used in development
- `make build` to build the project
- `cp local.env .env`, and update the variables with your settings

Finally, to run binary: `./bin/promotion`
