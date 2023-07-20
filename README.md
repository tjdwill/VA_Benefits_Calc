# VA Benefits Calculator
VA Benefits Calculator is a command-line program that allows the user to estimate the extent of their VA coverage or experiment to see what coverage a given combination produces.

---

### Disclaimer

The VA Benefits Calculator is not affiliated with the U.S. Department of Veterans Affairs and is intended for **educational purposes only**. Any estimate displayed is unofficial and should not be construed as an official result.

---

## How to Use

### Click-and-Go
If you want to double-click and go, the EXE version of the program is available. Simply download it and run the program.
The EXE was generated directly from the script using `auto-py-to-exe`.

### Running the Script
To use the program using a Python interpreter, run the script from the command-line (this was programmed using Python 3.11).
After changing into the directory containing the script, simply run:
```
> python vaCalc.py
```
and calculate away. As this program was created on a Windows machine, if you are on a Linux platform and wish to make the script executable directly, 
you may need to let the computer know to use Unix's newline pattern (no carriage returns). To do so, do the following:

1. Open the program in VIM
  ```console
    $ vim <some path>/vaCalc.py
  ```
2. Set the file format to Unix `:set ff=unix`
  * You can see what the current format is by `:set ff?`
3. Save the file and exit (`:x` or `:wq`)
4. Make the script executable
```console
  $ chmod +x <some path>/vaCalc.py
```

You should be able to run it from there. 


