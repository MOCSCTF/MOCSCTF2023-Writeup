FROM node:17-alpine

COPY src /
COPY flag /flag
COPY readflag.c /readflag.c
COPY package.json /package.json
COPY run.sh /run.sh

RUN apk add gcc g++ make cmake gfortran libffi-dev openssl-dev libtool
RUN chmod 0400 /flag && chown root:root /flag
RUN chmod 0444 /readflag.c && gcc /readflag.c -o /readflag
RUN chown root:root /readflag && chmod 4555 /readflag
WORKDIR /
RUN yarn
USER node
ENTRYPOINT ["yarn", "start"]