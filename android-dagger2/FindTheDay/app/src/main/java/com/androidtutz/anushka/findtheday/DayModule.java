package com.androidtutz.anushka.findtheday;

import javax.inject.Singleton;

import dagger.Module;
import dagger.Provides;

@Module
public class DayModule {


    @Singleton
    @Provides
    public DayChooser dayChooser(){
        return new DayChooser();
    }

}
