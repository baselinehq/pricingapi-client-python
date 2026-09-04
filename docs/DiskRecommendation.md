# DiskRecommendation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pricing** | [**DiskPrice**](DiskPrice.md) |  | [optional] 
**savings** | [**TypesSavings**](TypesSavings.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.disk_recommendation import DiskRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of DiskRecommendation from a JSON string
disk_recommendation_instance = DiskRecommendation.from_json(json)
# print the JSON string representation of the object
print(DiskRecommendation.to_json())

# convert the object into a dict
disk_recommendation_dict = disk_recommendation_instance.to_dict()
# create an instance of DiskRecommendation from a dict
disk_recommendation_from_dict = DiskRecommendation.from_dict(disk_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


