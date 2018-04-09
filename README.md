# Python_Port_Scanner
A Port Scanner programmed in Python 3.6. This is a Network Recon tool, and its purpose is to find weak access points on a server/host. The program asks for a target, and whether the user wishes to see closed ports. After user input, the program probes the target server or host for open ports. 

<h1>DISCLAIMER</h1>
This program is for educational/research purposes only. The author takes no responsibility and/or liability for how an individual chooses to use any of the source files provided. The author will not be liable for any losses and/or damages in connection to the use of the program and its provided files.


<hr />

<h2>Creating the Executable:</h2>
When creating the executable file you want to use the python module, <b>pyinstaller</b>. This allows the program to be ran anywhere. The first thing required is the pyinstaller module, so install it using pip:

<div style="background: #000000; color: #00ff00; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
<pre style="margin: 0;">
pip install pyinstaller
</pre>
</div>

Then type the following command on your windows command prompt to create the executable:
<div style="background: #000000; color: #00ff00; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
<pre style="margin: 0;">
pyinstaller -F name_of_python_script.py
</pre>
</div>

The -F input ensures that the executable is a single file that includes everything, rather then a folder. Once that's done navigate to the <b>dist</b> folder within the folder of your newly created python script, and grab the exe file.

The file is now created.
