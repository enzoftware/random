package com.androidtutz.anushka.memberapp;

import javax.inject.Singleton;

import dagger.Module;
import dagger.Provides;

@Module
class MemberDataModule {
    @Provides
    @Singleton
    MemberDataManager provideMemberDataManager(){
        return new MemberDataManager();
    }

}
