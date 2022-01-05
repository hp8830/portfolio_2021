package project_29;

public class EcommerceMainApplication {

    public static void main(String[] args) {

        ProductRepository productRepository = 
        ProductFactory.create();

        ProductCatalog productCatalog = new 
        ProductCatalog(productRepository);

        productCatalog.listAllProducts();
    }
    
}
