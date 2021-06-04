package com.dicoding.watcherapplication.core.data.source.remote.network

import com.dicoding.watcherapplication.core.data.source.remote.response.ListStudentResponse
import retrofit2.http.GET

interface ApiService {
    // student_mock
    // student
    // /postprocess/5
    @GET("/postprocess/5")
    suspend fun getList():ListStudentResponse

}