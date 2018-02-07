<!--- 20180206AnswersFirstLab1CARMandGAEB first feedback  -->
# **COMPUTER VISION - FIRST LAB 1**

Students: 

Carlos Andrés Rivera Morales

Gabriel Andrés Espinosa Barrios

## 1.  What is the ``grep`` command?

Grep processes text line by line and prints which match with a certain pattern. ``grep`` GREP is a general function command in terminalin a computer that allow searching plain-text data sets for lines that match a regular expression.

The founder aoutor of this command is [Kenneth Lane "Ken" Thompson](http://www.computerhistory.org/fellowawards/hall/ken-thompson/).


The general expression to use it is:

```grep [_OPTIONS_] _PATTERN_ [_FILE_...]```

![201802061Grep.png](https://fthmb.tqn.com/w64NmuHYjNFk_KSG6MJnu5VHkvQ=/768x0/filters:no_upscale()/grep-56b1ea713df78cdfa00329f4.png)

Figure 1. Git ``grep`` Definiton.


For instance,  If you want to search the phrase &quot;Hola Mundo&quot; in a file whose name is prueba.txt you have to write:

grep &quot;Hola Mundo&quot; prueba.txt

This command will return to you the lines where is the pattern.


![201802062Grep.png](https://github.com/ComputerVisionUniandes/IBIO4680/blob/master/01-Linux/Answers/ImagesLab1/201802061.png)

Figure 2. Git ``grep`` example use.

Grep has several options, such as:  color what highlights the pattern in each line, n, that will prefix  each matching line with its respective line number. There are other several commands in the documentation.


## 2. What is the meaning of ``#! /bin/bash`` at the start of scripts?

``#! /bin/bash`` Bin/Bash command is the the first line in the start of the scripts, meaning that the script should always be run with bash, rather than another shell. It allow what program will going to interpret the script when it pass to executed.

![201802061BinBash.png](https://www.howtogeek.com/wp-content/uploads/2016/07/ximg_577afca4b621d.png.pagespeed.gp+jp+jw+pj+ws+js+rj+rp+rw+ri+cp+md.ic.QmMEOwvkd2.png)

Figure 3. Standard example of the use of ``#! /bin/bash`` .

This line indicates which program must interpret the script. this sequence of characters is called **shebang**

** **

## 3. How many users exist in the course server?
Initial users of service.

![p2](ImagesLab1/p2.png)

Figure 4. Number of users.

To count the numbers of users in the server we can use:

cut -d: -f1 /etc/passwd

In the case of the course server we have the next users:



To count the number of lines returned in the command we can use:

```wc -l```



In this way the command final command returns:


![p3](ImagesLab1/p3.png)

Figure 5. Course server users.


However, formal users for the curse in our server at only nine (9).

![201802062Users.png](https://github.com/ComputerVisionUniandes/IBIO4680/blob/master/01-Linux/Answers/ImagesLab1/201802062.png)

Figure 6. Formal login users.


## 4. What command will produce a table of Users and Shells sorted by shell (tip: using ``cut`` and ``sort``)


![p4](ImagesLab1/p4.png)

The command used was compposed of several parts:

Cut: This command is used to process text.

Sort: Sorts text according to some column, in this case the second one.

Expand: With this command we can give some format to the output.



## 5. Create a script for finding duplicate images based on their content (tip: hash or checksum) You may look in the internet for ideas, Do not forget to include the source of any code you use.


![p5](ImagesLab1/p5.png)


![p6](ImagesLab1/p6.png)

```


#!/bin/bash

images=$(find .  -iname "*.tiff") # We search for the images with .tiff extension

dataImages=$(for im in ${images[*]}; do cksum $im  | cut -d" " -f1,3; done | sort) # We generated the checksum value

repeated=$(for im in ${images[*]}; do cksum $im  | cut -d" " -f1; done | sort -k1 | uniq -d) # We are searching for the files that have  repeated the checksum 


for im in ${repeated[*]}; do printf '%s\n' "${dataImages[@]}" | grep $im; done # we selected each checksum repeated and we filtered by them.


```

## 6. Download the [*bsds500*](https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/resources.html#bsds500) image segmentation database and decompress it (keep it in you hard drive, we will come back over this data in a few weeks).


![p7](ImagesLab1/p7.png)


The files were downloaded from:

https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/resources.html#bsds500

## 7. What is the disk size of the uncompressed dataset, How many images are in the directory 'BSR/BSDS500/data/images'?


![p8](ImagesLab1/p8.png)

The size of the directory is 72M.


![p9](ImagesLab1/p9.png)

The number of images in the folder are 505.

## 8. What is their resolution, what is their format?

Using  imageMagick we can

![p10](ImagesLab1/p10.png)

 Their format is JPEG and ther resolution is 481x321 or 321x481 depending if the image is in landscape or portrait.

## 9. How many of them are in *landscape* orientation (opposed to *portrait*)?


![p11](ImagesLab1/p11.png)

Using image Magick we can know the size of each image, with find we can detect each .jpg image, .

Using this we determined that there are 351 landscape and 154 portrait images.

## 10. Crop all images to make them square (256x256). Tip: do not forget about  [imagemagick](http://www.imagemagick.org/script/index.php).

To crop all images to (256x256) we first select using find all images in the directory BSR, afterwords using imageMagick with the command convert -crop we cropped them all.

Here, you can see the commands used.

![p12](ImagesLab1/p12.png)

```
 images=$(find ./BSRcopia -type f -name \*.gif -o -name \*.jpg) #here we select all images

for im in ${images[\*]}; do basefilename=$(basename $im); convert -crop 256x256+0+0 $im ./croppedImages/$basefilename; done  #Here we cropped the selected images.

```

In the next image we can observe that the size of each image is 256x256.


![p13](ImagesLab1/p13.png)

References

[https://www.thegeekstuff.com/2013/06/cut-command-examples/](https://www.thegeekstuff.com/2013/06/cut-command-examples/)

[https://www.tecmint.com/sort-command-linux/](https://www.tecmint.com/sort-command-linux/)

https://www.computerhope.com/unix/ucksum.htm

[https://www.imagemagick.org/script/identify.php](https://www.imagemagick.org/script/identify.php)

[https://stackoverflow.com/questions/10124314/grab-the-filename-in-unix-out-of-full-path](https://stackoverflow.com/questions/10124314/grab-the-filename-in-unix-out-of-full-path)

[https://www.imagemagick.org/discourse-server/viewtopic.php?t=17339](https://www.imagemagick.org/discourse-server/viewtopic.php?t=17339)




