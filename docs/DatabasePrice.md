# DatabasePrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **str** |  | [optional] 
**availability_zone** | **str** |  | [optional] 
**billing_config** | **str** |  | [optional] 
**capacity_unit** | **str** |  | [optional] 
**cost_per_capacity_unit** | **float** |  | [optional] 
**cost_per_hour** | **float** |  | [optional] 
**cost_per_io_request** | **float** |  | [optional] 
**cost_per_iops_hour** | **float** |  | [optional] 
**cost_per_storage_gb_hour** | **float** |  | [optional] 
**cost_per_throughput_mbps_hour** | **float** |  | [optional] 
**cost_per_vcpu_license_hour** | **float** |  | [optional] 
**cpu_cores** | **float** |  | [optional] 
**cpu_cores_cost_per_hour** | **float** |  | [optional] 
**created_at** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**deployment_option** | **str** |  | [optional] 
**edition** | **str** |  | [optional] 
**engine** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**instance_type** | **str** |  | [optional] 
**max_iops** | **float** |  | [optional] 
**max_storage_gb** | **float** |  | [optional] 
**max_throughput_mbps** | **float** |  | [optional] 
**min_iops** | **float** |  | [optional] 
**min_storage_gb** | **float** |  | [optional] 
**min_throughput_mbps** | **float** |  | [optional] 
**native_cost_per_hour** | **float** |  | [optional] 
**native_cost_per_storage_gb_hour** | **float** |  | [optional] 
**period_billing_hours** | **float** |  | [optional] 
**provider** | **str** |  | [optional] 
**ram_gb** | **float** |  | [optional] 
**ram_gb_cost_per_hour** | **float** |  | [optional] 
**raw_pricing_data** | **object** |  | [optional] 
**region** | **str** |  | [optional] 
**service** | **str** |  | [optional] 
**storage_type** | **str** |  | [optional] 
**tags** | **object** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**usage_type** | **str** |  | [optional] 

## Example

```python
from pricing_api_client.models.database_price import DatabasePrice

# TODO update the JSON string below
json = "{}"
# create an instance of DatabasePrice from a JSON string
database_price_instance = DatabasePrice.from_json(json)
# print the JSON string representation of the object
print(DatabasePrice.to_json())

# convert the object into a dict
database_price_dict = database_price_instance.to_dict()
# create an instance of DatabasePrice from a dict
database_price_from_dict = DatabasePrice.from_dict(database_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


