package com.dicoding.watcherapplication.core.domain.usecase

import com.bumptech.glide.load.engine.Resource
import com.dicoding.watcherapplication.core.domain.model.Student
import com.dicoding.watcherapplication.core.domain.repository.IWatcherRepository
import kotlinx.coroutines.flow.Flow

class WatcherInteractor(private val watcherRepository: IWatcherRepository): WatcherUseCase {
    override fun getAllStudent() = watcherRepository.getAllStudent()

}