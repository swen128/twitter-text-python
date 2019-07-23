import yaml


def read_yaml(path) -> dict:
    with open(path) as f:
        return yaml.load(f)
