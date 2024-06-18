import yaml

def generate_deployment_yaml(image_name, flask_app_file):
    # Define the deployment specification as a Python dictionary
    deployment_spec = {
        'apiVersion': 'apps/v1',
        'kind': 'Deployment',
        'metadata': {
            'name': 'wisecow-deployment'
        },
        'spec': {
            'replicas': 3,
            'selector': {
                'matchLabels': {
                    'app': 'wisecow'
                }
            },
            'template': {
                'metadata': {
                    'labels': {
                        'app': 'wisecow'
                    }
                },
                'spec': {
                    'containers': [
                        {
                            'name': 'wisecow',
                            'image': image_name,  # Pass your Docker image here
                            'ports': [
                                {
                                    'containerPort': 5000
                                }
                            ],
                            'env': [
                                {
                                    'name': 'FLASK_APP',
                                    'value': flask_app_file  # Pass your entry point script here
                                }
                            ]
                        }
                    ]
                }
            }
        }
    }

    # Convert Python dictionary to YAML
    deployment_yaml = yaml.dump(deployment_spec, default_flow_style=False)
    return deployment_yaml

# Example usage:
if __name__ == "__main__":
    # Replace with your actual Docker image and entry point script
    docker_image = '"D:\B.TECH\Mini  Project\QA\problem1\download.jpeg'
    flask_app = 'wisecow.py'

    generated_yaml = generate_deployment_yaml(docker_image, flask_app)
    print(generated_yaml)
