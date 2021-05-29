package com.dicoding.watcherapplication.core.data.source.local.room

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import com.dicoding.watcherapplication.core.data.source.local.entity.StudentEntity
import kotlinx.coroutines.flow.Flow

@Dao
interface WatcherDao {
    @Query("SELECT * FROM student")
    fun getAllStudent(): Flow<List<StudentEntity>>

    @Query("DELETE FROM student")
    fun deleteAllDataInTableStudent()

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    fun insertStudent(student: List<StudentEntity>)
}