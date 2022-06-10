package com.fishedee.invest.util;

import java.util.List;

public class StatisUtil {
    public static double average(List<Double> data){
        double result = 0;
        for( int i = 0 ;i != data.size();i++){
            result = result + data.get(i);
        }
        return result/data.size();
    }

    public static double standardDiviation(List<Double>data){
        double average = StatisUtil.average(data);
        double all = 0;
        for( int i = 0 ;i != data.size();i++){
            double single = data.get(i);
            all = all + (single-average)*(single-average);
        }
        return Math.sqrt(all/data.size());
    }

    public static double oneDayWave(List<Double> data){
        double high = data.get(0);
        double low = data.get(0);
        for( int i = 0 ;i != data.size() ;i++) {
            double single = data.get(i);
            if (single > high) {
                high = single;
            }
            if ( single < low ){
                low = single;
            }
        };
        double close = data.get(data.size()-1);
        double result = (high-low)/close;
        //System.out.printf("date wave %f %f %f dayWave:%f\n",high,low,close,result);
        return result;
    }
}
