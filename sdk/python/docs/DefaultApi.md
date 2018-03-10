# swagger_client.DefaultApi

All URIs are relative to *https://echo.services.developerjack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**echo**](DefaultApi.md#echo) | **GET** /echo | 


# **echo**
> Echo echo(echo=echo)



Echo's back the query string param if provided.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
echo = 'echo_example' # str | A string to echo back. (optional)

try:
    api_response = api_instance.echo(echo=echo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->echo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **echo** | **str**| A string to echo back. | [optional] 

### Return type

[**Echo**](Echo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

