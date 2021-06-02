package com.dicoding.watcherapplication.core.data

import com.dicoding.watcherapplication.core.data.source.local.LocalDataSource
import com.dicoding.watcherapplication.core.data.source.remote.RemoteDataSource
import com.dicoding.watcherapplication.core.data.source.remote.network.ApiResponse
import com.dicoding.watcherapplication.core.data.source.remote.response.StudentResponse
import com.dicoding.watcherapplication.core.domain.model.Student
import com.dicoding.watcherapplication.core.domain.repository.IWatcherRepository
import com.dicoding.watcherapplication.core.utils.AppExecutors
import com.dicoding.watcherapplication.core.utils.DataMapper
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

class WatcherRepository(
    private val remoteDataSource: RemoteDataSource,
    private val localDataSource: LocalDataSource,
    private val appExecutors: AppExecutors
): IWatcherRepository {
    override fun getAllStudent(): Flow<Resource<List<Student>>> =
        object : NetworkBoundResource<List<Student>, List<StudentResponse>>() {
            override fun loadFromDB(): Flow<List<Student>> {
                return localDataSource.getAllStudent().map {
                    DataMapper.mapEntitiesToDomainStudent(it)
                }
            }

            override fun shouldFetch(data: List<Student>?): Boolean =
//                data == null || data.isEmpty()
                true


            override suspend fun createCall(): Flow<ApiResponse<List<StudentResponse>>> =
                remoteDataSource.getAllStudent()

            override suspend fun saveCallResult(data: List<StudentResponse>) {
                localDataSource.deleteAllStudentTableData()//to clear all data and replace with new one to view
                val studentList = DataMapper.mapResponseToEntitiesStudent(data)
                localDataSource.insertStudent(studentList)
            }

        }.asFlow()


}