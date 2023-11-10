#プロパティ化
#これを使う前にファイルの中でタブ文字を使っているのを空白に変換する必要がある
import yaml

def yaml_to_properties(yaml_data):
    properties = []

    def traverse(data, path=[]):
        if isinstance(data, dict):
            for key, value in data.items():
                traverse(value, path + [key])
        elif isinstance(data, list):
            for index, value in enumerate(data):
                traverse(value, path + [str(index)])
        else:
            properties.append(".".join(path) + "=" + str(data).replace("\n"," "))

    traverse(yaml_data)
    return "\n".join(properties)

# YAMLファイルの読み込み
diff_all_foldernames = glob.glob("from_github_file_clear/"+"*")
#diff_all_foldernames = ["from_github_history_allcode_clear\\filenum_1_0_0\\2021-06-08T15-40-34Z_config.yml"]
print("yaml to prpperties")
for file in diff_all_foldernames:
    
    try:
        with open(file, "r") as yaml_file:
            yaml_data = yaml.safe_load(yaml_file)
    except:
        print("error")
        continue
    # YAMLデータをプロパティファイル形式に変換
    properties_content = yaml_to_properties(yaml_data)

    # プロパティファイルに保存
    save_file_name = "from_github_file_clear_proper/" + str(file.split("\\")[-1].split(".")[0]) + ".properties"
    with open(save_file_name, "w") as properties_file:
        properties_file.write(properties_content)
    print("ファイルに保存されました: " + str(save_file_name))
