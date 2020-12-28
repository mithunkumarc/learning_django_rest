#### Automatic primary key : 

By default, Django gives each model the following field:


        id = models.AutoField(primary_key=True)

This is an auto-incrementing primary key.

If you’d like to specify a custom primary key, specify primary_key=True on one of your fields.   
If Django sees you’ve explicitly set Field.primary_key, it won’t add the automatic id column.  
Each model requires exactly one field to have primary_key=True (either explicitly declared or automatically added).  
