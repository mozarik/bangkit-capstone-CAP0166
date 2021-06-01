package com.dicoding.watcherapplication.core.domain.usecase


import com.dicoding.watcherapplication.core.data.Resource
import com.dicoding.watcherapplication.core.domain.model.Student
import kotlinx.coroutines.flow.Flow

interface WatcherUseCase {
    fun getAllStudent(): Flow<Resource<List<Student>>>
}