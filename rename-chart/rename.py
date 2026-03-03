import subprocess
import os
import glob
import yaml




def pull_chart():

        login = subprocess.run(['helm', 'registry', 'login', 'ghcr.io', '--username', '', '--password', ''])

        pull = subprocess.run(['helm', 'pull', 'oci://ghcr.io/industrial-solutions/cordantassethealth', '--version', '25.1.1446'])

        untar = subprocess.run(['tar', '-xzf', 'cordantassethealth-25.1.1446.tgz'])

# with open('cordantassethealth/Chart.yaml', mode='r') as f:
#      data = yaml.safe_load(f)


# data['name'] = "cordantsuite"
# print(data['name'])

# with open('cordantassethealth/Chart.yaml', mode='w') as file:
#        file.write(yaml.dump(data))


# with open("cordantassethealth/values.yaml", mode='r') as f:
#        valuesfile = f.read()

# valuesfile = valuesfile.replace("cordantassethealth","cordantsuite")

# with open("cordantassethealth/values.yaml", mode='w') as file:
#        file.write(valuesfile)


def replace():

    for subdir, _, files in os.walk("cordantassethealth"):
        for filename in files:
            file_path = os.path.join(subdir, filename)
        # print("file_path ",file_path)
            with open(file_path, mode='r') as f:
                valuesfile = f.read()
            valuesfile = valuesfile.replace("cordantassethealth","cordantsuite")
            with open(file_path, mode='w') as file:
                file.write(valuesfile)


def helm_push():
    rename = subprocess.run(['mv','cordantassethealth','cordantsuite'])

    package = subprocess.run(['helm','package','cordantsuite'])

    helm_push = subprocess.run(['helm','push','cordantsuite-25.2.2446.tgz','oci://ghcr.io/industrial-solutions'])

