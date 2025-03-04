console.log('Hello Dr. Shaweta');


data = [
    {
    "number": "1",
    "author": "Von R. Glitschka",
    "quote": "The client may be king, but he's not the art director."
    },
    {
    "number": "2",
    "author": "Frank Capra",
    "quote": "A hunch is creativity trying to tell you something."
    },
    {
    "number": "3",
    "author": "Steven Heller",
    "quote": "As a profession, graphic designers have been shamefully remiss or ineffective about plying their craft for social or political betterment."
    }];
    
    console.log(data);
    var random = Math.floor(Math.random() * data.length); 
    console.log(data[random].quote);
    console.log(data[random].author);