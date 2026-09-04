# DatabasePricesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[DatabasePrice]**](DatabasePrice.md) |  | 

## Example

```python
from pricing_api_client.models.database_prices_request import DatabasePricesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DatabasePricesRequest from a JSON string
database_prices_request_instance = DatabasePricesRequest.from_json(json)
# print the JSON string representation of the object
print(DatabasePricesRequest.to_json())

# convert the object into a dict
database_prices_request_dict = database_prices_request_instance.to_dict()
# create an instance of DatabasePricesRequest from a dict
database_prices_request_from_dict = DatabasePricesRequest.from_dict(database_prices_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


