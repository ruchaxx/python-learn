import subprocess
import os
import glob
import yaml


login = subprocess.run(['helm', 'registry', 'login', 'ghcr.io', '--username', '', '--password', ''])

chart_list = ['25.1.1446','25.2.2079','25.2.2028','25.2.1788','25.2.1786']


def pull_chart():

        for chart in chart_list:
            pull = subprocess.run(['helm', 'pull', 'oci://ghcr.io/industrial-solutions/cordantassethealth', '--version', chart])



def helm_push(chart):
    rename = subprocess.run(['mv','cordantassethealth','cordantsuite'])

    package = subprocess.run(['helm','package','cordantsuite'])

    helm_push = subprocess.run(['helm','push','cordantsuite-'+chart+'.tgz','oci://ghcr.io/industrial-solutions'])

    delete_cordantassethealth = subprocess.run(['rm','-rf','cordantassethealth'])

    delete_cordantsuite = subprocess.run(['rm','-rf','cordantsuite'])


def replace():

    for chart in chart_list:
        untar = subprocess.run(['tar', '-xzf', 'cordantassethealth-'+chart+'.tgz'])

        for subdir, _, files in os.walk("cordantassethealth"):
            for filename in files:
                file_path = os.path.join(subdir, filename)
            # print("file_path ",file_path)
                try:
                    with open(file_path, mode='r', encoding='utf-8') as f:
                        valuesfile = f.read()
                    valuesfile = valuesfile.replace("cordantassethealth","cordantsuite")
                except Exception as e:
                    print("not found ",e)
                with open(file_path, mode='w', encoding='utf-8') as file:
                    file.write(valuesfile)

        helm_push(chart)



pull_chart()
replace()




