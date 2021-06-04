package com.dicoding.watcherapplication.core.data.source.local

import com.dicoding.watcherapplication.core.data.source.local.entity.StudentEntity
import com.dicoding.watcherapplication.core.data.source.local.room.WatcherDao
import kotlinx.coroutines.flow.Flow

class LocalDataSource(private val watcherDao: WatcherDao) {
    fun getAllStudent(): Flow<List<StudentEntity>> = watcherDao.getAllStudent()

    fun insertStudent(studentList: List<StudentEntity>) = watcherDao.insertStudent(studentList)

    fun deleteAllStudentTableData() = watcherDao.deleteAllDataInTableStudent()
}