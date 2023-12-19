from kubernetes import client, config
import yaml

# def download_deployments(namespace):
#     config.load_kube_config(config_file="config.yaml")  # Menggunakan konfigurasi dari config.yaml
#     api_instance = client.AppsV1Api()

#     try:
#         deployments = api_instance.list_namespaced_deployment(namespace).items

#         for deployment in deployments:
#             deployment_name = deployment.metadata.name
#             deployment_yaml = api_instance.read_namespaced_deployment(deployment_name, namespace).to_str()
#             file_name = f"deploy_{deployment_name}.yaml"

#             with open(file_name, "w") as yaml_file:
#                 yaml_file.write(deployment_yaml)

#             print(f"Deployment {deployment_name} configuration saved to {file_name}")
#     except Exception as e:
#         print(f"Error: {e}")

def download_deployments(namespace):
    config.load_kube_config(config_file="config.yaml")  # Menggunakan konfigurasi dari config.yaml
    api_instance = client.AppsV1Api()

    try:
        deployments = api_instance.list_namespaced_deployment(namespace).items

        for deployment in deployments:
            deployment_name = deployment.metadata.name
            deployment_data = api_instance.read_namespaced_deployment(deployment_name, namespace).to_dict()
            file_name = f"deploy_{deployment_name}.yaml"

            with open(file_name, "w") as yaml_file:
                yaml.dump(deployment_data, yaml_file, default_flow_style=False)

            print(f"Deployment {deployment_name} configuration saved to {file_name}")
    except Exception as e:
        print(f"Error: {e}")


def main():
    namespace = "develop-qoin"
    download_deployments(namespace)

if __name__ == "__main__":
    main()

