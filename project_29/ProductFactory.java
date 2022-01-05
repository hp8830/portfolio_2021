package project_29;

public class ProductFactory {

    public static ProductRepository create() {
        return new SQLProductRepository();
    }
    
}
