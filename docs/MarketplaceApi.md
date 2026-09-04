# pricing_api_client.MarketplaceApi

All URIs are relative to *https://pricing.baselinehq.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_marketplace_compute_get**](MarketplaceApi.md#v1_marketplace_compute_get) | **GET** /v1/marketplace/compute | List your compute prices
[**v1_marketplace_compute_id_delete**](MarketplaceApi.md#v1_marketplace_compute_id_delete) | **DELETE** /v1/marketplace/compute/{id} | Delete one compute price
[**v1_marketplace_compute_id_get**](MarketplaceApi.md#v1_marketplace_compute_id_get) | **GET** /v1/marketplace/compute/{id} | Read one compute price
[**v1_marketplace_compute_id_patch**](MarketplaceApi.md#v1_marketplace_compute_id_patch) | **PATCH** /v1/marketplace/compute/{id} | Change one compute price
[**v1_marketplace_compute_post**](MarketplaceApi.md#v1_marketplace_compute_post) | **POST** /v1/marketplace/compute | Publish compute prices
[**v1_marketplace_databases_get**](MarketplaceApi.md#v1_marketplace_databases_get) | **GET** /v1/marketplace/databases | List your database prices
[**v1_marketplace_databases_id_delete**](MarketplaceApi.md#v1_marketplace_databases_id_delete) | **DELETE** /v1/marketplace/databases/{id} | Delete one database price
[**v1_marketplace_databases_id_get**](MarketplaceApi.md#v1_marketplace_databases_id_get) | **GET** /v1/marketplace/databases/{id} | Read one database price
[**v1_marketplace_databases_id_patch**](MarketplaceApi.md#v1_marketplace_databases_id_patch) | **PATCH** /v1/marketplace/databases/{id} | Change one database price
[**v1_marketplace_databases_post**](MarketplaceApi.md#v1_marketplace_databases_post) | **POST** /v1/marketplace/databases | Publish database prices
[**v1_marketplace_disks_get**](MarketplaceApi.md#v1_marketplace_disks_get) | **GET** /v1/marketplace/disks | List your disk prices
[**v1_marketplace_disks_id_delete**](MarketplaceApi.md#v1_marketplace_disks_id_delete) | **DELETE** /v1/marketplace/disks/{id} | Delete one disk price
[**v1_marketplace_disks_id_get**](MarketplaceApi.md#v1_marketplace_disks_id_get) | **GET** /v1/marketplace/disks/{id} | Read one disk price
[**v1_marketplace_disks_id_patch**](MarketplaceApi.md#v1_marketplace_disks_id_patch) | **PATCH** /v1/marketplace/disks/{id} | Change one disk price
[**v1_marketplace_disks_post**](MarketplaceApi.md#v1_marketplace_disks_post) | **POST** /v1/marketplace/disks | Publish disk prices
[**v1_marketplace_filters_kind_get**](MarketplaceApi.md#v1_marketplace_filters_kind_get) | **GET** /v1/marketplace/filters/{kind} | List the filters a price kind accepts
[**v1_marketplace_models_get**](MarketplaceApi.md#v1_marketplace_models_get) | **GET** /v1/marketplace/models | List your model prices
[**v1_marketplace_models_id_delete**](MarketplaceApi.md#v1_marketplace_models_id_delete) | **DELETE** /v1/marketplace/models/{id} | Delete one model price
[**v1_marketplace_models_id_get**](MarketplaceApi.md#v1_marketplace_models_id_get) | **GET** /v1/marketplace/models/{id} | Read one model price
[**v1_marketplace_models_id_patch**](MarketplaceApi.md#v1_marketplace_models_id_patch) | **PATCH** /v1/marketplace/models/{id} | Change one model price
[**v1_marketplace_models_post**](MarketplaceApi.md#v1_marketplace_models_post) | **POST** /v1/marketplace/models | Publish model prices


# **v1_marketplace_compute_get**
> ComputePricePage v1_marketplace_compute_get(limit=limit, cursor=cursor, service=service, region=region, instance_type=instance_type, usage_type=usage_type)

List your compute prices

List the compute rates your organization has published. Only your own rates are returned, never another organization's.
Filters combine, and paging is by limit and an opaque cursor carried in the page of the previous response.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.compute_price_page import ComputePricePage
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
    api_instance = pricing_api_client.MarketplaceApi(api_client)
    limit = 56 # int | Maximum prices to return (default 500) (optional)
    cursor = 'cursor_example' # str | Cursor from the previous page (optional)
    service = 'service_example' # str | Filter by service (optional)
    region = 'region_example' # str | Filter by region (optional)
    instance_type = 'instance_type_example' # str | Filter by instance type (optional)
    usage_type = 'usage_type_example' # str | Filter by usage type (optional)

    try:
        # List your compute prices
        api_response = api_instance.v1_marketplace_compute_get(limit=limit, cursor=cursor, service=service, region=region, instance_type=instance_type, usage_type=usage_type)
        print("The response of MarketplaceApi->v1_marketplace_compute_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->v1_marketplace_compute_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum prices to return (default 500) | [optional] 
 **cursor** | **str**| Cursor from the previous page | [optional] 
 **service** | **str**| Filter by service | [optional] 
 **region** | **str**| Filter by region | [optional] 
 **instance_type** | **str**| Filter by instance type | [optional] 
 **usage_type** | **str**| Filter by usage type | [optional] 

### Return type

[**ComputePricePage**](ComputePricePage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of your prices |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_marketplace_compute_id_delete**
> v1_marketplace_compute_id_delete(id)

Delete one compute price

Delete a compute price you have published, by its id.
Usage still pinned to it stops resolving a price, so re-pin before deleting.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
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
    api_instance = pricing_api_client.MarketplaceApi(api_client)
    id = 'id_example' # str | Price id

    try:
        # Delete one compute price
        api_instance.v1_marketplace_compute_id_delete(id)
    except Exception as e:
        print("Exception when calling MarketplaceApi->v1_marketplace_compute_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Price id | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The price was deleted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_marketplace_compute_id_get**
> ComputePrice v1_marketplace_compute_id_get(id)

Read one compute price

Read a single compute rate your organization has published, by its id.
A price belonging to another organization is not visible and reads as not found.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.compute_price import ComputePrice
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
    api_instance = pricing_api_client.MarketplaceApi(api_client)
    id = 'id_example' # str | Price id

    try:
        # Read one compute price
        api_response = api_instance.v1_marketplace_compute_id_get(id)
        print("The response of MarketplaceApi->v1_marketplace_compute_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->v1_marketplace_compute_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Price id | 

### Return type

[**ComputePrice**](ComputePrice.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The price |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_marketplace_compute_id_patch**
> ComputePrice v1_marketplace_compute_id_patch(id, body)

Change one compute price

Change the rate or the descriptive fields of a compute price you have published. Send only the fields you want to change.
The fields that identify the price cannot be changed, because they describe a different SKU; delete the price and register a new one instead.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.compute_price import ComputePrice
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
    api_instance = pricing_api_client.MarketplaceApi(api_client)
    id = 'id_example' # str | Price id
    body = None # Dict[str, object] | Fields to change

    try:
        # Change one compute price
        api_response = api_instance.v1_marketplace_compute_id_patch(id, body)
        print("The response of MarketplaceApi->v1_marketplace_compute_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->v1_marketplace_compute_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Price id | 
 **body** | [**Dict[str, object]**](object.md)| Fields to change | 

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
**200** | The changed price |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_marketplace_compute_post**
> PublishedComputePrices v1_marketplace_compute_post(body)

Publish compute prices

Register your own compute rates so CostGraph can price machines it has no public price for, such as bare metal or a private cloud.
An entry is upserted on its natural key (provider, service, region, availability zone, usage type, instance type, operating system and period billing hours), so re-posting the same entry with a new cost keeps its id and reprices everything already using it. Changing any key field mints a new id, because it describes a different SKU.
The returned id is what you attach to a resource with the `costgraph.ai/pricing-id.compute` label or tag.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.compute_prices_request import ComputePricesRequest
from pricing_api_client.models.published_compute_prices import PublishedComputePrices
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
    api_instance = pricing_api_client.MarketplaceApi(api_client)
    body = pricing_api_client.ComputePricesRequest() # ComputePricesRequest | Prices to publish

    try:
        # Publish compute prices
        api_response = api_instance.v1_marketplace_compute_post(body)
        print("The response of MarketplaceApi->v1_marketplace_compute_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->v1_marketplace_compute_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComputePricesRequest**](ComputePricesRequest.md)| Prices to publish | 

### Return type

[**PublishedComputePrices**](PublishedComputePrices.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The published prices |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_marketplace_databases_get**
> DatabasePricePage v1_marketplace_databases_get(limit=limit, cursor=cursor, service=service, region=region, engine=engine, edition=edition, instance_type=instance_type, usage_type=usage_type)

List your database prices

List the database rates your organization has published. Only your own rates are returned, never another organization's.
Filters combine, and paging is by limit and an opaque cursor carried in the page of the previous response.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.database_price_page import DatabasePricePage
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
    api_instance = pricing_api_client.MarketplaceApi(api_client)
    limit = 56 # int | Maximum prices to return (default 500) (optional)
    cursor = 'cursor_example' # str | Cursor from the previous page (optional)
    service = 'service_example' # str | Filter by service (optional)
    region = 'region_example' # str | Filter by region (optional)
    engine = 'engine_example' # str | Filter by engine (optional)
    edition = 'edition_example' # str | Filter by edition (optional)
    instance_type = 'instance_type_example' # str | Filter by instance type (optional)
    usage_type = 'usage_type_example' # str | Filter by usage type (optional)

    try:
        # List your database prices
        api_response = api_instance.v1_marketplace_databases_get(limit=limit, cursor=cursor, service=service, region=region, engine=engine, edition=edition, instance_type=instance_type, usage_type=usage_type)
        print("The response of MarketplaceApi->v1_marketplace_databases_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->v1_marketplace_databases_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum prices to return (default 500) | [optional] 
 **cursor** | **str**| Cursor from the previous page | [optional] 
 **service** | **str**| Filter by service | [optional] 
 **region** | **str**| Filter by region | [optional] 
 **engine** | **str**| Filter by engine | [optional] 
 **edition** | **str**| Filter by edition | [optional] 
 **instance_type** | **str**| Filter by instance type | [optional] 
 **usage_type** | **str**| Filter by usage type | [optional] 

### Return type

[**DatabasePricePage**](DatabasePricePage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of your prices |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_marketplace_databases_id_delete**
> v1_marketplace_databases_id_delete(id)

Delete one database price

Delete a database price you have published, by its id.
Usage still pinned to it stops resolving a price, so re-pin before deleting.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
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
    api_instance = pricing_api_client.MarketplaceApi(api_client)
    id = 'id_example' # str | Price id

    try:
        # Delete one database price
        api_instance.v1_marketplace_databases_id_delete(id)
    except Exception as e:
        print("Exception when calling MarketplaceApi->v1_marketplace_databases_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Price id | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The price was deleted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_marketplace_databases_id_get**
> DatabasePrice v1_marketplace_databases_id_get(id)

Read one database price

Read a single database rate your organization has published, by its id.
A price belonging to another organization is not visible and reads as not found.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.database_price import DatabasePrice
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
    api_instance = pricing_api_client.MarketplaceApi(api_client)
    id = 'id_example' # str | Price id

    try:
        # Read one database price
        api_response = api_instance.v1_marketplace_databases_id_get(id)
        print("The response of MarketplaceApi->v1_marketplace_databases_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->v1_marketplace_databases_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Price id | 

### Return type

[**DatabasePrice**](DatabasePrice.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The price |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_marketplace_databases_id_patch**
> DatabasePrice v1_marketplace_databases_id_patch(id, body)

Change one database price

Change the rate or the descriptive fields of a database price you have published. Send only the fields you want to change.
The fields that identify the price cannot be changed, because they describe a different SKU; delete the price and register a new one instead.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.database_price import DatabasePrice
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
    api_instance = pricing_api_client.MarketplaceApi(api_client)
    id = 'id_example' # str | Price id
    body = None # Dict[str, object] | Fields to change

    try:
        # Change one database price
        api_response = api_instance.v1_marketplace_databases_id_patch(id, body)
        print("The response of MarketplaceApi->v1_marketplace_databases_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->v1_marketplace_databases_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Price id | 
 **body** | [**Dict[str, object]**](object.md)| Fields to change | 

### Return type

[**DatabasePrice**](DatabasePrice.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The changed price |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_marketplace_databases_post**
> PublishedDatabasePrices v1_marketplace_databases_post(body)

Publish database prices

Register your own managed database rates so CostGraph can price clusters it has no public price for.
An entry is upserted on its natural key (provider, service, region, engine, edition, instance type and usage type), so re-posting the same entry with a new cost keeps its id and reprices everything already using it.
The returned id is what you attach to a database with the `costgraph.ai/pricing-id.database` label or tag.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.database_prices_request import DatabasePricesRequest
from pricing_api_client.models.published_database_prices import PublishedDatabasePrices
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
    api_instance = pricing_api_client.MarketplaceApi(api_client)
    body = pricing_api_client.DatabasePricesRequest() # DatabasePricesRequest | Prices to publish

    try:
        # Publish database prices
        api_response = api_instance.v1_marketplace_databases_post(body)
        print("The response of MarketplaceApi->v1_marketplace_databases_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->v1_marketplace_databases_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DatabasePricesRequest**](DatabasePricesRequest.md)| Prices to publish | 

### Return type

[**PublishedDatabasePrices**](PublishedDatabasePrices.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The published prices |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_marketplace_disks_get**
> DiskPricePage v1_marketplace_disks_get(limit=limit, cursor=cursor, service=service, region=region, type=type, usage_type=usage_type)

List your disk prices

List the disk rates your organization has published. Only your own rates are returned, never another organization's.
Filters combine, and paging is by limit and an opaque cursor carried in the page of the previous response.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.disk_price_page import DiskPricePage
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
    api_instance = pricing_api_client.MarketplaceApi(api_client)
    limit = 56 # int | Maximum prices to return (default 500) (optional)
    cursor = 'cursor_example' # str | Cursor from the previous page (optional)
    service = 'service_example' # str | Filter by service (optional)
    region = 'region_example' # str | Filter by region (optional)
    type = 'type_example' # str | Filter by disk type (optional)
    usage_type = 'usage_type_example' # str | Filter by usage type (optional)

    try:
        # List your disk prices
        api_response = api_instance.v1_marketplace_disks_get(limit=limit, cursor=cursor, service=service, region=region, type=type, usage_type=usage_type)
        print("The response of MarketplaceApi->v1_marketplace_disks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->v1_marketplace_disks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum prices to return (default 500) | [optional] 
 **cursor** | **str**| Cursor from the previous page | [optional] 
 **service** | **str**| Filter by service | [optional] 
 **region** | **str**| Filter by region | [optional] 
 **type** | **str**| Filter by disk type | [optional] 
 **usage_type** | **str**| Filter by usage type | [optional] 

### Return type

[**DiskPricePage**](DiskPricePage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of your prices |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_marketplace_disks_id_delete**
> v1_marketplace_disks_id_delete(id)

Delete one disk price

Delete a disk price you have published, by its id.
Usage still pinned to it stops resolving a price, so re-pin before deleting.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
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
    api_instance = pricing_api_client.MarketplaceApi(api_client)
    id = 'id_example' # str | Price id

    try:
        # Delete one disk price
        api_instance.v1_marketplace_disks_id_delete(id)
    except Exception as e:
        print("Exception when calling MarketplaceApi->v1_marketplace_disks_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Price id | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The price was deleted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_marketplace_disks_id_get**
> DiskPrice v1_marketplace_disks_id_get(id)

Read one disk price

Read a single disk rate your organization has published, by its id.
A price belonging to another organization is not visible and reads as not found.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
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
    api_instance = pricing_api_client.MarketplaceApi(api_client)
    id = 'id_example' # str | Price id

    try:
        # Read one disk price
        api_response = api_instance.v1_marketplace_disks_id_get(id)
        print("The response of MarketplaceApi->v1_marketplace_disks_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->v1_marketplace_disks_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Price id | 

### Return type

[**DiskPrice**](DiskPrice.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The price |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_marketplace_disks_id_patch**
> DiskPrice v1_marketplace_disks_id_patch(id, body)

Change one disk price

Change the rate or the descriptive fields of a disk price you have published. Send only the fields you want to change.
The fields that identify the price cannot be changed, because they describe a different SKU; delete the price and register a new one instead.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
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
    api_instance = pricing_api_client.MarketplaceApi(api_client)
    id = 'id_example' # str | Price id
    body = None # Dict[str, object] | Fields to change

    try:
        # Change one disk price
        api_response = api_instance.v1_marketplace_disks_id_patch(id, body)
        print("The response of MarketplaceApi->v1_marketplace_disks_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->v1_marketplace_disks_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Price id | 
 **body** | [**Dict[str, object]**](object.md)| Fields to change | 

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
**200** | The changed price |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_marketplace_disks_post**
> PublishedDiskPrices v1_marketplace_disks_post(body)

Publish disk prices

Register your own block storage rates so CostGraph can price volumes it has no public price for.
An entry is upserted on its natural key (provider, service, region, availability zone, usage type, type and period billing hours), so re-posting the same entry with a new cost keeps its id and reprices everything already using it.
The returned id is what you attach to a volume with the `costgraph.ai/pricing-id.disk` label or tag.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.disk_prices_request import DiskPricesRequest
from pricing_api_client.models.published_disk_prices import PublishedDiskPrices
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
    api_instance = pricing_api_client.MarketplaceApi(api_client)
    body = pricing_api_client.DiskPricesRequest() # DiskPricesRequest | Prices to publish

    try:
        # Publish disk prices
        api_response = api_instance.v1_marketplace_disks_post(body)
        print("The response of MarketplaceApi->v1_marketplace_disks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->v1_marketplace_disks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DiskPricesRequest**](DiskPricesRequest.md)| Prices to publish | 

### Return type

[**PublishedDiskPrices**](PublishedDiskPrices.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The published prices |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_marketplace_filters_kind_get**
> FilterSet v1_marketplace_filters_kind_get(kind)

List the filters a price kind accepts

The query parameters you can filter this kind of price by. They differ by kind because the fields that identify a price differ: compute prices carry an instance type, disk prices a disk type, database prices an engine.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.filter_set import FilterSet
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
    api_instance = pricing_api_client.MarketplaceApi(api_client)
    kind = 'kind_example' # str | Price kind

    try:
        # List the filters a price kind accepts
        api_response = api_instance.v1_marketplace_filters_kind_get(kind)
        print("The response of MarketplaceApi->v1_marketplace_filters_kind_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->v1_marketplace_filters_kind_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kind** | **str**| Price kind | 

### Return type

[**FilterSet**](FilterSet.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_marketplace_models_get**
> ModelPricePage v1_marketplace_models_get(limit=limit, cursor=cursor, model=model, provider=provider, region=region, token_bucket=token_bucket)

List your model prices

List the model rates your organization has published. Only your own rates are returned, never another organization's.
Filters combine, and paging is by limit and an opaque cursor carried in the page of the previous response.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.model_price_page import ModelPricePage
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
    api_instance = pricing_api_client.MarketplaceApi(api_client)
    limit = 56 # int | Maximum prices to return (default 500) (optional)
    cursor = 'cursor_example' # str | Cursor from the previous page (optional)
    model = 'model_example' # str | Filter by model (optional)
    provider = 'provider_example' # str | Filter by model provider (optional)
    region = 'region_example' # str | Filter by region (optional)
    token_bucket = 'token_bucket_example' # str | Filter by token bucket (optional)

    try:
        # List your model prices
        api_response = api_instance.v1_marketplace_models_get(limit=limit, cursor=cursor, model=model, provider=provider, region=region, token_bucket=token_bucket)
        print("The response of MarketplaceApi->v1_marketplace_models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->v1_marketplace_models_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum prices to return (default 500) | [optional] 
 **cursor** | **str**| Cursor from the previous page | [optional] 
 **model** | **str**| Filter by model | [optional] 
 **provider** | **str**| Filter by model provider | [optional] 
 **region** | **str**| Filter by region | [optional] 
 **token_bucket** | **str**| Filter by token bucket | [optional] 

### Return type

[**ModelPricePage**](ModelPricePage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of your prices |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_marketplace_models_id_delete**
> v1_marketplace_models_id_delete(id)

Delete one model price

Delete a model price you have published, by its id.
Usage still pinned to it stops resolving a price, so re-pin before deleting.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
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
    api_instance = pricing_api_client.MarketplaceApi(api_client)
    id = 'id_example' # str | Price id

    try:
        # Delete one model price
        api_instance.v1_marketplace_models_id_delete(id)
    except Exception as e:
        print("Exception when calling MarketplaceApi->v1_marketplace_models_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Price id | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The price was deleted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_marketplace_models_id_get**
> ModelPrice v1_marketplace_models_id_get(id)

Read one model price

Read a single model rate your organization has published, by its id.
A price belonging to another organization is not visible and reads as not found.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.model_price import ModelPrice
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
    api_instance = pricing_api_client.MarketplaceApi(api_client)
    id = 'id_example' # str | Price id

    try:
        # Read one model price
        api_response = api_instance.v1_marketplace_models_id_get(id)
        print("The response of MarketplaceApi->v1_marketplace_models_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->v1_marketplace_models_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Price id | 

### Return type

[**ModelPrice**](ModelPrice.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The price |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_marketplace_models_id_patch**
> ModelPrice v1_marketplace_models_id_patch(id, body)

Change one model price

Change the rate or the descriptive fields of a model price you have published. Send only the fields you want to change.
The fields that identify the price cannot be changed, because they describe a different SKU; delete the price and register a new one instead.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.model_price import ModelPrice
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
    api_instance = pricing_api_client.MarketplaceApi(api_client)
    id = 'id_example' # str | Price id
    body = None # Dict[str, object] | Fields to change

    try:
        # Change one model price
        api_response = api_instance.v1_marketplace_models_id_patch(id, body)
        print("The response of MarketplaceApi->v1_marketplace_models_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->v1_marketplace_models_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Price id | 
 **body** | [**Dict[str, object]**](object.md)| Fields to change | 

### Return type

[**ModelPrice**](ModelPrice.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The changed price |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_marketplace_models_post**
> PublishedModelPrices v1_marketplace_models_post(body)

Publish model prices

Register your own token rates for models you host, so CostGraph can price calls it has no public rate for.
Entries are versioned: a price change closes the current row and opens a new one, so spend already recorded keeps the rate it was billed at.
The returned id is what you attach with the `costgraph.ai/pricing-id.model` label or tag. Each version carries its own id, so read the live entry back after a price change.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.model_prices_request import ModelPricesRequest
from pricing_api_client.models.published_model_prices import PublishedModelPrices
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
    api_instance = pricing_api_client.MarketplaceApi(api_client)
    body = pricing_api_client.ModelPricesRequest() # ModelPricesRequest | Prices to publish

    try:
        # Publish model prices
        api_response = api_instance.v1_marketplace_models_post(body)
        print("The response of MarketplaceApi->v1_marketplace_models_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->v1_marketplace_models_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModelPricesRequest**](ModelPricesRequest.md)| Prices to publish | 

### Return type

[**PublishedModelPrices**](PublishedModelPrices.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The published prices |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

