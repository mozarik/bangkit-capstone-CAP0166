package com.dicoding.watcherapplication.core.domain.usecase


import com.dicoding.watcherapplication.core.domain.repository.IWatcherRepository


class WatcherInteractor(private val watcherRepository: IWatcherRepository): WatcherUseCase {
    override fun getAllStudent() = watcherRepository.getAllStudent()

}