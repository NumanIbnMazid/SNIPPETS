from collections.abc import MutableMapping
from contextlib import suppress


def purify_data(data, keys_to_remove=None):
    """
    Removes a list of keys from a dictionary or list of dictionaries
    :param data: dictionary or list of dictionaries
    :param keys_to_remove: list of keys to remove
    :return: purified data
    """

    if keys_to_remove is None:
        keys_to_remove = ["timestamp", "created_at", "updated_at"]

    def remove_keys(data_item):
        for key in keys_to_remove:
            with suppress(KeyError):
                del data_item[key]
        for value in data_item.values():
            if isinstance(value, MutableMapping):
                purify_data(value, keys_to_remove)

    if isinstance(data, list):
        for item in data:
            remove_keys(item)
    else:
        remove_keys(data)

    return data


# *** Test ***
data = [
    {
        "model": "B",
        "pk": 2,
        "fields": {
            "created_at": "2022-08-02T17:52:53.503Z",
            "updated_at": "2022-08-02T17:52:53.503Z",
            "data_source": 3
        }
    },
    {
        "model": "A",
        "pk": 1,
        "fields": {
            "created_at": "2022-08-02T17:52:53.493Z",
            "updated_at": "2022-08-02T17:52:53.494Z",
            "data_source": 2
        }
    }
]

result = purify_data(data)

print(result)
# [{'model': 'B', 'pk': 2, 'fields': {'data_source': 3}}, {'model': 'A', 'pk': 1, 'fields': {'data_source': 2}}]
