package com.example;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
@RequestMapping("/hello")
public class MyHelloController {

    @RequestMapping(value = "/{id}/get", method = RequestMethod.GET)
    @ResponseBody
    public MyHello.HelloResponse getHello(
            @PathVariable("id") Long id,
            @RequestParam(value = "foo", required = false) String foo)
    {

        return MyHello.HelloResponse.newBuilder()
                .setID(id)
                .setContent("foo:" + foo)
                .build();
    }

    @RequestMapping(value = "/post", method = RequestMethod.POST)
    @ResponseBody
    public MyHello.HelloResponse postHello(
            @RequestBody MyHello.HelloRequest request)
    {
        return MyHello.HelloResponse.newBuilder()
                .setID(request.getID())
                .setContent(request.getFoo() + request.getBar())
                .build();
    }
}
