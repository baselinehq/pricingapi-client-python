# DiskRecommendationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_metadata** | **bool** |  | [optional] 
**instance** | [**TypesDisk**](TypesDisk.md) |  | [optional] 
**predicates** | [**TypesPredicates**](TypesPredicates.md) |  | [optional] 
**usage** | [**TypesDisk**](TypesDisk.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.disk_recommendation_request import DiskRecommendationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DiskRecommendationRequest from a JSON string
disk_recommendation_request_instance = DiskRecommendationRequest.from_json(json)
# print the JSON string representation of the object
print(DiskRecommendationRequest.to_json())

# convert the object into a dict
disk_recommendation_request_dict = disk_recommendation_request_instance.to_dict()
# create an instance of DiskRecommendationRequest from a dict
disk_recommendation_request_from_dict = DiskRecommendationRequest.from_dict(disk_recommendation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


