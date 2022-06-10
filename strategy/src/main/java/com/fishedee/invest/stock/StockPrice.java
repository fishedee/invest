package com.fishedee.invest.stock;

import java.math.BigDecimal;
import java.util.Optional;
import java.util.Random;

//模拟股市价格的随机游走
public class StockPrice {
    private double price;

    private double mean;

    private double originPrice;

    private double sigma;

    private int step;

    private int n;

    private Random random;

    private double sigmaSqrt;

    public StockPrice(double price,double mean,double sigma,int n){
        this.price = price;
        this.originPrice = price;
        this.mean = mean;
        this.sigma = sigma;
        this.n = n;
        this.step = 0;
        this.random = new Random();
        this.sigmaSqrt = Math.sqrt(sigma);
    }

    private double nextGaussian(){
        double gaussian = this.random.nextGaussian();
        double gaussian2 = this.sigmaSqrt * gaussian+ this.mean;
        return this.price + gaussian2;
    }

    private double nextRandom(){
        double rand = this.random.nextDouble()-0.5;
        double rand2 =  this.sigmaSqrt* rand + this.mean;
        return this.price + rand2;
    }


    private double nextRandom2(){
        double rand = this.random.nextDouble()-0.5;
        double rand2 = this.sigma*this.sigma;
        if( rand <= 0 ){
            rand2 = rand2 * -1;
        }
        return this.price + rand2;
    }

    private double nextOriginGaussian(){
        double gaussian = this.random.nextGaussian();
        double gaussian2 = this.sigmaSqrt * gaussian+ this.mean;
        return this.originPrice + gaussian2;
    }

    public boolean hasNext(){
        return this.step < this.n;
    }

    public double nextPrice(){
        if( this.hasNext() == false ){
            throw new RuntimeException("Nothing generate");
        }
        this.price = this.nextRandom();
        if( this.price < 0 ){
            this.price = 0;
        }
        this.step ++;
        return this.price;
    }
}
