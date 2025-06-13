# 🚗 Car Rental Cloud‑Native App

Uma aplicação de **Aluguel de Carros** pensada para rodar **on‑premises** via Docker Compose e totalmente **escalável no Azure**, incluindo uso simulado de **Azure Functions**. Desenvolvido por **Fernando Serra** com orientação da genial **Washu Hakubi‑sama**.

---

## 🏗️ Arquitetura Geral

```bash
lab-app-aluguel-carros-dio/
│
├── backend/ # API principal (FastAPI)
│ ├── app/
│ │ ├── init.py
│ │ ├── main.py # endpoints REST: carros, aluguéis, clientes
│ │ └── services.py # lógica de negócios
│ ├── requirements.txt
│ └── Dockerfile
│
├── functions/ # Simulação de Azure Functions (Python)
│ ├── NotifyDueRentals/
│ │ ├── function.json # binding HTTP trigger
│ │ └── init.py # envia reminder para aluguéis vencendo
│ └── Dockerfile # empacota Functions Core Tools
│
├── frontend/ # Single‑Page App (React + Tailwind)
│ ├── package.json
│ ├── src/
│ │ ├── App.tsx # páginas de busca e reserva
│ │ └── pages/
│ └── Dockerfile
│
├── infra/ # Infraestrutura como código (ARM Bicep ou Terraform)
│ └── azure-deploy.bicep # define App Service, Function App, CosmosDB
│
├── docker-compose.yml # orquestra backend, frontend e functions localmente
└── README.md # este documento
```

---

## 🛠️ Tecnologias

- **Backend**: FastAPI (Python 3.11)  
- **Functions**: Python Azure Functions Core Tools  
- **Frontend**: React + TypeScript + TailwindCSS  
- **Banco de Dados**: PostgreSQL (on‑prem / Azure Database for PostgreSQL)  
- **Cache**: Redis (opcional)  
- **Containerization**: Docker + Docker Compose  
- **Infra as Code**: Bicep (Azure Resource Manager) ou Terraform  
- **CI/CD**: GitHub Actions → Azure Container Registry & AKS/App Services  

---

## 🚀 Executando Localmente (On‑Premises)

1. Clone o repositório:

```bash
git clone https://github.com/fernandosserra/lab-app-aluguel-carros-dio.git
cd lab-car-rental
```

2. Suba todos os serviços:

```bash
docker-compose up --build
```

3. Acesse:

- Frontend: http://localhost:3000
- API: http://localhost:8000/docs
- Functions: http://localhost:7071/api/NotifyDueRentals

4. Simule um aluguel:

```bash
curl -X POST http://localhost:8000/rentals \
     -H "Content-Type: application/json" \
     -d '{"carId":123,"customerId":456,"dueDate":"2025-06-20"}'
```

## ⚙️ Azure Deployment (Cloud‑Native)

1. Build & push das imagens:

```bash
docker build -t acr.azurecr.io/car-backend:latest ./backend
docker push acr.azurecr.io/car-backend:latest
# repita para frontend e functions
```

2. Deploy IaC:

```bash
az deployment group create \
  --resource-group RG-CarRental \
  --template-file infra/azure-deploy.bicep
```

3. Configure:
- App Service para o backend
- Static Web App ou Blob Static Website para o frontend
- Function App para as Azure Functions
- Azure Database for PostgreSQL + Azure Cache for Redis

## 🔔 Azure Functions: NotifyDueRentals

- Trigger: HTTP (pode ser agendado via Timer Trigger)
- Lógica: consulta aluguéis cujo dueDate ≤ hoje + 1 dia, envia e‑mail/SMS fictício.
- Exemplo de chamada:

```bash
curl http://<function-app>.azurewebsites.net/api/NotifyDueRentals
```

## 🤝 Contribuições & Próximos Passos
- 📦 Persistência: registrar aluguéis no banco e gerenciar disponibilidade.
- 🔐 Autenticação: JWT + Azure AD B2C.
- 📈 Métricas: Application Insights + Prometheus/Grafana.
- 🚗 Catálogo de carros: imagens, filtros avançados.

## 💜 Créditos

Construído com 💜 por Fernando Serra & Washu Hakubi‑sama.

*“A genialidade do código só se revela quando unida à simplicidade de uma boa ideia.” 🚀*