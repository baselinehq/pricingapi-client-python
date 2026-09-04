# DatabasePriceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**providers** | [**List[DatabasePrice]**](DatabasePrice.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.database_price_list import DatabasePriceList

# TODO update the JSON string below
json = "{}"
# create an instance of DatabasePriceList from a JSON string
database_price_list_instance = DatabasePriceList.from_json(json)
# print the JSON string representation of the object
print(DatabasePriceList.to_json())

# convert the object into a dict
database_price_list_dict = database_price_list_instance.to_dict()
# create an instance of DatabasePriceList from a dict
database_price_list_from_dict = DatabasePriceList.from_dict(database_price_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


