---
published: true
key: '4'
title: Build Your Personal Blog / Website at githib.io for Free!
tags:
  - Github
  - Jekyll
  - Blog
---
Your own blog can help you to develop your personal brand. You can easily use github.io pages to setup a free blog.

# Setup on server
1. First you need an github account. If you dont have, go to github and create one and log in with your account.

2. For a ready-made blog setup, choose from existing jekyll [themes](https://github.com/kitian616/jekyll-TeXt-theme). 
    
3. Fork the theme. 

   ![github_fork.PNG]({{site.baseurl}}/images/github_fork.PNG)

4. Rename it according to: username.github.io 

   ![github_rename.PNG]({{site.baseurl}}/images/github_rename.PNG)


After a few seconds your blog should be visible at: ```username.github.io```
You can edit your blog from the web (github.com) or you can edit it in your local machine and then push it into github.com. 

# Setup on PC (Windows)

1. download and install git [here](https://git-scm.com/download/win).

2. download and install rubyinstaller [here](https://rubyinstaller.org/). Make sure to check ```Run the ridk install``` at the last step.

3. Install Jekyll and Bundler using

   ```ps
   gem install github-pages
   ```
   
4. Check if Jekyll has been installed properly: 

   ```ps
   jekyll -v
   ```
   
   ![jekyll_version.PNG]({{site.baseurl}}/images/jekyll_version.PNG)

5. Clone your newly created blog

   ```ps
   git clone https://github.com/yourusername/yourusername.github.io.git
   ```
   
6. add the following to your Gemfile

   ```ps
   source "https://rubygems.org"
   gem "github-pages", group: :jekyll_plugins
   ```
   
7. Serve the site and watch for markup/sass changes 

   ```ps	
   jekyll serve or bundle exec jekyll serve
   ```
   
8. View your website at http://127.0.0.1:4000/

9. Commit any changes and push everything to the master branch of your GitHub user repository. GitHub Pages will then rebuild and serve your website.


# Setup on PC (Linux)



# Troubleshooting

1. if you get error like  ```gem not found```, then run
   
   ```ps
   gem update
   bundle config set path 'vendor/cache'  or   bundle install --path vendor/cache
   bundle install   
   ```

2. if time errors occur, then add the following in the gem file
   
   ```ps
   gem 'tzinfo-data', platforms: [:mingw, :mswin, :x64_mingw]
   bundle update
   ```
