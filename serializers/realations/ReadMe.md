serializer relations : 

        serializers return related info(two or more tables) to user.
        generally foreign key/linked information shown as id.
        serializer relation help to include more information of linked table.
        
####ex : singer object contains song objects

#### without serializer relation

        {
          id : 1,
          singer: "jayashree",
          song: [
            1,        # these are song ids
            2,
            3
          ]
        }
        
####  with serializer relation
        
        {
          id : 1,
          singer: "jayashree",
          song: [
            "car car",        # these are song titles
            "oora kannu",
            "sukumara"
          ]
        }
        
        instead of title you can present url hyper links too

1. Relational fields are used to represent model relationships. 

2. They can be applied to ForeignKey, ManyToManyField and OneToOneField relationships,as well as to reverse relationships, 
and custom relationships such as GenericForeignKey.


