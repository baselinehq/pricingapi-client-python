# Instance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_zone** | **str** |  | [optional] 
**fallback_to_base_pricing** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**instance_type** | **str** |  | [optional] 
**operating_system** | **str** |  | [optional] 
**provider** | [**GithubComBaselinehqGolangSharedTypesProvider**](GithubComBaselinehqGolangSharedTypesProvider.md) |  | [optional] 
**region** | **str** |  | [optional] 
**service** | [**TypesService**](TypesService.md) |  | [optional] 
**usage_type** | [**GithubComBaselinehqGolangSharedTypesUsageType**](GithubComBaselinehqGolangSharedTypesUsageType.md) |  | [optional] 
**vm** | [**GithubComBaselinehqGolangSharedTypesVM**](GithubComBaselinehqGolangSharedTypesVM.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.instance import Instance

# TODO update the JSON string below
json = "{}"
# create an instance of Instance from a JSON string
instance_instance = Instance.from_json(json)
# print the JSON string representation of the object
print(Instance.to_json())

# convert the object into a dict
instance_dict = instance_instance.to_dict()
# create an instance of Instance from a dict
instance_from_dict = Instance.from_dict(instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


