# AffectedResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from pricing_api_client.models.affected_resource import AffectedResource

# TODO update the JSON string below
json = "{}"
# create an instance of AffectedResource from a JSON string
affected_resource_instance = AffectedResource.from_json(json)
# print the JSON string representation of the object
print(AffectedResource.to_json())

# convert the object into a dict
affected_resource_dict = affected_resource_instance.to_dict()
# create an instance of AffectedResource from a dict
affected_resource_from_dict = AffectedResource.from_dict(affected_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


