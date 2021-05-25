package com.dicoding.watcherapplication.core.data.source.remote

import android.util.Log
import com.dicoding.watcherapplication.core.data.source.remote.network.ApiResponse
import com.dicoding.watcherapplication.core.data.source.remote.network.ApiService
import com.dicoding.watcherapplication.core.data.source.remote.response.StudentResponse
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.flow

class RemoteDataSource(private val apiService: ApiService) {

    suspend fun getAllStudent(): Flow<ApiResponse<List<StudentResponse>>> {
        //get data from api
        return flow {
            try {
                val response = apiService.getList()
                val dataArray = response.data
                if (dataArray.isNotEmpty()) {
                    emit(ApiResponse.Success(response.data))
                } else {
                    emit(ApiResponse.Empty)
                }
            } catch (e : Exception) {
                emit(ApiResponse.Error(e.toString()))
                Log.e("RemoteDataSource", e.toString())
            }
        }
    }
}