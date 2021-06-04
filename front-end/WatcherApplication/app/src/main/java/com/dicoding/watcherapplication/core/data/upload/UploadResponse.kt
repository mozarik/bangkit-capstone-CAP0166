package com.dicoding.watcherapplication.core.data.upload

class UploadResponse {
    private lateinit var status: String

    public fun getStatus(): String {
        return status
    }

    public fun setStatus(status: String) {
        this.status = status
    }
}