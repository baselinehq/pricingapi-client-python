# TypesRunnerPlanFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee** | **float** |  | [optional] 
**per** | **str** |  | [optional] 
**period** | **str** |  | [optional] 
**plan** | **str** |  | [optional] 

## Example

```python
from pricing_api_client.models.types_runner_plan_fee import TypesRunnerPlanFee

# TODO update the JSON string below
json = "{}"
# create an instance of TypesRunnerPlanFee from a JSON string
types_runner_plan_fee_instance = TypesRunnerPlanFee.from_json(json)
# print the JSON string representation of the object
print(TypesRunnerPlanFee.to_json())

# convert the object into a dict
types_runner_plan_fee_dict = types_runner_plan_fee_instance.to_dict()
# create an instance of TypesRunnerPlanFee from a dict
types_runner_plan_fee_from_dict = TypesRunnerPlanFee.from_dict(types_runner_plan_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


