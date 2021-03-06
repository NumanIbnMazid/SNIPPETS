
data = {
    "key1": "value1",
    "key2": "value2",
    "key3": {
        "nestedKey1": "nestedValue1",
        "nestedKey2": "nestedValue2",
        "nestedKey3": [
            {
                "insideKey1": "insideValue1",
                "insideKey2": "insideValue2",
            }
        ],
    }
}

nested_list = [1, 2, 3, ["X", "Y", ["6", {"Key1": "value1", "key2": "value2"}, 2, 3, 4]]]

key_pos = {"": -1}

def iterate_all(iterable, returned="key", pre_tab=0, pre_k=""):
    """Returns an iterator that returns all keys or values
       of a (nested) iterable.
       
       Arguments:
           - iterable: <list> or <dictionary>
           - returned: <string> "key" or "value"
           
       Returns:
           - <iterator>
    """
  
    if isinstance(iterable, dict):
        tab_num = key_pos[pre_k] + 1
        for key, value in iterable.items():
            key_pos[key] = tab_num
            if returned == "key":
                tab = "\t" * tab_num
                yield f"{tab}{key}\n"
            elif returned == "value":
                if not (isinstance(value, dict) or isinstance(value, list)):
                    yield value
            else:
                raise ValueError("'returned' keyword only accepts 'key' or 'value'.")
            for ret in iterate_all(value, returned=returned, pre_tab=tab_num, pre_k=key):
                yield ret
    elif isinstance(iterable, list):
        tab_num = key_pos[pre_k] + 1
        for el in iterable:
            for ret in iterate_all(el, returned=returned, pre_tab=tab_num, pre_k=pre_k):
                yield ret
    

keys = []
# keys = set()
for key in iterate_all(iterable=data, returned="key"):
    keys.append(key)
    # keys.add(key)

# result = ''.join(list(keys))
result = ''.join(keys)

# print(len(keys))
with open('get_keys_vals_dict_test.txt', 'w') as outfile:
    outfile.write(str(result))
