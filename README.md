# Smart Calculator

This is my Smart Calculator project, built for the Stardance Hack Club challenge.

## About

A calculator I originally coded in Python, then turned into a web app. The currency conversion side is meant to help tourists exchange currencies easily, without needing to search for and download a separate app. It handles basic math, plus square root, absolute value, and number inverse, along with currency conversion between USD, EUR, GBP, and QAR.

## Features

- Basic math operations (addition, subtraction, multiplication, division)
- Absolute value of a number
- Square root of a number
- Number inverse (additive inverse)
- Currency converter for a set of common currencies
- Note: the Python version also keeps a history of past calculations, which isn't currently on the website version

## Currency Rates Note

The exchange rates used in this calculator are static values (checked and corrected as of late July 2026), not a live feed. That means they will slowly go out of date. If you're using this for anything beyond a demo, look up current rates instead of trusting the numbers baked into the code.

## Tech Used

- HTML
- CSS
- JavaScript
- Originally built and tested in Python first

## Challenges

Getting the f-string formatting right in Python confused me for a while, and indexing numbers correctly was tricky too. I also went through a few different design attempts and ran into 404 errors trying to figure out GitHub Pages, so I ended up deploying with Netlify instead.

## AI Usage

I wrote the original Python code myself. AI helped me with the f-string formatting, since I got confused there, and it also helped me understand some of the modules I used, though I didn't just take AI's word for it, I went and searched on my own to see how other people approached similar calculator projects to understand it better myself.

For the website version, I didn't know HTML, CSS, or JavaScript yet, so I had AI build the actual website for me, including the design and layout. I went through about 5 different prototypes before landing on the final version, which is what's live now. After completing the Star Dance Challenge's HTML lesson, I learned how the code actually works and can now read and understand it myself.

I also used AI to help clean up and organize the wording of this README, catch a couple of incorrect exchange rates in my currency converter, and set up the instructions below for running the project locally.

## Running Locally

You don't need any special setup or dependencies for this project. It is a single static HTML file.

**Option 1: Just open the file**
1. Download or clone this repository
2. Open the `index.html` file directly in your browser (double-click it, or right-click -> Open With -> your browser)

**Option 2: Using VS Code + Live Server**
1. Clone the repository:
   ```
   git clone https://github.com/facxts/calculator.git
   ```
2. Open the folder in VS Code.
3. Install the "Live Server" extension if you don't already have it.
4. Right-click `index.html` and choose "Open with Live Server"
5. The project will open automatically at a local address like `http://127.0.0.1:5500`

**Running the Python version**

If you want to try the original Python version of the calculator instead of the web version:
```
python smart_calculator.py
```
 Make sure you have Python installed in VS Code

## Live Site

https://calculator-project-qt.netlify.app/

## Author

Made by [facxts](https://github.com/facxts)
