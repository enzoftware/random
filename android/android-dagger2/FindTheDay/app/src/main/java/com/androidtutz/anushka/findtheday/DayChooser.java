package com.androidtutz.anushka.findtheday;

/**
 * Created by K. A. ANUSHKA MADUSANKA on 1/26/2018.
 */

public class DayChooser {
    private int givenIndex;
    private String selectedDay;

    public String getTheDay(int index) {
        int reminder = index % 5;
        switch (reminder) {
            case 1:
                selectedDay = "Monday";
                break;
            case 2:
                selectedDay = "Tuesday";
                break;
            case 3:
                selectedDay = "Wednesday";
                break;
            case 4:
                selectedDay = "Thursday";
                break;
            case 0:
                selectedDay = "Friday";
                break;

        }
        return selectedDay;
    }


}
