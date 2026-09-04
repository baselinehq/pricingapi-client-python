# DiskPricePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DiskPrice]**](DiskPrice.md) |  | [optional] 
**page** | [**Page**](Page.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.disk_price_page import DiskPricePage

# TODO update the JSON string below
json = "{}"
# create an instance of DiskPricePage from a JSON string
disk_price_page_instance = DiskPricePage.from_json(json)
# print the JSON string representation of the object
print(DiskPricePage.to_json())

# convert the object into a dict
disk_price_page_dict = disk_price_page_instance.to_dict()
# create an instance of DiskPricePage from a dict
disk_price_page_from_dict = DiskPricePage.from_dict(disk_price_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


