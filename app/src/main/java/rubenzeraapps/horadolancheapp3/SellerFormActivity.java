package rubenzeraapps.horadolancheapp3;

import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class SellerFormActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_seller_form);

        EditText login = (EditText) findViewById(R.id.login);
        EditText password = (EditText) findViewById(R.id.password);
        EditText email = (EditText) findViewById(R.id.email);

        Button submit = (Button) findViewById(R.id.submitBtn);

        submit.setOnClickListener(new View.OnClickListener(){
            public void onClick(View v){
                Toast.makeText(SellerFormActivity.this,"Tentando cadastrar", Toast.LENGTH_LONG).show();
                HTTPClient sh = new HTTPClient();
                // Making a request to url and getting response
                String url = "http://127.0.0.1:5000/sellers";
                String jsonStr = sh.makePostCall(url);
                Toast.makeText(SellerFormActivity.this, jsonStr, Toast.LENGTH_LONG).show();
            }
        });

    }
}
