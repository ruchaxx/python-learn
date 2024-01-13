
## Introduction

This chart bootstraps keycloak deployment on a [Kubernetes](http://kubernetes.io) cluster using the [Helm](https://helm.sh) package manager.

## Prerequisites
- Kubernetes 1.27
- [Helm](https://helm.sh/docs/intro/install/) 3.11.2
- [Kubectl](https://kubernetes.io/docs/tasks/tools/) v1.28.3

## Installation

You can get the chart version by searching package 'keycloak' on https://github.com/orgs/BentlyNevada-bh/packages

To install a chart, use the helm install command and specify the chart name and any required values:

```console
helm registry login ghcr.io/bentlynevada-bh/ --username username --password gh_token
helm pull oci://ghcr.io/bentlynevada-bh/keycloak --version chart_version --untar
RELEASE_NAME="my-release"
helm install "$RELEASE_NAME" "keycloak" --values keycloak/values.yaml
```

You can also download the chart using this workflow - https://github.com/BentlyNevada-bh/helm-charts/actions/workflows/helm-chart-download.yml

## Parameters

### Repository and Image Details

| Name                  | Description                                             | Value                       |
| --------------------- | ------------------------------------------------------- | --------------------------- |
| `repository`          | Name of the repository from which image will be pulled. | `ghcr.io/bentlynevada-bh`   |
| `image.name`          | Image name                                              | `quay.io/keycloak/keycloak` |
| `image.pullPolicy`    | Specify a imagePullPolicy                               | `Always`                    |
| `image.tag`           | Image tag                                               | `22.0.5`                    |
| `postgres.image.name` |                                                         | `postgres`                  |
| `postgres.image.tag`  |                                                         | `14.10`                     |
| `theme.enabled`       |                                                         | `true`                      |
| `theme.image.name`    |                                                         | `bh-keycloak-theme`         |
| `theme.image.tag`     |                                                         | `94`                        |
| `logger.enabled`      |                                                         | `true`                      |
| `logger.image.name`   |                                                         | `bh-audit-logger`           |
| `logger.image.tag`    |                                                         | `v1.2.0.103`                |

### Image Pull Secrets

| Name                       | Description                                       | Value                |
| -------------------------- | ------------------------------------------------- | -------------------- |
| `imagePullSecrets[0].name` | Image pull secret name for pulling docker images. | `bn-image-pullcreds` |

### PostgreSQL

| Name                                    | Description                       | Value      |
| --------------------------------------- | --------------------------------- | ---------- |
| `postgresql.postgresqlDatabase`         |                                   | `keycloak` |
| `postgresql.postgresqlUsername`         | Username for PostgreSQL instance. | `""`       |
| `postgresql.postgresqlDatabaseHost`     |                                   | `""`       |
| `postgresql.postgresqlDatabasePort`     |                                   | `5432`     |
| `postgresql.additionalSSLConfiguration` |                                   | `""`       |

### Configuration

| Name                                                        | Description                                                                                                                  | Value            |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `enabled`                                                   | Flag to enable or disable the app/svc                                                                                        | `true`           |
| `replicaCount`                                              | Number of replicas to deploy                                                                                                 | `2`              |
| `nameOverride`                                              | String to partially override common.names.fullname                                                                           | `""`             |
| `podDisruptionBudget.enabled`                               | Deploy a [PodDisruptionBudget]                                                                                               | `false`          |
| `podDisruptionBudget.minAvailable`                          | Number of pods that are available after eviction as number or percentage (eg.: 50%)                                          | `1`              |
| `extraEnv`                                                  | Extra environment varaibles should be 'only' for testing purpose. Values will be populated using ArgoCD appliation manifest. | `""`             |
| `serviceAccount.create`                                     | Enable the creation of a ServiceAccount for pods                                                                             | `true`           |
| `serviceAccount.annotations`                                | Annotations to add to the service account                                                                                    | `{}`             |
| `serviceAccount.name`                                       | Name of the created ServiceAccount                                                                                           | `""`             |
| `securityContext.allowPrivilegeEscalation`                  | Set container's Security Context allowPrivilegeEscalation                                                                    | `false`          |
| `securityContext.runAsNonRoot`                              | Set container's Security Context runAsNonRoot                                                                                | `true`           |
| `securityContext.runAsUser`                                 | Set container's Security Context runAsUser                                                                                   | `10001`          |
| `securityContext.capabilities.drop`                         | Set container's Security Context capabilities                                                                                | `["ALL"]`        |
| `securityContext.seccompProfile.type`                       | The seccomp options to use by the containers in this pod                                                                     | `RuntimeDefault` |
| `resources.requests.memory`                                 | The resources memory requests for the container                                                                              | `1024Mi`         |
| `resources.requests.cpu`                                    | The resources cpu requests for the container                                                                                 | `500m`           |
| `resources.limits.memory`                                   | The resources memory limits for the container                                                                                | `1024Mi`         |
| `resources.limits.cpu`                                      | The resources cpu limits for the container                                                                                   | `2000m`          |
| `userName`                                                  |                                                                                                                              | `admin`          |
| `autoscaling.enabled`                                       | Enable Horizontal Pod Autoscaler ([HPA])                                                                                     | `true`           |
| `autoscaling.minReplicas`                                   | Minimum number of replicas [HPA]                                                                                             | `2`              |
| `autoscaling.maxReplicas`                                   | Maximum number of replicas [HPA]                                                                                             | `3`              |
| `autoscaling.metrics[0].resource.name`                      | Metrics resource name                                                                                                        | `memory`         |
| `autoscaling.metrics[0].resource.target.type`               | Metrics target type                                                                                                          | `Utilization`    |
| `autoscaling.metrics[0].resource.target.averageUtilization` | Average memory utilization percentage [HPA]                                                                                  | `80`             |
| `autoscaling.metrics[0].type`                               | Metrics type                                                                                                                 | `Resource`       |
| `autoscaling.metrics[1].resource.name`                      | Metrics resource name                                                                                                        | `cpu`            |
| `autoscaling.metrics[1].resource.target.averageUtilization` | Average cpu utilization percentage [HPA]                                                                                     | `80`             |
| `autoscaling.metrics[1].resource.target.type`               | Metrics target type                                                                                                          | `Utilization`    |
| `autoscaling.metrics[1].type`                               | Metrics type                                                                                                                 | `Resource`       |
| `autoscaling.behavior.scaleDown.stabilizationWindowSeconds` | Scale down stabilizationWindowSeconds                                                                                        | `300`            |
| `autoscaling.behavior.scaleDown.policies[0].type`           | Scale down policies type                                                                                                     | `Pods`           |
| `autoscaling.behavior.scaleDown.policies[0].value`          | Scale down policies value                                                                                                    | `1`              |
| `autoscaling.behavior.scaleDown.policies[0].periodSeconds`  | Scale down policies periodSeconds                                                                                            | `300`            |
| `adminHost`                                                 | KC_HOSTNAME_ADMIN_URL Set the base URL for accessing the administration console, including scheme, host, port and path       | `""`             |

### Ingress

| Name                       | Description                 | Value    |
| -------------------------- | --------------------------- | -------- |
| `ingress.enabled`          |                             | `true`   |
| `ingress.ingressClassName` |                             | `nginx`  |
| `ingress.path`             |                             | `/?(.*)` |
| `KcHealthEnabled`          | Enable Keyclaok Healthcheck | `true`   |

