package com.fishedee.invest.stock;

import java.math.BigDecimal;
import java.util.Optional;
import java.util.Random;

//模拟股市价格的随机游走
public class StockPrice {
    private double price;

    private double mean;

    private double sigma;

    private int step;

    private int n;

    private Random random;

    private double sigmaSqrt;

    public StockPrice(double price,double mean,double sigma,int n){
        this.price = price;
        this.mean = mean;
        this.sigma = sigma;
        this.n = n;
        this.step = 0;
        this.random = new Random();
        this.sigmaSqrt = Math.sqrt(sigma);
    }

    private double nextGaussian(){
        double gaussian = this.random.nextGaussian();
        double result = this.sigmaSqrt * gaussian+ this.mean;
        return result;
    }

    public boolean hasNext(){
        return this.step < this.n;
    }

    public double nextPrice(){
        if( this.hasNext() == false ){
            throw new RuntimeException("Nothing generate");
        }
        double gaussian =  this.nextGaussian();
        this.price = this.price +gaussian;
        this.step ++;
        return this.price;
    }
}
