import sys
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

def send_mail(podlist):
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
      body = service_name + ' logs are attached'
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

# Get the list of pods for the specified service
pods = api_instance.list_namespaced_pod(namespace)

podlist = []
#print("\npods ",pods)
# Print the pod names

for pod in pods.items:
   print(pod.metadata.name)
   podlist.append(pod.metadata.name)
   #print("in for")

print("\n pod list ",podlist)
# Retrieve pod logs
for pod in podlist:
   pod_logs = api_instance.read_namespaced_pod_log(name=pod, namespace=namespace)
   with open(pod+'.txt',mode='w') as f:
         f.write(pod_logs)
   with open(pod+'.txt',mode='r') as f:
       lines = f.read()
   #print("\n pod of {} lines {}".format(pod,lines))
   if lines.find('ERROR') != -1:
       print("in if")
       find_error = True
       break
   else:
       print("in else")

if find_error == True:
    send_mail(podlist)
    print("\nEmail sent sussesfully")