package com.dicoding.watcherapplication.core.data.source.remote.response

import com.google.gson.annotations.SerializedName

data class ListStudentResponse (
    @field:SerializedName("status")
    val status: Int,

    @field:SerializedName("data")
    val data: List<StudentResponse>
)