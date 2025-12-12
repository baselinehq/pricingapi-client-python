# GithubComBaselinehqGolangSharedTypesInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_zone** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**instance_type** | **str** |  | [optional] 
**operating_system** | **str** |  | [optional] 
**provider** | [**GithubComBaselinehqGolangSharedTypesProvider**](GithubComBaselinehqGolangSharedTypesProvider.md) |  | [optional] 
**region** | **str** |  | [optional] 
**service** | [**GithubComBaselinehqGolangSharedTypesService**](GithubComBaselinehqGolangSharedTypesService.md) |  | [optional] 
**usage_type** | [**GithubComBaselinehqGolangSharedTypesUsageType**](GithubComBaselinehqGolangSharedTypesUsageType.md) |  | [optional] 
**vm** | [**GithubComBaselinehqGolangSharedTypesVM**](GithubComBaselinehqGolangSharedTypesVM.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.github_com_baselinehq_golang_shared_types_instance import GithubComBaselinehqGolangSharedTypesInstance

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComBaselinehqGolangSharedTypesInstance from a JSON string
github_com_baselinehq_golang_shared_types_instance_instance = GithubComBaselinehqGolangSharedTypesInstance.from_json(json)
# print the JSON string representation of the object
print(GithubComBaselinehqGolangSharedTypesInstance.to_json())

# convert the object into a dict
github_com_baselinehq_golang_shared_types_instance_dict = github_com_baselinehq_golang_shared_types_instance_instance.to_dict()
# create an instance of GithubComBaselinehqGolangSharedTypesInstance from a dict
github_com_baselinehq_golang_shared_types_instance_from_dict = GithubComBaselinehqGolangSharedTypesInstance.from_dict(github_com_baselinehq_golang_shared_types_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


