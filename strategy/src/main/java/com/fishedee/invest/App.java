package com.fishedee.invest;

import com.fishedee.invest.net_strategy.NetStrategyTest;
import javafx.application.Application;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * Hello world!
 *
 */
@SpringBootApplication
public class App implements ApplicationRunner
{
    public static void main( String[] args ) {
        SpringApplication.run(App.class,args);
    }

    @Autowired
    private NetStrategyTest netStrategyTest;

    @Override
    public void run(ApplicationArguments args) throws Exception{
        netStrategyTest.go();
    }
}
