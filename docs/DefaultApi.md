# pricing_api_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthz_get**](DefaultApi.md#healthz_get) | **GET** /healthz | Health check endpoint
[**marketplace_providers_compute_delete**](DefaultApi.md#marketplace_providers_compute_delete) | **DELETE** /marketplace/providers/compute | Delete a custom provider instance
[**marketplace_providers_compute_get**](DefaultApi.md#marketplace_providers_compute_get) | **GET** /marketplace/providers/compute | Get your custom pricing entries
[**marketplace_providers_compute_post**](DefaultApi.md#marketplace_providers_compute_post) | **POST** /marketplace/providers/compute | Register a custom provider
[**pricing_compute_post**](DefaultApi.md#pricing_compute_post) | **POST** /pricing/compute | Get  pricing for an instance
[**pricing_disks_post**](DefaultApi.md#pricing_disks_post) | **POST** /pricing/disks | Get  pricing for a disk
[**providers_get**](DefaultApi.md#providers_get) | **GET** /providers | Get details for the providers
[**recommendations_compute_post**](DefaultApi.md#recommendations_compute_post) | **POST** /recommendations/compute | Get recommendations for compute instances
[**recommendations_disks_post**](DefaultApi.md#recommendations_disks_post) | **POST** /recommendations/disks | Get recommendations for disks


# **healthz_get**
> Dict[str, str] healthz_get()

Health check endpoint

Health check endpoint

### Example


```python
import pricing_api_client
from pricing_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pricing_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pricing_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricing_api_client.DefaultApi(api_client)

    try:
        # Health check endpoint
        api_response = api_instance.healthz_get()
        print("The response of DefaultApi->healthz_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->healthz_get: %s\n" % e)
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
**200** | Health check response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplace_providers_compute_delete**
> TypesCustomPricingResponse marketplace_providers_compute_delete(id)

Delete a custom provider instance

Delete a custom provider instance

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import pricing_api_client
from pricing_api_client.models.types_custom_pricing_response import TypesCustomPricingResponse
from pricing_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pricing_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pricing_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricing_api_client.DefaultApi(api_client)
    id = 'id_example' # str | Instance ID

    try:
        # Delete a custom provider instance
        api_response = api_instance.marketplace_providers_compute_delete(id)
        print("The response of DefaultApi->marketplace_providers_compute_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->marketplace_providers_compute_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Instance ID | 

### Return type

[**TypesCustomPricingResponse**](TypesCustomPricingResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pricing response for a custom provider |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplace_providers_compute_get**
> TypesMarketplaceProvidersResponse marketplace_providers_compute_get()

Get your custom pricing entries

Get your custom pricing entries

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import pricing_api_client
from pricing_api_client.models.types_marketplace_providers_response import TypesMarketplaceProvidersResponse
from pricing_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pricing_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pricing_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricing_api_client.DefaultApi(api_client)

    try:
        # Get your custom pricing entries
        api_response = api_instance.marketplace_providers_compute_get()
        print("The response of DefaultApi->marketplace_providers_compute_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->marketplace_providers_compute_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TypesMarketplaceProvidersResponse**](TypesMarketplaceProvidersResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pricing response for custom pricing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplace_providers_compute_post**
> TypesCustomPricingResponse marketplace_providers_compute_post(instance)

Register a custom provider

Register a custom provider

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import pricing_api_client
from pricing_api_client.models.types_custom_price_request import TypesCustomPriceRequest
from pricing_api_client.models.types_custom_pricing_response import TypesCustomPricingResponse
from pricing_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pricing_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pricing_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricing_api_client.DefaultApi(api_client)
    instance = pricing_api_client.TypesCustomPriceRequest() # TypesCustomPriceRequest | Pricing RecommendationRequest

    try:
        # Register a custom provider
        api_response = api_instance.marketplace_providers_compute_post(instance)
        print("The response of DefaultApi->marketplace_providers_compute_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->marketplace_providers_compute_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**TypesCustomPriceRequest**](TypesCustomPriceRequest.md)| Pricing RecommendationRequest | 

### Return type

[**TypesCustomPricingResponse**](TypesCustomPricingResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pricing response for a custom provider |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pricing_compute_post**
> SchemaComputePricingsRow pricing_compute_post(instance)

Get  pricing for an instance

Get pricing

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import pricing_api_client
from pricing_api_client.models.github_com_baselinehq_golang_shared_types_instance import GithubComBaselinehqGolangSharedTypesInstance
from pricing_api_client.models.schema_compute_pricings_row import SchemaComputePricingsRow
from pricing_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pricing_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pricing_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricing_api_client.DefaultApi(api_client)
    instance = pricing_api_client.GithubComBaselinehqGolangSharedTypesInstance() # GithubComBaselinehqGolangSharedTypesInstance | Instance

    try:
        # Get  pricing for an instance
        api_response = api_instance.pricing_compute_post(instance)
        print("The response of DefaultApi->pricing_compute_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->pricing_compute_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**GithubComBaselinehqGolangSharedTypesInstance**](GithubComBaselinehqGolangSharedTypesInstance.md)| Instance | 

### Return type

[**SchemaComputePricingsRow**](SchemaComputePricingsRow.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pricing for a given instance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pricing_disks_post**
> SchemaDiskPricingsRow pricing_disks_post(instance)

Get  pricing for a disk

Get pricing for disks

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import pricing_api_client
from pricing_api_client.models.schema_disk_pricings_row import SchemaDiskPricingsRow
from pricing_api_client.models.types_disk import TypesDisk
from pricing_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pricing_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pricing_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricing_api_client.DefaultApi(api_client)
    instance = pricing_api_client.TypesDisk() # TypesDisk | Disks

    try:
        # Get  pricing for a disk
        api_response = api_instance.pricing_disks_post(instance)
        print("The response of DefaultApi->pricing_disks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->pricing_disks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**TypesDisk**](TypesDisk.md)| Disks | 

### Return type

[**SchemaDiskPricingsRow**](SchemaDiskPricingsRow.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pricing for a given disk |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_get**
> Dict[str, ProviderConfig] providers_get()

Get details for the providers

Get details for the providers

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import pricing_api_client
from pricing_api_client.models.provider_config import ProviderConfig
from pricing_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pricing_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pricing_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricing_api_client.DefaultApi(api_client)

    try:
        # Get details for the providers
        api_response = api_instance.providers_get()
        print("The response of DefaultApi->providers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->providers_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dict[str, ProviderConfig]**](ProviderConfig.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of providers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recommendations_compute_post**
> Dict[str, List[TypesComputeResultsValueInner]] recommendations_compute_post(instance)

Get recommendations for compute instances

Get recommendations for compute instances
Recommendations, InstancePricing, VM, and Savings

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import pricing_api_client
from pricing_api_client.models.types_compute_request import TypesComputeRequest
from pricing_api_client.models.types_compute_results_value_inner import TypesComputeResultsValueInner
from pricing_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pricing_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pricing_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricing_api_client.DefaultApi(api_client)
    instance = pricing_api_client.TypesComputeRequest() # TypesComputeRequest | Instance

    try:
        # Get recommendations for compute instances
        api_response = api_instance.recommendations_compute_post(instance)
        print("The response of DefaultApi->recommendations_compute_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->recommendations_compute_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**TypesComputeRequest**](TypesComputeRequest.md)| Instance | 

### Return type

**Dict[str, List[TypesComputeResultsValueInner]]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recommendations_disks_post**
> Dict[str, List[TypesDiskResultsValueInner]] recommendations_disks_post(instance)

Get recommendations for disks

Get recommendations for disks used in the server
Recommendations, DiskPricing, and Savings

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import pricing_api_client
from pricing_api_client.models.types_disk_request import TypesDiskRequest
from pricing_api_client.models.types_disk_results_value_inner import TypesDiskResultsValueInner
from pricing_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pricing_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pricing_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricing_api_client.DefaultApi(api_client)
    instance = pricing_api_client.TypesDiskRequest() # TypesDiskRequest | Instance

    try:
        # Get recommendations for disks
        api_response = api_instance.recommendations_disks_post(instance)
        print("The response of DefaultApi->recommendations_disks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->recommendations_disks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**TypesDiskRequest**](TypesDiskRequest.md)| Instance | 

### Return type

**Dict[str, List[TypesDiskResultsValueInner]]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

