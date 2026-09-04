# pricing_api_client.DefaultApi

All URIs are relative to *https://pricing.baselinehq.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthz_get**](DefaultApi.md#healthz_get) | **GET** /healthz | Health check endpoint
[**marketplace_providers_compute_delete**](DefaultApi.md#marketplace_providers_compute_delete) | **DELETE** /marketplace/providers/compute | Delete a custom provider instance
[**marketplace_providers_compute_get**](DefaultApi.md#marketplace_providers_compute_get) | **GET** /marketplace/providers/compute | Get your custom pricing entries
[**marketplace_providers_compute_post**](DefaultApi.md#marketplace_providers_compute_post) | **POST** /marketplace/providers/compute | Register a custom provider
[**marketplace_providers_databases_delete**](DefaultApi.md#marketplace_providers_databases_delete) | **DELETE** /marketplace/providers/databases | Delete a custom database pricing entry
[**marketplace_providers_databases_get**](DefaultApi.md#marketplace_providers_databases_get) | **GET** /marketplace/providers/databases | Get your custom database pricing entries
[**marketplace_providers_databases_post**](DefaultApi.md#marketplace_providers_databases_post) | **POST** /marketplace/providers/databases | Register custom database pricing
[**marketplace_providers_disks_delete**](DefaultApi.md#marketplace_providers_disks_delete) | **DELETE** /marketplace/providers/disks | Delete a custom disk provider entry
[**marketplace_providers_disks_get**](DefaultApi.md#marketplace_providers_disks_get) | **GET** /marketplace/providers/disks | Get your custom disk pricing entries
[**marketplace_providers_disks_post**](DefaultApi.md#marketplace_providers_disks_post) | **POST** /marketplace/providers/disks | Register a custom disk provider
[**marketplace_providers_models_delete**](DefaultApi.md#marketplace_providers_models_delete) | **DELETE** /marketplace/providers/models | Delete a custom model pricing entry
[**marketplace_providers_models_get**](DefaultApi.md#marketplace_providers_models_get) | **GET** /marketplace/providers/models | Get your custom model pricing entries
[**marketplace_providers_models_post**](DefaultApi.md#marketplace_providers_models_post) | **POST** /marketplace/providers/models | Register custom model pricing
[**pricing_compute_post**](DefaultApi.md#pricing_compute_post) | **POST** /pricing/compute | Get pricing for an instance
[**pricing_disks_post**](DefaultApi.md#pricing_disks_post) | **POST** /pricing/disks | Get pricing for a disk
[**pricing_post**](DefaultApi.md#pricing_post) | **POST** /pricing | Get pricing for an instance
[**providers_get**](DefaultApi.md#providers_get) | **GET** /providers | Get details for the providers
[**recommendations_compute_post**](DefaultApi.md#recommendations_compute_post) | **POST** /recommendations/compute | Get recommendations for compute instances
[**recommendations_disks_post**](DefaultApi.md#recommendations_disks_post) | **POST** /recommendations/disks | Get recommendations for disks
[**recommendations_post**](DefaultApi.md#recommendations_post) | **POST** /recommendations | Get recommendations for compute instances


# **healthz_get**
> Dict[str, str] healthz_get()

Health check endpoint

Health check endpoint
Superseded by GET /v1/healthz.

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
> RegisteredComputePrices marketplace_providers_compute_delete(id)

Delete a custom provider instance

Delete one of your compute rates by id.
A rate a resource is already priced against cannot be deleted; the request fails while that link exists, so re-pin those resources first.
Once it is gone, a resource still carrying its id stops resolving a price rather than falling back to attribute matching.
Superseded by DELETE /v1/marketplace/compute/{id}, which returns RFC 9457 problem responses on failure.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.registered_compute_prices import RegisteredComputePrices
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

[**RegisteredComputePrices**](RegisteredComputePrices.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pricing response for a custom provider |  -  |
**400** | Invalid id |  -  |
**401** | Provider and organization do not match |  -  |
**404** | Instance not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplace_providers_compute_get**
> ComputePriceList marketplace_providers_compute_get(limit=limit, offset=offset, service=service, region=region, instance_type=instance_type, usage_type=usage_type)

Get your custom pricing entries

List the compute rates your organization has registered. Only your own rates are returned, never another organization's.
Filters combine, and paging is by limit and offset.
Superseded by GET /v1/marketplace/compute, which returns RFC 9457 problem responses on failure.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.compute_price_list import ComputePriceList
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
    api_instance = pricing_api_client.DefaultApi(api_client)
    limit = 56 # int | Maximum entries to return (default 500) (optional)
    offset = 56 # int | Entries to skip (optional)
    service = 'service_example' # str | Filter by service (optional)
    region = 'region_example' # str | Filter by region (optional)
    instance_type = 'instance_type_example' # str | Filter by instance type (optional)
    usage_type = 'usage_type_example' # str | Filter by usage type (optional)

    try:
        # Get your custom pricing entries
        api_response = api_instance.marketplace_providers_compute_get(limit=limit, offset=offset, service=service, region=region, instance_type=instance_type, usage_type=usage_type)
        print("The response of DefaultApi->marketplace_providers_compute_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->marketplace_providers_compute_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum entries to return (default 500) | [optional] 
 **offset** | **int**| Entries to skip | [optional] 
 **service** | **str**| Filter by service | [optional] 
 **region** | **str**| Filter by region | [optional] 
 **instance_type** | **str**| Filter by instance type | [optional] 
 **usage_type** | **str**| Filter by usage type | [optional] 

### Return type

[**ComputePriceList**](ComputePriceList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pricing response for custom pricing |  -  |
**400** | Invalid limit or offset |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplace_providers_compute_post**
> RegisteredComputePrices marketplace_providers_compute_post(instance)

Register a custom provider

Register your own compute rates so CostGraph can price machines it has no public price for, such as bare metal or a private cloud.
An entry is upserted on its natural key (provider, service, region, availability zone, usage type, instance type, operating system and period billing hours), so re-posting the same entry with a new cost keeps its id and reprices everything already using it. Changing any key field mints a new id, because it describes a different SKU.
The returned id is what you attach to a resource with the `costgraph.ai/pricing-id.compute` label or tag. Treat it as a secret you hand out deliberately: anyone holding it can pin to the rate, which is how a provider prices clusters it sells on.
Superseded by POST /v1/marketplace/compute, which returns RFC 9457 problem responses on failure.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.compute_prices_request import ComputePricesRequest
from pricing_api_client.models.registered_compute_prices import RegisteredComputePrices
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
    api_instance = pricing_api_client.DefaultApi(api_client)
    instance = pricing_api_client.ComputePricesRequest() # ComputePricesRequest | Custom pricing request

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
 **instance** | [**ComputePricesRequest**](ComputePricesRequest.md)| Custom pricing request | 

### Return type

[**RegisteredComputePrices**](RegisteredComputePrices.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pricing response for a custom provider |  -  |
**400** | Invalid request body |  -  |
**401** | Provider and organization do not match |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplace_providers_databases_delete**
> RegisteredDatabasePrices marketplace_providers_databases_delete(id)

Delete a custom database pricing entry

Delete one of your managed database rates by id.
A rate a database or one of its reports still references cannot be deleted; the request fails while that reference exists, so re-pin first.
Once it is gone, a database still carrying its id stops resolving a price.
Superseded by DELETE /v1/marketplace/databases/{id}, which returns RFC 9457 problem responses on failure.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.registered_database_prices import RegisteredDatabasePrices
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
    api_instance = pricing_api_client.DefaultApi(api_client)
    id = 'id_example' # str | Database pricing ID

    try:
        # Delete a custom database pricing entry
        api_response = api_instance.marketplace_providers_databases_delete(id)
        print("The response of DefaultApi->marketplace_providers_databases_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->marketplace_providers_databases_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Database pricing ID | 

### Return type

[**RegisteredDatabasePrices**](RegisteredDatabasePrices.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pricing response for custom database pricing |  -  |
**400** | Invalid id |  -  |
**401** | Provider and organization do not match |  -  |
**404** | Database pricing entry not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplace_providers_databases_get**
> DatabasePriceList marketplace_providers_databases_get(limit=limit, offset=offset, service=service, region=region, engine=engine, edition=edition, instance_type=instance_type, usage_type=usage_type)

Get your custom database pricing entries

List the managed database rates your organization has registered. Only your own rates are returned.
Filters combine, and paging is by limit and offset.
Superseded by GET /v1/marketplace/databases, which returns RFC 9457 problem responses on failure.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.database_price_list import DatabasePriceList
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
    api_instance = pricing_api_client.DefaultApi(api_client)
    limit = 56 # int | Maximum entries to return (default 500) (optional)
    offset = 56 # int | Entries to skip (optional)
    service = 'service_example' # str | Filter by service (optional)
    region = 'region_example' # str | Filter by region (optional)
    engine = 'engine_example' # str | Filter by engine (optional)
    edition = 'edition_example' # str | Filter by edition (optional)
    instance_type = 'instance_type_example' # str | Filter by instance type (optional)
    usage_type = 'usage_type_example' # str | Filter by usage type (optional)

    try:
        # Get your custom database pricing entries
        api_response = api_instance.marketplace_providers_databases_get(limit=limit, offset=offset, service=service, region=region, engine=engine, edition=edition, instance_type=instance_type, usage_type=usage_type)
        print("The response of DefaultApi->marketplace_providers_databases_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->marketplace_providers_databases_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum entries to return (default 500) | [optional] 
 **offset** | **int**| Entries to skip | [optional] 
 **service** | **str**| Filter by service | [optional] 
 **region** | **str**| Filter by region | [optional] 
 **engine** | **str**| Filter by engine | [optional] 
 **edition** | **str**| Filter by edition | [optional] 
 **instance_type** | **str**| Filter by instance type | [optional] 
 **usage_type** | **str**| Filter by usage type | [optional] 

### Return type

[**DatabasePriceList**](DatabasePriceList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pricing response for custom database pricing |  -  |
**400** | Invalid limit or offset |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplace_providers_databases_post**
> RegisteredDatabasePrices marketplace_providers_databases_post(instance)

Register custom database pricing

Register your own managed database rates, keyed by engine, edition, deployment option, storage type and instance type alongside the usual provider, service and region.
An entry is upserted on the full natural key (provider, service, region, availability zone, usage type, engine, edition, deployment option, billing config, storage type, instance type, architecture and period billing hours), so re-posting with a new cost keeps its id; changing any key field mints a new one.
The returned id is what you attach with the `costgraph.ai/pricing-id.database` label or tag.
Superseded by POST /v1/marketplace/databases, which returns RFC 9457 problem responses on failure.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.database_prices_request import DatabasePricesRequest
from pricing_api_client.models.registered_database_prices import RegisteredDatabasePrices
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
    api_instance = pricing_api_client.DefaultApi(api_client)
    instance = pricing_api_client.DatabasePricesRequest() # DatabasePricesRequest | Custom database pricing request

    try:
        # Register custom database pricing
        api_response = api_instance.marketplace_providers_databases_post(instance)
        print("The response of DefaultApi->marketplace_providers_databases_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->marketplace_providers_databases_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**DatabasePricesRequest**](DatabasePricesRequest.md)| Custom database pricing request | 

### Return type

[**RegisteredDatabasePrices**](RegisteredDatabasePrices.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pricing response for custom database pricing |  -  |
**400** | Invalid request body |  -  |
**401** | Provider and organization do not match |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplace_providers_disks_delete**
> RegisteredDiskPrices marketplace_providers_disks_delete(id)

Delete a custom disk provider entry

Delete one of your storage rates by id.
A rate a volume is already priced against cannot be deleted; the request fails while that link exists, so re-pin those volumes first.
Once it is gone, a volume still carrying its id stops resolving a price.
Superseded by DELETE /v1/marketplace/disks/{id}, which returns RFC 9457 problem responses on failure.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.registered_disk_prices import RegisteredDiskPrices
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
    api_instance = pricing_api_client.DefaultApi(api_client)
    id = 'id_example' # str | Disk pricing ID

    try:
        # Delete a custom disk provider entry
        api_response = api_instance.marketplace_providers_disks_delete(id)
        print("The response of DefaultApi->marketplace_providers_disks_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->marketplace_providers_disks_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Disk pricing ID | 

### Return type

[**RegisteredDiskPrices**](RegisteredDiskPrices.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pricing response for a custom disk provider |  -  |
**400** | Invalid id |  -  |
**401** | Provider and organization do not match |  -  |
**404** | Disk pricing entry not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplace_providers_disks_get**
> DiskPriceList marketplace_providers_disks_get(limit=limit, offset=offset, service=service, region=region, type=type, usage_type=usage_type)

Get your custom disk pricing entries

List the storage rates your organization has registered. Only your own rates are returned.
Filters combine, and paging is by limit and offset.
Superseded by GET /v1/marketplace/disks, which returns RFC 9457 problem responses on failure.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.disk_price_list import DiskPriceList
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
    api_instance = pricing_api_client.DefaultApi(api_client)
    limit = 56 # int | Maximum entries to return (default 500) (optional)
    offset = 56 # int | Entries to skip (optional)
    service = 'service_example' # str | Filter by service (optional)
    region = 'region_example' # str | Filter by region (optional)
    type = 'type_example' # str | Filter by disk type (optional)
    usage_type = 'usage_type_example' # str | Filter by usage type (optional)

    try:
        # Get your custom disk pricing entries
        api_response = api_instance.marketplace_providers_disks_get(limit=limit, offset=offset, service=service, region=region, type=type, usage_type=usage_type)
        print("The response of DefaultApi->marketplace_providers_disks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->marketplace_providers_disks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum entries to return (default 500) | [optional] 
 **offset** | **int**| Entries to skip | [optional] 
 **service** | **str**| Filter by service | [optional] 
 **region** | **str**| Filter by region | [optional] 
 **type** | **str**| Filter by disk type | [optional] 
 **usage_type** | **str**| Filter by usage type | [optional] 

### Return type

[**DiskPriceList**](DiskPriceList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pricing response for custom disk pricing |  -  |
**400** | Invalid limit or offset |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplace_providers_disks_post**
> RegisteredDiskPrices marketplace_providers_disks_post(instance)

Register a custom disk provider

Register your own storage rates, priced per GB hour with optional IOPS and throughput components and the capacity band they apply to.
An entry is upserted on its natural key (provider, service, region, availability zone, disk type, usage type and period billing hours), so re-posting with a new cost keeps its id; changing a key field mints a new one.
Capacity, IOPS and throughput bands are not part of that key, so a second band for the same disk type replaces the first: give each band its own usage type.
The returned id is what you attach with the `costgraph.ai/pricing-id.storage` label or tag.
Superseded by POST /v1/marketplace/disks, which returns RFC 9457 problem responses on failure.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.disk_prices_request import DiskPricesRequest
from pricing_api_client.models.registered_disk_prices import RegisteredDiskPrices
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
    api_instance = pricing_api_client.DefaultApi(api_client)
    instance = pricing_api_client.DiskPricesRequest() # DiskPricesRequest | Custom disk pricing request

    try:
        # Register a custom disk provider
        api_response = api_instance.marketplace_providers_disks_post(instance)
        print("The response of DefaultApi->marketplace_providers_disks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->marketplace_providers_disks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**DiskPricesRequest**](DiskPricesRequest.md)| Custom disk pricing request | 

### Return type

[**RegisteredDiskPrices**](RegisteredDiskPrices.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pricing response for a custom disk provider |  -  |
**400** | Invalid request body |  -  |
**401** | Provider and organization do not match |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplace_providers_models_delete**
> RegisteredModelPrices marketplace_providers_models_delete(id)

Delete a custom model pricing entry

Delete one of your model rates by id. The row is closed rather than removed, so spend already priced against it keeps that rate.
Usage still pinned to it stops resolving a price, so re-pin before deleting.
Superseded by DELETE /v1/marketplace/models/{id}, which returns RFC 9457 problem responses on failure.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.registered_model_prices import RegisteredModelPrices
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
    api_instance = pricing_api_client.DefaultApi(api_client)
    id = 'id_example' # str | Model pricing ID

    try:
        # Delete a custom model pricing entry
        api_response = api_instance.marketplace_providers_models_delete(id)
        print("The response of DefaultApi->marketplace_providers_models_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->marketplace_providers_models_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model pricing ID | 

### Return type

[**RegisteredModelPrices**](RegisteredModelPrices.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pricing response for custom model pricing |  -  |
**400** | Invalid id |  -  |
**401** | Host and organization do not match |  -  |
**404** | Model pricing entry not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplace_providers_models_get**
> ModelPriceList marketplace_providers_models_get(limit=limit, offset=offset, model=model, provider=provider, region=region, token_bucket=token_bucket)

Get your custom model pricing entries

List the live version of each model rate your organization has registered. Only your own rates are returned.
Filters combine, and paging is by limit and offset.
Superseded by GET /v1/marketplace/models, which returns RFC 9457 problem responses on failure.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.model_price_list import ModelPriceList
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
    api_instance = pricing_api_client.DefaultApi(api_client)
    limit = 56 # int | Maximum entries to return (default 500) (optional)
    offset = 56 # int | Entries to skip (optional)
    model = 'model_example' # str | Filter by model (optional)
    provider = 'provider_example' # str | Filter by model provider (optional)
    region = 'region_example' # str | Filter by region (optional)
    token_bucket = 'token_bucket_example' # str | Filter by token bucket (optional)

    try:
        # Get your custom model pricing entries
        api_response = api_instance.marketplace_providers_models_get(limit=limit, offset=offset, model=model, provider=provider, region=region, token_bucket=token_bucket)
        print("The response of DefaultApi->marketplace_providers_models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->marketplace_providers_models_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum entries to return (default 500) | [optional] 
 **offset** | **int**| Entries to skip | [optional] 
 **model** | **str**| Filter by model | [optional] 
 **provider** | **str**| Filter by model provider | [optional] 
 **region** | **str**| Filter by region | [optional] 
 **token_bucket** | **str**| Filter by token bucket | [optional] 

### Return type

[**ModelPriceList**](ModelPriceList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pricing response for custom model pricing |  -  |
**400** | Invalid limit or offset |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplace_providers_models_post**
> RegisteredModelPrices marketplace_providers_models_post(instance)

Register custom model pricing

Register custom token pricing for models you host. Entries are versioned: a price change closes the current row and opens a new one, so historic spend keeps the rate it was billed at.
The returned id is what you attach with the `costgraph.ai/pricing-id.model` label or tag. Each version carries its own id, so read the live entry back after a price change instead of holding on to an earlier one.
Superseded by POST /v1/marketplace/models, which returns RFC 9457 problem responses on failure.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.model_prices_request import ModelPricesRequest
from pricing_api_client.models.registered_model_prices import RegisteredModelPrices
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
    api_instance = pricing_api_client.DefaultApi(api_client)
    instance = pricing_api_client.ModelPricesRequest() # ModelPricesRequest | Custom model pricing request

    try:
        # Register custom model pricing
        api_response = api_instance.marketplace_providers_models_post(instance)
        print("The response of DefaultApi->marketplace_providers_models_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->marketplace_providers_models_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**ModelPricesRequest**](ModelPricesRequest.md)| Custom model pricing request | 

### Return type

[**RegisteredModelPrices**](RegisteredModelPrices.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pricing response for custom model pricing |  -  |
**400** | Invalid request body |  -  |
**401** | Host and organization do not match |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pricing_compute_post**
> ComputePrice pricing_compute_post(instance)

Get pricing for an instance

Get pricing for compute instances
Superseded by POST /v1/pricing/compute, which returns RFC 9457 problem responses on failure.

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
    api_instance = pricing_api_client.DefaultApi(api_client)
    instance = pricing_api_client.Instance() # Instance | Instance

    try:
        # Get pricing for an instance
        api_response = api_instance.pricing_compute_post(instance)
        print("The response of DefaultApi->pricing_compute_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->pricing_compute_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**Instance**](Instance.md)| Instance | 

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
**200** | Pricing for a given instance |  -  |
**400** | Invalid request body |  -  |
**401** | Unauthorized |  -  |
**404** | Pricing not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pricing_disks_post**
> DiskPrice pricing_disks_post(instance)

Get pricing for a disk

Get pricing for a disk
Superseded by POST /v1/pricing/disks, which returns RFC 9457 problem responses on failure.

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
    api_instance = pricing_api_client.DefaultApi(api_client)
    instance = pricing_api_client.Disk() # Disk | Disk

    try:
        # Get pricing for a disk
        api_response = api_instance.pricing_disks_post(instance)
        print("The response of DefaultApi->pricing_disks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->pricing_disks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**Disk**](Disk.md)| Disk | 

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
**200** | Pricing for a given disk |  -  |
**400** | Invalid request body |  -  |
**401** | Unauthorized |  -  |
**404** | Pricing not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pricing_post**
> ComputePrice pricing_post(instance)

Get pricing for an instance

Get pricing for compute instances
Superseded by POST /v1/pricing/compute, which returns RFC 9457 problem responses on failure.

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
    api_instance = pricing_api_client.DefaultApi(api_client)
    instance = pricing_api_client.Instance() # Instance | Instance

    try:
        # Get pricing for an instance
        api_response = api_instance.pricing_post(instance)
        print("The response of DefaultApi->pricing_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->pricing_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**Instance**](Instance.md)| Instance | 

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
**200** | Pricing for a given instance |  -  |
**400** | Invalid request body |  -  |
**401** | Unauthorized |  -  |
**404** | Pricing not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_get**
> Dict[str, ProviderConfig] providers_get()

Get details for the providers

Get details for the providers
Superseded by GET /v1/providers, which returns RFC 9457 problem responses on failure.

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

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of providers |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recommendations_compute_post**
> List[ComputeRecommendation] recommendations_compute_post(instance)

Get recommendations for compute instances

Get the cheapest compute candidate per provider with savings versus the requested instance
Superseded by POST /v1/recommendations/compute, which returns RFC 9457 problem responses on failure.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.compute_recommendation import ComputeRecommendation
from pricing_api_client.models.compute_recommendation_request import ComputeRecommendationRequest
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
    api_instance = pricing_api_client.DefaultApi(api_client)
    instance = pricing_api_client.ComputeRecommendationRequest() # ComputeRecommendationRequest | Instance

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
 **instance** | [**ComputeRecommendationRequest**](ComputeRecommendationRequest.md)| Instance | 

### Return type

[**List[ComputeRecommendation]**](ComputeRecommendation.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request body |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recommendations_disks_post**
> List[DiskRecommendation] recommendations_disks_post(instance)

Get recommendations for disks

Get the cheapest disk candidate per provider with savings versus the requested disk
Superseded by POST /v1/recommendations/disks, which returns RFC 9457 problem responses on failure.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.disk_recommendation import DiskRecommendation
from pricing_api_client.models.disk_recommendation_request import DiskRecommendationRequest
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
    api_instance = pricing_api_client.DefaultApi(api_client)
    instance = pricing_api_client.DiskRecommendationRequest() # DiskRecommendationRequest | Instance

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
 **instance** | [**DiskRecommendationRequest**](DiskRecommendationRequest.md)| Instance | 

### Return type

[**List[DiskRecommendation]**](DiskRecommendation.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request body |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recommendations_post**
> List[ComputeRecommendation] recommendations_post(instance)

Get recommendations for compute instances

Get the cheapest compute candidate per provider with savings versus the requested instance
Superseded by POST /v1/recommendations/compute, which returns RFC 9457 problem responses on failure.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import pricing_api_client
from pricing_api_client.models.compute_recommendation import ComputeRecommendation
from pricing_api_client.models.compute_recommendation_request import ComputeRecommendationRequest
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
    api_instance = pricing_api_client.DefaultApi(api_client)
    instance = pricing_api_client.ComputeRecommendationRequest() # ComputeRecommendationRequest | Instance

    try:
        # Get recommendations for compute instances
        api_response = api_instance.recommendations_post(instance)
        print("The response of DefaultApi->recommendations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->recommendations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**ComputeRecommendationRequest**](ComputeRecommendationRequest.md)| Instance | 

### Return type

[**List[ComputeRecommendation]**](ComputeRecommendation.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request body |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

