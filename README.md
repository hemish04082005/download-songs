# download-songs
This script would download the song(s) for you. You need to create a file (songs.txt) and place it in a folder which is the same folder in which the script is placed. Even if you don't create a songs.txt file, it would tell you that songs.txt file is not present and a window would popup to manually select the file which contains the list of songs to be downloaded.

(I assume that the songs rank top on youtube when given the names that you have mentioned in the list. If there may be duplicate songs, consider writing keywords with songname like if you want to search the song Closer, you may type "Closer chainsmokers".)

Note: The script requires Python3 and is not supported for Python2

Just fulfill the pip requirements given in requirements.txt and run the script (first copy the script into folder in which you want to download songs and run the script of that folder) (making sure that you have the list of songs in songs.txt file) Make sure that you have active Internet Connection otherwise the script would show you "No Internet Connection" and would exit itself. After that, it would ask you for quality levels. 5 quality levels are provided. High quality levels lead to large file sizes and vice-versa. You need to enter the quality levels in form of number( like 1, 2, 3, 4, 5 ; they would be asked by the script), type the desired quality level number and press enter. Then, automatic processing would be done. If any song(s) could not be downloaded by the script it would show "Failed" after the song and the name of that song would be copied to templog.txt (this file would be created in the folder in which you are running the script if there are any fails). Then, it would ask you whether to empty out the text file in which list of songs is stored, so that songs are not downloaded when you run the script next time. You may press y or n (not case sensitive) and then press enter. "y" refers to Yes and "n" refers to No.

# Extra information for Android Termux Environment
If you are running this in android termux environment, you should remove code started with comments (there are two places in where such comments are there, just copy this text and find):
 # ---------should be removed for android termux-start------------
and ending with
 # ---------should be removed for android termux-end------------
as tkinter is not supported for Android Termux. So, the result would be that if you don't place songs.txt in same folder, the script would not work and thus would exit itself and it would not ask you to specify the location by selection as in the case of windows or linux or mac.

# Instructions for running release binaries
The release binaries provided are packaged through pyinstaller module.

The Windows binary is packaged under 32-bit Windows XP environment to retain maximum compatibility and thus is compatible with Windows XP 64-bit, Windows Vista, 7, 8 , 8.1 both 32 bit and 64 bit 
To run the file in Windows, just double click the download-songs.exe file and it would run in console.

For Linux:
I don't have 32 bit environment for Linux. The binary provided is only for 64 bit environment and tested on Ubuntu 18.04 LTS. It would work on Debian Buster, Ubuntu 20.04 LTS, Linux Mint 19 and 20, Zorin OS 15 and Zorin OS 15 Lite. It may also work on RHEL based distributions, but is not tested. You may contribute by packaging the script in 32 bit environment and testing for RHEL based distros.

To run the binary, open the terminal in directory containing the downloaded binary and run the binary like this:
./download-songsx64

# Disclaimer
This script does not promote the downloading of copyright content. This is solely for educational purposes for learning web scrapping by python. I am not responsible for any piracy.