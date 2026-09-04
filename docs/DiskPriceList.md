# DiskPriceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**providers** | [**List[DiskPrice]**](DiskPrice.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.disk_price_list import DiskPriceList

# TODO update the JSON string below
json = "{}"
# create an instance of DiskPriceList from a JSON string
disk_price_list_instance = DiskPriceList.from_json(json)
# print the JSON string representation of the object
print(DiskPriceList.to_json())

# convert the object into a dict
disk_price_list_dict = disk_price_list_instance.to_dict()
# create an instance of DiskPriceList from a dict
disk_price_list_from_dict = DiskPriceList.from_dict(disk_price_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


