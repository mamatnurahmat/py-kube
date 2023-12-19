import yaml
import os

# def get_images_from_yaml(yaml_file):
#     with open(yaml_file, 'r') as file:
#         deployment_data = yaml.safe_load(file)

#     containers = deployment_data['spec']['template']['spec']['containers']

#     image_names = [container['image'] for container in containers]

#     return image_names

def get_images_from_yaml(yaml_file):
    with open(yaml_file, 'r') as file:
        deployment_data = yaml.safe_load(file)
        print(deployment_data)  # Cetak isi YAML untuk memahami strukturnya

def process_yaml_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".yaml"):
            yaml_file_path = os.path.join(directory, filename)
            image_names = get_images_from_yaml(yaml_file_path)

            print(f"Images in {filename}:")
            for image_name in image_names:
                print(f"- {image_name}")
            print()

def main():
    yaml_directory = "."  # Ganti dengan direktori tempat Anda menyimpan file YAML

    process_yaml_files_in_directory(yaml_directory)

if __name__ == "__main__":
    main()
