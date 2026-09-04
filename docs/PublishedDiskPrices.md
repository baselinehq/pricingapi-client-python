# PublishedDiskPrices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DiskPrice]**](DiskPrice.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.published_disk_prices import PublishedDiskPrices

# TODO update the JSON string below
json = "{}"
# create an instance of PublishedDiskPrices from a JSON string
published_disk_prices_instance = PublishedDiskPrices.from_json(json)
# print the JSON string representation of the object
print(PublishedDiskPrices.to_json())

# convert the object into a dict
published_disk_prices_dict = published_disk_prices_instance.to_dict()
# create an instance of PublishedDiskPrices from a dict
published_disk_prices_from_dict = PublishedDiskPrices.from_dict(published_disk_prices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


