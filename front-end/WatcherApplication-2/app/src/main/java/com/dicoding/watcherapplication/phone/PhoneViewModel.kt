package com.dicoding.watcherapplication.phone

import androidx.lifecycle.ViewModel
import androidx.lifecycle.asLiveData
import com.dicoding.watcherapplication.core.domain.usecase.WatcherUseCase

class PhoneViewModel(watcherUseCase: WatcherUseCase) : ViewModel() {
    val student = watcherUseCase.getAllStudent().asLiveData()
}