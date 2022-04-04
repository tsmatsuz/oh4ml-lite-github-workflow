from azureml.core import ScriptRunConfig, Environment
from azureml.core.runconfig import DockerConfiguration

def main(workspace):
    myenv = Environment.from_conda_specification(name='arima-env', file_path='code/train/environment.yml')
    docker_config = DockerConfiguration(use_docker=True)

    src = ScriptRunConfig(
        source_directory='code/train',
        script='train.py',
        compute_target='demo-cpucluster1',
        environment=myenv,
        docker_runtime_config=docker_config)

    return src
