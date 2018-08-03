FROM node:6.10.3

RUN npm install -g @compodoc/compodoc
COPY ./package.json .

COPY ./tsconfig.app.json ./app/src/tsconfig.app.json

CMD npm run doc
