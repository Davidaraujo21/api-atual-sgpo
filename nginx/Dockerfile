FROM nginx:1.16.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

EXPOSE 3006

CMD [ "nginx", "-g", "daemon off;" ]
