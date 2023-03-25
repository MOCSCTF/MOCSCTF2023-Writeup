FROM openjdk:8
WORKDIR /app
COPY src/yamlconfig.jar ./
COPY flag /flag
COPY readflag /readflag
RUN chmod 0400 /flag && chmod 4555 /readflag

RUN groupadd -r web && useradd -r -g web web

USER web

CMD ["java", "-jar", "yamlconfig.jar"]