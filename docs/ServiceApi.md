# pricing_api_client.ServiceApi

All URIs are relative to *https://pricing.baselinehq.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_healthz_get**](ServiceApi.md#v1_healthz_get) | **GET** /v1/healthz | Check the service is live


# **v1_healthz_get**
> Dict[str, str] v1_healthz_get()

Check the service is live

Report that the pricing service is accepting requests. No credential is required.

### Example


```python
import pricing_api_client
from pricing_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://pricing.baselinehq.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = pricing_api_client.Configuration(
    host = "https://pricing.baselinehq.cloud"
)


# Enter a context with an instance of the API client
with pricing_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricing_api_client.ServiceApi(api_client)

    try:
        # Check the service is live
        api_response = api_instance.v1_healthz_get()
        print("The response of ServiceApi->v1_healthz_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->v1_healthz_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The service is live |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

