import yaml


def get_config(full_path):
    with open(full_path, "r") as f:
        try:
            default_config = yaml.load(f, Loader=yaml.FullLoader)
        except yaml.YAMLError as exc:
            assert False, "default.yaml error: {}".format(exc)
    return default_config
