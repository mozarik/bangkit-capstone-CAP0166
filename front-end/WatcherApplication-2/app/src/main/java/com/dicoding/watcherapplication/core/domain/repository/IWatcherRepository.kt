package com.dicoding.watcherapplication.core.domain.repository

import com.dicoding.watcherapplication.core.data.Resource
import com.dicoding.watcherapplication.core.domain.model.Student
import kotlinx.coroutines.flow.Flow

interface IWatcherRepository {
    fun getAllStudent(): Flow<Resource<List<Student>>>

}