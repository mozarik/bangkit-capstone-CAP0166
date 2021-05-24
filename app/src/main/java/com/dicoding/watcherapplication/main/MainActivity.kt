package com.dicoding.watcherapplication.main

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import com.dicoding.watcherapplication.R
import com.dicoding.watcherapplication.databinding.ActivityMainBinding
import com.dicoding.watcherapplication.phone.PhoneActivity

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.buttonUpload.setOnClickListener {
            Toast.makeText(this, "Button Upload is Unfinished, please for the next update...", Toast.LENGTH_SHORT).show()
        }

        binding.buttonChooseImage.setOnClickListener {
            Toast.makeText(this, "Button ChooseImage is Unfinished, please for the next update...", Toast.LENGTH_SHORT).show()
        }

        binding.buttonCheckResult.setOnClickListener {
            val intent = Intent(this, PhoneActivity::class.java)
            startActivity(intent)
        }
    }
}