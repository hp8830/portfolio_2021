package portfolio_2021_11_05.java_project_01;
public class Employee {
    private String employeeId;
    private String employeeName;
    private String employeeAddress;
    private String contactNumber;
    private String employeeType;

    // TO FOLLOW THE REASON FOR CHANGE FOR SINGLE RESPONSIBILITY PRINCPLES HAS BEEN MOVED TO ITS OWN CLASS EmployeeRepository.java
    public void save() {
       new EmployeeRepository().save(this);
    }

    // TO FOLLOW THE REASON FOR CHANGE FOR SINGLE RESPONSIBILITY PRINCPLES HAS BEEN MOVED TO ITS OWN CLASS EmployeeRepository.java
    // Calculates the tax based on the employee Types
    public void calculateTax() {
        new TaxCalculator().calculateTax(this);
    }

    public String getEmployeeId() {
        return employeeId;
    }

    public void setEmployeeId(String employeeId) {
        this.employeeId = employeeId;
    }

    public String getEmployeeName() {
        return employeeName;
    }

    public void setEmployeeName(String employeeName) {
        this.employeeName = employeeName;
    }

    public String getEmployeeAddress() {
        return employeeAddress;
    }

    public void setEmployeeAddress(String employeeAddress) {
        this.employeeAddress = employeeAddress;
    }

    public String getContactNumber() {
        return contactNumber;
    }

    public void setContactNumber(String contactNumber) {
        this.contactNumber = contactNumber;
    }

    public String getEmployeeType() {
        return employeeType;
    }

    public void setEmployeeType(String employeeType) {
        this.employeeType = employeeType;
    }


}


//Reasons to change; 1. Changes in Employee Attributes; 2. Changes in Database; 3. Changes in Tax Calculation 