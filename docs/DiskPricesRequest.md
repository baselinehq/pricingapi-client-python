# DiskPricesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[DiskPrice]**](DiskPrice.md) |  | 

## Example

```python
from pricing_api_client.models.disk_prices_request import DiskPricesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DiskPricesRequest from a JSON string
disk_prices_request_instance = DiskPricesRequest.from_json(json)
# print the JSON string representation of the object
print(DiskPricesRequest.to_json())

# convert the object into a dict
disk_prices_request_dict = disk_prices_request_instance.to_dict()
# create an instance of DiskPricesRequest from a dict
disk_prices_request_from_dict = DiskPricesRequest.from_dict(disk_prices_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


