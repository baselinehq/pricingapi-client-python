# Disk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_zone** | **str** |  | [optional] 
**capacity_gb** | **float** |  | [optional] 
**fallback_to_base_pricing** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**iops** | **float** |  | [optional] 
**provider** | [**GithubComBaselinehqGolangSharedTypesProvider**](GithubComBaselinehqGolangSharedTypesProvider.md) |  | [optional] 
**region** | **str** |  | [optional] 
**service** | [**TypesService**](TypesService.md) |  | [optional] 
**throughput_mbps** | **float** |  | [optional] 
**type** | **str** |  | [optional] 
**usage_type** | [**GithubComBaselinehqGolangSharedTypesUsageType**](GithubComBaselinehqGolangSharedTypesUsageType.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.disk import Disk

# TODO update the JSON string below
json = "{}"
# create an instance of Disk from a JSON string
disk_instance = Disk.from_json(json)
# print the JSON string representation of the object
print(Disk.to_json())

# convert the object into a dict
disk_dict = disk_instance.to_dict()
# create an instance of Disk from a dict
disk_from_dict = Disk.from_dict(disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


