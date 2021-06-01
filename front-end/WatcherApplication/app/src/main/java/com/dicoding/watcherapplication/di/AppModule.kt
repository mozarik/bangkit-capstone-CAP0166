package com.dicoding.watcherapplication.di

import com.dicoding.watcherapplication.core.domain.usecase.WatcherInteractor
import com.dicoding.watcherapplication.core.domain.usecase.WatcherUseCase
import com.dicoding.watcherapplication.phone.PhoneViewModel
import org.koin.android.viewmodel.dsl.viewModel
import org.koin.dsl.module

val useCaseModule = module {
    factory<WatcherUseCase> { WatcherInteractor(get()) }
}

val viewModelModule = module {
    viewModel { PhoneViewModel(get()) }
}