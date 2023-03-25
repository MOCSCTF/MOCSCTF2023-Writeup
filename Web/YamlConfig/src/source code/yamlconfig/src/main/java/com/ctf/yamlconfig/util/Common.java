package com.ctf.yamlconfig.util;

public class Common {

    public final static String exampleConfig =
            "!!com.ctf.yamlconfig.config.DataSourceConfig {\n" +
            "  host: 127.0.0.1,\n" +
            "  port: 3306,\n" +
            "  username: SilentE,\n" +
            "  password: 123456,\n" +
            "  database: Test,\n" +
            "  type: mysql,\n" +
            "  params: \"characterEncoding=utf-8&serverTimezone=GMT&useUnicode=true\"\n" +
            "}";
    public static boolean isValid(String origin) {
        if (origin.contains("[") || origin.contains("]") || origin.contains("ScriptEngineManager") || origin.contains("InputStream")
                || origin.contains("OutputStream") || origin.contains("JdbcRowSetImpl") || origin.contains("jndi") || origin.contains("javax.naming") || origin.contains("org.apache.tomcat")) {
            return false;
        }
        return true;
    }
}
