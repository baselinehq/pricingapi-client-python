# TypesPredicates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_zones** | **List[str]** |  | [optional] 
**disk_types** | **List[str]** |  | [optional] 
**instance_types** | **List[str]** |  | [optional] 
**operating_systems** | **List[str]** |  | [optional] 
**providers** | **List[str]** |  | [optional] 
**regions** | **List[str]** |  | [optional] 
**services** | **List[str]** |  | [optional] 
**usage_types** | **List[str]** |  | [optional] 

## Example

```python
from pricing_api_client.models.types_predicates import TypesPredicates

# TODO update the JSON string below
json = "{}"
# create an instance of TypesPredicates from a JSON string
types_predicates_instance = TypesPredicates.from_json(json)
# print the JSON string representation of the object
print(TypesPredicates.to_json())

# convert the object into a dict
types_predicates_dict = types_predicates_instance.to_dict()
# create an instance of TypesPredicates from a dict
types_predicates_from_dict = TypesPredicates.from_dict(types_predicates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


