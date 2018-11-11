package com.androidtutz.anushka.findtheday;

import javax.inject.Singleton;

import dagger.Component;

// IF PROVIDES SINGLENTON - THE COMPONENT HAVE @SINGLENTON
@Singleton
@Component(modules = DayModule.class)
public interface DayComponent {
    void inject(DayFragment dayFragment);
}
