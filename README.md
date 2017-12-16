# CrackPassword

This is a python command line tool that tries to crack encrypted passwords in a shadow file through a brute force approach. 

The program accomplishes this in two ways 

## Dictionary lookup
   This will try all the all of the passwords found in the myspace-withcount.txt
   
   To run this command type:
        
        python crack.py dictionarycrack [shadow file]  myspace-withcount.txt
   
   dictionary file is large so may take a while.

 
## ASCII Permutations
  This will try combinations of ascii characters "abc..ABC...123...!@#" etc
  
  To run:
      
      python crack.py permcrack  [shadowfile]  [suspected length of passord]
    
  Note: as there are many possible combinations may also take a while.
