# pricing_api_client.ProvidersApi

All URIs are relative to *https://pricing.baselinehq.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_providers_get**](ProvidersApi.md#v1_providers_get) | **GET** /v1/providers | List the providers CostGraph prices


# **v1_providers_get**
> Dict[str, ProviderConfig] v1_providers_get()

List the providers CostGraph prices

Return every provider the pricing catalogue covers, with the filter values each one accepts.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.provider_config import ProviderConfig
from pricing_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://pricing.baselinehq.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = pricing_api_client.Configuration(
    host = "https://pricing.baselinehq.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pricing_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricing_api_client.ProvidersApi(api_client)

    try:
        # List the providers CostGraph prices
        api_response = api_instance.v1_providers_get()
        print("The response of ProvidersApi->v1_providers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->v1_providers_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dict[str, ProviderConfig]**](ProviderConfig.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The providers CostGraph prices |  -  |
**401** | Unauthenticated |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

