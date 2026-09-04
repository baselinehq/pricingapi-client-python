# ComputePrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **str** |  | [optional] 
**availability_zone** | **str** |  | [optional] 
**cost_per_hour** | **float** |  | [optional] 
**cpu_cores** | **float** |  | [optional] 
**cpu_cores_cost_per_hour** | **float** |  | [optional] 
**created_at** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**gpu_cost_per_hour** | **float** |  | [optional] 
**gpu_count** | **float** |  | [optional] 
**gpu_type** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**instance_type** | **str** |  | [optional] 
**native_cost_per_hour** | **float** |  | [optional] 
**operating_system** | **str** |  | [optional] 
**period_billing_hours** | **float** |  | [optional] 
**provider** | **str** |  | [optional] 
**ram_gb** | **float** |  | [optional] 
**ram_gb_cost_per_hour** | **float** |  | [optional] 
**raw_pricing_data** | **object** |  | [optional] 
**region** | **str** |  | [optional] 
**service** | **str** |  | [optional] 
**tags** | **object** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**usage_type** | **str** |  | [optional] 

## Example

```python
from pricing_api_client.models.compute_price import ComputePrice

# TODO update the JSON string below
json = "{}"
# create an instance of ComputePrice from a JSON string
compute_price_instance = ComputePrice.from_json(json)
# print the JSON string representation of the object
print(ComputePrice.to_json())

# convert the object into a dict
compute_price_dict = compute_price_instance.to_dict()
# create an instance of ComputePrice from a dict
compute_price_from_dict = ComputePrice.from_dict(compute_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


