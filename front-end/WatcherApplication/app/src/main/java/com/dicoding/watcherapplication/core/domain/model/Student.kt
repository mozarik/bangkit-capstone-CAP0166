package com.dicoding.watcherapplication.core.domain.model

import android.os.Parcelable
import kotlinx.parcelize.Parcelize
// import kotlinx.android.parcel.Parcelize

@Parcelize
data class Student (
    var name: String,
    var percentage: String,
    var image: String
) : Parcelable