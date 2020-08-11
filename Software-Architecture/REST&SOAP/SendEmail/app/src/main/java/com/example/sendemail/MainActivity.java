package com.example.sendemail;

import androidx.appcompat.app.AppCompatActivity;

import android.os.AsyncTask;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    Button soap;
    Button rest;
    Button email;

    EditText url1;
    EditText url2;
    EditText url3;
    EditText title;
    EditText payload;

    TextView returnmessage;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        init();
    }

    public void init()
    {
        soap = (Button)findViewById(R.id.soap);
        rest = (Button)findViewById(R.id.rest);
        email = (Button)findViewById(R.id.email);
        url1 = (EditText)findViewById(R.id.url1);
        url2 = (EditText)findViewById(R.id.url2);
        url3 = (EditText)findViewById(R.id.url3);
        title = (EditText)findViewById(R.id.title);
        payload = (EditText)findViewById(R.id.payload);

        returnmessage = (TextView)findViewById(R.id.returnmessage);


        rest.setOnClickListener(new View.OnClickListener() {
        @Override
        public void onClick(View v) {
             class SendEmail extends AsyncTask<String,String,String> {
                protected String doInBackground(String... lalala) {
                    String _url = lalala[0];
                    String _title = lalala[1];
                    String _payload = lalala[2];
                    WebServicesClient s = new WebServicesClient();
                    System.out.println(_url);
                    s.SetParameter(_url,_title,_payload);
                    try {
                        return s.RestRequest();
                    } catch (Exception e) {
                        e.printStackTrace();
                        return "NO";
                    }

                }

                protected void onPostExecute(String result) {
                    returnmessage.setText(result);
                    System.out.print(result);
                }
            }

            System.out.println("点进来了");
            String _url = url1.getText().toString()+","+url2.getText().toString()+","+url3.getText().toString();
            String _title = title.getText().toString();
            String _payload = payload.getText().toString();
            List<String> a = new ArrayList<>();
            a.add(_url);a.add(_title );a.add(_payload );

            new SendEmail().execute(_url,_title,_payload);
        }
            });

        soap.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                class SendEmail extends AsyncTask<String,String,String> {
                    protected String doInBackground(String... lalala) {
                        String _url = lalala[0];
                        String _title = lalala[1];
                        String _payload = lalala[2];
                        WebServicesClient s = new WebServicesClient();
                        System.out.println(_url);
                        s.SetParameter(_url,_title,_payload);
                        try {
                           return s.SoapRequest();
                        } catch (Exception e) {

                            e.printStackTrace();
                            return "NO";
                        }

                    }

                    protected void onPostExecute(String result) {
                        returnmessage.setText(result);System.out.print(result);
                    }
                }

                System.out.println("点进来了");
                String _url = url1.getText().toString()+","+url2.getText().toString()+","+url3.getText().toString();
                String _title = title.getText().toString();
                String _payload = payload.getText().toString();
                List<String> a = new ArrayList<>();
                a.add(_url);a.add(_title );a.add(_payload );

                new SendEmail().execute(_url,_title,_payload);
            }
        });

        email.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                class SendEmail extends AsyncTask<String,String,String> {
                    protected String doInBackground(String... lalala) {
                        String _url = lalala[0];
                        WebServicesClient s = new WebServicesClient();
                        System.out.println(_url);
                        s.SetUrl(_url);
                        try {
                            return s.EmailRequest();

                        } catch (Exception e) {

                            e.printStackTrace();
                            return "NO";
                        }

                    }

                    protected void onPostExecute(String result) {
                        returnmessage.setText(result);System.out.print(result);
                    }
                }

                System.out.println("点进来了");
                String _url = url1.getText().toString()+","+url2.getText().toString()+","+url3.getText().toString();
                List<String> a = new ArrayList<>();
                a.add(_url);

                new SendEmail().execute(_url);
            }
        });

    }

}
