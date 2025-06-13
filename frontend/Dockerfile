# ---------- Stage 1: Build do Frontend ----------
FROM node:18-alpine AS build

# Define diretório de trabalho
WORKDIR /app

# Copia package.json e lockfile e instala dependências
COPY package.json yarn.lock* package-lock.json* ./
RUN \
  if [ -f yarn.lock ]; then yarn install --frozen-lockfile; \
  else npm ci; \
  fi

# Copia todo o código-fonte e gera a build de produção
COPY . .
RUN npm run build

# ---------- Stage 2: Serve via Nginx ----------
FROM nginx:alpine

# Remove configuração default e adiciona a sua
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/

# Copia arquivos estáticos da build
COPY --from=build /app/dist /usr/share/nginx/html

# Exponha a porta 80
EXPOSE 80

# Inicia o Nginx em foreground
CMD ["nginx", "-g", "daemon off;"]
