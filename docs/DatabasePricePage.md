# DatabasePricePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DatabasePrice]**](DatabasePrice.md) |  | [optional] 
**page** | [**Page**](Page.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.database_price_page import DatabasePricePage

# TODO update the JSON string below
json = "{}"
# create an instance of DatabasePricePage from a JSON string
database_price_page_instance = DatabasePricePage.from_json(json)
# print the JSON string representation of the object
print(DatabasePricePage.to_json())

# convert the object into a dict
database_price_page_dict = database_price_page_instance.to_dict()
# create an instance of DatabasePricePage from a dict
database_price_page_from_dict = DatabasePricePage.from_dict(database_price_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


