# ---------- build stage ----------
FROM node:20-alpine AS build
WORKDIR /app

# Pass through your backend URLs at build time
ARG VITE_PRODUCTS_URL=http://localhost:8002
ARG VITE_CUSTOMERS_URL=http://localhost:8001

ENV VITE_PRODUCTS_URL=$VITE_PRODUCTS_URL \
    VITE_CUSTOMERS_URL=$VITE_CUSTOMERS_URL \
    CI=true              

COPY . .

RUN corepack enable \
    && pnpm install --frozen-lockfile \
    && pnpm run build

# ---------- run stage ----------
FROM nginx:1.27-alpine
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
