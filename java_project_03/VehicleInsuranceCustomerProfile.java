package portfolio_2021_11_05.java_project_03;

import java.util.Random;

public class VehicleInsuranceCustomerProfile implements CustomerProfile{

    public boolean isLoyalCustomer() {
        return new Random().nextBoolean();
    }

}
