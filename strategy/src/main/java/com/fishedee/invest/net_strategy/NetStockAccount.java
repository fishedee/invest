package com.fishedee.invest.net_strategy;

import com.fishedee.invest.stock.StockAccount;

import java.math.BigDecimal;

public class NetStockAccount {
    public enum State {
        MONEY_AND_STOCK,
        TWO_STOCK,
        TWO_MONEY,
    }

    private StockAccount account;

    private State state;

    public NetStockAccount(StockAccount stockAccount){
        this.account = stockAccount;
        this.state = State.MONEY_AND_STOCK;
    }

    public void buy(BigDecimal price){
        //价格下跌到sigma%以下
        if( state == State.MONEY_AND_STOCK ){
            //余额全部买了
            this.account.buy(this.account.getBalance(),price);
            state = State.TWO_STOCK;
        }else if( state == State.TWO_MONEY ){
            //买一半
            account.buy(this.account.getBalance().divide(new BigDecimal("2"),8,BigDecimal.ROUND_HALF_UP),price);
            state = State.MONEY_AND_STOCK;
        }else{
            //throw new RuntimeException("TWO_STOCK状态不能购买");
        }
    }

    public void sell(BigDecimal price){
        if( state == State.MONEY_AND_STOCK ){
            //股票全卖了
            account.sell(price,this.account.getAmount());
            state = State.TWO_MONEY;
        }else if( state == State.TWO_STOCK){
            //卖一半
            account.sell(price,this.account.getAmount().divide(new BigDecimal("2"),8,BigDecimal.ROUND_HALF_UP));
            state = State.MONEY_AND_STOCK;
        }else{
            //throw new RuntimeException("TWO_MONEY状态不能卖");
        }
    }

    public void end(BigDecimal price){
        if( state == State.TWO_MONEY ){
            this.buy(price);
        }else if(state == State.TWO_STOCK){
            this.sell(price);
        }
    }
}
