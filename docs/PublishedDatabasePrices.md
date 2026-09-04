# PublishedDatabasePrices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DatabasePrice]**](DatabasePrice.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.published_database_prices import PublishedDatabasePrices

# TODO update the JSON string below
json = "{}"
# create an instance of PublishedDatabasePrices from a JSON string
published_database_prices_instance = PublishedDatabasePrices.from_json(json)
# print the JSON string representation of the object
print(PublishedDatabasePrices.to_json())

# convert the object into a dict
published_database_prices_dict = published_database_prices_instance.to_dict()
# create an instance of PublishedDatabasePrices from a dict
published_database_prices_from_dict = PublishedDatabasePrices.from_dict(published_database_prices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


