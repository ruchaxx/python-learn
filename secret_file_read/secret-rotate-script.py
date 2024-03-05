import sys
import yaml
import traceback
import os
from pathlib import Path

secret_files_path = []


def add_client_secrets(base_secrets: list, secrets_path: str, env_name):
    """ Checks the secrets for each client and adds new secret if new tenant is added or
        update the secret value if the secret value for any client changes in base secrets """
    try:
        with open(secrets_path, "r+") as secrets_file:
            secrets_file_data = list(yaml.safe_load_all(secrets_file))
            env_name = str(env_name).split("-secrets")[0]
            for ind_, base_secret_name in enumerate(base_secrets):
                if base_secret_name:
                    svc_names = list(base_secret_name.get('data', {}).keys())
                    base_secret_name["metadata"]["namespace"] = env_name
                    for _svc_name in secrets_file_data:
                        if _svc_name:
                            secret_file_svc_name = _svc_name.get('metadata', {}).get('name', None)
                            if secret_file_svc_name:
                                temp_name = "APP_" + secret_file_svc_name.replace("-", "_").replace("_secret",
                                                                                                    "").upper()
                                if temp_name in svc_names:
                                    _svc_name["data"][f"CLIENT_SECRET_{chr((ind_ + 1) + 64)}"] = base_secret_name.get(
                                        'data', {}).get(temp_name)
                                    _svc_name["metadata"]["namespace"] = env_name
                                elif secret_file_svc_name == base_secret_name.get("metadata", {}).get("name", ""):
                                    _svc_name["data"] = base_secret_name.get('data', {})
            return secrets_file_data
    except Exception as e:
        print(traceback.format_exc())


def check_secrets_file(path: str):
    try:
        for root_, dirs_, files_ in os.walk(top=path):
            for _file in files_:
                if "secret" in str(_file):
                    secret_files_path.append({_file: f"{root_}/{str(_file)}"})
            for dir_ in dirs_:
                if dir_:
                    check_secrets_file(path=dir_)
    except Exception as e:
        print(traceback.format_exc())


def get_svc_and_index(s_name):
    svc_name_index = {}
    for index_, svc in enumerate(s_name):
        if svc:
            svc_name_index[f"{svc.get('metadata').get('name')}"] = index_
    return svc_name_index


def write_output(metadata: dict, res_data: list, base_sec: list, path_to_write: str, env: str, keycloak_password: dict,
                 base_password: list):
    try:
        sec_names = list(metadata.keys())
        pass_names = list(keycloak_password.keys())
        res_data_secret_names = list(map(lambda reg: reg.get('metadata', {}).get('name') if reg else "", res_data))
        for key in sec_names:
            if key not in res_data_secret_names:
                base_sec[metadata.get(key, {})]["metadata"]["namespace"] = str(env).split("-secrets")[0]
                res_data.append(base_sec[metadata[key]])

        for password in pass_names:
            if password not in res_data_secret_names:
                base_password[keycloak_password.get(password, {})]["metadata"]["namespace"] = \
                    str(env).split("-secrets")[0]
                res_data.append(base_password[keycloak_password[password]])
        with open(path_to_write, "w") as f:
            yaml.dump_all(res_data, f)
    except Exception as e:
        print(traceback.format_exc())


if __name__ == "__main__":
    base_secrets_file_path = sys.argv[1]
    target_dir_to_add_secrets = sys.argv[2]
    no_of_tenant = sys.argv[3]
    if Path(target_dir_to_add_secrets).is_file():
        _file = target_dir_to_add_secrets.split("/")[-1]
        secret_files_path.append({_file: f"{target_dir_to_add_secrets}"})
    else:
        # Get the secret files path from provided env
        check_secrets_file(path=target_dir_to_add_secrets)

    with open(base_secrets_file_path, "r") as file:
        base_secrets_dict_ = list(yaml.safe_load_all(file))

        base_secrets_dict = [x for x in base_secrets_dict_ if
                             "keycloak-client-secrets-tenant" in x.get('metadata', {}).get('name')]
        keycloak_passwords = [x for x in base_secrets_dict_ if
                              "keycloak-realm-passwords-tenant" in x.get('metadata', {}).get('name')]

        # Convert the base secret list into dict with its name as key index as value eg: {tenant_a: 0}
        secret_metadata = get_svc_and_index(base_secrets_dict[:int(no_of_tenant)])
        keycloak_passwords_metadata = get_svc_and_index(keycloak_passwords[:int(no_of_tenant)])

        # Loop through each secret file from the secret_files_path
        for secret_file in secret_files_path:
            # file name and the path for further use like creating namespace from file name
            env_, path_ = list(secret_file.items())[0]

            print(f" INFO: Current secret file name {env_} and path {path_}")

            response = add_client_secrets(base_secrets=base_secrets_dict[:int(no_of_tenant)],
                                          secrets_path=path_, env_name=env_)

            # Write the changes to same path
            write_output(base_password=keycloak_passwords, keycloak_password=keycloak_passwords_metadata,
                         metadata=secret_metadata, res_data=response, base_sec=base_secrets_dict, path_to_write=path_,
                         env=env_, )
            print(f" MESSAGE: ✔ Changes are done in {env_} inside {path_}")