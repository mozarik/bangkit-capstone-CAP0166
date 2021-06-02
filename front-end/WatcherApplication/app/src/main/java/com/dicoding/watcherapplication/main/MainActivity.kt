package com.dicoding.watcherapplication.main

import android.Manifest
import android.annotation.SuppressLint
import android.app.AlertDialog
import android.app.ProgressDialog
import android.content.DialogInterface
import android.content.Intent
import android.database.Cursor
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Environment
import android.provider.MediaStore
import android.util.Base64
import android.widget.Toast
import androidx.core.content.FileProvider
import com.bumptech.glide.Glide
import com.bumptech.glide.load.engine.DiskCacheStrategy
import com.dicoding.watcherapplication.BuildConfig
import com.dicoding.watcherapplication.core.data.upload.Api
import com.dicoding.watcherapplication.core.data.upload.UploadResponse
import com.dicoding.watcherapplication.databinding.ActivityMainBinding
import com.dicoding.watcherapplication.phone.PhoneActivity
import com.karumi.dexter.Dexter
import com.karumi.dexter.MultiplePermissionsReport
import com.karumi.dexter.PermissionToken
import com.karumi.dexter.listener.multi.MultiplePermissionsListener
import retrofit.Callback
import retrofit.RetrofitError
import retrofit.client.Response
import java.io.ByteArrayOutputStream
import java.io.File
import java.io.IOException
import java.text.SimpleDateFormat
import java.util.*

class MainActivity : AppCompatActivity() {

    var REQ_CAMERA = 100
    val REQUEST_PICK_PHOTO = 2
    var cameraFilePath: String? = null
    var imageBytes: ByteArray? = null

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.buttonUpload.setOnClickListener {
            upload()
//            Toast.makeText(this, "Button Upload is Unfinished, please for the next update...", Toast.LENGTH_SHORT).show()

        }

        binding.buttonChooseImage.setOnClickListener {
//            Toast.makeText(this, "Button ChooseImage is Unfinished, please for the next update...", Toast.LENGTH_SHORT).show()
            showPictureDialog()
        }

