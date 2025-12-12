# TypesDiskResultsValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk** | [**SchemaDiskPricingsRow**](SchemaDiskPricingsRow.md) |  | [optional] 
**disk_pricing** | [**SchemaDiskPricingsRow**](SchemaDiskPricingsRow.md) |  | [optional] 
**savings** | [**TypesSavings**](TypesSavings.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.types_disk_results_value_inner import TypesDiskResultsValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of TypesDiskResultsValueInner from a JSON string
types_disk_results_value_inner_instance = TypesDiskResultsValueInner.from_json(json)
# print the JSON string representation of the object
print(TypesDiskResultsValueInner.to_json())

# convert the object into a dict
types_disk_results_value_inner_dict = types_disk_results_value_inner_instance.to_dict()
# create an instance of TypesDiskResultsValueInner from a dict
types_disk_results_value_inner_from_dict = TypesDiskResultsValueInner.from_dict(types_disk_results_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


