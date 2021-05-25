package com.dicoding.watcherapplication.core.di

import androidx.room.Room
import com.dicoding.watcherapplication.core.data.WatcherRepository
import com.dicoding.watcherapplication.core.data.source.local.LocalDataSource
import com.dicoding.watcherapplication.core.data.source.local.room.WatcherDatabase
import com.dicoding.watcherapplication.core.data.source.remote.RemoteDataSource
import com.dicoding.watcherapplication.core.data.source.remote.network.ApiService
import com.dicoding.watcherapplication.core.domain.repository.IWatcherRepository
import com.dicoding.watcherapplication.core.utils.AppExecutors
import okhttp3.OkHttpClient
import okhttp3.logging.HttpLoggingInterceptor
import org.koin.android.ext.koin.androidContext
import org.koin.dsl.module
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import java.util.concurrent.TimeUnit

val databaseModule = module {
    factory { get<WatcherDatabase>().watcherDao() }
    single {
        Room.databaseBuilder(
            androidContext(),
            WatcherDatabase::class.java,"Watcher.db"
        ).fallbackToDestructiveMigration().build()
    }
}

val networkModule = module {
    single {
        OkHttpClient.Builder()
            .addInterceptor(HttpLoggingInterceptor().setLevel(HttpLoggingInterceptor.Level.BODY))
            .connectTimeout(120, TimeUnit.SECONDS)
            .readTimeout(120, TimeUnit.SECONDS)
            .build()
    }
    single {
        val retrofit = Retrofit.Builder()
            .baseUrl("https://link.api.this.is.only.dummy.baka.com")
            .addConverterFactory(GsonConverterFactory.create())
            .client(get())
            .build()
        retrofit.create(ApiService::class.java)
    }
}

val repositoryModule = module {
    single { LocalDataSource(get()) }
    single { RemoteDataSource(get())}
    factory { AppExecutors() }
    single<IWatcherRepository> {
        WatcherRepository(
            get(),
            get(),
            get()
        )
    }
}