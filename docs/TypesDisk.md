# TypesDisk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_zone** | **str** |  | [optional] 
**capacity_gb** | **float** |  | [optional] 
**id** | **str** |  | [optional] 
**iops** | **float** |  | [optional] 
**provider** | [**GithubComBaselinehqGolangSharedTypesProvider**](GithubComBaselinehqGolangSharedTypesProvider.md) |  | [optional] 
**region** | **str** |  | [optional] 
**service** | [**GithubComBaselinehqGolangSharedTypesService**](GithubComBaselinehqGolangSharedTypesService.md) |  | [optional] 
**throughput_mbps** | **float** |  | [optional] 
**type** | **str** |  | [optional] 
**usage_type** | [**GithubComBaselinehqGolangSharedTypesUsageType**](GithubComBaselinehqGolangSharedTypesUsageType.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.types_disk import TypesDisk

# TODO update the JSON string below
json = "{}"
# create an instance of TypesDisk from a JSON string
types_disk_instance = TypesDisk.from_json(json)
# print the JSON string representation of the object
print(TypesDisk.to_json())

# convert the object into a dict
types_disk_dict = types_disk_instance.to_dict()
# create an instance of TypesDisk from a dict
types_disk_from_dict = TypesDisk.from_dict(types_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


