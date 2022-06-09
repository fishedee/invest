package com.fishedee.invest.stock;

import java.math.BigDecimal;

public class StockAccount {
    private BigDecimal balance;

    private BigDecimal amount;

    private BigDecimal feePrecent;

    public StockAccount(){
        this.balance = new BigDecimal("0");
        this.amount = new BigDecimal("0");
        this.feePrecent = new BigDecimal("0");
    }

    public void setBalance(BigDecimal balance){
        this.balance = balance;
    }

    public void setAmount(BigDecimal amount){
        this.amount = amount;
    }

    public BigDecimal getBalance(){
        return this.balance;
    }

    public BigDecimal getAmount(){
        return this.amount;
    }

    public void setFeePrecent(BigDecimal feePrecent){
        this.feePrecent = feePrecent;
    }

    public void buy(BigDecimal target,BigDecimal price){
        BigDecimal amount = target.divide(price,0,BigDecimal.ROUND_FLOOR);
        BigDecimal total = amount.multiply(price);
        this.balance = this.balance.subtract(total);
        this.amount = this.amount.add(amount);
    }

    public void sell(BigDecimal price,BigDecimal amount){
        amount = amount.setScale(0,BigDecimal.ROUND_FLOOR);
        BigDecimal total = price.multiply(amount);
        this.balance = this.balance.add(total);
        this.amount = this.amount.subtract(amount);
        //卖出的时候计算费用
        this.balance = this.balance.subtract( total.multiply(this.feePrecent));
    }
}
