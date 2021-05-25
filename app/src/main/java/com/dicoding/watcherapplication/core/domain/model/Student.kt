package com.dicoding.watcherapplication.core.domain.model

import android.os.Parcelable
import kotlinx.android.parcel.Parcelize

@Parcelize
data class Student (
    var name: String,
    var image: String
) : Parcelable