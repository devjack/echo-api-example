# Echo API Example
This is a simple API to echo back a string. It's primary purpose is to demonstrate that API spec's are for more than just documentation.

In this example, an OpenAPI spec is used for

* Mocking an API as a prototype
* Testing an API implementation against the spec
* Generating Postman collections for deeper testing
* Eventually, generating documentation

## Mocking a new API
First, for the purposes of rapid prototyping, craft an API spec using tools like SwaggerHub.

Here's a [spec I created earlier](https://app.swaggerhub.com/apis/devjack/Echo-API-Example/1.0.0) that allows you to do some mock API calls.


## Implementing that API
Start coding against the API spec to implement various features. This API is quite simple, just an `/echo` endpoint.

### Code Generation
You _can_ use a variety of tools to generate code from your API spec.

```
pip install swagger_py_codegen
swagger_py_codegen -s openapi.yml . -p echo
```

To make this work for the spec I've then gone and modified the `/v1` prefix in the blueprint, and the `echo/v1/api/echo.py` file to implement `?echo`.

I personally, however, am not a fan of code-gen and code magic in general. So, for such a simple API I prefer to setup and implement this myself.

### Implementation
If implementing this yourself then you want to setup the repo (or just clone this one) and then go ahead and install the dependencies.

#### Setup
```
git clone https://github.com/devjack/echo-api-example.git && cd echo-api-example

# A simple virtual env for this project
python -m venv ../echo-api-example.env
. ../echo-api-example.env/bin/activate
```

#### Dependencies
Simplest - use requirements.txt

```
pip install -r requirements.txt
```

If you prefer, you can install the three dependencies directly.

```
pip install zappa flask
```

## Test against the spec
We'll use dredd to do this.

```
npm install -g dredd
dredd init
dredd
```


## Extra tests (Postman)
You can [import an OpenAPI spec to postman](https://www.getpostman.com/docs/v6/postman/collections/data_formats). But, I've already done that for you in `echo-example.postman_collection.json`.
You can then [write tests against API calls](https://www.getpostman.com/docs/v6/postman/scripts/test_scripts). For more reading I'd highly recommend reading this [excellent collection of tips](http://blog.getpostman.com/2017/07/28/api-testing-tips-from-a-postman-professional/) for API testing.

Since we already have a postman collection in the repo:

```
npm install -g newman
newman run echo-example.postman_collection.json
```

## Deployment
From scratch, you can run `zappa init` to setup a serverless deployment.

I've already generated (and further configured for TLS and a custom domain etc) so deployments are run by:

```
# First time
zappa deploy

# subsequent times
zappa update production
```

See `zappa_settings.json` for an example.
