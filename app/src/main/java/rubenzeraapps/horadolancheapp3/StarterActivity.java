package rubenzeraapps.horadolancheapp3;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.content.Intent;

public class StarterActivity extends AppCompatActivity {


    public void userOption(View view){
        Intent it = new Intent(StarterActivity.this, MappingActivity.class);
        startActivity(it);
    }

    public void sellerOption(View view){
        Intent it = new Intent(StarterActivity.this, SellerFormActivity.class);
        startActivity(it);
    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_starter);

    }
}
