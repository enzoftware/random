package com.androidtutz.anushka.findtheday;

import android.net.Uri;
import android.os.Bundle;
import android.support.v4.app.FragmentManager;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity implements DayFragment.OnFragmentInteractionListener {

    private EditText enteredValue;
    private Button viewButton;
    private int input;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        enteredValue = (EditText) findViewById(R.id.etIndex);
        viewButton = (Button) findViewById(R.id.btnView);


        viewButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {


                if (!enteredValue.getText().toString().equals("")) {


                    input = Integer.parseInt(enteredValue.getText().toString());


                    FragmentManager fragmentManager = getSupportFragmentManager();
                    DayFragment dayFragment = DayFragment.newInstance(input);
                    dayFragment.show(fragmentManager, "Sample Fragment");


                }

            }
        });


    }

    @Override
    public void onFragmentInteraction(Uri uri) {

    }
}
