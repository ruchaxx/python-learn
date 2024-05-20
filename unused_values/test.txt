{{/*
Expand the name of the chart.
*/}}
{{- define "accs-fdn-svc.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "accs-fdn-svc.fullname" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}



{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "accs-fdn-svc.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "accs-fdn-svc.labels" -}}
helm.sh/chart: {{ include "accs-fdn-svc.chart" . }}
{{ include "accs-fdn-svc.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "accs-fdn-svc.selectorLabels" -}}
app.kubernetes.io/name: {{ include "accs-fdn-svc.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Create the name of the service account to use
*/}}
{{- define "accs-fdn-svc.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{- default (include "accs-fdn-svc.fullname" .) .Values.serviceAccount.name }}
{{- else }}
{{- default "default" .Values.serviceAccount.name }}
{{- end }}
{{- end }}

{{/*
Create the service DNS name.
*/}}
{{- define "accs-fdn-svc.serviceDnsName" -}}
{{ .Release.Namespace }}.svc.cluster.local
{{- end }}