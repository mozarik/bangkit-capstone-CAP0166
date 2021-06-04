package com.dicoding.watcherapplication.core.data.source.local.room

import androidx.room.Database
import androidx.room.RoomDatabase
import com.dicoding.watcherapplication.core.data.source.local.entity.StudentEntity

@Database(entities = [StudentEntity::class], version = 1, exportSchema = false)
abstract class WatcherDatabase : RoomDatabase() {
    abstract fun watcherDao(): WatcherDao

//    companion object {
//        @Volatile
//        private var INSTANCE: WatcherDatabase? = null
//
//        fun getInstance(context: Context): WatcherDatabase =
//    }
}