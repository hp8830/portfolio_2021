package portfolio_2021_11_05.java_project_02;

public class InsurancePremiumDiscountCalculator {
    
    public int 
    calculatePremiumDiscountPercent(CustomerProfile customer)
    {
        if (customer.isLoyalCustomer()) {
                  return 20;
        }
        return 0;
    }

}
