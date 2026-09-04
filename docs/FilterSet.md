# FilterSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | **List[str]** |  | [optional] 
**kind** | **str** |  | [optional] 

## Example

```python
from pricing_api_client.models.filter_set import FilterSet

# TODO update the JSON string below
json = "{}"
# create an instance of FilterSet from a JSON string
filter_set_instance = FilterSet.from_json(json)
# print the JSON string representation of the object
print(FilterSet.to_json())

# convert the object into a dict
filter_set_dict = filter_set_instance.to_dict()
# create an instance of FilterSet from a dict
filter_set_from_dict = FilterSet.from_dict(filter_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


