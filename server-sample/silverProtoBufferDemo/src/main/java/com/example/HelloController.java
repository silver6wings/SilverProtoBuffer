package com.example;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
@RequestMapping("/hello")
public class HelloController {
    @RequestMapping(value = "", method = RequestMethod.GET)
    @ResponseBody
    public Hello.hello printHello() {
        return Hello.hello.newBuilder()
                .setHelloId(1)
                .setHelloName("xx")
                .build();
    }
}