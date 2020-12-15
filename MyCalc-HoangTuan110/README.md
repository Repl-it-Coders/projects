# MyCalc
A simple calculator made by me. Can calculate up to whatever numbers you want!

# Getting started
Just basically clone this:
```sh
git clone https://github.com/Repl-it-Coders/MyCalc
```

Then, `cd` to the directory:
```sh
cd mycalc
# Or:
cd MyCalc
```

And finally, run the `main.py` file to test it(Make sure you have Python 3):
```sh
python3 main.py
```
You should see `50.0` at the output.

If you want to try other calculations, first, edit the file with your favourite text editor/IDE. Then, on 3 final lines:
```py
code = "100 / 2"
mylang = MyLang()
mylang.parse(code)
```

Edit the `code` value to something like:
```py
code = "200 / 2"
```

Run the file again, and you should see the result of your calculator!

# Problem
The only problem with this calculator so far is the unbalance of how it cuts down the left, right and operator (when you calculate up to more than 2 numbers). For example:
```
100 / 2 + 2
```

That should be `52.0`, but the calculator outputs `25.0`.

On that expression, the calculator calculates somewhat like this:
```
Left is 100
Right is 2 + 2 = 4
Operator is /
-------------
Result: 100 / 4 = 25.0
```

While in correct way, it should be:
```
Left is 100 / 2 = 50.0
Right is 2
Operator is +
-------------
Result: 50.0 + 2 = 52.0
```

I still have no idea how to fix this, but maybe in the future, I will find it!

# License
This is in the MIT license.
