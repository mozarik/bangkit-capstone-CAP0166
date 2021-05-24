package com.dicoding.watcherapplication.core.data.source.remote.response

import com.google.gson.annotations.SerializedName

data class StudentResponse (
    @field:SerializedName("name")
    val name: String,

    @field:SerializedName("img")
    val img: String
)