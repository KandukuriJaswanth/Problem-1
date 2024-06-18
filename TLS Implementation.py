from kubernetes import client, config

def main():
    # Load Kubernetes configuration (adjust as needed, e.g., for local testing or in-cluster configuration)
    config.load_kube_config()

    # Define Kubernetes API objects
    v1 = client.CoreV1Api()
    apps_v1 = client.AppsV1Api()

    # Define deployment object
    deployment = client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name="wisecow-deployment"),
        spec=client.V1DeploymentSpec(
            replicas=1,
            selector=client.V1LabelSelector(
                match_labels={"app": "wisecow"}
            ),
            template=client.V1PodTemplateSpec(
                metadata=client.V1ObjectMeta(labels={"app": "wisecow"}),
                spec=client.V1PodSpec(
                    containers=[
                        client.V1Container(
                            name="wisecow",
                            image="your-image:latest",
                            ports=[client.V1ContainerPort(container_port=5000)],
                            volume_mounts=[
                                client.V1VolumeMount(
                                    name="tls-certs",
                                    mount_path="/etc/ssl/certs",
                                    read_only=True
                                )
                            ]
                        )
                    ],
                    volumes=[
                        client.V1Volume(
                            name="tls-certs",
                            secret=client.V1SecretVolumeSource(secret_name="tls-secret")
                        )
                    ]
                )
            )
        )
    )

    # Create deployment
    apps_v1.create_namespaced_deployment(namespace="default", body=deployment)

if __name__ == "__main__":
    main()
