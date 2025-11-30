import csv
import pandas as pd
from kubernetes import client, config
def load_k8s_config():
    try:
        config.load_kube_config()
    except Exception as e:
        print(f"Error loading Kubernetes config: {e}")
        exit(1)
def fetch_pod_data():
    v1 = client.CoreV1Api()
    pod_list = v1.list_pod_for_all_namespaces(watch=False)
    pod_data = []
    for pod in pod_list.items:
        pod_data.append({
            "namespace": pod.metadata.namespace,
            "name": pod.metadata.name,
            "status": pod.status.phase,
            "created_at": pod.metadata.creation_timestamp,
            "node_name": pod.spec.node_name,
        })
    return pod_data
def write_data_to_csv(data, filename):
    headers = ["namespace", "name", "status", "created_at", "node_name"]
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
    print(f"Data written to {filename}")
def read_data_from_csv(filename):
    df = pd.read_csv(filename)
    return df
def main():
    load_k8s_config()
    pod_data = fetch_pod_data()
    csv_filename = 'k8s_pod_data.csv'
    write_data_to_csv(pod_data, csv_filename)
    df = read_data_from_csv(csv_filename)
    print("\nData extracted from the CSV file:")
    print(df)
if __name__ == "__main__":
    main()