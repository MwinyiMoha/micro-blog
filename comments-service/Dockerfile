# Alias for common image

FROM node:10-alpine AS nodejs


# Build Stage

FROM nodejs AS builder

WORKDIR /app

COPY package*.json ./

RUN npm i

COPY . .

RUN npm run build


# Final 

FROM nodejs

LABEL maintainer="Mohammed Mwijaa<mm.mwijaa@gmail.com>"

RUN mkdir -p /home/node/app/dist

RUN chown -R node:node /home/node/app 

WORKDIR /home/node/app

RUN npm i -g pm2

COPY package*.json process.yml ./

USER node

RUN npm i --only=production

COPY --chown=node:node --from=builder /app/dist ./dist

EXPOSE 3000

CMD ["pm2-runtime", "--raw", "process.yml"]
