import re
import yaml

def properties_to_yaml(properties_data):
    yaml_data = {}

    for line in properties_data.split("\n"):
        if line.strip() == "":
            continue

        key, value = line.split("=")
        keys = key.split(".")
        current_dict = yaml_data

        for k in keys[:-1]:
            if k.isdigit():
                k = int(k)
            if k not in current_dict:
                current_dict[k] = {}
            current_dict = current_dict[k]

        if keys[-1].isdigit():
            keys[-1] = int(keys[-1])

        # Check if the last key is already present as a list
        if keys[-1] in current_dict:
            if not isinstance(current_dict[keys[-1]], list):
                current_dict[keys[-1]] = [current_dict[keys[-1]]]
            current_dict[keys[-1]].append(parse_value(value.strip()))
        else:
            current_dict[keys[-1]] = parse_value(value.strip())

    return yaml_data

def parse_value(value):
    # Try to convert value to int or float if possible
    if re.match(r"^-?\d+$", value):
        return int(value)
    elif re.match(r"^-?\d+\.\d+$", value):
        return float(value)
    else:
        return value

# プロパティファイルの読み込み
properties_file_path = "from_github_file_clear_proper/example.properties"
with open(properties_file_path, "r") as properties_file:
    properties_data = properties_file.read()

# プロパティデータをYAMLに変換
yaml_data = properties_to_yaml(properties_data)

# YAMLデータをファイルに保存
yaml_save_file_path = "from_github_file_clear_proper/example.yaml"
with open(yaml_save_file_path, "w") as yaml_save_file:
    yaml.dump(yaml_data, yaml_save_file, default_flow_style=False)

print("YAMLファイルに保存されました:", yaml_save_file_path)
