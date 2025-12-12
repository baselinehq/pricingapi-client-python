# TypesDiskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_metadata** | **bool** |  | [optional] 
**instance** | [**TypesDisk**](TypesDisk.md) |  | [optional] 
**predicates** | [**TypesPredicates**](TypesPredicates.md) |  | [optional] 
**usage** | [**TypesDisk**](TypesDisk.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.types_disk_request import TypesDiskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TypesDiskRequest from a JSON string
types_disk_request_instance = TypesDiskRequest.from_json(json)
# print the JSON string representation of the object
print(TypesDiskRequest.to_json())

# convert the object into a dict
types_disk_request_dict = types_disk_request_instance.to_dict()
# create an instance of TypesDiskRequest from a dict
types_disk_request_from_dict = TypesDiskRequest.from_dict(types_disk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


