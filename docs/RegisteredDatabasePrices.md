# RegisteredDatabasePrices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[DatabasePrice]**](DatabasePrice.md) |  | [optional] 
**status** | [**RegistrationStatus**](RegistrationStatus.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.registered_database_prices import RegisteredDatabasePrices

# TODO update the JSON string below
json = "{}"
# create an instance of RegisteredDatabasePrices from a JSON string
registered_database_prices_instance = RegisteredDatabasePrices.from_json(json)
# print the JSON string representation of the object
print(RegisteredDatabasePrices.to_json())

# convert the object into a dict
registered_database_prices_dict = registered_database_prices_instance.to_dict()
# create an instance of RegisteredDatabasePrices from a dict
registered_database_prices_from_dict = RegisteredDatabasePrices.from_dict(registered_database_prices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


