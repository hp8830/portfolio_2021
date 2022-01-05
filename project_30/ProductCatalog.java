package project_30;

public class ProductCatalog {

    public void listAllProducts() {
        
        ProductRepository productRepository = ProductFactory.create();

        productRepository.getAllProductNames();
        //List all products here
    }
    
}
