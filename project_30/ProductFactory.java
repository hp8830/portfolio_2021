package project_30;

public class ProductFactory {

    public static ProductRepository create() {
        return new SQLProductRepository();
    }
    
}
