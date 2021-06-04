package com.dicoding.watcherapplication.core.utils

import com.dicoding.watcherapplication.core.data.source.local.entity.StudentEntity
import com.dicoding.watcherapplication.core.data.source.remote.response.StudentResponse
import com.dicoding.watcherapplication.core.domain.model.Student

object DataMapper {
    fun mapResponseToEntitiesStudent(input: List<StudentResponse>): List<StudentEntity> {
        val studentList = ArrayList<StudentEntity>()
        input.map {
            val student = StudentEntity(
                id = it.id,
                name = it.name,
                image = it.img,
                percentage = it.percentage
            )
            studentList.add(student)
        }
        return studentList
    }

    fun mapEntitiesToDomainStudent(input: List<StudentEntity>): List<Student> =
        input.map {
            Student(
                id = it.id,
                name = it.name,
                percentage = it.percentage,
                image = it.image
            )
        }

    fun mapDomainToEntityStudent(input: Student) = StudentEntity(
        id = input.id,
        name = input.name,
        percentage = input.percentage,
        image = input.image
    )
}