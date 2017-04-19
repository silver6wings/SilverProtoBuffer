package com.silver6wings.silverprotobufferdemo;

import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;

import com.silver6wings.HelloDemoProvider;
import com.silver6wings.MyHello;
import com.silver6wings.protobuffer.SilverProtoManager;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        String simulatorLocalURL = "http://10.0.2.2:8080";
        SilverProtoManager.getInstance().setBaseServerURL(simulatorLocalURL);

        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

//                HelloDemoProvider.helloGet(
//                        getApplicationContext(),
//                        "ABC",
//                        123,
//                        new HelloDemoProvider.HelloResponseHandler() {
//                            @Override
//                            public void onResponse(MyHello.HelloResponse response, int responseCode, int httpCode, Throwable throwable) {
//                                if (responseCode == SilverProtoManager.ResponseCodeSuccess) {
//                                    Log.i("SilverProtobufferDemo", "Response:" + response.getContent());
//                                }
//                                else
//                                {
//                                    Log.i("SilverProtobufferDemo", "Response: Not success");
//
//                                }
//                            }
//                        });

                HelloDemoProvider.helloPost(
                        getApplicationContext(),
                        MyHello.HelloRequest.newBuilder().setBar("asdf").setFoo("qwer").setID(123),
                        new HelloDemoProvider.HelloResponseHandler() {
                            @Override
                            public void onResponse(MyHello.HelloResponse response, int responseCode, int httpCode, Throwable throwable) {
                                if (responseCode == SilverProtoManager.ResponseCodeSuccess) {
                                    Log.i("SilverProtobufferDemo", "Response:" + response.getContent());
                                }
                                else
                                {
                                    Log.i("SilverProtobufferDemo", "Response: Not success");

                                }
                            }
                        }
                );
            }
        });
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
