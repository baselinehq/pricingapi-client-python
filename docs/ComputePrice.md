# ComputePrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **str** |  | [optional] 
**availability_zone** | **str** |  | [optional] 
**cost_per_hour** | **float** | On-demand-equivalent hourly USD; multiply by provider_pricing_rules.month_hours for monthly. | [optional] 
**cpu_cores** | **float** |  | [optional] 
**cpu_cores_cost_per_hour** | **float** |  | [optional] 
**created_at** | **str** |  | [optional] 
**currency** | **str** | Currency the provider published this price in. Cost columns are always normalized USD. | [optional] 
**gpu_cost_per_hour** | **float** |  | [optional] 
**gpu_count** | **float** |  | [optional] 
**gpu_type** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**instance_type** | **str** |  | [optional] 
**native_cost_per_hour** | **float** | cost_per_hour as published, before FX normalization. Zero when currency is USD. | [optional] 
**operating_system** | **str** |  | [optional] 
**period_billing_hours** | **float** | Commitment term the raw price covers: 1&#x3D;hourly on-demand; 8640/25920/43200&#x3D;1mo/3mo/1yr buckets. cost_per_hour is already normalized to hourly. | [optional] 
**provider** | **str** |  | [optional] 
**ram_gb** | **float** |  | [optional] 
**ram_gb_cost_per_hour** | **float** |  | [optional] 
**raw_pricing_data** | **object** |  | [optional] 
**region** | **str** |  | [optional] 
**resizable** | **bool** | True when the row carries per-vCPU and per-GB rates for a shape sized at launch; resolution stores and returns a row priced at the requested vCPU and memory. NULL or false is a fixed-size shape. | [optional] 
**service** | **str** |  | [optional] 
**tags** | **object** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**usage_type** | **str** | Pricing tier token (ONDEMAND, RESERVED, SPOT_*, *_HBP, *_BYOL, Commit1Yr/3Yr). Filter to ONDEMAND for normal pricing. | [optional] 

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


