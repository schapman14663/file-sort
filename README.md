# FILE SORT
A short program to sort files from my downloads folder into other folders in my home directory. 

## 19 Sep 26
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

## 20 Sep 2026
Okay so I basically have this done. I got a working version made but
it had more nesting than I like, so I removed part of that nesting 
into a move_file function. It's not perfectly finished because I
should still implement an error handling procedure to prompt me to
update the dictionary that contains the directories and file
extensions when I have a file that isn't already there so can't be
sorted. 

## 21 Sep 2026
It occurs to me that I could list the Downloads directory again to
check if the file has actually moved. So I've implemented that 
functionality. This should allow me to, as above, get notified if
I need to update the script.

I have also updated the script to use to not deprecated subprocess 
module, and to use a scandir() method so I can skip directories,
which I will continue to sort manually. 

So for now, I can consider this project done.
