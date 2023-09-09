# link-shortener
This repository contains a link shortening project. 


After deploying to localhost, the user can send POST requests to http://127.0.0.1:8000/api/tokens/ to get the shortened link.
Access the original content by going to http://127.0.0.1:8000/{short_url}/.

Example POST request:
{ 
  "full_url": "https://habr.com/ru/news/584022/"
}



The project is based on an [article]([https://www.example.com](https://habr.com/ru/articles/718800/)https://habr.com/ru/articles/718800/) from habr. 
The main difference is the hashing of links.
