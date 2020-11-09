# Build stage

FROM node:14-alpine AS builder

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . ./

RUN npm run build


# Final

FROM nginx:latest

COPY --from=builder /app/dist/frontend-service /usr/share/nginx/html
