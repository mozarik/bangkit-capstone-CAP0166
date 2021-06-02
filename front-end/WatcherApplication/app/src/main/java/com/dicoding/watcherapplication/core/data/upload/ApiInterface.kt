package com.dicoding.watcherapplication.core.data.upload

import retrofit.Callback
import retrofit.http.Field
import retrofit.http.FormUrlEncoded
import retrofit.http.POST

interface ApiInterface {
    @FormUrlEncoded
    @POST("/student_list/post_mock")
    fun upload(
        @Field("id") id: Int,
        @Field("photo") photo: String?,
        callback: Callback<UploadResponse?>?
    )

    /*@FormUrlEncoded
    @POST("/ers/register")
    fun upload(
        @Field("user") user: String?,
        @Field("password") password: String?,
        @Field("roles") roles: String?,
        @Field("email") email: String?,
        @Field("divison") divison: String?,
        @Field("position") position: String?,
        callback: Callback<UploadResponse?>?
    )*/
}