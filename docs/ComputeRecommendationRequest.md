# ComputeRecommendationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_metadata** | **bool** |  | [optional] 
**instance** | [**GithubComBaselinehqGolangSharedTypesInstance**](GithubComBaselinehqGolangSharedTypesInstance.md) |  | [optional] 
**predicates** | [**TypesPredicates**](TypesPredicates.md) |  | [optional] 
**usage** | [**GithubComBaselinehqGolangSharedTypesVM**](GithubComBaselinehqGolangSharedTypesVM.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.compute_recommendation_request import ComputeRecommendationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeRecommendationRequest from a JSON string
compute_recommendation_request_instance = ComputeRecommendationRequest.from_json(json)
# print the JSON string representation of the object
print(ComputeRecommendationRequest.to_json())

# convert the object into a dict
compute_recommendation_request_dict = compute_recommendation_request_instance.to_dict()
# create an instance of ComputeRecommendationRequest from a dict
compute_recommendation_request_from_dict = ComputeRecommendationRequest.from_dict(compute_recommendation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


