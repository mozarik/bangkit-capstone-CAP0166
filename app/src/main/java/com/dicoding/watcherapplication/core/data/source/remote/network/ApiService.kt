package com.dicoding.watcherapplication.core.data.source.remote.network

import com.dicoding.watcherapplication.core.data.source.remote.response.ListStudentResponse
import retrofit2.http.GET

interface ApiService {

    @GET("")
    suspend fun getList():ListStudentResponse
}