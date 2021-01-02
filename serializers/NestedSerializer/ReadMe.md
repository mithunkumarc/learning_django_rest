NestedSerializer: instead of showing only primary key id of linked record, whole object is shown

example : 
          
          instead of showing only song id, like this
          
          {
            "name" : "sonu nigam",
            "sung" : 1 # song id
          }
          
          whole song object is shown
          
          {
            "name" : "sonu nigam",
            "sung" : {
                "title" : "tanhayee",
                "duration" : 4,
                "id" : 1
            }
          }
          
          
          
           
