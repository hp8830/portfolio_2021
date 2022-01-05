package project_30;

import java.util.Arrays;
import java.util.List;

import project_29.ProductRepository;

public class SQLProductRepository implements ProductRepository{
    
    public List<String> getAllProductNames() {

        return Arrays.asList("soap", "toothpaste");
    }
}
