# pricing_api_client.PricingApi

All URIs are relative to *https://pricing.baselinehq.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_pricing_compute_post**](PricingApi.md#v1_pricing_compute_post) | **POST** /v1/pricing/compute | Price a machine
[**v1_pricing_disks_post**](PricingApi.md#v1_pricing_disks_post) | **POST** /v1/pricing/disks | Price a volume


# **v1_pricing_compute_post**
> ComputePrice v1_pricing_compute_post(instance)

Price a machine

Resolve the hourly rate CostGraph would bill for a machine with the given shape, in the given region and usage type.
Prices you have published for the machine's provider are preferred over the public catalogue.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.compute_price import ComputePrice
from pricing_api_client.models.instance import Instance
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
    api_instance = pricing_api_client.PricingApi(api_client)
    instance = pricing_api_client.Instance() # Instance | Machine to price

    try:
        # Price a machine
        api_response = api_instance.v1_pricing_compute_post(instance)
        print("The response of PricingApi->v1_pricing_compute_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingApi->v1_pricing_compute_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**Instance**](Instance.md)| Machine to price | 

### Return type

[**ComputePrice**](ComputePrice.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The resolved price |  -  |
**400** | Invalid request body |  -  |
**401** | Unauthenticated |  -  |
**404** | No price matches the machine |  -  |
**422** | Validation failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pricing_disks_post**
> DiskPrice v1_pricing_disks_post(instance)

Price a volume

Resolve the rate CostGraph would bill for a block volume of the given type and capacity, in the given region.
Prices you have published for the volume's provider are preferred over the public catalogue.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.disk import Disk
from pricing_api_client.models.disk_price import DiskPrice
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
    api_instance = pricing_api_client.PricingApi(api_client)
    instance = pricing_api_client.Disk() # Disk | Volume to price

    try:
        # Price a volume
        api_response = api_instance.v1_pricing_disks_post(instance)
        print("The response of PricingApi->v1_pricing_disks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingApi->v1_pricing_disks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**Disk**](Disk.md)| Volume to price | 

### Return type

[**DiskPrice**](DiskPrice.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The resolved price |  -  |
**400** | Invalid request body |  -  |
**401** | Unauthenticated |  -  |
**404** | No price matches the volume |  -  |
**422** | Validation failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

