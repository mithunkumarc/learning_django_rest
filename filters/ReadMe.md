
search filter : wildcards   

1. to search starts with letter : use ^

        search_fields= ['^name',]
    
        url?search=r

2. to search exact matches

        search_fields = ['=name']
  
  
3. full text search : not supported in post grey?

        search_fields = ['@name']
  
4. Regex search : $ :  need to explore  
