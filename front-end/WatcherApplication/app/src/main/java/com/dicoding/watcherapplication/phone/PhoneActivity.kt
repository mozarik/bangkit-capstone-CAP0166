package com.dicoding.watcherapplication.phone


import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import androidx.recyclerview.widget.LinearLayoutManager
import com.dicoding.watcherapplication.R
import com.dicoding.watcherapplication.core.data.Resource
import com.dicoding.watcherapplication.core.ui.StudentViewAdapter
//import com.dicoding.watcherapplication.core.utils.DataDummy
import com.dicoding.watcherapplication.databinding.ActivityPhoneBinding
import org.koin.android.viewmodel.ext.android.viewModel

class PhoneActivity : AppCompatActivity() {

    private val phoneViewModel: PhoneViewModel by viewModel()
    private lateinit var binding: ActivityPhoneBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityPhoneBinding.inflate(layoutInflater)
        setContentView(binding.root)

        supportActionBar?.title = "Student List"

        val studentViewAdapter = StudentViewAdapter()
//        studentViewAdapter.onItemClick = {
//
//        }

        phoneViewModel.student.observe(this, { dataStudent ->
            if (dataStudent != null) {
                when(dataStudent) {
                    is Resource.Loading -> binding.progressBar.visibility = View.VISIBLE
                    is Resource.Success -> {
                        binding.progressBar.visibility = View.GONE
                        studentViewAdapter.setData(dataStudent.data)
                    }
                    is Resource.Error -> {
                        binding.progressBar.visibility = View.GONE
                        binding.viewError.root.visibility = View.VISIBLE
                        binding.viewError.textError.text = dataStudent.message ?: getString(R.string.page_error)
                    }
                }
            }

            //data dummy for testing the student list
            //note: don't forget to comment above code (from if to it curly brace)
//            studentViewAdapter.setData(DataDummy.generateStudentDummy())
        })

        with(binding.recyclerViewStudent) {
            layoutManager = LinearLayoutManager(context)
            setHasFixedSize(true)
            adapter = studentViewAdapter
        }
    }
}