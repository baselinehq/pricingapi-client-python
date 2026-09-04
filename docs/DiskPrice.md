# DiskPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_zone** | **str** |  | [optional] 
**cost_per_gb_hour** | **float** |  | [optional] 
**cost_per_iops_hour** | **float** |  | [optional] 
**cost_per_throughput_mbps_hour** | **float** |  | [optional] 
**created_at** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**max_capacity_gb** | **float** |  | [optional] 
**max_iops** | **float** |  | [optional] 
**max_throughput_mbps** | **float** |  | [optional] 
**min_capacity_gb** | **float** |  | [optional] 
**min_iops** | **float** |  | [optional] 
**min_throughput_mbps** | **float** |  | [optional] 
**native_cost_per_gb_hour** | **float** |  | [optional] 
**native_cost_per_iops_hour** | **float** |  | [optional] 
**native_cost_per_throughput_mbps_hour** | **float** |  | [optional] 
**period_billing_hours** | **float** |  | [optional] 
**provider** | **str** |  | [optional] 
**raw_pricing_data** | **object** |  | [optional] 
**region** | **str** |  | [optional] 
**service** | **str** |  | [optional] 
**tags** | **object** |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**usage_type** | **str** |  | [optional] 

## Example

```python
from pricing_api_client.models.disk_price import DiskPrice

# TODO update the JSON string below
json = "{}"
# create an instance of DiskPrice from a JSON string
disk_price_instance = DiskPrice.from_json(json)
# print the JSON string representation of the object
print(DiskPrice.to_json())

# convert the object into a dict
disk_price_dict = disk_price_instance.to_dict()
# create an instance of DiskPrice from a dict
disk_price_from_dict = DiskPrice.from_dict(disk_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


