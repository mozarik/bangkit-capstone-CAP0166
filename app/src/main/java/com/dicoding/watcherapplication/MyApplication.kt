package com.dicoding.watcherapplication

import android.app.Application
import com.dicoding.watcherapplication.core.di.databaseModule
import com.dicoding.watcherapplication.core.di.networkModule
import com.dicoding.watcherapplication.core.di.repositoryModule
import com.dicoding.watcherapplication.di.useCaseModule
import com.dicoding.watcherapplication.di.viewModelModule
import org.koin.android.ext.koin.androidContext
import org.koin.android.ext.koin.androidLogger
import org.koin.core.context.startKoin
import org.koin.core.logger.Level

class MyApplication: Application() {
    override fun onCreate(){
        super.onCreate()
        startKoin {
            androidLogger(Level.NONE)
            androidContext(this@MyApplication)
            modules(
                listOf(
                    databaseModule,
                    networkModule,
                    repositoryModule,
                    useCaseModule,
                    viewModelModule
                )
            )
        }
    }
}