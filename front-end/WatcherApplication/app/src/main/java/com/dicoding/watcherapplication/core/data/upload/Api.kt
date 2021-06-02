package com.dicoding.watcherapplication.core.data.upload

import retrofit.RestAdapter

object Api {
    val client: ApiInterface
        get(){
            val adapter = RestAdapter.Builder()
                .setEndpoint("https://ce6ca273-76c5-45f1-b418-f5e2bf5b71db.mock.pstmn.io")
                //.setEndpoint("http://172.17.14.162:8080")
                .build()
            return adapter.create(ApiInterface::class.java)
        }
}