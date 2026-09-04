# ComputeRecommendation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pricing** | [**ComputePrice**](ComputePrice.md) |  | [optional] 
**savings** | [**TypesSavings**](TypesSavings.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.compute_recommendation import ComputeRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeRecommendation from a JSON string
compute_recommendation_instance = ComputeRecommendation.from_json(json)
# print the JSON string representation of the object
print(ComputeRecommendation.to_json())

# convert the object into a dict
compute_recommendation_dict = compute_recommendation_instance.to_dict()
# create an instance of ComputeRecommendation from a dict
compute_recommendation_from_dict = ComputeRecommendation.from_dict(compute_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


