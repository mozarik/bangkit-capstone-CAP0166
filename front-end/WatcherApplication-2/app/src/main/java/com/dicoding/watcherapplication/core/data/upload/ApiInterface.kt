package com.dicoding.watcherapplication.core.data.upload

import okhttp3.MultipartBody
import okhttp3.ResponseBody
import retrofit2.Call
import retrofit2.http.*


interface ApiInterface {

    //====retro 2
//    @Headers("Content-Type: multipart/form-data")
    @Multipart
    @POST("/uploadfile/")
    fun upload(
        @Part file: MultipartBody.Part
    ): Call<ResponseBody>

}