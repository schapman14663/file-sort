# FILE SORT
A short program to sort files from my downloads folder into other folders in my home directory. 

19 Sep 26
This should be a pretty short project, but I should also make notes.
At the moment, I wake up very early in the morning to go to the gym
and then I work a fairly normal 9 - 5 style shift with the exception
that its the busiest time of year for us and so I'm actually working
a significant amount of overtime. 

As a result, it may take a few days for this to be written since I
don't have tons of time on my hands. I'm mainly trying to keep the
problem solving gears in my brain moving, as well as practicing 
documentation and explaining my decisions.

For some reason my initial thought was going to be some kind of string
split operation since file extensions are typically in the form of 
".abc" but this very quickly stopped being possible as I realised that some of my files will end up being ".tar.gz" so that's not an
option, it probably wasn't the best option to begin with so that's fine.

I do currently getting the list of files in a directory sorted, next
step is to make a way to get the file extensions. I also need to
implement a list of destination directories, as well as consider
some way to differentiate a document from a book even if they may
use the same file type (.pdf documents for example) but this is 
likely to be a case of me needing to rename files to mark them as 
books and documents and then sorting them that way.


