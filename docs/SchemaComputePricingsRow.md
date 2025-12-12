# SchemaComputePricingsRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_zone** | **str** |  | [optional] 
**cost_per_hour** | **float** |  | [optional] 
**cpu_cores** | **float** |  | [optional] 
**cpu_cores_cost_per_hour** | **float** |  | [optional] 
**created_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**instance_type** | **str** |  | [optional] 
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
from pricing_api_client.models.schema_compute_pricings_row import SchemaComputePricingsRow

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaComputePricingsRow from a JSON string
schema_compute_pricings_row_instance = SchemaComputePricingsRow.from_json(json)
# print the JSON string representation of the object
print(SchemaComputePricingsRow.to_json())

# convert the object into a dict
schema_compute_pricings_row_dict = schema_compute_pricings_row_instance.to_dict()
# create an instance of SchemaComputePricingsRow from a dict
schema_compute_pricings_row_from_dict = SchemaComputePricingsRow.from_dict(schema_compute_pricings_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


