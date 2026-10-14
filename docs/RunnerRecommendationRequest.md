# RunnerRecommendationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billed_minutes** | **float** |  | [optional] 
**current** | [**TypesRunnerCurrent**](TypesRunnerCurrent.md) |  | [optional] 
**job_count** | **int** |  | [optional] 
**jobs_seconds** | **List[float]** |  | [optional] 
**monthly_minutes** | **float** |  | [optional] 
**public_repo** | **bool** |  | [optional] 
**self_hosted** | [**TypesRunnerSelfHosted**](TypesRunnerSelfHosted.md) |  | [optional] 
**shape** | [**TypesRunnerShape**](TypesRunnerShape.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.runner_recommendation_request import RunnerRecommendationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerRecommendationRequest from a JSON string
runner_recommendation_request_instance = RunnerRecommendationRequest.from_json(json)
# print the JSON string representation of the object
print(RunnerRecommendationRequest.to_json())

# convert the object into a dict
runner_recommendation_request_dict = runner_recommendation_request_instance.to_dict()
# create an instance of RunnerRecommendationRequest from a dict
runner_recommendation_request_from_dict = RunnerRecommendationRequest.from_dict(runner_recommendation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


