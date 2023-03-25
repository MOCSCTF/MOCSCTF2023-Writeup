package com.ctf.yamlconfig.controller;

import com.ctf.yamlconfig.util.Common;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.yaml.snakeyaml.Yaml;

import java.lang.reflect.Method;
import java.util.HashMap;

@RestController
public class ConfigController {
    @GetMapping({"/"})
    public String index() {
        return "Hello, friend!";
    }

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
}
