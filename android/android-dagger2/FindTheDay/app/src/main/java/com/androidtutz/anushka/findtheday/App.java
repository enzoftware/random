package com.androidtutz.anushka.findtheday;

import android.app.Application;

public class App extends Application {
    private DayComponent dayComponent;
    public static App app;

    @Override
    public void onCreate() {
        super.onCreate();
        app = this;
        dayComponent = DaggerDayComponent.builder()
                .dayModule(new DayModule())
                .build();
    }

    public DayComponent getDayComponent() {
        return dayComponent;
    }

    public static App getApp() {
        return app;
    }
}
