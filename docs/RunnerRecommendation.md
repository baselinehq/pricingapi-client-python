# RunnerRecommendation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billed_seconds** | **float** |  | [optional] 
**compute_source** | **str** |  | [optional] 
**cost** | **float** |  | [optional] 
**cost_per_month** | **float** |  | [optional] 
**fetched_on** | **str** |  | [optional] 
**flags** | **List[str]** |  | [optional] 
**plan_fees** | [**List[TypesRunnerPlanFee]**](TypesRunnerPlanFee.md) |  | [optional] 
**pricing_model** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**runtime_seconds** | **float** |  | [optional] 
**savings_vs_current** | **float** |  | [optional] 
**sku** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 
**vm_instance_type** | **str** |  | [optional] 

## Example

```python
from pricing_api_client.models.runner_recommendation import RunnerRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerRecommendation from a JSON string
runner_recommendation_instance = RunnerRecommendation.from_json(json)
# print the JSON string representation of the object
print(RunnerRecommendation.to_json())

# convert the object into a dict
runner_recommendation_dict = runner_recommendation_instance.to_dict()
# create an instance of RunnerRecommendation from a dict
runner_recommendation_from_dict = RunnerRecommendation.from_dict(runner_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


