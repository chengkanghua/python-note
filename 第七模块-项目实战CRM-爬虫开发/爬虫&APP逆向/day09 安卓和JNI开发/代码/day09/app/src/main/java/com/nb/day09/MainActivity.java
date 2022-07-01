package com.nb.day09;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    // Used to load the 'native-lib' library on application startup.
    static {
        System.loadLibrary("native-lib");
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Example of a call to a native method
        TextView tv = findViewById(R.id.sample_text);
        tv.setText(stringFromJNI());


        int v1 = encryptUtils.add(1, 2);
        String v2 = encryptUtils.sign("xxxxx");

        Log.e("encryptUtils.add====", String.valueOf(v1));
        Log.e("encryptUtils.sign====", v2);

        int v3 = DynamicUtils.add(100,200);
        Log.e("DynamicUtils.add====", String.valueOf(v3));
    }

    /**
     * A native method that is implemented by the 'native-lib' native library,
     * which is packaged with this application.
     */
    public native String stringFromJNI();
}