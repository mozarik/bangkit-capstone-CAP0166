package com.dicoding.watcherapplication.core.data.source.remote.network

import com.dicoding.watcherapplication.core.data.source.remote.response.ListStudentResponse
import com.dicoding.watcherapplication.core.data.source.remote.response.PostRequest
import retrofit2.Call
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.Headers
import retrofit2.http.POST

interface ApiService {

    @GET("dummy")
    suspend fun getList():ListStudentResponse

    //upload (haven't tested) maybe need suspend like getList()?
    @Headers("Content-Type: application/json")
    @POST("uploadfile/")
    suspend fun postPhoto(@Body photo: PostRequest): Call<PostRequest>
}