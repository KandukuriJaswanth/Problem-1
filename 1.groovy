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
                        'image': '<your-image>',  # Replace with your Docker image
                        'ports': [
                            {
                                'containerPort': 5000
                            }
                        ],
                        'env': [
                            {
                                'name': 'FLASK_APP',
                                'value': 'wisecow.py'  # Adjust as needed
                            }
                        ]
                    }
                ]
            }
        }
    }
}

# Convert Python dictionary to YAML (optional, for writing to a file)
import yaml

deployment_yaml = yaml.dump(deployment_spec, default_flow_style=False)
print(deployment_yaml)
