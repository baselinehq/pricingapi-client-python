# SchemaDiskPricingsRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_zone** | **str** |  | [optional] 
**cost_per_gb_hour** | **float** |  | [optional] 
**cost_per_iops_hour** | **float** |  | [optional] 
**cost_per_throughput_mbps_hour** | **float** |  | [optional] 
**created_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**max_capacity_gb** | **float** |  | [optional] 
**max_iops** | **float** |  | [optional] 
**max_throughput_mbps** | **float** |  | [optional] 
**min_capacity_gb** | **float** |  | [optional] 
**min_iops** | **float** |  | [optional] 
**min_throughput_mbps** | **float** |  | [optional] 
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
from pricing_api_client.models.schema_disk_pricings_row import SchemaDiskPricingsRow

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaDiskPricingsRow from a JSON string
schema_disk_pricings_row_instance = SchemaDiskPricingsRow.from_json(json)
# print the JSON string representation of the object
print(SchemaDiskPricingsRow.to_json())

# convert the object into a dict
schema_disk_pricings_row_dict = schema_disk_pricings_row_instance.to_dict()
# create an instance of SchemaDiskPricingsRow from a dict
schema_disk_pricings_row_from_dict = SchemaDiskPricingsRow.from_dict(schema_disk_pricings_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


