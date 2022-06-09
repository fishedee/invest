package com.fishedee.invest.net_strategy;

import com.fishedee.invest.stock.StockAccount;
import com.fishedee.invest.stock.StockPrice;
import org.apache.logging.log4j.util.Strings;
import org.springframework.stereotype.Component;

import java.math.BigDecimal;

@Component
public class NetStrategyTest {

    private double allPrice = 0;
    private int allPriceNumber = 0;

    public double singleTest(){
        StockAccount account = new StockAccount();
        account.setBalance(new BigDecimal("100000"));//手上预先也有10万的现金
        account.setAmount(new BigDecimal("1000"));//手上预先有1000股的底仓，每股初始价格为100元
        account.setFeePrecent(new BigDecimal("0.0002"));//万分之二的手续费，只在卖出时收取
        NetStockAccount netStockAccount = new NetStockAccount(account);
        double price = 100;

        for( int i = 0 ;i != 365;i++){
            double todayPrice = price;
            //0.35%
            double sigma = 0.0035;
            double priceGo = sigma * todayPrice;
            boolean hasAmount = (account.getAmount().signum() != 0);
            //结果：
            //mean为0的时候，实际到手为96855
            //mean为0.01的时候，实际到手为112424
            //mean为-0.01的时候，实际到手为75676
            StockPrice stockPrice = new StockPrice(price,0,price *sigma*0.1,10);
            while( stockPrice.hasNext() ){
                price = stockPrice.nextPrice();
                allPrice += price;
                allPriceNumber++;
                if( price <  -priceGo +todayPrice){
                    netStockAccount.buy(new BigDecimal(price));
                }else if( price > priceGo+todayPrice){
                    netStockAccount.sell(new BigDecimal(price));
                }
            }
            netStockAccount.end(new BigDecimal(price));
        }

        System.out.println(String.format("balance:%s ,amount:%s,radio:%s",
                account.getBalance(),
                account.getAmount(),
                account.getBalance().divide(new BigDecimal("100"),8,BigDecimal.ROUND_HALF_UP)));
        return account.getBalance().doubleValue();
    }

    public void go(){
        double total = 0;
        int n = 10000;
        for( int i = 0 ;i != n;i++){
            total += this.singleTest();
        }
        System.out.println(String.format("average result: %f,averagePrice:%f",
                total/n,
                allPrice/allPriceNumber));
    }
}
