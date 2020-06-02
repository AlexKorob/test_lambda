import re


def read_env():
    with open(".env", "r") as file:
        data = file.read()
        new_params_string = ""
        environment_variables = re.findall(r"(\w+=\w+.+)", data)
        for line in environment_variables:
            key, value = line.split("=")
            new_key = ""
            for num, key_part in enumerate(key.split("_")):
                key_part = key_part.lower()
                if num != 0:
                    key_part = key_part.title()
                new_key += key_part
            new_params_string += f"ParameterKey={new_key},ParameterValue={value} "
        print(new_params_string.strip())


read_env()
