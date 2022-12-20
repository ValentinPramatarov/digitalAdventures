def double_collection_max_str_len(collection):
    max_len = 0

    for lvl_1_element in collection:
        for el in lvl_1_element:
            if len(el) > max_len:
                max_len = len(el)

    return max_len
