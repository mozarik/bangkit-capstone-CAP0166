package com.dicoding.watcherapplication.core.data.source.remote.response

import com.google.gson.annotations.SerializedName

data class StudentResponse (

    @field:SerializedName("id")
    val id: Int,

    @field:SerializedName("name")
    val name: String,

    @field:SerializedName("percentage")
    val percentage: String,

    @field:SerializedName("img_url")
    val img: String
)