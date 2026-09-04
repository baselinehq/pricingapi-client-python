# RegisteredDiskPrices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[DiskPrice]**](DiskPrice.md) |  | [optional] 
**status** | [**RegistrationStatus**](RegistrationStatus.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.registered_disk_prices import RegisteredDiskPrices

# TODO update the JSON string below
json = "{}"
# create an instance of RegisteredDiskPrices from a JSON string
registered_disk_prices_instance = RegisteredDiskPrices.from_json(json)
# print the JSON string representation of the object
print(RegisteredDiskPrices.to_json())

# convert the object into a dict
registered_disk_prices_dict = registered_disk_prices_instance.to_dict()
# create an instance of RegisteredDiskPrices from a dict
registered_disk_prices_from_dict = RegisteredDiskPrices.from_dict(registered_disk_prices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


