def recurs(src: dict, value: str, deep = 1, parent = None):
    for k, v in src.items():
        if isinstance(v, dict):
            recurs(v, value)
            deep += 1
        elif isinstance(v, list):
            recurs(v, value)
            deep += 1
        else:
            if v == value:
                print(f"Значение {value} найдено на глубине {deep}")
                return


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

print(recurs(source_dict, Bob))