        binding.buttonCheckResult.setOnClickListener {
            val intent = Intent(this, PhoneActivity::class.java)
            startActivity(intent)
        }
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        if (requestCode == REQ_CAMERA && resultCode == RESULT_OK) {
            cameraFilePath?.let { convertImage(it) }
        } else if (requestCode == REQUEST_PICK_PHOTO && resultCode == RESULT_OK) {
            val imageUri: Uri? = data!!.data
            val filePathColumn = arrayOf(MediaStore.Images.Media.DATA)
            assert(imageUri != null)
            val cursor: Cursor = imageUri?.let {
                contentResolver.query(it, filePathColumn, null, null, null)
            }!!
            cursor.moveToFirst()
            val columnIndex: Int = cursor.getColumnIndex(filePathColumn[0])
            val mediaPath: String = cursor.getString(columnIndex)
            cursor.close()
            cameraFilePath = mediaPath
            convertImage(mediaPath)
        }
    }

    //choose image function=================

    private fun showPictureDialog() {
        val pictureDialog: AlertDialog.Builder = AlertDialog.Builder(this)
        pictureDialog.setTitle("Select Action")
        val pictureDialogItems = arrayOf(
                "Select photo from gallery",
                "Capture photo from camera"
        )
        pictureDialog.setItems(pictureDialogItems,
                DialogInterface.OnClickListener { dialog, which ->
                    when (which) {
                        0 -> uploadImage()
                        1 -> takeCameraImage()
                    }
                })
        pictureDialog.show()
    }

    protected fun takeCameraImage() {
        Dexter.withActivity(this)
                .withPermissions(
                        Manifest.permission.CAMERA,
                        Manifest.permission.WRITE_EXTERNAL_STORAGE,
                        Manifest.permission.ACCESS_COARSE_LOCATION,
                        Manifest.permission.ACCESS_FINE_LOCATION
                )
                .withListener(object : MultiplePermissionsListener {
                    override fun onPermissionsChecked(report: MultiplePermissionsReport) {
                        if (report.areAllPermissionsGranted()) {
                            try {
                                val intent = Intent(MediaStore.ACTION_IMAGE_CAPTURE)
                                intent.putExtra(
                                        MediaStore.EXTRA_OUTPUT,
                                        createImageFile()?.let {
                                            FileProvider.getUriForFile(
                                                    this@MainActivity,
                                                    BuildConfig.APPLICATION_ID.toString() + ".provider",
                                                    it
                                            )
                                        }
                                )
                                startActivityForResult(intent, REQ_CAMERA)
                            } catch (ex: IOException) {
                                Toast.makeText(
                                        this@MainActivity,
                                        "Gagal membuka kamera!",
                                        Toast.LENGTH_SHORT,
                                ).show()
                            }
                        }
                    }

                    override fun onPermissionRationaleShouldBeShown(
                            p0: MutableList<com.karumi.dexter.listener.PermissionRequest>?,
                            p1: PermissionToken?
                    ) {
                        p1!!.continuePermissionRequest()
                    }

                }).check()
    }

    protected fun uploadImage() {
        Dexter.withActivity(this)
                .withPermissions(
                        Manifest.permission.CAMERA,
                        Manifest.permission.WRITE_EXTERNAL_STORAGE,
                        Manifest.permission.ACCESS_COARSE_LOCATION,
                        Manifest.permission.ACCESS_FINE_LOCATION
                )
                .withListener(object : MultiplePermissionsListener {
                    override fun onPermissionsChecked(report: MultiplePermissionsReport) {
                        if (report.areAllPermissionsGranted()) {
                            val galleryIntent =
                                    Intent(
                                        Intent.ACTION_PICK,
                                        MediaStore.Images.Media.EXTERNAL_CONTENT_URI
                                    )
                            startActivityForResult(galleryIntent, REQUEST_PICK_PHOTO)
                        }
                    }

                    override fun onPermissionRationaleShouldBeShown(
                            p0: MutableList<com.karumi.dexter.listener.PermissionRequest>?,
                            p1: PermissionToken?
                    ) {
                        p1!!.continuePermissionRequest()
                    }

                }).check()
    }

    @Throws(IOException::class)
    private fun createImageFile(): File? {
        @SuppressLint("SimpleDateFormat") val imageFileName =
                SimpleDateFormat("yyMMdd_HHmmss").format(Date())
        val directoryImage =
                File(Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DCIM), "")
        val fileImage: File = File.createTempFile(imageFileName, ".jpg", directoryImage)
        cameraFilePath = fileImage.getAbsolutePath()
        return fileImage
    }

    private fun convertImage(urlImg: String) {
        val imgFile = File(urlImg)
        if (imgFile.exists()) {
            val cekSize: Long = imgFile.length()
            val options = BitmapFactory.Options()
            if (cekSize > 1000000) options.inSampleSize = 4 else options.inSampleSize = 0
            val bitmap = BitmapFactory.decodeFile(cameraFilePath, options)
            val baos = ByteArrayOutputStream()
            bitmap.compress(Bitmap.CompressFormat.JPEG, 100, baos)
            Glide.with(this)
                    .load(bitmap)
                    .diskCacheStrategy(DiskCacheStrategy.ALL)
                    .placeholder(android.R.drawable.ic_menu_gallery)
                    .into(binding.imageUpload)
            imageBytes = baos.toByteArray()
        }
    }

    //======================================= upload image

    private fun upload(){
        if (imageBytes == null || imageBytes!!.isEmpty()){
            Toast.makeText(this, "Pilih foto dulu sebelum upload", Toast.LENGTH_SHORT).show()
        }

        else {
            val mProgress = ProgressDialog(this)
            mProgress.setTitle("Mohon tunggu")
            mProgress.setCancelable(false)
            mProgress.setMessage("Sedang upload foto")
            mProgress.show()

            val baseImg: String = Base64.encodeToString(imageBytes, Base64.DEFAULT)
            Api.client.upload(
                100,
                baseImg, object : Callback<UploadResponse?> {
                    override fun success(signUpResponse: UploadResponse?, response: Response?){
                        mProgress.dismiss()
                        Toast.makeText(this@MainActivity, "sukses upload", Toast.LENGTH_LONG).show()
                    }

                    override fun failure(error: RetrofitError){
                        Toast.makeText(this@MainActivity, error.toString(), Toast.LENGTH_LONG).show()
                        mProgress.dismiss()
                    }
                })
        }

    }



}