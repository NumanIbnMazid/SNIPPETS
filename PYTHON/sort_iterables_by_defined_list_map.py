print(
    """
**************** Sort Dictionaries in List by Defined List Map ****************
"""
)


my_dict_list = [
    {
        "type": "Apple",
        "Extra": {"A": "B", "C": "D"},
        "ExtraTwo": "Example"
    },
    {
        "type": "Orange",
        "Extra": {"A": "B", "C": "D"},
        "ExtraTwo": "Example"
    },
    {
        "type": "Z",
        "Extra": {"A": "B", "C": "D"},
        "ExtraTwo": "Example"
    },
    {
        "type": "Lichi",
        "Extra": {"A": "B", "C": "D"},
        "ExtraTwo": "Example"
    },
    {
        "type": "Y",
        "Extra": {"A": "B", "C": "D"},
        "ExtraTwo": "Example"
    },
    {
        "type": "X",
        "Extra": {"A": "B", "C": "D"},
        "ExtraTwo": "Example"
    },
    {
        "type": "Banana",
        "Extra": {"A": "B", "C": "D"},
        "ExtraTwo": "Example"
    }
]

sort_map_list = ["Z", "Apple", "X", "Banana", "Lichi"]

tracker_dict = {}
refined_list = []

i = 0

for key in my_dict_list:
    tracker_dict[key["type"]] = i
    i += 1

for key in sort_map_list:
    refined_list.append(my_dict_list[tracker_dict[key]])


for key in my_dict_list:
    if key not in refined_list:
        refined_list.append(key)


print(
    "\n 1. [Sort Dictionaries in List by Defined List Map] => Refined List: \n\n",
    refined_list, "\n"
)

for item in refined_list:
    print(item)


print(
    """
**************** Sort Items in Dictionary by Defined List Map ****************
"""
)

sort_map_list = ["Z", "Apple", "X", "Banana", "Lichi"]


my_dict = {
    "X": 100,
    "Banana": 100,
    "Orange": 50,
    "Y": 50,
    "Apple": 150,
    "Z": 150,
    "Lichi": 200
}

refined_dictionary = {}

for key in sort_map_list:
    if key in my_dict:
        refined_dictionary[key] = my_dict[key]

for key, value in my_dict.items():
    if key not in refined_dictionary:
        refined_dictionary[key] = value

print(
    "\n 2. [Sort Items in Dictionary by Defined List Map] => Refined Dictionary: \n\n",
    refined_dictionary, "\n"
)

for item in refined_dictionary:
    print(item)
