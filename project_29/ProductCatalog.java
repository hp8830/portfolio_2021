package project_29;

import java.util.List;

public class ProductCatalog {
    
    private ProductRepository productRepository;
    
    public ProductCatalog(ProductRepository productRepository) {
        this.productRepository = productRepository;
    }

    public void listAllProducts() {
      
        List<String> allProductNames = 
        productRepository.getAllProductNames();

        //Display product names
    }
    
}
