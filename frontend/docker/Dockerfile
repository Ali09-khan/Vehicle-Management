FROM node:20.4.0-alpine as build

WORKDIR /app

COPY . .

RUN npm i -g pnpm

RUN pnpm i --frozen-lockfile
RUN pnpm vite build

FROM nginx:1.25.3-alpine

COPY --from=build /app/dist /var/www/html

COPY docker/nginx/nginx.conf /etc/nginx/nginx.conf
COPY docker/nginx/default.conf /etc/nginx/conf.d/default.conf

RUN chown nginx:nginx /var/www/html

ENTRYPOINT ["nginx", "-g", "daemon off;"]
