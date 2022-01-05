package portfolio_2021_11_05.java_project_03;

public class InsurancePremiumDiscountCalculator {

    public int calculatePremiemDiscountPercent(CustomerProfile customer) {
        if (customer.isLoyalCustomer()) {
            return 20;
        }
        return 0;
    }
    
}
