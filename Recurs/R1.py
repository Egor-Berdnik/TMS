def recurs(src: dict, value: str, deep = 1, parent = None):
    if isinstance(src, dict):
         deep += 1
         for k, v in src.items():
            recurs(v, value, deep = deep, parent = k)
    elif isinstance(src, (list, set)):
        for item in src:
            recurs(item, value, deep = deep, parent = parent)
    elif isinstance(src, str):
        if src == value:
            print(f"Значение {value} найдено на глубине {deep}, parent = {parent}")
            return src

source_dict = {
    "key1": {
        "key2": {
            "key3": [
                "John",
                {
                    "key4": "Bob",
                    "key5": "Alex",
                    "key6": {
                        "key7": [
                            {
                                "key7": "Jessica",
                                "key8": {
                                    "key9": [
                                        "Alex"
                                    ]
                                }
                            }
                        ]
                    }
                }
            ]
        }
    },
    "key4": "Kate"
}

recurs(source_dict, "Bob")