import sys
from kubernetes import client, config



config.load_kube_config()
api_instance = client.CoreV1Api()



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