# pricing_api_client.RecommendationsApi

All URIs are relative to *https://pricing.baselinehq.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_recommendations_compute_post**](RecommendationsApi.md#v1_recommendations_compute_post) | **POST** /v1/recommendations/compute | Find cheaper machines
[**v1_recommendations_disks_post**](RecommendationsApi.md#v1_recommendations_disks_post) | **POST** /v1/recommendations/disks | Find cheaper volumes


# **v1_recommendations_compute_post**
> List[ComputeRecommendation] v1_recommendations_compute_post(instance)

Find cheaper machines

Return the cheapest machine per provider that still meets the requested shape, with the saving against the machine you asked about.

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
    api_instance = pricing_api_client.RecommendationsApi(api_client)
    instance = pricing_api_client.ComputeRecommendationRequest() # ComputeRecommendationRequest | Machine to improve on

    try:
        # Find cheaper machines
        api_response = api_instance.v1_recommendations_compute_post(instance)
        print("The response of RecommendationsApi->v1_recommendations_compute_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecommendationsApi->v1_recommendations_compute_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**ComputeRecommendationRequest**](ComputeRecommendationRequest.md)| Machine to improve on | 

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
**200** | The cheapest candidate per provider |  -  |
**400** | Invalid request body |  -  |
**401** | Unauthenticated |  -  |
**404** | No candidate matches the machine |  -  |
**422** | Validation failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_recommendations_disks_post**
> List[DiskRecommendation] v1_recommendations_disks_post(instance)

Find cheaper volumes

Return the cheapest volume per provider that still meets the requested capacity and performance, with the saving against the volume you asked about.

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
    api_instance = pricing_api_client.RecommendationsApi(api_client)
    instance = pricing_api_client.DiskRecommendationRequest() # DiskRecommendationRequest | Volume to improve on

    try:
        # Find cheaper volumes
        api_response = api_instance.v1_recommendations_disks_post(instance)
        print("The response of RecommendationsApi->v1_recommendations_disks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecommendationsApi->v1_recommendations_disks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**DiskRecommendationRequest**](DiskRecommendationRequest.md)| Volume to improve on | 

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
**200** | The cheapest candidate per provider |  -  |
**400** | Invalid request body |  -  |
**401** | Unauthenticated |  -  |
**404** | No candidate matches the volume |  -  |
**422** | Validation failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

