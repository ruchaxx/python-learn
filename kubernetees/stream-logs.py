import sys
import os
from kubernetes import client, config
import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


config.load_kube_config()
api_instance = client.CoreV1Api()

find_error = False
pod_state = ''

def send_mail(podlist,pod_state):
      smtp_obj = smtplib.SMTP('smtp-mail.outlook.com',587)
      #smtp_obj = smtplib.SMTP('smtp.gmail.com',587)
      smtp_obj.ehlo()
      smtp_obj.starttls()
      email = 'puranik_rucha@outlook.com'
      password = getpass.getpass('Enter Password : ')
      smtp_obj.login(email,password)
      msg = MIMEMultipart()
      msg['From'] = email
      msg['To'] = email
      msg['Subject'] = service_name + ' Logs'
      body = service_name + ' pod state is ' + pod_state
      msg.attach(MIMEText(body, 'plain'))

      ## ATTACHMENT PART OF THE CODE IS HERE
      for pod in podlist:
         attachment = open(pod+'.txt', 'rb')
         part = MIMEBase('application', "octet-stream")
         part.set_payload((attachment).read())
         encoders.encode_base64(part)
         part.add_header('Content-Disposition', "attachment; filename= %s" % pod+'.txt')
         msg.attach(part)
      smtp_obj.send_message(msg)
      smtp_obj.quit()



# Specify namespace and pod name
namespace = "k-test"
service_name = sys.argv[1]

 # Get the service by name
# service = api_instance.read_namespaced_service(name=service_name, namespace=namespace)
# print("\nservice ",service.spec.selector)

# selector = ",".join([f"{key}={value}" for key, value in service.spec.selector.items()])
# print("\nselector ",selector)

############################

# select_list = []
# for key, value in service.spec.selector.items():
#     select_list.append(key+'='+value)

# print("select list ",select_list)

# select = ''
# select = ','.join(select_list)

# print("select ",select)
# Get the list of pods for the specified service
pods = api_instance.list_namespaced_pod(namespace,label_selector='app.kubernetes.io/name='+service_name)

podlist = []
#print("\npods ",pods)
# Print the pod names

for pod in pods.items:
   print(pod.metadata.name)
   podlist.append(pod.metadata.name)
   print("\nstatus ",pod.status.phase)
   #print("in for")

print("\n pod list ",podlist)
# Retrieve pod logs


def write_file(podlist):
   for pod in podlist:
        pod_logs = api_instance.read_namespaced_pod_log(name=pod, namespace=namespace,follow=True,_preload_content=False)
        with open(pod+'.txt',mode='w') as f:
            for line in pod_logs:
                f.write(line.decode('utf-8'))

def delete_file(podlist):
    for pod in podlist:
        if os.path.exists(pod+'.txt'):
            os.remove(pod+'.txt')
        else:
            print("The file does not exist")

for pod in podlist:
   pod_logs = api_instance.read_namespaced_pod_log(name=pod, namespace=namespace,follow=True,_preload_content=False)
   for line in pod_logs:
       for pod_status in pods.items:
        if (line.decode('utf-8').find('Use') != -1) and (pod_status.status.phase == 'Running'):
            print("in if")
            find_error = True
            pod_state = pod_status.status.phase
            break
        elif (line.decode('utf-8').find('Use') != -1) and ((pod_status.status.phase == 'CrashLoopBackOff') or (pod_status.status.phase == 'Error')):
            print("in elif")
            find_error = True
            pod_state = pod_status.status.phase
            break
        else:
            print("in else")
   pod_logs.close()

if find_error == True:
    write_file(podlist)
    send_mail(podlist,pod_state )
    delete_file(podlist)
    print("\nEmail sent sussesfully")