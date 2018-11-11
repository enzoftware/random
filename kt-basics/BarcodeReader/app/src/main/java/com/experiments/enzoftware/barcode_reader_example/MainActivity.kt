package com.experiments.enzoftware.barcode_reader_example

import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.util.SparseArray
import com.google.android.gms.vision.Frame
import com.google.android.gms.vision.barcode.Barcode
import com.google.android.gms.vision.barcode.BarcodeDetector
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val myBitmap : Bitmap = BitmapFactory.decodeResource(applicationContext.resources,R.drawable.codig)
        imgview.setImageBitmap(myBitmap)

        button.setOnClickListener {

            val detector = BarcodeDetector.Builder(applicationContext)
                    .setBarcodeFormats(Barcode.ALL_FORMATS)
                    .build()
            if (!detector.isOperational){
                txtContent.text = "Could not setup the detector"
            }

            val frame = Frame.Builder().setBitmap(myBitmap).build()
            val barcodeList : SparseArray<Barcode> = detector.detect(frame)
            Log.i("barcode",barcodeList.size().toString())
            val thisCode = barcodeList.valueAt(0)
            txtContent.text = thisCode.rawValue
        }
    }
}
