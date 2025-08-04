# API Monitoramento com Kubernetes (Kind)

Este projeto contém os manifests YAML para orquestrar uma aplicação Flask com Prometheus, Grafana e Node Exporter usando o Kubernetes via Kind.

## Pré-requisitos
- Docker
- Kind
- kubectl

## Passos para rodar

### 1. Criar o cluster Kind
```bash
kind create cluster --name monitoramento
```

### 2. Build da imagem local da API
```bash
docker build -t api-monitoramento:latest .
kind load docker-image api-monitoramento:latest --name monitoramento
```

### 3. Aplicar os manifests
```bash
kubectl apply -f .
```

### 4. Verificar serviços
```bash
kubectl get svc
```

Acesse via navegador:

- Prometheus: `http://localhost:<NodePort-prometheus>`
- Grafana: `http://localhost:<NodePort-grafana>`

Usuário padrão do Grafana: `admin`, senha: `admin` (padrão da imagem)

---

Adaptado por Jean Campagnoli, com ❤️ e observabilidade!
