package com.dicoding.watcherapplication.core.ui

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import com.dicoding.watcherapplication.R
import com.dicoding.watcherapplication.core.domain.model.Student
import com.dicoding.watcherapplication.databinding.ItemListBinding

class StudentViewAdapter : RecyclerView.Adapter<StudentViewAdapter.ListViewAdapter>() {

    private val listData = ArrayList<Student>()
    var onItemClick: ((Student) -> Unit)? = null

    fun setData(newListData: List<Student>?) {
        if(newListData == null) return
        listData.clear()
        listData.addAll(newListData)
        notifyDataSetChanged()
    }

    inner class ListViewAdapter(itemView: View) : RecyclerView.ViewHolder(itemView) {
        private val binding = ItemListBinding.bind(itemView)
        fun bind(data: Student) {
            with(binding) {
                Glide.with(itemView.context)
                    .load(data.image)
                    .into(imageStudent)

                textStudentName.text = data.name

                textStudentStatusPercentage.text = data.percentage
            }
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int) =
        ListViewAdapter(LayoutInflater.from(parent.context).inflate(R.layout.item_list, parent, false))

    override fun onBindViewHolder(holder: ListViewAdapter, position: Int) {
        val data = listData[position]
        holder.bind(data)
    }

    override fun getItemCount(): Int = listData.size
}