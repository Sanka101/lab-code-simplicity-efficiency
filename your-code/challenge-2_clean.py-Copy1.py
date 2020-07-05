{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Random string generator"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "\"\"\"\n",
    "The code below generates a given number of random strings that consists of numbers and \n",
    "lower case English letters. You can also define the range of the variable lengths of\n",
    "the strings being generated.\n",
    "\n",
    "The code is functional but has a lot of room for improvement. Use what you have learned\n",
    "about simple and efficient code, refactor the code.\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# First step, divide function and execution of code into different cells"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Instead of writing entire alphabet use string.acii method\n",
    "\n",
    "import string\n",
    "alphabet= list(string.ascii_lowercase)\n",
    "\n",
    "# Instead of writing 0-9, create list with sequence\n",
    "# second step convert to strings\n",
    "\n",
    "numbers= list(range(0,10))\n",
    "numbers\n",
    "strnums = [str(num) for num in numbers]\n",
    "strnums\n",
    "\n",
    "# Add both lists\n",
    "a_total= alphabet + strnums"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "# This function is developed to return random strings\n",
    "\n",
    "def RandomStringGenerator(l=12, a= a_total):\n",
    "    p = 0\n",
    "    s = ''\n",
    "    while p<l:\n",
    "        import random\n",
    "        s += random.choice(a)\n",
    "        p += 1\n",
    "    return s\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def BatchStringGenerator(n, a=8, b=12):\n",
    "    r = []\n",
    "    for i in range(n):\n",
    "        c = None\n",
    "        if a < b:\n",
    "            import random\n",
    "            c = random.choice(range(a, b))\n",
    "        elif a == b:\n",
    "            c = a\n",
    "        else:\n",
    "            import sys\n",
    "            sys.exit('Incorrect min and max string lengths. Try again.')\n",
    "        r.append(RandomStringGenerator(c))\n",
    "    return r"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "# If input is wrong you will notice only until execution\n",
    "# Therefore we introduce a while loop that repeats until correct input\n",
    "\n",
    "# I will create a function for all the inputs\n",
    "# Because that function will \"correct\" possbile wrong inputs\n",
    "\n",
    "def minimum_length():\n",
    "    try:\n",
    "# Only integer input and greater than zero is correct\n",
    "        a = int(input('Enter minimum string length: '))\n",
    "        while a < 0:\n",
    "            a = int(input('Enter minimum string length: '))\n",
    "    except:\n",
    "        print(\"You cant choose that\")\n",
    "        # Ask again\n",
    "        minimum_length()\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def maximum_length():\n",
    "    try:\n",
    "# Only integer input and greater than zero is correct\n",
    "        b = int(input('Enter maximum string length: '))\n",
    "        while b < 0:\n",
    "            b = int(input('Enter maximum string length: '))\n",
    "    except:\n",
    "        print(\"You can't choose that\")\n",
    "        # Ask again\n",
    "        maximum_length()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def total_strings():\n",
    "    try:\n",
    "# Only integer input and greater than zero is correct\n",
    "        n = int(input('How many random strings to generate? '))\n",
    "        while n < 0:\n",
    "            n = int(input('How many random strings to generate? '))\n",
    "    except:\n",
    "        print(\"You cant choose that\")\n",
    "        # Ask again\n",
    "        total_strings()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter minimum string length: fd\n",
      "You cant choose that\n",
      "Enter minimum string length: 2\n",
      "Enter maximum string length: fda\n",
      "You can't choose that\n",
      "Enter maximum string length: 4\n",
      "How many random strings to generate? dsaf\n",
      "You cant choose that\n",
      "How many random strings to generate? 2\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "'NoneType' object cannot be interpreted as an integer",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-7-6d515878727d>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mn\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mtotal_strings\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mBatchStringGenerator\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mn\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0ma\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mb\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-3-0116405d08d2>\u001b[0m in \u001b[0;36mBatchStringGenerator\u001b[1;34m(n, a, b)\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mBatchStringGenerator\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mn\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0ma\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m8\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mb\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m12\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m     \u001b[0mr\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m     \u001b[1;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mn\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m         \u001b[0mc\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0ma\u001b[0m \u001b[1;33m<\u001b[0m \u001b[0mb\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: 'NoneType' object cannot be interpreted as an integer"
     ]
    }
   ],
   "source": [
    "a = minimum_length()\n",
    "b = maximum_length()\n",
    "n = total_strings()\n",
    "\n",
    "print(BatchStringGenerator(n, a, b))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
